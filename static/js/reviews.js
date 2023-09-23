/*jshint esversion: 6 */

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
var deleteButtons = document.getElementsByClassName("btn-delete");
var editButtons = document.getElementsByClassName("btn-edit");
var deleteConfirm = document.getElementById("deleteConfirm");
var reviewText = document.getElementsByTagName("textarea")[0];
var reviewForm = document.getElementById("reviewForm");
var submitForm = document.getElementById("submitButton");


// to clear the review textarea box

reviewText.value = "";

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");
        deleteConfirm.href = `delete_review/${reviewId}`;
        deleteModal.show();
    });
}

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        reviewText.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    });
}

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);