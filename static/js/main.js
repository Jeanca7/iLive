function showPeriod(){
  let rentCheckBox = document.getElementById("rent_checkbox");
  let shareCheckBox = document.getElementById("share_checkbox");
  let period = document.getElementById("period");
  
  if (rentCheckBox.checked == true || shareCheckBox.checked == true){
    period.style.display = "block";
  }else{
    period.style.display = "none";
  }
}

