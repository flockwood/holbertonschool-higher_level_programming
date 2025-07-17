// Add click event listener to the toggle_header element
document.querySelector('#toggle_header').addEventListener('click', function() {
    const header = document.querySelector('header');
    
    // Check current class and toggle
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});
