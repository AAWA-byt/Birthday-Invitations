// Automatically remove flash messages after 5 seconds
setTimeout(() => {
    const flashContainer = document.getElementById('flash-container');
    if (flashContainer) {
        flashContainer.remove();
        
    }
}, 3000);