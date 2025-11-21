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

async function createMessage(){
    let message=document.querySelector("#createMessage").value;
    
    if(message === ""){
        alert("留言不可為空格！"); 
        return 
    }
    
    let response=await fetch("/createMessage",{
        method:"POST",
        headers: {
            "Content-Type": "application/json"
        },
        body:JSON.stringify({"content":message}) 
    });
    
    if(response.redirected){
        window.location.href = response.url;} 
}

async function deleteMessage(messageId){ 
    if (confirm("確定要刪除這則留言嗎？") === false) {
        return; 
    }
    let response = await fetch("/deleteMessage", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
       
        body: JSON.stringify({ "message_id": messageId }) 
    });
    
    if (response.redirected) {
        window.location.href = response.url;} 
}