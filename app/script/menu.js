const toggleButton = document.querySelector('#container nav .toggle');

const headerElement = document.querySelector('#container nav')

toggleButton.addEventListener('click', function() {
    headerElement.classList.toggle('active');
})