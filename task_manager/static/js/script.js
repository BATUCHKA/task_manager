// Add event listener when document is ready
document.addEventListener('DOMContentLoaded', function () {
  // Add confirmation for delete buttons
  const deleteButtons = document.querySelectorAll('.btn-danger');
  deleteButtons.forEach(button => {
    button.addEventListener('click', function (e) {
      if (!confirm('Are you sure you want to delete this task?')) {
        e.preventDefault();
      }
    });
  });

  // Auto-hide alerts after 5 seconds
  const alerts = document.querySelectorAll('.alert');
  alerts.forEach(alert => {
    setTimeout(function () {
      alert.style.opacity = '0';
      alert.style.transition = 'opacity 1s';
      setTimeout(function () {
        alert.remove();
      }, 1000);
    }, 5000);
  });
});