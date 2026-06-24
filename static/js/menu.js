const menuButton = document.querySelector("[data-menu-button]");
const sidebar = document.querySelector("[data-sidebar]");
const navLinks = document.querySelectorAll(".site-nav__link");

if (menuButton && sidebar) {
  menuButton.addEventListener("click", () => {
    const isOpen = sidebar.classList.toggle("is-open");

    menuButton.setAttribute("aria-expanded", String(isOpen));
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      sidebar.classList.remove("is-open");
      menuButton.setAttribute("aria-expanded", "false");
    });
  });
}