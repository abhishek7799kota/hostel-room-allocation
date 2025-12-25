document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".glass-card");
    cards.forEach((card, index) => {
        card.style.animation = `fadeIn 0.6s ease ${(index+1)*0.2}s forwards`;
    });
});
