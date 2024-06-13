// JavaScript for Report pages

document.addEventListener('DOMContentLoaded', function () {
    console.log('Report script loaded');

    // Handle form submission for creating a new report
    const reportForm = document.getElementById('create-report-form');
    if (reportForm) {
        reportForm.addEventListener('submit', function (event) {
            event.preventDefault();
            createReport();
        });
    }

    // Function to create a new report
    function createReport() {
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;

        if (!title || !description) {
            alert('Please fill in all fields');
            return;
        }

        const reportData = { title, description };

        fetch('/api/reports', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(reportData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Report created successfully');
                window.location.href = '/reports';
            } else {
                alert('Failed to create report');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Fetch and display reports
    const reportList = document.getElementById('report-list');
    if (reportList) {
        fetch('/api/reports')
            .then(response => response.json())
            .then(data => {
                data.forEach(report => {
                    const li = document.createElement('li');
                    li.textContent = `Title: ${report.title}, Description: ${report.description}`;
                    reportList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }
});