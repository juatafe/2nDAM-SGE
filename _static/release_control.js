document.addEventListener("DOMContentLoaded", () => {
  const today = new Date();
  document.querySelectorAll("details.dropdown").forEach(el => {
    const release = el.getAttribute("data-release");
    if (release) {
      const rDate = new Date(release);
      if (today < rDate) {
        el.innerHTML = "<p><em>La solució estarà disponible a partir del "
          + rDate.toLocaleDateString() + ".</em></p>";
      }
    }
  });
});
