/* script.js */
document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('bootstrapForm');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        var formData = new FormData(form);

        fetch('https://docs.google.com/forms/d/e/1FAIpQLSfBvRMPRejFulKg4pQh3TSdbh1rfg13FA8WUYOzA8oBC-aL4w/formResponse', {
            method: 'POST',
            body: formData
        })
        .then(function (response) {
            if (response.ok) {
                alert('Form Submitted. Thanks.');
            } else {
                alert('Error submitting form.');
            }
        })
        .catch(function (error) {
            console.error('Error:', error);
        });
    });
});
