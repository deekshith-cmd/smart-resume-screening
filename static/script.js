// File upload preview
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('resume');
    const form = document.querySelector('form');
    
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const fileName = e.target.files[0]?.name;
            if (fileName) {
                console.log('File selected:', fileName);
            }
        });
    }
    
    if (form) {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('.btn');
            submitBtn.textContent = 'Analyzing...';
            submitBtn.disabled = true;
        });
    }
});
