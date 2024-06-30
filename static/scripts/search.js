document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('search-form');
    const resultsDiv = document.getElementById('results');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        
        const skill = document.getElementById('skill').value;

        try {
            const response = await fetch(`/search-workers?skill=${encodeURIComponent(skill)}`);

            if (!response.ok) {
                throw new Error('Search failed');
            }

            const results = await response.json();

            // Clear previous results
            resultsDiv.innerHTML = '';

            // Display new results
            results.forEach(result => {
                const resultItem = document.createElement('div');
                resultItem.className = 'result-item';
                resultItem.textContent = `${result.firstName} ${result.lastName} - ${result.services}`;
                resultsDiv.appendChild(resultItem);
            });
        } catch (error) {
            console.error('Error searching workers:', error);
            // Handle error (e.g., display error message)
        }
    });
});