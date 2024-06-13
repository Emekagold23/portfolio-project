// JavaScript for Job pages

document.addEventListener('DOMContentLoaded', function () {
    console.log('Job script loaded');

    // Handle form submission for creating a new job
    const jobForm = document.getElementById('create-job-form');
    if (jobForm) {
        jobForm.addEventListener('submit', function (event) {
            event.preventDefault();
            createJob();
        });
    }

    // Function to create a new job
    function createJob() {
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const location = document.getElementById('location').value;

        if (!title || !description || !location) {
            alert('Please fill in all fields');
            return;
        }

        const jobData = { title, description, location };

        fetch('/api/jobs', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(jobData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Job created successfully');
                window.location.href = '/jobs';
            } else {
                alert('Failed to create job');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Fetch and display jobs
    const jobList = document.getElementById('job-list');
    if (jobList) {
        fetch('/api/jobs')
            .then(response => response.json())
            .then(data => {
                data.forEach(job => {
                    const li = document.createElement('li');
                    li.textContent = `Title: ${job.title}, Description: ${job.description}, Location: ${job.location}`;
                    jobList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }
});
