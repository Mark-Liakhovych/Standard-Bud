document.addEventListener('DOMContentLoaded', function () {
  // Добавляем обработчик события на кнопку burger-button
  const burgerButton = document.getElementById('burger-button');
  if (burgerButton) {
    burgerButton.addEventListener('click', function () {
      const headerMenu = document.getElementById('header-menu');
      if (headerMenu) {
        this.classList.toggle('active');
        headerMenu.classList.toggle('active');
        if (headerMenu.classList.contains('active')) {
          document.body.classList.add('no-scroll');
        } else {
          document.body.classList.remove('no-scroll');
        }
      }
    });
  }

  // Добавляем обработчик событий на все элементы с классом card
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    card.addEventListener('click', function () {
      // Закрываем все карточки
      cards.forEach(c => c.classList.remove('open'));
      // Открываем текущую карточку
      this.classList.add('open');
    });
  });

  // Добавляем обработчик события на контейнер scrollContainer
  const scrollContainer = document.getElementById("scrollContainer");
  if (scrollContainer) {
    let isScrolling = false;

    scrollContainer.addEventListener("wheel", function (e) {
      e.preventDefault(); // Предотвращаем стандартное поведение скроллинга

      if (isScrolling) {
        return; // Если скролл уже в процессе, игнорируем
      }

      const scrollDistance = 630; // Расстояние прокрутки в пикселях

      isScrolling = true;

      let startScrollLeft = scrollContainer.scrollLeft;
      let endScrollLeft = startScrollLeft + scrollDistance * Math.sign(e.deltaY); // Учитываем направление скролла
      let startTime = null;

      const scrollAnimation = (timestamp) => {
        if (!startTime) {
          startTime = timestamp;
        }

        const elapsedTime = timestamp - startTime;
        const duration = 500; // Длительность анимации в миллисекундах

        const progress = Math.min(elapsedTime / duration, 1);

        const easeInOutQuad = (t) => {
          return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
        };

        const newScrollLeft = startScrollLeft + (endScrollLeft - startScrollLeft) * easeInOutQuad(progress);

        scrollContainer.scrollLeft = newScrollLeft;

        if (progress < 1) {
          requestAnimationFrame(scrollAnimation);
        } else {
          isScrolling = false; // Скролл завершен
        }
      };

      requestAnimationFrame(scrollAnimation);
    });
  }
});
