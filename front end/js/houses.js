var appartment_container = document.getElementById("appartments_container");

axios.get('http://127.0.0.1:5000/api/v1/houses')
  .then(function (response) {
    var appartment_container_inner_html = ""
    houses = response.data.houses
    houses.forEach(house => {
        var imgno = 1
                var househtml = `
                <div class="col-12 col-md-6 col-lg-4">
                <a href="./house.html?id=${house._id}">

                <div class="appartment-box">
                <div class="appartment-image">
                    <!-- Appartment Image  -->
                    <img src="images/samplehouse${house._id}.jpg" alt="">
                </div>
                <div class="appartment-info">
                    <div class="appartment-title">
                    <!-- Appartment Address  -->
                    <p>${house.location_word}</p>
                    </div>
                    <div class="appartment-details">
                    <div class="price left">
                        <!-- Appartment Price  -->
                        <p>${house.rent_amount_per_month} Birr </p>
                    </div>
                    <div class="flex-center">
                        50 m <sup>2</sup>
                    </div>
                    <div class="bedrooms right flex-center">
                        <img src="images/bed.svg" class="left" alt="">
                        <!-- Appartment Number Of Bedrooms  -->
                        <p class="left">${house.number_of_bedrooms} BD</p>
                    </div>
                    <div class="bathrooms right flex-center">
                        <img src="images/shower.svg" class="left" alt="">
                        <!-- Appartment Number of Bathrooms  -->
                        <p class="left">2 BA</p>
                    </div>
                    </div>
                </div>
                </div>
                </a>
            </div>`
           
            appartment_container_inner_html += househtml
            imgno++
            if(imgno>5){
                imgno=1
            }

    });
    appartment_container.innerHTML = appartment_container_inner_html
    console.log(houses);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })

  var search_btn = document.getElementById("search_btn");

  search_btn.addEventListener("click", function (e) {
      var keyword = document.getElementById("search_word").value;

      e.preventDefault() 
    //   keyword = document.getElementById("searchinput").value;
    var keyword_holder = document.getElementById("keyword_holder");
    keyword_holder.innerHTML = `search results for ${keyword}`
      axios.get(`http://127.0.0.1:5000/api/v1/houses/search/${keyword}`)
      .then(function (response) {
          var housecontainer = document.getElementById("appartments_container");
  
          appartment_container_inner_html = ""
  
          houses = response.data.houses
          houses.forEach(house => {
              var imgno = 1
                      var househtml = `
                      <div class="col-12 col-md-6 col-lg-4">
                      <a href="./house.html?id=${house._id}">
  
                      <div class="appartment-box">
                      <div class="appartment-image">
                          <!-- Appartment Image  -->
                          <img src="images/samplehouse${house._id}.jpg" alt="">
                      </div>
                      <div class="appartment-info">
                          <div class="appartment-title">
                          <!-- Appartment Address  -->
                          <p>${house.location_word}</p>
                          </div>
                          <div class="appartment-details">
                          <div class="price left">
                              <!-- Appartment Price  -->
                              <p>${house.rent_amount_per_month} Birr </p>
                          </div>
                          <div class="flex-center">
                              50 m <sup>2</sup>
                          </div>
                          <div class="bedrooms right flex-center">
                              <img src="images/bed.svg" class="left" alt="">
                              <!-- Appartment Number Of Bedrooms  -->
                              <p class="left">${house.number_of_bedrooms} BD</p>
                          </div>
                          <div class="bathrooms right flex-center">
                              <img src="images/shower.svg" class="left" alt="">
                              <!-- Appartment Number of Bathrooms  -->
                              <p class="left">2 BA</p>
                          </div>
                          </div>
                      </div>
                      </div>
                      </a>
                  </div>`
              
                  appartment_container_inner_html += househtml
                  imgno++
                  if(imgno>5){
                      imgno=1
                  }
  
          });
          housecontainer.innerHTML = appartment_container_inner_html
          // document.location.reload()
      })
      .catch(function (error) {
          // handle error
          console.log(error);
      })  

    //   var keyword_holder = document.getElementById("keyword_holder")
    //   keyword_holder.innerHTML = `Search Results for "${keyword}"`;
  })