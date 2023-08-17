document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById('modal');
    var closeButton = document.getElementById('closeBtn');

    // Open the modal when the page loads
    modal.style.display = 'block';

    // Close the modal when the close button is clicked
    closeButton.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    // Close the modal when the user clicks outside the modal content
    window.addEventListener('click', function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});


