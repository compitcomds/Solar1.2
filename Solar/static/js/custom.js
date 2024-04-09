/*--------------------- Copyright (c) 2019 -----------------------
[Master Javascript]
Project: Interior Design - Multipurpose Responsive HTML Template
Version: 
Assigned to: 
-------------------------------------------------------------------*/

(function ($) {
	"use strict";
	var Solar = {
		initialised: false,
		version: 1.0,
		mobile: false,
		init: function () {

			if(!this.initialised) {
				this.initialised = true;
			} else {
				return;
			}

		/*-------------- Solar Installation Functions Calling ---------------------------------------------------
		------------------------------------------------------------------------------------------------*/

			this.Testimonial_slider();
			this.Blog();
			this.Partner();
			this.Gallery();
			this.Bottom();
			this.Toggle();
			this.Counter();
			this.Product();
			
		},
		
		/*-------------- Solar Installation Functions Calling ---------------------------------------------------
		---------------------------------------------------------------------------------------------------*/

		
		// Testimonial__slider
			Testimonial_slider: function(){
				if($('.solar_testimonial_slider .swiper-container').length > 0){
				var swiper = new Swiper('.solar_testimonial_slider .swiper-container', {
				  spaceBetween: 30,
				  speed: 800,
				  loop: true,
				  centeredSlides: true,
				  autoplay: {
					delay: 2500,
					disableOnInteraction: false,
				  },
				  pagination: {
					el: '.swiper-pagination',
					clickable: true,
				  },
				  navigation: {
					nextEl: '.solar_testimonial_slider .swiper-button-next',
					prevEl: '.solar_testimonial_slider .swiper-button-prev',
				  },
				});
				}
			},
		// Testimonial__slider


		// Product Post Slide
		// Product Post Slide
// Product Post Slide
Product: function() {
    if ($('.solar_product_section .swiper-container').length > 0) {
        var swiper = new Swiper('.solar_product_section .swiper-container', {
            loop: true,
            slidesPerView: 4,
            spaceBetween: 10,
            autoplay: {
                delay: 1500,
                disableOnInteraction: false,
            },
            breakpoints: {
                2000:{
                    slidesPerView: 3,
                    spaceBetween: 30,
                },
				1300: {
					slidesPerView: 4,
					spaceBetween: 15,
				},
				1000:{
                    slidesPerView: 3,
                    spaceBetween: 30,
                },
                768: {
                    slidesPerView: 2,
                    spaceBetween: 10,
                },
                440: {
                    slidesPerView: 1,
                    spaceBetween: 10,
                }
            }
        });

        // Pause autoplay on mouseenter
        $('.solar_product_section .swiper-container').on('mouseenter', function() {
            swiper.autoplay.stop();
        });

        // Resume autoplay on mouseleave
        $('.solar_product_section .swiper-container').on('mouseleave', function() {
            swiper.autoplay.start();
        });
    }
}
,
		// Product Post Slide
		// Blog Post Slider 
			Blog: function(){  
				if($('.solar_team_section .swiper-container').length > 0){
					var swiper = new Swiper('.solar_team_section .swiper-container', {
					  slidesPerView: 3,
					  spaceBetween: 10,
					  speed: 600,
					  pagination: {
						el: '.swiper-pagination',
						clickable: true,
					  },
					  autoplay: {
						delay: 2500,
						disableOnInteraction: false,
					  },
					  breakpoints: {
						1024: {
						  slidesPerView: 2,
						  spaceBetween: 30,
						},
						768: {
						  slidesPerView: 2,
						  spaceBetween: 30,
						},
						640: {
						  slidesPerView: 1,
						  spaceBetween: 20,
						},
						320: {
						  slidesPerView: 1,
						  spaceBetween: 10,
						}
					  }
					});
				}
			},
		// // Blog Post Slider
		
		// // Partner Slider 
			Partner: function(){  
				if($('.solar_partner_section .swiper-container').length > 0){
					 var swiper = new Swiper('.solar_partner_section .swiper-container', {
					  slidesPerView: 5,
					  spaceBetween: 50,
					  // init: false,
					  autoplay: {
						delay: 2000,
						disableOnInteraction: false,
					  },
					  breakpoints: {
						1024: {
						  slidesPerView: 4,
						  spaceBetween: 30,
						},
						768: {
						  slidesPerView: 4,
						  spaceBetween: 15,
						},
						760: {
						  slidesPerView: 3,
						  spaceBetween: 10,
						},
						440:{
							slidesPerView: 2,
							spaceBetween: 10,
						},
						380: {
						  slidesPerView: 1,
						  spaceBetween: 10,
						}
					  }
					});
				}
			},
		// Partner
		
		// Gallery
			Gallery: function(){  
				if($('.solar_portfolio').length > 0){
					
					$(document).on('click', '[data-toggle="lightbox"]', function(event) {
					event.preventDefault();
					$(this).ekkoLightbox();
					});

				}
			},
		// Gallery
		
		// Bottom To Top
			Bottom: function(){  
				if($('#button').length > 0){
					
					var btn = $('#button');

					$(window).scroll(function() {
					  if ($(window).scrollTop() > 300) {
						btn.addClass('show');
					  } else {
						btn.removeClass('show');
					  }
					});

					btn.on('click', function(e) {
					  e.preventDefault();
					  $('html, body').animate({scrollTop:0}, '300');
					});


				}
			},
		// Bottom To Top
		
		// Toggle			
			Toggle: function () {
					$(".solar_toggle").click(function() {
					$(".solar_menus").toggleClass('solar_menu_show');
					});
				
					$('.solar-close-icon').on('click', function(){
					$('.solar_menus.solar_menu_show').removeClass('solar_menu_show')
					});
				
			},
		// Toggle
		
		// Counter			
			Counter: function () {
				if($(".solar_counter").length > 0){
					
					
					$('.count').each(function () {
						$(this).prop('Counter',0).animate({
							Counter: $(this).text()
						}, {
							duration: 4000,
							easing: 'swing',
							step: function (now) {
								$(this).text(Math.ceil(now));
							}
						});
					});
					
				}
			},
		// Counter
		
		
	
		
		
		
	/*------------------------------------------------------------------*/ 
	
	};
	Solar.init();	 
	
		
}(jQuery));	


