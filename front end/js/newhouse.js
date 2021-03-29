var house_submit = document.getElementById("house-submit");
house_submit.addEventListener("click", function (e) {
    e.preventDefault()
    

    var location_word = document.getElementById("location_word").value
    var number_of_bedrooms = document.getElementById("bedrooms").value
    var description = document.getElementById("description").value
    var area_in_square_meter = document.getElementById("area_in_square_meter").value
    var rent_amount_per_month = document.getElementById("rent_amount_per_month").value

    var lat;
    var long;
    var coordinates
    navigator.geolocation.getCurrentPosition(function(position) {
        console.log(position.coords.latitude)
        lat = position.coords.latitude;
        long = position.coords.longitude;
        console.log(lat)
        coordinates = `POINT(${lat} ${long})`  
        console.log(coordinates)   
        req_obj = {
            "location_word" : location_word,
            "number_of_bedrooms" : number_of_bedrooms,
            "description": description,
            "area_in_square_meter": area_in_square_meter,
            "rent_amount_per_month": rent_amount_per_month,
            "coordinates" : coordinates
    
        }
    
        axios.defaults.withCredentials = true
        axios.post('http://127.0.0.1:5000/api/v1/houses', req_obj)
          .then(function (response) {
            console.log(response.data);
            window.open(`http://127.0.0.1:5500/house.html?id=${response.data._id}`); 
            
          })
          .catch(function (error) {
            window.open(`./login.html`); 
            console.log("not here");
            console.log(error.response.data)
          });

    });
})