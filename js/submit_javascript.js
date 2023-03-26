
  

async function SubmitVars() {
// data to be sent to the POST request
var vweeks = document.getElementById("books").value;
var vyears = document.getElementById("years").value;
var vbooks = document.getElementById("books").value;
var vprojects = document.getElementById("projects").value;
var vearn = document.getElementById("earn").value;

let _data = {
        weeks: vweeks,
        years: vyears,
        books: vbooks,
        projects: vprojects,
        earn: vearn,
  }
  
  const response = await fetch('https://redandgreen.co.uk/vars', {
    method: "POST",
    body: JSON.stringify(_data),
    headers: {"Content-type": "application/json; charset=UTF-8"}
  })
  const responseText = await response.text();
  console.log(responseText); // logs 'OK'

  var x = document.getElementById("demo");  
  x.style.color = "red"; 
  x.innerHTML = JSON.stringify(responseText).substring(16,24);


}

// https://neuro-2fle3wxkia-nw.a.run.app/vars