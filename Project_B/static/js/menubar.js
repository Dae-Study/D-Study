const openMenuButton = document.getElementById('openMenu');
const closeMenuButton = document.getElementById('closeMenu');
const menu = document.getElementById('menu');

openMenuButton.addEventListener('click', () => {
  menu.classList.add('on');
});

closeMenuButton.addEventListener('click', () => {
  menu.classList.remove('on');
});