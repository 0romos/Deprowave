//  Use [ctrl + shift + s] to hide and show the friend & channel sidebar

let isSidebarOpen = false;

function toggleSidebar() {
  const sidebar = document.querySelector('.sidebar-1tnWFu');
  
  if (isSidebarOpen) {
    sidebar.style.width = '0px';
  } else {
    sidebar.style.width = '240px';
  }
  
  isSidebarOpen = !isSidebarOpen;
}

document.addEventListener('keydown', function(event) {
  if (event.ctrlKey && event.shiftKey && event.key === 'S') {
    toggleSidebar();
  }
});
