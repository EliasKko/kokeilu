'use strict';
let nums = []
let run = true;
for (let i =+ prompt('anna luku'); run === true; i =+ prompt('anna luku')) {
  if (nums.includes(i)) {
    run = false
    break;

  }
  else {
    nums.push(i)
  }
}
console.log(nums)