function updateSidebar() {
    const recordsContainer = document.getElementById('recordsContainer');
    recordsContainer.innerHTML = '';
    let records = JSON.parse(localStorage.getItem('records')) || [];
    records.forEach((record, index) => {
        let div = document.createElement('div');
        div.className = 'sidebar-item';
        div.innerHTML = `<span>${record.name}</span>
                        <span>
                            <button class="action-button" onclick="deleteRecord(${index})">Delete</button>
                            <button class="action-button" onclick="editRecord(${index})">Edit</button>
                        </span>`;
        recordsContainer.appendChild(div);
    });

    document.querySelectorAll('.sidebar-item').forEach(item => {
        item.addEventListener('click', () => {
            if (!e.target.classList.contains('action-button')) {
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
    let records = JSON.parse(localStorage.getItem('records')) || [];
    records.splice(index, 1);
    localStorage.setItem('records', JSON.stringify(records));
    updateSidebar();
}

function editRecord(index) {
    let records = JSON.parse(localStorage.getItem('records')) || [];
    let newName = prompt("Enter new name for the record:", records[index].name);
    if (newName) {
        records[index].name = newName;
        localStorage.setItem('records', JSON.stringify(records));
        updateSidebar();
    }
}

window.onload = updateSidebar;
window.addEventListener('storage', updateSidebar);