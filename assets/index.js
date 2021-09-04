
let default_value = 0;
let spanValue;
let barFill;
var starttime;
if (window.location.pathname == "/apps/efficiency") {
  
  const foundSpan = setInterval(() => {
    spanValue = document.getElementById("spanNumber").innerHTML;
    barFill = document.getElementById("rangeBarFill");
  
  }, 1000)

  function rangeBar(number) {
    const opacity = 0.95;
    const barFill = document.getElementById("rangeBarFill");
    // barFill.style.width = `${number}%`;
    // console.log("Entre")
    let color = "";
    if (number > 0 && number < 50) {
      color = `rgba(${231},${76},${60},${opacity})`;
      //rojo
    }
    if (number >= 50 && number < 60) {
      //naranja
      color = `rgba(${243},${157},${49},${opacity})`;
    }
    if (number >= 60 && number < 70) {
      //amarillo
      color = `rgba(${241},${196},${48},${opacity})`;
    }
    if (number >= 70) {
      color = `rgba(${97},${205},${115},${opacity})`;
      //verder
    }
    barFill.style.background = color;
  }
  function fillBarAnimation(timestamp, div, fill, duration) {
    var timestamp = timestamp || new Date().getTime();
    var runtime = timestamp - starttime;
    var progress = runtime / duration;
    progress = Math.min(progress, 1);
    div.style.width = (fill * progress).toFixed(2) + "%";
    if (runtime < duration) {
      // if duration not met yet
      requestAnimationFrame(function (timestamp) {
        // call requestAnimationFrame again with parameters
        fillBarAnimation(timestamp, div, fill, duration);
      });
    }
  }
  setInterval(() => {
    // console.log(spanValue)
    // console.log(default_value)
    if (parseFloat(spanValue) != default_value) {
    
      rangeBar(parseFloat(spanValue))
      requestAnimationFrame(function (timestamp) {
        starttime = timestamp || new Date().getTime(); //if browser doesn't support requestAnimationFrame, generate our own timestamp using Date
        fillBarAnimation(timestamp, barFill, parseFloat(spanValue), 1500); // 400px over 1 second
      })
      default_value = parseFloat(spanValue)
  
    }
    // if (spanValue) {
    
    //   clearInterval(foundSpan)
    //   console.log("Borrado", foundSpan)
    // }
  }, 500);
}
