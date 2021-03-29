// // {
//     "password": "hello",
//     "email" : "7b8b55cdcf-efba18@inbox.mailtrap.io",
//     "username" : "biruk",
//     "phone_number" : "0930995547",
//     "password_confirm": "hello"
// }


var submit_button = document.getElementById("contact-submit")
submit_button.addEventListener("click", function (e) {
    e.preventDefault()
    console.log(req_obj)
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var phone_number = document.getElementById("phone_number").value;
    var password_confirm = document.getElementById("password_confirm").value;
    var password = document.getElementById("password").value;

    var req_obj = {
        "password": password,
        "email" : email,
        "username" : username,
        "phone_number" : phone_number,
        "password_confirm": password_confirm
    }
    
    axios.post('http://127.0.0.1:5000/api/v1/users/register', req_obj)
      .then(function (response) {
        console.log(response);
        var register_container = document.getElementById("contact");
        register_container.innerHTML = "verification email sent to your email account check your email"
      })
      .catch(function (error) {
        console.log(error.response.data)
      });
})
