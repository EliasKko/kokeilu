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
  } catch (error) {
    console.log(error.message);
  }
})