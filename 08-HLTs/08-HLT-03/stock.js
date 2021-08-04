var stock = ["milk","eggs","bacon","mushrooms","sugar","tea"];

document.getElementById("itemlist").innerHTML = "Items in stock:" + stock;

var item = window.prompt("What would you like to buy ?")

if(stock.includes(item)){
    window.alert(item + " is currently in stock");
}
else{
    console.log(item+ " is not in stock");
    var ans= window.prompt("Would you like to order "+item+"?");
    if (ans === "yes"){stock.push(item)}
}

document.getElementById("stock").innerHTML = item+" ordered";