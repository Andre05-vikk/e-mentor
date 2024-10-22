

document.getElementById("registerBtn").onclick = function() {
    document.getElementById("registerModal").style.display = "block";
};

document.getElementById("loginBtn").onclick = function() {
    document.getElementById("loginModal").style.display = "block";
};

document.getElementById("registerClose").onclick = function() {
    document.getElementById("registerModal").style.display = "none";
};

document.getElementById("loginClose").onclick = function() {
    document.getElementById("loginModal").style.display = "none";
};

window.onclick = function(event) {
    if (event.target == document.getElementById("registerModal")) {
        document.getElementById("registerModal").style.display = "none";
    }
    if (event.target == document.getElementById("loginModal")) {
        document.getElementById("loginModal").style.display = "none";
    }
};

// Select2 dropdown initialiseerimine
$(document).ready(function() {
    $('#programming-languages').select2({
        placeholder: "Vali programmeerimiskeel",
        allowClear: true,
        data: [
            {id: 'python', text: 'Python'},
            {id: 'javascript', text: 'JavaScript'},
            {id: 'java', text: 'Java'},
            {id: 'csharp', text: 'C#'},
            {id: 'cplus', text: 'C++'},
            {id: 'typescript', text: 'TypeScript'},
            {id: 'ruby', text: 'Ruby'},
            {id: 'php', text: 'PHP'},
            {id: 'swift', text: 'Swift'},
            {id: 'kotlin', text: 'Kotlin'},
            {id: 'go', text: 'Go'},
            {id: 'rust', text: 'Rust'},
            {id: 'scala', text: 'Scala'},
            {id: 'perl', text: 'Perl'},
            {id: 'lua', text: 'Lua'},
            {id: 'r', text: 'R'},
            {id: 'matlab', text: 'MATLAB'},
            {id: 'sql', text: 'SQL'},
            {id: 'dart', text: 'Dart'},
            {id: 'htmlcss', text: 'HTML/CSS'}
        ]
    });
});
