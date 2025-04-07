'use strict';
let nums = []
let num =+ prompt('give a number')
for (let i = num; i != 0; nums.push(i)) {
  i =+ prompt('give a number')
}
nums.sort(function(a, b){return b-a});
document.querySelector('#target').innerHTML = nums;


