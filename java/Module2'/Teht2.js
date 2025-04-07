'use strict';
let participants = [];
let num =+ prompt('number of participants')
participants.length = num
for (let i = 0; i < num; i++ ) {
  name = prompt('participants name')
  participants.push(name)
}
participants.sort()
const lista = document.getElementById('target')
for (let person of participants) {
      let li = document.createElement('li');
      li.textContent = person;
      lista.appendChild(li);
}