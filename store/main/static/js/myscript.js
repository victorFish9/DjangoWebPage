function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

window.addEventListener('DOMContentLoaded', function() {
    var titleElement = document.getElementById('dynamic-title');
    var titles = ["Welcome", "Bienvenue", "Benvenuta"]; // Add the desired titles here
    var currentIndex = 0;

    function changeTitle() {
      currentIndex = (currentIndex + 1) % titles.length;
      titleElement.textContent = titles[currentIndex];
    }

    setInterval(changeTitle, 5000); // Change title every 5 seconds
  });