function updateSidebar() {
    const recordsContainer = document.getElementById('recordsContainer');
    recordsContainer.innerHTML = '';
    let records = JSON.parse(localStorage.getItem('records')) || [];
    records.forEach((record, index) => {
        let div = document.createElement('div');
        div.className = 'sidebar-item';
        div.innerHTML =  `<span>${record.name}</span>
                          <button class="edit-button" onclick="editRecord(${index})">✐</button>
                          <button class="delete-button" onclick="deleteRecord(${index})">✖</button>`;
        recordsContainer.appendChild(div);
    });

    document.querySelectorAll('.sidebar-item').forEach(item => {
        item.addEventListener('click', (e) => {
            if (!e.target.classList.contains('edit-button') && !e.target.classList.contains('delete-button')) {
                const recordIndex = Array.from(item.parentNode.children).indexOf(item);
                const record = records[recordIndex];
                if (record) {  // 검색 결과 기록 함수
                    parent.openRecord(record.query);
                } else {
                    alert('Content not found.');
                }
            }
        });
    });
}

function deleteRecord(index) {
    if (confirm("삭제하시겠습니까?")) {
        let records = JSON.parse(localStorage.getItem('records')) || [];
        records.splice(index, 1);
        localStorage.setItem('records', JSON.stringify(records));
        updateSidebar();
    }
}

function editRecord(index) {
    let records = JSON.parse(localStorage.getItem('records')) || [];
    let newName = prompt("제목을 입력하세요:", records[index].name);
    if (newName) {
        records[index].name = newName;
        localStorage.setItem('records', JSON.stringify(records));
        updateSidebar();
    }
}

window.onload = updateSidebar;
window.addEventListener('storage', updateSidebar);