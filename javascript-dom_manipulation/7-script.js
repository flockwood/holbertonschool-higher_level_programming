// Fetch Star Wars movies data from the API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    // Get the ul element with id 'list_movies'
    const moviesList = document.querySelector('#list_movies');
    
    // Loop through each movie in the results array
    data.results.forEach(movie => {
      // Create a new li element
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      
      // Add the li element to the ul
      moviesList.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error fetching movies:', error);
  });
