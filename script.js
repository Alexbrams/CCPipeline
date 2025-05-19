const allMoviesTBody = document.querySelector("#allItems tbody")

const showTable = function(moviesArray){
    allMoviesTBody.innerHTML = ""
    for(let i = 0; i < moviesArray.length;i++) { 
        let trText = `<tr><th scope="row">${moviesArray[i].Givenname} ${moviesArray[i].Surname}</th><td>${moviesArray[i].Country}</td><td>${moviesArray[i].NationalId}</td><td>${"+"+moviesArray[i].TelephoneCountryCode} ${moviesArray[i].Telephone}</td><td>${moviesArray[i].Streetaddress}, ${moviesArray[i].City}</td></tr>`
        allMoviesTBody.innerHTML += trText
    }

} 

fetch('./data.json')
    .then((response) => response.json())
    .then((json) => {
        showTable(json)
    });
