// Array for product of list items id, image, title, and price.
const product = [
    {
        id: 0,
        image: 'https://blog.digitalcook.fr/wp-content/uploads/2021/04/Landing-Page.png',
        title: 'Builidng a Landing page',
        price: 1,
    },
    {
        id: 1,
        image: 'https://tse1.mm.bing.net/th?id=OIP.sDkW6w1i7ET_BaR_UMonHQHaI3&pid=Api&P=0&h=220',
        title: 'Build your own web server',
        price: 1,
    },
    {
        id: 2,
        image: 'https://www.pinclipart.com/picdir/big/117-1176996_checklist-clipart.png',
        title: 'To Do App',
        price: 1,
    },
    {
        id: 3,
        image: 'https://www.zeumic.com.au/wp-content/uploads/2018/04/zeumic-e-commerce-cycle-st-kilda-image.jpg',
        title: 'E-commerce Website',
        price: 1,
    }
];

// Extracts item and returns item
const categories = [
    ...new Set(product.map((item)=>{return item}))
]

// Counter variable
let i=0;

// Obtains 'root' element and creates inner HTML element using variables 'image' and 'title'
document.getElementById('root').innerHTML = categories.map((item)=>
{
    var {image, title} = item;
    return(
        `<div class='box'>
            <div class='img-box'>
                <img class='images' src=${image}></img>
            </div>
        <div class='bottom'>
        <p>${title}</p>
        `+
        "<button onclick='addtocart("+(i++)+")'>Join</button>"+
        `</div>
        </div>`
    )
}).join('')

// Array to store items in variable 'cart'
var cart =[];

// Adds item to cart
function addtocart(a){
    cart.push({...categories[a]});
    displaycart();
}

// Removes an item from cart
function delElement(a){
    cart.splice(a, 1);
    displaycart();
}

// Displays items in 'cart'
function displaycart(){
    let j = 0, total=0;

    // Updates count of items in cart
    document.getElementById("count").innerHTML=cart.length;

    // Handles empty cart and cart with items
    if(cart.length==0){

        // Displays message if cart is empty
        document.getElementById('cartItem').innerHTML = "Group list empty";
        document.getElementById("total").innerHTML = " "+0+"";
    } else {

        // Displays each item in cart available for deletion
        document.getElementById("cartItem").innerHTML = cart.map((items)=>
        {   
            // Assigns variables image, title, and price to 'items'
            // Updates 'price'
            var {image, title, price} = items;
            total=total+price;
            document.getElementById("total").innerHTML = " "+total+"";
            return(
                `<div class='cart-item'>
                <div class='row-img'>
                    <img class='rowimg' src=${image}>
                </div>
                <p style='font-size:12px;'>${title}</p>
              `+
                "<i class='fa-solid fa-trash' onclick='delElement("+ (j++) +")'></i></div>"
            );
        }).join('');
    }
}