;(function($) {
    'use strict'

    var retinaLogo =  function() {
        var retina = window.devicePixelRatio > 1 ? true : false;
        var $logo = $('.site-logo img');
        var $logo_retina = $logo.data('retina');

        if ( retina && $logo_retina ) {
            $logo.attr({
                src: $logo.data('retina'),
                width: $logo.data('width'),
                height: $logo.data('height')
            });
        }
    };

    var searchIcon =  function() {
        if ( !$('body').hasClass('header-style-5') ) {
            $('.header-search-icon').on('click', function() {
                var searchForm = $(this).parent().find('.header-search-form'),
                    searchField = $(this).parent().find('.header-search-field');

                searchForm.stop().fadeToggle(function () {
                    searchField.focus();
                });

                return false;
            });
        }
    };

    var mobiNav = function() {
        var menuType = 'desktop';

        $(window).on('load resize', function() {
            var
            mode = 'desktop',
            wrapMenu = $('#site-header .wrap-inner');

            if ( matchMedia( 'only screen and (max-width: 991px)' ).matches )
                mode = 'mobile';

            if ( mode != menuType ) {
                menuType = mode;

                if ( mode == 'mobile' ) {
                    $('#main-nav').attr('id', 'main-nav-mobi')
                        .appendTo('#site-header')
                        .hide().children('.menu')
                            .find('li:has(ul)')
                            .children('ul')
                                .removeAttr('style')
                                .hide()
                                .before('<span class="arrow"></span>');
                } else {
                    $('#main-nav-mobi').attr('id', 'main-nav')
                        .removeAttr('style')
                        .appendTo(wrapMenu)
                        .find('.sub-menu')
                            .removeAttr('style')
                        .prev().remove();
                            
                    $('.mobile-button').removeClass('active');
                }
            }
        });

        $(document).on('click', '.mobile-button', function() {
            $(this).toggleClass('active');
            $('#main-nav-mobi').slideToggle();
        })

        $(document).on('click', '#main-nav-mobi .arrow', function() {
            $(this).toggleClass('active').next().slideToggle();
        })
    };

    var headerFixed = function() {
        if ( $('body').hasClass('header-fixed') ) {
            var nav = $('#site-header');
            if ( nav.length ) {
                var offsetTop = nav.offset().top,
                    headerHeight = nav.height(),
                    injectSpace = $('</div>', {
                        height: headerHeight
                    }).insertAfter(nav);

                $(window).on('load scroll', function(){
                    if ( $(window).scrollTop() > offsetTop ) {
                        nav.addClass('is-fixed');
                        injectSpace.show();
                    } else {
                        nav.removeClass('is-fixed');
                        injectSpace.hide();
                    }

                    if ( $(window).scrollTop() > 400 ) { 
                        nav.addClass('is-small');
                    } else {
                        nav.removeClass('is-small');
                    }
                })
            }
        }     
    };
    
    var videoPopup = function() {
        if ( $().magnificPopup ) {
            $('.popup-video').magnificPopup({
                disableOn: 700,
                type: 'iframe',
                mainClass: 'mfp-fade',
                removalDelay: 160,
                preloader: false,
                fixedContentPos: true
            });
        };
    };

    var imagePopup = function() {
        if ( $().magnificPopup ) {
            $('.popup-image').magnificPopup({
                disableOn: 700,
                type: 'image',
                gallery:{
                    enabled: true
                },
                mainClass: 'mfp-fade',
                removalDelay: 160,
                preloader: false,
                fixedContentPos: true
            });
        };
    };

    var scrollToTop =  function() {
        $(window).scroll(function() {
            if ( $(this).scrollTop() > 800 ) {
                $('#scroll-top').addClass('show');
            } else {
                $('#scroll-top').removeClass('show');
            }
        });

        $('#scroll-top').on('click', function() {
            $('html, body').animate({ scrollTop: 0 }, 1000 , 'easeInOutExpo');
        return false;
        });
    };

    var preLoader =  function() {
        if ( $().animsition ) {
            $('.animsition').animsition({
                inClass: 'fade-in',
                outClass: 'fade-out',
                inDuration: 1500,
                outDuration: 800,
                loading: true,
                loadingParentElement: 'body',
                loadingClass: 'animsition-loading',
                timeout: false,
                timeoutCountdown: 5000,
                onLoadEvent: true,
                browser: [
                    '-webkit-animation-duration',
                    '-moz-animation-duration',
                    'animation-duration'
                    ],
                overlay: false,
                overlayClass: 'animsition-overlay-slide',
                overlayParentElement: 'body',
                transition: function(url){ window.location.href = url; }
            });
        }
    };

    var animateWOW =  function() {
        new WOW().init();
    };

    var parallax =  function() {
        var iOS = ( navigator.userAgent.match(/(iPad|iPhone|iPod)/g) ? true : false );
        /*
         * Please note that background attachment fixed doesn't work on iOS
         */ 
        if (!iOS) {
            $('.parallax').css({backgroundAttachment:'fixed'});
        } else {
            $('.parallax').css({backgroundAttachment:'scroll'});
        }

        if ( $().parallax && matchMedia( 'only screen and (min-width: 992px)' ).matches ) {
            $('.row-projects').parallax("50%", 0.45);

        }
    };

    var inViewport =  function() {
        $('[data-inviewport="yes"]').waypoint(function() {
            $(this).trigger('on-appear');
        }, { offset: '90%', triggerOnce: true });

        $(window).on('load', function() {
            setTimeout(function() {
                $.waypoints('refresh');
            }, 100);
        });
    };

    // Dom Ready
    $(function() {
        retinaLogo();
        searchIcon();
        mobiNav();
        headerFixed();
        videoPopup();
        imagePopup();
        scrollToTop();
        preLoader();
        animateWOW();
        $( window ).load(function() {
            parallax();
            inViewport();
        });
    });

})(jQuery);