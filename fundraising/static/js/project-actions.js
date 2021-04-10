// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementsById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
  btn.addEventListener("click", function(event){
      event.preventDefault()
      modal.style.display = "block";
});


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}



// Get the modal
var report-comment-modal = document.getElementById("Modal");

// Get the button that opens the modal
var report-comment-btn = document.getElementsById("Btn");

// Get the <span> element that closes the modal
var span_report = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
report-comment-btn.addEventListener("click", function(event){
      event.preventDefault()
      report-comment-modal .style.display = "block";
});


// When the user clicks on <span> (x), close the modal
span_report.onclick = function() {
  report-comment-modal .style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == report-comment-modal ) {
    report-comment-modal .style.display = "none";
  }
}
