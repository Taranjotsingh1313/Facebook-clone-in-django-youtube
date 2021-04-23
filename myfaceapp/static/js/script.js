let account = document.getElementById("create-account");
let login = document.getElementById("login");
const cross = document.getElementById("crosses");
account.addEventListener("click", () => {
  login.style.display = "flex";
});
cross.addEventListener("click", () => {
  login.style.display = "none";
});
