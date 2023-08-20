document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById('modal');
    var closeButton = document.getElementById('closeBtn');
    var logo = document.querySelector('.logo');

    // Check if the modal should be displayed today
    var lastVisit = localStorage.getItem('lastVisit');
    var currentDate = new Date().toDateString();

    if (!lastVisit || lastVisit !== currentDate) {
        modal.style.display = 'block';
        localStorage.setItem('lastVisit', currentDate);
    }

    // Function to open the modal
    function openModal() {
        modal.style.display = 'block';
    }

    // Function to close the modal
    function closeModal() {
        modal.style.display = 'none';
    }

    // Close the modal when the close button is clicked
    closeButton.addEventListener('click', closeModal);

    // Close the modal when the user clicks outside the modal content
    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            closeModal();
        }
    });

    // Open the modal when the logo is clicked
    logo.addEventListener('click', openModal);
});




