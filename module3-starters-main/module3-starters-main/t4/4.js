'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
const htmlElem = document.querySelector('#target');
for (let student of students) {
  const li = document.createElement('option');
  li.innerHTML = `${student.name}`;
  li.value = `${student.id}`;
  htmlElem.appendChild(li)
}
