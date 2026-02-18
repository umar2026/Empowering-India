// Smooth scroll to dashboard
document.getElementById("exploreBtn").addEventListener("click", function() {
    document.getElementById("dashboard").scrollIntoView({
        behavior: "smooth"
    });
});

// Hide loader when iframe loads
const iframe = document.getElementById("tableauFrame");
const loader = document.getElementById("loader");

iframe.onload = function() {
    loader.style.display = "none";
};
