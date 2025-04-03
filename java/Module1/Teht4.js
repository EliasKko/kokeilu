'use strict';
const name = prompt('give me your name:');
let Class;
switch (name) {
  case 'Malfoy':
    Class = ('You are in Slytherin');
    break;
  case 'Anna':
    Class = ('You are in Hufflepuff');
    break;
  case 'Ron':
    Class = ('You are in Ravenclaw');
    break;
  case 'Harry':
    Class = ('You are in Gryffindor');
    break;
  default:
    Class = ('Youre not on this school, GET OUT!');



}
document.querySelector('#target').innerHTML = Class;