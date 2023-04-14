// var  = ''


let url = "http://api.open-notify.org/astros.json";

let options = {
  method : "GET"
}

var something =
fetch(url,options)
.then(response => (response.json()))
.then(json =>something = (json.number))




async function foo() {
  // const res = await fetch(url,options) ;
  const result = await something;
  const miro = result;
  // console.log(something); // or use the result variable
      var cardContainer = document.getElementById("cardContainer");

      // Clear existing cards
      cardContainer.innerHTML = "";

      // Create new cards
      console.log(something)
      for (var i = 0; i < something; i++) {
        var card = document.createElement("div");
        card.className = "card";
        // card.textContent = "Card ban gaye mkc" + (i + 1);
        var x = i +1
        var iframe = document.createElement('iframe');
        // var html = '<body>Foo</body>';
        iframe.src = '/hehe' + x + '.html';
        var c = document.body.appendChild(iframe);
        console.log(c)
       
       
      }
      
    }
 
foo() ;


// const result = await foo();
// console.log(result)