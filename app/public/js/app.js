// Flash Messages
document.addEventListener('DOMContentLoaded', function () {
    var flashes = document.querySelectorAll('.flash-message');

    flashes.forEach(function (flash) {
        setTimeout(function () {
            flash.classList.add('hidden');
        }, 5000);
    });
});