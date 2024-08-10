/*
function openNewPage() {
  var urlInput = document.getElementById("urlInput").value;
  var selectElement = document.getElementById("options");
  var selectedOption = selectElement.value;
  
  if (urlInput && selectedOption) {
      // Full URL을 조합하여 이동
      var fullUrl = urlInput + '/' + selectedOption;
      location.href = fullUrl;
  } else {
      alert('Please enter a URL and select an option.');
  }
} */

// 새로운 페이지 여는 함수
function openNewPage() {  
    var selectElement = document.getElementById("options");  // 드롭다운 메뉴 요소 가져오기
    var selectedOption = selectElement.value;  // 선택된 옵션의 값 가져오기
    var urlInput = document.getElementById("urlInput").value.trim();  // URL 입력 필드의 값 가져오기 및 공백 제거
    
    if (urlInput && selectedOption) {  // 주소 입력과 옵션이 선택된 경우
        saveRecord(urlInput, selectedOption);  // 사이드바에 기록 추가 (URL + 선택된 옵션)
        location.href = selectedOption;  // 선택된 옵션 페이지로 이동
    } else {
        alert('옵션 선택과 주소 입력을 모두 다 해주세요.');  // 경고 메시지 표시
    }
}

// 검색 기록을 저장하는 함수
function saveRecord(url, option) {
    let records = JSON.parse(localStorage.getItem('records')) || [];  // 기존 기록을 가져오거나 빈 배열 생성
    const timestamp = new Date().toISOString();  // 현재 시간을 ISO 형식으로 저장
    records.push({ url, option, timestamp, name: url + "/" + option });  // 새 기록을 배열에 추가 (name을 url + "/" + option으로 사용)
    localStorage.setItem('records', JSON.stringify(records));  // 로컬 스토리지에 기록을 저장
    const iframeSidebar = document.getElementById('iframesidebar').contentWindow;  // iframe 요소를 가져옴
    iframeSidebar.updateSidebar();  // 사이드바 업데이트 함수 호출
}


// 검색 기록을 열어주는 함수
function openRecord(record) {         // 옵션 페이지 이동 
    if (record && record.option) {
        location.href = record.option;    // (백엔드와 연결 시 여기를 수정)
    } else {
        alert('Record not found.');
    }
}

// 로컬 스토리지 변경 시 사이드바 업데이트
window.addEventListener('storage', () => {
    const iframeSidebar = document.getElementById('iframesidebar').contentWindow;  // iframe 요소를 가져옴
    iframeSidebar.updateSidebar();  // 사이드바 업데이트 함수 호출
});

// Enter 키를 눌렀을 때 새로운 페이지 열기
document.onkeyup = function (e) {
    let keyCode = e.keyCode;  // 눌린 키의 키 코드를 가져옴
    if (keyCode === 13) openNewPage();  // Enter 키(키 코드 13)를 누르면 openNewPage 함수 호출
}