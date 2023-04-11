
const data = [
    {
       title : "aaa",
       rating : "8.7"
    },
    {
        title : "bbb",
        rating : "8.5"
     }
];

array.forEach((element, i ) => {
    
const mainn = document.querySelector(".mainn");


//create card

const card = document.createElement('div');
card.classList = 'card';

const movieCard = `
 
<div class="col-xl-4 col-md-6">
<article>

  <div class="post-img">
    <img src="assets/img/blog/blog-1.jpg" alt="" class="img-fluid">
  </div>

  <p class="post-category">${data[i].title}</p> 

  <h2 class="title">
    <a href="email-notif1.html">${data[i].rating}</a>
  </h2>
</article>
</div>

`;

card.innerHTML += movieCard;
mainn.appendChild(card);
});