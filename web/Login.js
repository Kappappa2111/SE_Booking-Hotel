let slideIndex = 0;
const slides = document.querySelectorAll(".slide");
const totalSlides = slides.length;

function showSlides() {
    slides.forEach((slide, index) => {
        slide.style.opacity = "0";
    });

    slides[slideIndex].style.opacity = "1";
    slideIndex = (slideIndex + 1) % totalSlides;
}
setInterval(showSlides, 5000);

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); 
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const role = document.getElementById("choose-your-role").value;

    if (username && password) {
        if (role === "Admin") {
            window.location.href = "Adminpage.html";  
        } else if (role === "Tourist") {
            window.location.href = "homepage.html"; 
        } else {
            alert("Please select a valid role.");
        }
    } else {
        alert("Please enter valid login details.");
    }
});

showSlides();
