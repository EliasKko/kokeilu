'use strict';
const nums = [1,4,5,6,7,78,98,99,60];
let evennums = [];
document.querySelector('#target2').innerHTML = nums;
function even() {
  for (let i = 0; i < nums.length; i++ ){
    let num = nums[i];
    if (num % 2 == 0) {
      evennums.push(num)
    }
  }

  document.querySelector('#target').innerHTML = evennums;
  return;
}

even();