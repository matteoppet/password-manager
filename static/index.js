function passwordCheck() {
    const password = document.getElementById("register-password").value;
    const check = document.getElementById("check-password");

    if (password.length < 8) {
        check.innerText = "Invalid"
        check.style.color = "red"
    }
    else {
        check.innerText = "Valid"
        check.style.color = "green"
    }
}

function confirmCheck() {
    const password = document.getElementById("register-password").value;
    const confirm = document.getElementById("confirm").value;
    const check = document.getElementById("check-confirm");

    if (password != confirm) {
        check.innerText = "Password must be the same as the confirmation"
        check.style.color = "red"
    }
    else {
        check.innerText = "Valid"
        check.style.color = "green"
    }
}