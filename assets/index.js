
let default_value = 0;
let spanValue
let barFill
const foundSpan = setInterval(() => {
  spanValue = document.getElementById("spanNumber").innerHTML;
  barFill = document.getElementById("rangeBarFill");
  console.log("Iniciados")
},500)

function rangeBar(number) {
  const opacity = 0.5;
  barFill.style.width = `${number}%`;
  console.log("Entre")
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

setInterval(() => {
  console.log(spanValue)
  console.log(default_value)
  if (parseFloat(spanValue) != default_value) {
    
    rangeBar(parseFloat(spanValue))
    default_value = parseFloat(spanValue)
  
  }
  // if (spanValue) {
    
  //   clearInterval(foundSpan)
  //   console.log("Borrado", foundSpan)
  // }
},500);
