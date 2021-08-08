$.global = new Object();

$.global.item = 1;
$.global.total = 0;

$(document).ready(function() 
	{

	var WindowWidth = $('.card-videos').width();
	var SlideCount = $('#slides iframe').length;
	var SlidesWidth = SlideCount * WindowWidth;


  if (SlideCount < 1) {
      var elementleft = document.querySelector("#left");
      elementleft.addEventListener("mousedown", event => {
         alert('You haven\'t uploaded any videos, click upload!');
      });
  }
  if (SlideCount < 1) {
      var elementright = document.querySelector("#right");
      elementright.addEventListener("mousedown", event => {
         alert('You haven\'t uploaded any videos, click upload!');
      });
  }


	
   $.global.item = 0;
    $.global.total = SlideCount; 
    
	$('.slide').css('width',WindowWidth+'px');
	$('#slides').css('width',SlidesWidth+'px');

  $("#slides li:nth-child(1)").addClass('active');
  

    
  $('#left').click(function() { Slide('back'); }); 

  $('#right').click(function() { Slide('forward'); }); 

   
  });

function Slide(direction)
	{
 

     if (direction == 'back') { 
       var $target = $.global.item - 1;
       $(".slide").removeClass('active');
       let frames = document.getElementsByTagName("iframe")[$.global.item+0].src += '';
   };
 
 
     if (direction == 'forward') { 
       var $target = $.global.item + 1;
       $(".slide").removeClass('active');
       let frames = document.getElementsByTagName("iframe")[$.global.item+0].src += '';
      }  
     
     if ($target == -1) { DoIt($.global.total-1); } 
     else if ($target == $.global.total) { DoIt(0); }  
     else { DoIt($target); }

    
	}

function DoIt(target)
  {
   
    var $windowwidth = $('.card-videos').width();
	  var $margin = $windowwidth * target; 
    var $actualtarget = target+1;
  
    
    $("#slides li:nth-child("+$actualtarget+")").addClass('active');

   
    
    $('#slides').css('transform','translate3d(-'+$margin+'px,0px,0px)');	
    
    $.global.item = target; 
    

  }


