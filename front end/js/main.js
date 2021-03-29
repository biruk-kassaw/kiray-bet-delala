$(document).ready(function () {
  /* Check width on page load*/
  if ($(window).width() < 993) {
    $('.menu-button').addClass('hide'); 
  }
  else { }
});

$(window).resize(function () {
  /*If browser resized, check width again */
  if ($(window).width() < 993) {
    $('.menu-button').removeClass('hide');
  }
  else { 
    $('.menu-button').addClass('hide'); 
  }
});

$(function () {
  var hasBeenTrigged = false;
  $(window).scroll(function () {
    if ($(this).scrollTop() >= 100 && !hasBeenTrigged) { // if scroll is greater/equal then 100 and hasBeenTrigged is set to false.
      $('nav').addClass('small-nav'); 
      hasBeenTrigged = true;
    } else if ($(this).scrollTop() <= 100 && hasBeenTrigged) {
      $('nav').removeClass('small-nav');
      hasBeenTrigged = false;
    }
  });
});
//Toogle Mobile Menu
$(".menu-button").click(function () {
  $('.menu').toggleClass('slide');
});
// Scroll To Section of Page
$(document).on('click', 'a[href^="#"]', function (e) {
  e.preventDefault();
  $('.menu').removeClass('slide');
  $('html, body').stop().animate({
    scrollTop: $($(this).attr('href')).offset().top
  }, 800, 'linear');
});

var logout = document.getElementById("logoutlink");
logout.addEventListener("click", function (e) {
  e.preventDefault();
  axios.get('http://127.0.0.1:5000/api/v1/users/logout')
  .then(function (response) {
    document.location.reload()
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })

  
})