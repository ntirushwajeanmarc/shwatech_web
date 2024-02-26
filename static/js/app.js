    // Initialize highlight.js and specify the language
    document.addEventListener('DOMContentLoaded', (event) => {
        document.querySelectorAll('pre code').forEach((block) => {
            hljs.highlightElement(block);
        });
    });
//search functionalities
document.getElementById('search-form').addEventListener('input', function(event) {
    const query = event.target.value;
    fetch(`/search?q=${query}`)
        .then(response => response.json())
        .then(results => {
            const searchResultsModal = new bootstrap.Modal(document.getElementById('search-results-modal'));
            const searchResultsBody = document.getElementById('search-results-body');
            searchResultsBody.innerHTML = ''; // Clear previous results
            if (results.length === 0) {
                searchResultsBody.innerHTML = 'No results found.';
            } else {
                results.forEach(result => {
                    searchResultsBody.innerHTML += `<a href="${result.url}">${result.title}</a><br>`;
                });
            }
            searchResultsModal.show(); // Show the modal
        })
        .catch(error => {
            console.error('Error:', error);
        });
});