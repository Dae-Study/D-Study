
const Searching = Search.prototype;

function Search() {
  this.url = document.querySelector('input[name = "search');
  this.result = document.querySelector('.SelectSearch')
  this.searchBtn = document.querySelector('.S-button');
  this.form = document.querySelector('.search');

  this.Result();
}

Searching.Result = function() {
  this.form.addEventListener('button', e => {

    e.preventDefault();

    let result = this.result.value;
    let url = this.url.vaule;

    if(result === "filtering") 
      location.href = "filtering.html";
    else if(result === "compare") 
      location.href = "compare.html";
    else if(result === "report")
      location.href = "report.html"; 
  });
}

new Search();