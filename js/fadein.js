// Test Functions
$(document).ready(function() {
  $("#simratPic").click(function() {
    $("#simratProfile").fadeToggle();
  });
});

$(document).ready(function() {
  $("#rupreetPic").click(function() {
    $("#rupreetProfile").fadeToggle();
  });
});

$(document).ready(function() {
  $("#ameliaPic").click(function() {
    $("#ameliaProfile").fadeToggle();
  });
});

$(document).ready(function() {
  $("#bobPic").click(function() {
    $("#bobProfile").fadeToggle();
  });
});

$(document).ready(function() {
  $("#manrosePic").click(function() {
    $("#manroseProfile").fadeToggle();
  });
});

// Clicking on Mangat's Portrait
var toggle = false;
$(document).ready(function() {
  $("#mangatPic").click(function() {
    // if description hasn't been toggled already
    if (toggle == false) {
      // dim all other pictures and background
      $("#amanpreetPic").css("z-index", "-4200")
      $("#amanpreetPic").css("opacity", "0.6")
      $("#nishchayPic").css("z-index", "-4200")
      $("#nishchayPic").css("opacity", "0.6")
      $("#charithPic").css("z-index", "-4200")
      $("#charithPic").css("opacity", "0.6")
      $(".body").css("background-color", "#252530")
      // fade in box and slide in to the right
      $("#box1").fadeToggle();
      $("#box1").animate({left: '120px'});
      // toggle variable
      toggle = true;
    }
    // if the description has been toggled already
    else {
      // reset the state of all the other pictures and background
      $("#amanpreetPic").css("z-index", "420")
      $("#amanpreetPic").css("opacity", "1")
      $("#nishchayPic").css("z-index", "420")
      $("#nishchayPic").css("opacity", "1")
      $("#charithPic").css("z-index", "420")
      $("#charithPic").css("opacity", "1")
      $(".body").css("background-color", "#272739")
      // fade out the box
      $("#box1").fadeToggle();
      // toggle variable
      toggle = false;
    }
  });
});
