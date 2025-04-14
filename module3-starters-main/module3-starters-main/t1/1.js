'use strict';

const ulElem = document.querySelector('#target');

const htmlList = `
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>`

ulElem.innerHTML = htmlList;

ulElem.classList.add("my-list");