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
    
    if (selectedOption) {
        location.href = selectedOption;
    } else {
        alert('Please select a page.');
    }
}