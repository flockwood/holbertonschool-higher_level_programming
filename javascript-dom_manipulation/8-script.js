// Wait for the DOM to be fully loaded since script is in <head>
document.addEventListener('DOMContentLoaded', function() {
  // Fetch the translation from the API
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      // Display the hello translation in the element with id 'hello'
      document.querySelector('#hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching translation:', error);
    });
});
