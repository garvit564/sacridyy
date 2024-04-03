document.addEventListener('DOMContentLoaded', function() {
    const mantras = document.querySelectorAll('.mantra-item'); // Get all mantra items
    let index = 0; // Index to track the current mantra

    // Hide all mantras except the first one
    for (let i = 1; i < mantras.length; i++) {
        mantras[i].style.display = 'none';
    }

    function displayNextMantra() {
        // Fade out the current mantra
        mantras[index].style.opacity = 0;
        setTimeout(() => {
            // After the fade-out animation completes, hide the current mantra
            mantras[index].style.display = 'none';
            // Increment index and wrap around if needed
            index = (index + 1) % mantras.length;
            // Display the next mantra
            mantras[index].style.display = 'block';
            // Fade in the next mantra
            setTimeout(() => {
                mantras[index].style.opacity = 1;
            }, 10); // Delay to ensure the display property is applied before fading in
        }, 1000); // Adjust the delay according to your animation duration
    }
    setInterval(displayNextMantra, 14000); // Display next mantra every 2 seconds
});
