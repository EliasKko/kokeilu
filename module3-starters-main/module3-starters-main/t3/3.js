'use strict';
const names = ['John', 'Paul', 'Jones'];
const target = document.querySelector('#target');
//const lista = document.createElement('ul');

for (let name of names) {
  const li = document.createElement('li');
  li.innerHTML = `<li>${name}</li>`;
  target.appendChild(li);
}

target.appendChild(lista);