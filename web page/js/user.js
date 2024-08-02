const loginN = document.getElementById('LOGIN_N');
const loginFN = document.getElementById('LOGIN_FN');
const loginBtn = document.getElementById('LOGIN_BTN');

function color() {
    if(loginN.value.length > 0 && loginFN.value.length > 0){
        loginBtn.style.backgroundColor = "rgb(97, 132, 189)";
        loginBtn.disabled = false;
    }else{
        loginBtn.style.backgroundColor = "rgba(153, 193, 238, 0.745)";
        loginBtn.disabled = true;
    }
}

function moveToIndex(){
    location.href="search.html";
}

loginN.addEventListener('keyup', color);
loginFN.addEventListener('keyup', color);
loginBtn.addEventListener('click',moveToIndex);

document.onkeyup = function (e) {
    let keyCode = e.keyCode;
    if (keyCode === 13) moveToIndex();
}