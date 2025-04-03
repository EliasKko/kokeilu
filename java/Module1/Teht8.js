'use strict';
let nums = [];
let num1 =+ prompt('give me start year');
let Leap = [];
nums.push(num1)
const num2 =+ prompt('give me end year');
nums.push(num2)
for  (let i = num1; i < num2; i++) {
  if (i % 100 == 0){
    if (i % 100 == 0){
      Leap.push(i);
    }
  }
  else if (i % 4 == 0) {
    Leap.push(i);
  }
}
document.querySelector('#target').innerHTML = Leap;