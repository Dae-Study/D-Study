// 로그인 입력 필드와 버튼 요소 가져오기
const loginFN = document.getElementById('LOGIN_FN');  // 성 입력 필드
const loginN = document.getElementById('LOGIN_N');  // 이름 입력 필드
const loginBtn = document.getElementById('LOGIN_BTN');  // 로그인 버튼

// 입력 필드의 내용에 따라 버튼 색상과 상태 변경하는 함수
function color() {
    // 두 입력 필드가 모두 비어있지 않은 경우
    if (loginFN.value.length > 0 && loginN.value.length > 0) {
        loginBtn.style.backgroundColor = "rgb(97, 132, 189)";  // 버튼 색상을 활성화 색상으로 변경
        loginBtn.disabled = false;  // 버튼 활성화
    } else {
        loginBtn.style.backgroundColor = "rgba(153, 193, 238, 0.745)";  // 버튼 색상을 비활성화 색상으로 변경
        loginBtn.disabled = true;  // 버튼 비활성화
    }
}

// 로그인 버튼을 클릭하면 search.html로 이동하는 함수
function moveToIndex() {
    location.href = "search.html";  // search.html 페이지로 이동
}

// 입력 필드에 키를 눌렀을 때 color 함수 호출
loginFN.addEventListener('keyup', color);  // 성 입력 필드에 이벤트 리스너 추가
loginN.addEventListener('keyup', color);  // 이름 입력 필드에 이벤트 리스너 추가

// 로그인 버튼을 클릭했을 때 moveToIndex 함수 호출
loginBtn.addEventListener('click', moveToIndex);

// Enter 키를 눌렀을 때 moveToIndex 함수 호출
document.onkeyup = function (e) {
    let keyCode = e.keyCode;  // 눌린 키의 코드 가져오기
    if (keyCode === 13) moveToIndex();  // Enter 키(코드 13)를 눌렀을 때 moveToIndex 함수 호출
}
