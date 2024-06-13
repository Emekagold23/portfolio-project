document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.getElementById('search-form');
    const resultsDiv = document.getElementById('results');

    searchForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission
        const skill = document.getElementById('skill').value;
        searchWorkers(skill);
    });

    function searchWorkers(skill) {
        fetch(`/search/results?skill=${encodeURIComponent(skill)}`)
            .then(response => response.json())
            .then(data => {
                displayResults(data);
            })
            .catch(error => console.error('Error:', error));
    }

    function displayResults(data) {
        resultsDiv.innerHTML = ''; // Clear previous results
        if (data.error) {
            resultsDiv.innerHTML = `<p>${data.error}</p>`;
            return;
        }
        const ul = document.createElement('ul');
        data.forEach(worker => {
            const li = document.createElement('li');
            li.textContent = `ID: ${worker.id}, Username: ${worker.username}, Email: ${worker.email}, Skills: ${worker.skills}`;
            ul.appendChild(li);
        });
        resultsDiv.appendChild(ul);
    }
});