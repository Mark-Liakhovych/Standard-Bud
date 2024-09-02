document.addEventListener('DOMContentLoaded', function () {
  const burgerButton = document.getElementById('burger-button');
  const headerMenu = document.getElementById('header-menu');

  if (burgerButton && headerMenu) {
    burgerButton.addEventListener('click', function () {
      this.classList.toggle('active');
      headerMenu.classList.toggle('active');

      if (headerMenu.classList.contains('active')) {
        document.body.classList.add('no-scroll');
      } else {
        document.body.classList.remove('no-scroll');
      }
    });
  }
});


