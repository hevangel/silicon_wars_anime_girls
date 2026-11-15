const panorama = document.querySelector("#panorama");
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
document.querySelector(".panorama-controls").hidden = false;
document.querySelectorAll("[data-direction]").forEach((button) => {
  button.addEventListener("click", () => {
    panorama.scrollBy({
      left: Number(button.dataset.direction) * panorama.clientWidth * .75,
      behavior: reducedMotion.matches ? "instant" : "smooth"
    });
  });
});
