function myFunction() {
  var checkBox = document.getElementById("checkbox");

  if (checkBox.checked == false){
    
    alert("請勾選同意條款");
} 
}

function positivenumber(){
  var number=document.getElementById("hotel_id");
  var id=number.value.trim()
  var int_id=Number(id)

  if (!Number.isInteger(int_id) || int_id<=0){
    alert("請輸入正整數")
  }else {
   window.location.href = "/hotel/" + int_id;
}}