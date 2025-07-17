// Fetch Star Wars character data from the API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    // Display the character name in the element with id 'character'
    document.querySelector('#character').textContent = data.name;
  })
  .catch(error => {
    console.error('Error fetching character:', error);
  });
