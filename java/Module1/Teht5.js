'use strict';
const Year =+ prompt('Give me a year')
let Leap;
if (Year % 4 == 0){
  Leap = ('It is a leap year');
}
else {
  Leap = ('It is NOT a leap year');
}
document.querySelector('#target').innerHTML = Leap;
