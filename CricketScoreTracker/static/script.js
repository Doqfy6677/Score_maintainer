// This file is included for future enhancements
// Additional JavaScript functionality can be added here if needed

// Example: Function to detect network status for offline capabilities
function checkNetworkStatus() {
    const isOnline = navigator.onLine;
    if (!isOnline) {
        console.log('App is running in offline mode');
        // Show offline notification if needed
    }
}

// Listen for online/offline events
window.addEventListener('online', checkNetworkStatus);
window.addEventListener('offline', checkNetworkStatus);

// Check network status on page load
document.addEventListener('DOMContentLoaded', checkNetworkStatus);