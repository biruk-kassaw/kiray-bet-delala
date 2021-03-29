
var submit_button = document.getElementById("contact-submit")
submit_button.addEventListener("click", function (e) {
    e.preventDefault()
    console.log(req_obj)
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    var req_obj = {
        "password": password,
        "email" : email,
    }
    axios.defaults.withCredentials = true

    // axios.defaults.headers.post ['Access-Control-Allow-Origin'] = '*',

    axios.post('http://127.0.0.1:5000/api/v1/users/login', req_obj)
      .then(function (response) {
          console.log(req_obj)
        console.log(response);
        var register_container = document.getElementById("contact");
        register_container.innerHTML = `Loged in successfully <br><a class="btn btn-primary m-2" role="button" href="./uploadhouse.html">
        click here to upload your house
      </a>`
        // window.open("http://127.0.0.1:5000/api/v1/users"); 
      })
      .catch(function (error) {
          document.getElementById("invalid-log-in").textContent = "Invalid User Name Or Password"
          console.log("error new")
        console.log(error.response.data)
      });
})
