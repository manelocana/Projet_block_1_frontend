


// Header
fetch('../templates/header.html')
  .then(res => res.text())
  .then(html => {
    document.getElementById('header').innerHTML = html;
  });


  
// Footer
fetch('../templates/footer.html')
  .then(res => res.text())
  .then(html => {
    document.getElementById('footer').innerHTML = html;
  });
