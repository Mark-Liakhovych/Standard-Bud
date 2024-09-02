document.addEventListener("DOMContentLoaded", function () {
  console.log('Js Started');

  const button = document.getElementById('myButton');
  if (!button) return; // Прекращаем выполнение, если элемент не найден

  // Проверяем ширину экрана перед запуском анимации
  if (window.innerWidth <= 575.98) {
    button.style.display = 'block';
  } else {
    const fillText = document.querySelector(".textContainer");
    const content = document.getElementById('content');
    const header = document.getElementById('header');
    const sections = [
      document.getElementById('ourmission'),
      document.getElementById('services'),
      document.getElementById('comingsoon'),
      document.getElementById('building'),
      document.getElementById('achievements'),
      document.getElementById('projects'),
      document.getElementById('key'),
      document.getElementById('faqs')
    ];
    const footer = document.getElementById('footer');

    header && header.classList.add('hidden');
    sections.forEach(section => section && section.classList.add('hidden'));
    footer && footer.classList.add('hidden');
    document.body.classList.add('no-scroll');

    if (fillText) {
      gsap.to(fillText, {
        backgroundPosition: "100% 100%",
        color: "#F8F8F8",
        duration: 1.6,
        ease: "none",
        onComplete: function () {
          fillText.classList.add("active");
          setTimeout(function () {
            content && content.classList.add('visible');
            header && header.classList.remove('hidden');
            header && header.classList.add('visible');
            sections.forEach(section => {
              section && section.classList.remove('hidden');
              section && section.classList.add('visible');
            });
            footer && footer.classList.remove('hidden');
            footer && footer.classList.add('visible');
            document.body.classList.remove('no-scroll');
          }, 1000);
        }
      });
    }
  }

  const burgerButton = document.getElementById('burger-button');
  if (burgerButton) {
    burgerButton.addEventListener('click', function () {
      const headerMenu = document.getElementById('header-menu');
      this.classList.toggle('active');
      headerMenu && headerMenu.classList.toggle('active');
      if (headerMenu && headerMenu.classList.contains('active')) {
        document.body.classList.add('no-scroll');
      } else {
        document.body.classList.remove('no-scroll');
      }
    });
  }

  // Модальные окна
  const modals = [
    { showBtn: ".show-modal1", mask: ".mask-modal1", modal: ".modal1", closeBtn: ".close-modal1", activeClass: "active1", modalActiveClass: "modal-active1" },
    { showBtn: ".show-modal2", mask: ".mask-modal2", modal: ".modal2", closeBtn: ".close-modal2", activeClass: "active2", modalActiveClass: "modal-active2" },
    { showBtn: ".show-modal3", mask: ".mask-modal3", modal: ".modal3", closeBtn: ".close-modal3", activeClass: "active3", modalActiveClass: "modal-active3" },
    { showBtn: ".show-modal4", mask: ".mask-modal4", modal: ".modal4", closeBtn: ".close-modal4", activeClass: "active4", modalActiveClass: "modal-active4" }
  ];

  modals.forEach(({ showBtn, mask, modal, closeBtn, activeClass, modalActiveClass }) => {
    const showButton = document.querySelector(showBtn);
    const maskElement = document.querySelector(mask);
    const modalElement = document.querySelector(modal);
    const closeButton = document.querySelector(closeBtn);

    if (showButton && maskElement && modalElement && closeButton) {
      showButton.addEventListener("click", () => {
        document.body.classList.add("modal-open");
        maskElement.classList.add(activeClass);
        modalElement.classList.add(modalActiveClass);
      });

      const closeModal = () => {
        maskElement.classList.remove(activeClass);
        modalElement.classList.remove(modalActiveClass);
        document.body.classList.remove("modal-open");
      };

      closeButton.addEventListener("click", closeModal);
      maskElement.addEventListener("click", closeModal);
    }
  });

  document.addEventListener("keyup", (e) => {
    if (e.keyCode === 27) { // Escape key
      modals.forEach(({ mask, modal, activeClass, modalActiveClass }) => {
        const maskElement = document.querySelector(mask);
        const modalElement = document.querySelector(modal);
        if (maskElement && modalElement) {
          maskElement.classList.remove(activeClass);
          modalElement.classList.remove(modalActiveClass);
          document.body.classList.remove("modal-open");
        }
      });
    }
  });

  // Анимация прокрутки
  const scrollContainer = document.getElementById("scrollContainer");
  if (scrollContainer) {
    let isScrolling = false;
    scrollContainer.addEventListener("wheel", function (e) {
      e.preventDefault();
      if (isScrolling) return;
      const scrollDistance = 630;
      isScrolling = true;
      let startScrollLeft = scrollContainer.scrollLeft;
      let endScrollLeft = startScrollLeft + scrollDistance * Math.sign(e.deltaY);
      let startTime = null;
      const scrollAnimation = (timestamp) => {
        if (!startTime) startTime = timestamp;
        const elapsedTime = timestamp - startTime;
        const duration = 500;
        const progress = Math.min(elapsedTime / duration, 1);
        const easeInOutQuad = (t) => (t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t);
        const newScrollLeft = startScrollLeft + (endScrollLeft - startScrollLeft) * easeInOutQuad(progress);
        scrollContainer.scrollLeft = newScrollLeft;
        if (progress < 1) {
          requestAnimationFrame(scrollAnimation);
        } else {
          isScrolling = false;
        }
      };
      requestAnimationFrame(scrollAnimation);
    });
  }

  // Аккордеоны
  const accordions = document.querySelectorAll(".accordion");
  accordions.forEach(accordion => {
    accordion.addEventListener("click", () => {
      const isOpen = accordion.classList.contains("open");
      accordions.forEach(a => a.classList.remove("open"));
      if (!isOpen) {
        accordion.classList.add("open");
      }
    });
  });
});





































































