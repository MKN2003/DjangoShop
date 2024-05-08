//create constuctor to populate fruity inventory with

function fruitBasket(fruitType, pricing, measurement, descript, image) {
	this.fruitType = fruitType
	this.pricing = pricing
	this.measurement = measurement //lbs, bushel, etc
	this.descript = descript
	this.image = image
}

var fruityArray = []

var fruit0 = new fruitBasket("blueberries", 3.99, "/pint", "basket o'plump and delicious blueberries", "https://github.com/tesslynne/Bloom-Ecommerce-Fruit/blob/master/images/blueberries.jpg?raw=true")
var fruit1 = new fruitBasket("raspberries", 3.99, "/pint", "stain-your-fingers delicious raspberries", "https://github.com/tesslynne/Bloom-Ecommerce-Fruit/blob/master/images/raspberries.jpg?raw=true")
var fruit2 = new fruitBasket("mixed berries", 7.00, "/bushel", "a bushel of nature's candy in all colors", "https://github.com/tesslynne/Bloom-Ecommerce-Fruit/blob/master/images/mixed-berries.jpg?raw=true")
var fruit3 = new fruitBasket("nectarines", 2.99,"/lb", "juicy nectarines perfect for early spring picnics", "https://github.com/tesslynne/Bloom-Ecommerce-Fruit/blob/master/images/nectarines.jpg?raw=true")
var fruit4 = new fruitBasket("petite navel oranges", 2.00, "/2 lbs", "SPECIAL price! easy-to-peel petite navel oranges", "https://github.com/tesslynne/Bloom-Ecommerce-Fruit/blob/master/images/oranges.jpg?raw=true")
var fruit5 = new fruitBasket("red cherries", 5.50 ,"/lb", "sweet plump cherries to stain your fingertips with", "https://github.com/tesslynne/Bloom-Ecommerce-Fruit/blob/master/images/cherries.jpg?raw=true")
var fruit6 = new fruitBasket("plums", 1.15, "/lb", "reminds us of childhood summers", "https://github.com/tesslynne/Bloom-Ecommerce-Fruit/blob/master/images/plums.jpg?raw=true")
var fruit7 = new fruitBasket("cantaloupe", 1.85, " each", "sweet slices o'heaven await!", "https://github.com/tesslynne/Bloom-Ecommerce-Fruit/blob/master/images/melon.jpg?raw=true")
var fruit8 = new fruitBasket("gala apples", 1.85, " /lb", "sweet and snappy crunch!", "https://github.com/tesslynne/Bloom-Ecommerce-Fruit/blob/master/images/apples.jpg?raw=true")


//push the above variables into the new fruity array!

fruityArray.push(fruit0)
fruityArray.push(fruit1)
fruityArray.push(fruit2)
fruityArray.push(fruit3)
fruityArray.push(fruit4)
fruityArray.push(fruit5)
fruityArray.push(fruit6)
fruityArray.push(fruit7)
fruityArray.push(fruit8)

for ( i = 0; i < fruityArray.length; i++ ) {
//create text notes and variables for images/buttons
	var fruitImg = fruityArray[i].image 
	//create placeholder for images
	var fruitName = document.createTextNode(fruityArray[i].fruitType) 
	//create text node for kind of fruit
	var costMeasure = document.createTextNode("$" + fruityArray[i].pricing + fruityArray[i].measurement) //create txt for pricing info
	var fruitProfile = document.createTextNode(fruityArray[i].descript) 
	//button text
	var buyButton = document.createTextNode("add to basket") 


	//create Bootstrap elements to hold inventory
	var newColumn = document.createElement("div")
	var imgDiv = document.createElement("div")
	var img = document.createElement("img")
	var captionDiv = document.createElement("div")
	var descriptText = document.createElement("p")
	var captionPriceTxt = document.createElement("h4")
	var captionTitle = document.createElement("h4")
	

	var buy = document.createElement("button")
	buy.appendChild(buyButton)
	
	captionDiv.appendChild(fruitName)
	captionDiv.appendChild(captionTitle)
	captionDiv.appendChild(captionPriceTxt)
	captionDiv.appendChild(descriptText)

	captionTitle.appendChild(fruitName)

	captionPriceTxt.appendChild(costMeasure)
	descriptText.appendChild(fruitProfile)
	img.src = fruitImg
	

//set bootstrap classes
	img.className= "img-responsive"
	captionDiv.className = "caption"
	captionTitle.className = "h4"
	captionPriceTxt.className = "pull-right"
	buy.className = "btn btn-primary btn-sm"

	

//append
	newColumn.className = "col-sm-4 col-lg-4 col-md-4"
	imgDiv.className = "produce fruitType" + i +  "thumbnail"
	imgDiv.appendChild(img)
	captionDiv.appendChild(captionPriceTxt)
	captionDiv.appendChild(captionTitle)
	captionDiv.appendChild(descriptText)
	captionDiv.appendChild(buy)
	newColumn.appendChild(imgDiv)
	newColumn.appendChild(captionDiv)

	document.getElementById("fruits").appendChild(newColumn)
	



}


//still in the works as of 2/24: 


// create a function that on click of "Your Basket", it shows
// user's selections as they shop. use create element 'modal-dialog'
// and use class name "bs.dropdown"