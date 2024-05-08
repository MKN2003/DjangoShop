from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, TemplateView

from products.forms import RegisterForm, LoginForm
from products.models import ProductsModel, CategoryModel, CartModel, FavoriteModel
from products.handler import bot

# Create your views here.


def home_page(request):
    products = ProductsModel.objects.all()
    categories = CategoryModel.objects.all()

    #Поиск

    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        if get_product:
            exact_product = ProductsModel.objects.filter(product_name__icontains=get_product)

            context = {'products': products, 'categories': categories, 'search_product': exact_product}
            return render(request, template_name='index.html', context=context)
    else:
        context = {'products': products, 'categories': categories}
        return render(request, template_name='index.html', context=context)


# def search_products(request):
#     if request.method == 'POST':
#         get_product = request.POST.get('search_product')
#
#         try:
#             exact_product = ProductsModel.objects.get(product_name__icontains=get_product)
#             print(f'Yeeeeah we found for you this product {exact_product}')
#             return redirect(f'product/{exact_product.id}')
#         except:
#             print('Not Found')
#             return redirect('/')


def single_product(request, id):
    product = ProductsModel.objects.get(id=id)
    context = {'product': product}
    return render(request, 'single-product.html', context=context)


class MyFormView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login'


class MyLoginFormView(CreateView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'


def logout_view(request):
    logout(request)
    return redirect('/')


class LogoutEnter(TemplateView):
    template_name = 'logout.html'


def category_page(request, id):
    categories = CategoryModel.objects.get(id=id)
    products = ProductsModel.objects.filter(category=categories)

    context = {'categores': categories, 'products': products}
    return render(request, template_name='category.html', context=context)


def add_product_to_cart(request, id):
    if request.method == 'POST':
        checker = ProductsModel.objects.get(id=id)

        if checker.count >= int(request.POST.get('pr_count')):
            CartModel.objects.create(user_id=request.user.id,
                                     user_product=checker,
                                     user_product_quantity=int(request.POST.get('pr_count'))).save()
            return redirect('/user_cart')
        else:
            return redirect('/')


def user_cart(request):
    cart = CartModel.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        main_text = 'Новый заказ'

        for i in cart:
            main_text += (f'Товар: {i.user_product}\n'
                          f'Кол-во: {i.user_product_quantity}\n'
                          f'ID Пользователя: {i.user_id}\n'
                          f'Цена: {i.user_product.price}\n')
            bot.send_message(-1002116409884, main_text)
            cart.delete()
            return redirect('/')

    else:
        return render(request, 'cart.html', {'cart': cart})


def add_favorite(request, id):
    if request.method == 'POST':
        product = ProductsModel.objects.get(id=id)
        FavoriteModel.objects.create(user_id=request.user.id, user_product=product).save()
        return redirect('/user_favorite')


def user_favorite(request):
    favorite = FavoriteModel.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        main_text = 'Избранные'

        for i in favorite:
            main_text += (f'Товар: {i.user_product}\n'
                         f'Цена: {i.user_product.price}\n'
                         f'ID: {i.user_id}')
    else:
        return render(request, 'favorite.html', {'favorite': favorite})