new WOW().init();








// Contact Form Submission
function checkRequire(formId , targetResp){
targetResp.html('');
var email = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/;
var url = /(http|ftp|https):\/\/[\w-]+(\.[\w-]+)+([\w.,@?^=%&amp;:\/~+#-]*[\w@?^=%&amp;\/~+#-])?/;
var image = /\.(jpe?g|gif|png|PNG|JPE?G)$/;
var mobile = /^[\s()+-]*([0-9][\s()+-]*){6,20}$/;
var facebook = /^(https?:\/\/)?(www\.)?facebook.com\/[a-zA-Z0-9(\.\?)?]/;
var twitter = /^(https?:\/\/)?(www\.)?twitter.com\/[a-zA-Z0-9(\.\?)?]/;
var google_plus = /^(https?:\/\/)?(www\.)?plus.google.com\/[a-zA-Z0-9(\.\?)?]/;
var check = 0;
$('#er_msg').remove();
var target = (typeof formId == 'object')? $(formId):$('#'+formId);
target.find('input , textarea , select').each(function(){
if($(this).hasClass('require')){
if($(this).val().trim() == ''){
check = 1;
$(this).focus();
targetResp.html('You missed out some fields.');
$(this).addClass('error');
return false;
}else{
$(this).removeClass('error');
}
}
if($(this).val().trim() != ''){
var valid = $(this).attr('data-valid');
if(typeof valid != 'undefined'){
if(!eval(valid).test($(this).val().trim())){
$(this).addClass('error');
$(this).focus();
check = 1;
targetResp.html($(this).attr('data-error'));
return false;
}else{
$(this).removeClass('error');
}
}
}
});
return check;
}
$(".submitForm").on("click", function() {
var _this = $(this);
var targetForm = _this.closest('form');
var errroTarget = targetForm.find('.response');
var check = checkRequire(targetForm , errroTarget);

if(check == 0){
var formDetail = new FormData(targetForm[0]);
formDetail.append('form_type' , _this.attr('form-type'));
$.ajax({
method : 'post',
url : 'ajaxmail.php',
data:formDetail,
cache:false,
contentType: false,
processData: false
}).done(function(resp){
console.log(resp);
if(resp == 1){
targetForm.find('input').val('');
targetForm.find('textarea').val('');
errroTarget.html('<p style="color:white;">Mail has been sent successfully.</p>');
}else{
errroTarget.html('<p style="color:white;">Something went wrong please try again latter.</p>');
}
});
}
});


