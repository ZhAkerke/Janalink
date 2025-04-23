function toggleText(button) {
    var fullText = button.previousElementSibling;
    if (fullText.style.display === "none") {
        fullText.style.display = "block";
        button.innerHTML = "Read Less";
    } else {
        fullText.style.display = "none";
        button.innerHTML = "Read More";
    }
}
