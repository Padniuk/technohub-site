function isElementInViewport(el) {
  const rect = el.getBoundingClientRect();
  const viewportHeight = window.innerHeight;
 
  return (
    rect.top >= 0 &&
    rect.bottom <= (window.innerHeight + 1 || document.documentElement.clientHeight + 1)
  );
}

function handleScroll() {
  const header = document.querySelector('header');
  const footer = document.querySelector('footer');
  const telegramLink = document.querySelector('.telegram-link');

  if (isElementInViewport(header) || isElementInViewport(footer)) {
    telegramLink.style.display = 'none';
  } else {
    telegramLink.style.display = 'block';
  }
}

window.addEventListener('scroll', handleScroll);