'use strict';
const items = ['First item', 'Second item', 'Third item']
const Target = document.querySelector('#target')
const li1 = document.createElement('li');
li1.innerHTML = `First item`
const li2 = document.createElement('li');
li2.innerHTML = `Second item`
const li3 = document.createElement('li');
li3.innerHTML = `Third item`
Target.appendChild(li1)
Target.appendChild(li2)
Target.appendChild(li3)
