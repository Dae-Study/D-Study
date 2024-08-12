// 사이드바를 업데이트하는 함수
function updateSidebar() {
    const recordsContainer = document.getElementById('recordsContainer');  // 사이드바 컨테이너 요소를 가져옴
    recordsContainer.innerHTML = '';  // 기존 내용을 지움
    let records = JSON.parse(localStorage.getItem('records')) || [];  // 로컬 스토리지에서 기록을 가져오거나 빈 배열 생성
    console.log(records);
    
    // 기록 배열을 역순으로 처리하여 가장 최근 기록이 위로 오도록 함
    records.slice().reverse().forEach((record, index) => {
        let div = document.createElement('div');  // 새로운 div 요소 생성
        div.className = 'sidebar-item';  // 클래스 이름 설정
        div.innerHTML = `<span>${record.name}</span>
                         <button class="edit-button" onclick="editRecord(${index})">✐</button>
                         <button class="delete-button" onclick="deleteRecord(${index})">✖</button>`;  // 기록 이름과 편집/삭제 버튼 추가
        recordsContainer.appendChild(div);  // 기존 내용 아래에 새 기록 추가
    });

    // 각 사이드바 항목에 클릭 이벤트 리스너 추가
    document.querySelectorAll('.sidebar-item').forEach((item, index) => {
        item.addEventListener('click', (e) => {
            // 편집 또는 삭제 버튼이 클릭되지 않은 경우에만 기록을 엶
            if (!e.target.classList.contains('edit-button') && !e.target.classList.contains('delete-button')) {
                // 역순으로 처리했으므로 인덱스 조정 필요
                const actualIndex = records.length - 1 - index;
                const record = records[actualIndex];  // 역순에서 원래 인덱스 계산하여 해당 기록을 가져옴
                if (record) {  // 기록이 있는 경우
                    parent.openRecord(record);  // 부모 창에서 openRecord 함수 호출
                } else {
                    alert('Content not found.');  // 기록이 없는 경우 경고 메시지 표시
                }
            }
        });
    });
}

// 기록을 삭제하는 함수
function deleteRecord(index) {
    if (confirm("삭제하시겠습니까?")) {  // 삭제 확인
        let records = JSON.parse(localStorage.getItem('records')) || [];  // 로컬 스토리지에서 기록을 가져오거나 빈 배열 생성
        records.splice(records.length - 1 - index, 1);  // 역순에서 원래 인덱스 계산하여 지정한 인덱스의 기록을 삭제
        localStorage.setItem('records', JSON.stringify(records));  // 수정된 기록을 로컬 스토리지에 저장
        updateSidebar();  // 사이드바 업데이트
    }
}

// 기록을 편집하는 함수
function editRecord(index) {
    let records = JSON.parse(localStorage.getItem('records')) || [];  // 로컬 스토리지에서 기록을 가져오거나 빈 배열 생성
    let actualIndex = records.length - 1 - index;  // 역순에서 원래 인덱스 계산
    let newName = prompt("제목을 입력하세요:", records[actualIndex].name);  // 새 이름을 입력받음
    if (newName) {  // 이름이 입력된 경우
        records[actualIndex].name = newName;  // 기록의 이름을 새 이름으로 변경
        localStorage.setItem('records', JSON.stringify(records));  // 수정된 기록을 로컬 스토리지에 저장
        updateSidebar();  // 사이드바 업데이트
    }
}

// 페이지 로드 시 사이드바 업데이트
window.onload = updateSidebar;
// 로컬 스토리지 변경 시 사이드바 업데이트
window.addEventListener('storage', updateSidebar);
