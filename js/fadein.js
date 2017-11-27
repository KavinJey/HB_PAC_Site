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

var toggle = false;
$(document).ready(function() {
  $("#mangatPic").click(function() {
    if (toggle == false) {
      $("#amanpreetPic").css("z-index", "-4200")
      $("#amanpreetPic").css("opacity", "0.6")
      $("#nishchayPic").css("z-index", "-4200")
      $("#nishchayPic").css("opacity", "0.6")
      $("#charithPic").css("z-index", "-4200")
      $("#charithPic").css("opacity", "0.6")
      $(".body").css("background-color", "#252530")
      $("#box1").fadeToggle();
      $("#box1").animate({left: '100px'});
      toggle = true;
    }
    else {
      $("#amanpreetPic").css("z-index", "420")
      $("#amanpreetPic").css("opacity", "1")
      $("#nishchayPic").css("z-index", "420")
      $("#nishchayPic").css("opacity", "1")
      $("#charithPic").css("z-index", "420")
      $("#charithPic").css("opacity", "1")
      $(".body").css("background-color", "#272739")
      $("#box1").fadeToggle();
      toggle = false;
    }
  });
});
