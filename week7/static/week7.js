async function signup(){
    let name=document.querySelector("#signup-name").value;
    let email=document.querySelector("#signup-email").value;
    let password=document.querySelector("#signup-password").value;

    if(name === "" || email === "" || password === ""){
        alert("姓名、信箱或密碼不可為空格！"); 
        return 
    }
    
    let response=await fetch("/signup",{
        method:"POST",
        headers: {
            "Content-Type": "application/json"
        },
        body:JSON.stringify({"name":name,"email":email,"password":password})
    });
    
    if(response.redirected){
        window.location.href = response.url;}
    }

async function signin(){
    let email=document.querySelector("#signin-email").value;
    let password=document.querySelector("#signin-password").value;
    
    if(email === "" || password === ""){
        alert("信箱或密碼不可為空格！"); 
        return 
    }
    
    let response=await fetch("/login",{
        method:"POST",
        headers: {
            "Content-Type": "application/json"
        },
        body:JSON.stringify({"email":email,"password":password})
    });
    
    if(response.redirected){
        window.location.href = response.url;} 
}

async function findMember(){
    let member_id=document.querySelector("#findMember").value;
    let member=document.querySelector("#member");
    
    if(member_id === ""){ 
        alert("會員編號不可為空格！"); 
        return 
    }
    
    let response=await fetch("/api/member/"+ member_id,{
        method:"GET",
    }); 
    let result=await response.json();
    
    if (result.data !== null && result.data) {
        member.innerHTML = "<div>" + result.data.name + "(" + result.data.email + ")</div>";
    } else {
        member.innerHTML = "<div>No Data</div>"; 
    }
}

async function updateName() {
    let newName = document.querySelector("#newName").value;
    let success=document.querySelector("#success");
    let welcomeName=document.querySelector("#welcomeName");

    if( newName === ""){
        alert("輸入不可為空格！"); 
        return 
    }

    let response=await fetch("/api/member", {
        method: 'PATCH',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data = {"name": newName})
        })
        let result=await response.json();
            
        if (result.ok) {
            success.innerHTML = "<div>更新成功</div>"; 
            welcomeName.innerHTML = newName + "，歡迎登入系統";
        } else {
            success.innerHTML = "<div>更新失敗</div>";  
        }
};

async function getFullrecords(){
    let searched=document.querySelector("#searched");
    
    let response=await fetch("/api/records",{
        method:"GET",
    }); 
    let result=await response.json();
    searched.innerHTML="";
    if(result.data !== null){
    for(let i=0; i<result.data.length;i++){
        let displayTime = result.data[i].time.replace('T', ' ');
        searched.innerHTML += "<div>" + 
        result.data[i].name + "(" + displayTime + ")"+"</div>";
}}else{
    searched.innerHTML = "<div>目前無被查詢紀錄 </div>";
}
}
getFullrecords();
