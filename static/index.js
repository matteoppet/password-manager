function passwordCheck() {

    const password = document.getElementById("register-password").value;
    const check = document.getElementById("check-password");

    if (password.length < 8) {
        check.innerText = "Invalid";
        check.style.color = "red";
    }
    else {
        check.innerText = "Valid";
        check.style.color = "green";
    }
}


function confirmCheck() {

    const password = document.getElementById("register-password").value;
    const confirm = document.getElementById("confirm").value;
    const check = document.getElementById("check-confirm");

    if (password != confirm) {
        check.innerText = "Password must be the same as the confirmation";
        check.style.color = "red";
    }
    else {
        check.innerText = "Valid";
        check.style.color = "green";
    }
}


function seePasswordLogin() {
    var password = document.getElementById("login-password");

    if (password.type === "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }
}


function seePasswordAccount() {
    var password = document.getElementById("account-password");
    var icon = document.getElementById("span_text");

    if (password.type === "password") {
        password.type = "text";

        icon.innerHTML = "visibility_off";

    } else {
        password.type = "password";

        icon.innerHTML = "visibility";
    }
}


function deleteItem(value) {
    
    const askConfirm = confirm("Are you sure you want to delete the password?");

    if (askConfirm === true) {
        $.ajax({
            type:'POST',
            url: `/delete/${value}`,
            success:function()
            {
                alert('Item Deleted Successfully');
                location.reload(true); 
            },
            error:function()
            {
                alert('Error Deleting the Item');
                location.reload(true)
            }
        })
    }
}


function copyToClipboard(value) {
    navigator.clipboard.writeText(value).then(function() {
        alert('Copying to clipboard was successful!');
      }, function(err) {
        alert('Async: Could not copy text: ', err);
    });
}


function deleteAccount(value) {
    
    let askConfirm = confirm("Are you sure you want to delete your account?");

    localStorage.setItem('email-user', []);

    if (askConfirm === true) {
        $.ajax({
            type:'POST',
            url: `/delete-account/${value}`,
            success:function()
            {
                alert('Account Deleted Successfully');
                location.reload(true); 
            },
        })
    }
}


function initThemeSelector() {
    // DOM Elements
    const themeSelect = document.getElementById("themeSelect");
    const htmlTag = document.querySelector("html");
    const theme = localStorage.getItem("theme");

    // Apply the saved theme on reload
    if (theme) {
        htmlTag.setAttribute("data-bs-theme", theme);
    }

    // Change the attribute and set the item 
    themeSelect.addEventListener("change", () => {
        htmlTag.setAttribute("data-bs-theme", themeSelect.value);
        localStorage.setItem("theme", themeSelect.value);
    });

    // Apply the value of the select as the theme saved
    themeSelect.value = theme;

}

initThemeSelector();



function checkBoxEmail() {
    const ls = localStorage.getItem("email-user");
    const checkbox = document.getElementById("checkBoxEmail");

    if (ls === '') {
        checkbox.checked = false;
    } else {
        checkbox.checked = true;
    }
}

checkBoxEmail()