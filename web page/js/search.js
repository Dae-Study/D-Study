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

function openNewPage() {
    var selectElement = document.getElementById("options");
    var selectedOption = selectElement.value;
    var urlInput = document.getElementById("urlInput").value.trim();
    
    if (selectedOption) {
        saveRecord(urlInput + "/" + selectedOption);
        location.href = selectedOption;
    } else {
        alert('Please select a page.');
    }
}

function saveRecord(query) {
    let records = JSON.parse(localStorage.getItem('records')) || [];
    const timestamp = new Date().toISOString();
    records.push({ query, timestamp, name: name || query });
    localStorage.setItem('records', JSON.stringify(records));
    const iframeSidebar = document.getElementById('iframesidebar').contentWindow;
    iframeSidebar.updateSidebar();
}

function openRecord(query) {  // 검색 결과 기록 함수
    location.href = query;    // 백엔드꺼 연결시 여기서!!
}

window.addEventListener('storage', () => {
    const iframeSidebar = document.getElementById('iframesidebar').contentWindow;
    iframeSidebar.updateSidebar();
});

document.onkeyup = function (e) {
    let keyCode = e.keyCode;
    if (keyCode === 13) openRecord();
}