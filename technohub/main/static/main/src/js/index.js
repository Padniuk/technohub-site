window.onload = function(){
  var slides = document.getElementsByClassName('about__content-slide'),
      addActive = function(slide) {slide.classList.add('active')},
      removeActive = function(slide) {slide.classList.remove('active')};
  addActive(slides[0]);
  
  setInterval(function (){
    for (var i = 0; i < slides.length; i++){
      if (i + 1 == slides.length) {
        addActive(slides[0]);
        slides[0].style.zIndex = 100;
        setTimeout(removeActive, 350, slides[i])
        break;
      }
      if (slides[i].classList.contains('active')) { 
        slides[i].removeAttribute('style');
        setTimeout(removeActive, 350, slides[i]);
        addActive(slides[i + 1]);
        break;
      }
    } 
  }, 8000);
}

function isElementInViewport(el) {
  const rect = el.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
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


document.addEventListener("DOMContentLoaded", function() {
  const faqDetails = document.querySelectorAll("faq__content-details");

  faqDetails.forEach(detail => {
      detail.addEventListener("toggle", function() {
          this.classList.toggle("open");
      });
  });
});
