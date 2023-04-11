console.log("wow")
const table = document.getElementsByClassName('table')[0];
console.log(table);

function createCard(number) {
  const card = document.createElement('div');
  card.className = "card";

  const topNumber = document.createElement('div');
  topNumber.innerText = number;
  
  
  const bottomNumber = document.createElement('div');
  bottomNumber.className = "right";
  bottomNumber.innerText = number;

  card.append(topNumber);
  card.append(bottomNumber);

  return card;
  
}

table.append(createCard(5));