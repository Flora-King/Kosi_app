/*jshint esversion: 6 */

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
let deleteButtons = document.getElementsByClassName("btn-delete");
let editButtons = document.getElementsByClassName("btn-edit");
let deleteConfirm = document.getElementById("deleteConfirm");
let reviewText = document.getElementsByTagName("textarea")[0];
let reviewForm = document.getElementById("reviewForm");
let submitButton = document.getElementById("submitButton");

// to clear the review textarea box
if (reviewText) {
  reviewText.value = "";
}

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

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("review_id");
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        reviewText.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    });
}