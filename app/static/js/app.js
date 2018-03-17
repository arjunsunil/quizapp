var count =0
var timeleft = 600
function convertSeconds(s) {
  min = floor(s/60);
  sec = s % 60;
  return nf(min,2) + " : " + nf(sec,2)
}
function setup(){
  noCanvas();
  var timer = select("#timer");
  timer.html(convertSeconds(timeleft - count));
  function timelt() {
    count++;
    timer.html(convertSeconds(timeleft -count));
    if ((timeleft -count) == 0 ){
      document.getElementById("submit").click();
    }
  }
  setInterval(timelt,1000)
}
$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});
