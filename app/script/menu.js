const toggleButton = document.querySelector('#container header .toggle');

const navElement = document.querySelector('#container header')

toggleButton.addEventListener('click', function() {
    navElement.classList.toggle('active');
})