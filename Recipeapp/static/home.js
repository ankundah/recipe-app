// function openTab(event, tabName) {
//     var i;
//     var tabContents = document.getElementsByClassName("tab-content");
//     var tabButtons = document.getElementsByClassName("tab-button");

//     // Hide all tab contents
//     for (i = 0; i < tabContents.length; i++) {
//         tabContents[i].classList.remove("active");
//     }

//     // Remove active class from all tab buttons
//     for (i = 0; i < tabButtons.length; i++) {
//         tabButtons[i].classList.remove("active");
//     }

//     // Show the current tab and add an "active" class to the button that opened the tab
//     document.getElementById(tabName).classList.add("active");
//     event.currentTarget.classList.add("active");
// }

document.getElementById('recipeForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('name', document.getElementById('name').value);
    formData.append('ingredients', document.getElementById('ingredients').value);
    formData.append('description', document.getElementById('description').value);
    formData.append('image', document.getElementById('img').files[0]);

    fetch('/recipes/home/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // Make sure to include CSRF token for Django
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Redirect to the list of recipes
        window.location.href = '/recipes/home/list';
    })
    .catch((error) => {
        console.error('Error:', error);
        // Handle error (e.g., show an error message)
    });
});

function getCookie(name) {
   let cookieValue = null;
   if (document.cookie && document.cookie !== '') {
       const cookies = document.cookie.split(';');
       for (let i = 0; i < cookies.length; i++) {
           const cookie = cookies[i].trim();
           if (cookie.substring(0, name.length + 1) === (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
            }
        }
   }
   return cookieValue;
}

function openTab(tabName) {
    var i;
    var x = document.getElementsByClassName("tab-content");
    var tabButtons = document.getElementsByClassName("tab-button");
    for (i = 0; i < x.length; i++) {
        x[i].classList.remove("active");
    }
    for (i = 0; i < tabButtons.length; i++) {
        tabButtons[i].classList.remove("active");
    }
    document.getElementById(tabName).classList.add("active");
    event.currentTarget.classList.add("active");
}
