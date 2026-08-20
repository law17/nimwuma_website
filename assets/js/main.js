(() => {
  const navToggle = document.querySelector('[data-nav-toggle]');
  const nav = document.querySelector('[data-nav]');

  if (navToggle && nav) {
    navToggle.addEventListener('click', () => {
      const open = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open', !open);
    });
  }

  document.querySelectorAll('.nav-submenu-toggle').forEach((button) => {
    button.addEventListener('click', () => {
      const open = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!open));
      button.closest('.has-submenu')?.classList.toggle('submenu-open', !open);
    });
  });

  document.addEventListener('click', (event) => {
    if (!event.target.closest('.has-submenu')) {
      document.querySelectorAll('.has-submenu.submenu-open').forEach((item) => {
        item.classList.remove('submenu-open');
        item.querySelector('.nav-submenu-toggle')?.setAttribute('aria-expanded', 'false');
      });
    }
  });
})();
