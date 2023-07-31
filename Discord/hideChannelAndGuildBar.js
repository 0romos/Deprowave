let isSidebarOpen = false;
    let isGuildsOpen = true; // Initialize it to true if you want the guilds to be open by default
    
    function toggleSidebar() {
      const sidebar = document.querySelector('.sidebar-1tnWFu');
      const guilds = document.querySelector('.guilds-2JjMmN');
      
      if (isSidebarOpen) {
        sidebar.style.width = '0';
      } else {
        sidebar.style.width = '240px';
      }
      
      isSidebarOpen = !isSidebarOpen;
      
      if (isGuildsOpen) {
        guilds.style.marginLeft = '0';
      } else {
        guilds.style.marginLeft = '-72px';
      }
      
      isGuildsOpen = !isGuildsOpen;
    }
    
    document.addEventListener('keydown', function(event) {
      if (event.ctrlKey && event.shiftKey && event.key === 'S') {
        toggleSidebar();
      }
    });
