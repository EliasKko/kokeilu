'use strict';

const searchForm = document.querySelector('#search_form')
searchForm.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const value_from_input = document.querySelector('input[name=q]').value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${value_from_input}`);
        const jsonData = await response.json();
        const showName = jsonData[1]
        console.log(showName)
        const htmlElem = document.querySelector('#results')
        htmlElem.innerHTML = ``;
        const Artcl = document.createElement('article')
        const url = document.createElement('a')
        url.target="_blank"
        url.innerHTML = jsonData[1].show.url;
        Artcl.appendChild(url)
        const h = document.createElement('h2');
        h.innerHTML = jsonData[1].show.name;
        Artcl.appendChild(h)
        const img = document.createElement('img')
        if (jsonData[1].show.image) {
            const img = document.createElement('img');
            img.src = jsonData[1].show.image.medium;
            img.alt = jsonData[1].show.name;
            Artcl.appendChild(img);}
        htmlElem.appendChild(Artcl)
    } catch (error) {
        console.log(error.message);
    }


})



