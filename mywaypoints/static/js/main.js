function typecastRoutes(routes){
              routes.forEach(function(route){
                  route.bounds = asBounds(route.bounds);
                  // I don't think `overview_path` is used but it exists on the
                  // response of DirectionsService.route()
                  route.overview_path = asPath(route.overview_polyline);

                  route.legs.forEach(function(leg){
                      leg.start_location = asLatLng(leg.start_location);
                      leg.end_location   = asLatLng(leg.end_location);

                      leg.steps.forEach(function(step){
                          step.start_location = asLatLng(step.start_location);
                          step.end_location   = asLatLng(step.end_location);
                          step.path = asPath(step.polyline);
                      });

                  });
              });
          }

          function asBounds(boundsObject){
              return new google.maps.LatLngBounds(asLatLng(boundsObject.southwest),
                                              asLatLng(boundsObject.northeast));
          }

          function asLatLng(latLngObject){
              return new google.maps.LatLng(latLngObject.lat, latLngObject.lng);
          }

          function asPath(encodedPolyObject){
              return google.maps.geometry.encoding.decodePath(encodedPolyObject.points);
          }

          


// (function($) {
//   "use strict"; // Start of use strict

//   // Smooth scrolling using jQuery easing
//   $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
//     if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
//       var target = $(this.hash);
//       target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
//       if (target.length) {
//         $('html, body').animate({
//           scrollTop: (target.offset().top - 56)
//         }, 1000, "easeInOutExpo");
//         return false;
//       }
//     }
//   });

//   // Closes responsive menu when a scroll trigger link is clicked
//   $('.js-scroll-trigger').click(function() {
//     $('.navbar-collapse').collapse('hide');
//   });

//   // Activate scrollspy to add active class to navbar items on scroll
//   // $('body').scrollspy({
//   //   target: '#mainNav',
//   //   offset: 57
//   // });

//   // Collapse Navbar
//   // var navbarCollapse = function() {
//   //   if ($("#mainNav").offset().top > 100) {
//   //     $("#mainNav").addClass("navbar-shrink");
//   //   } else {
//   //     $("#mainNav").removeClass("navbar-shrink");
//   //   }
//   // };
//   // Collapse now if page is not at top
//   // navbarCollapse();
//   // Collapse the navbar when page is scrolled
//   $(window).scroll(navbarCollapse);

//   // Scroll reveal calls
//   window.sr = ScrollReveal();

//   sr.reveal('.sr-icon-1', {
//     delay: 200,
//     scale: 0
//   });
//   sr.reveal('.sr-icon-2', {
//     delay: 400,
//     scale: 0
//   });
//   sr.reveal('.sr-icon-3', {
//     delay: 600,
//     scale: 0
//   });
//   sr.reveal('.sr-icon-4', {
//     delay: 800,
//     scale: 0
//   });
//   sr.reveal('.sr-button', {
//     delay: 200,
//     distance: '15px',
//     origin: 'bottom',
//     scale: 0.8
//   });
//   sr.reveal('.sr-contact-1', {
//     delay: 200,
//     scale: 0
//   });
//   sr.reveal('.sr-contact-2', {
//     delay: 400,
//     scale: 0
//   });

//   // Magnific popup calls
//   $('.popup-gallery').magnificPopup({
//     delegate: 'a',
//     type: 'image',
//     tLoading: 'Loading image #%curr%...',
//     mainClass: 'mfp-img-mobile',
//     gallery: {
//       enabled: true,
//       navigateByImgClick: true,
//       preload: [0, 1]
//     },
//     image: {
//       tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
//     }
//   });

// }); // End of use strict
