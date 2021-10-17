console.log('correcto');
//console.log(hola);

function get_data(){
    console.log("Dentro de la función")
    const xhttp = new XMLHttpRequest();
    xhttp.open('GET', '/static/js/users.json', true)
    xhttp.send();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            let datos = JSON.parse(this.responseText)
            console.log(datos)
            let res = document.querySelector("#content_users");
            res.innerHTML="";
            for (let item of datos){
                res.innerHTML +=`
                <div class="col">
                    <div class="mx-auto v-card v-sheet theme--light" style="max-width: 344px;">
                        <div class="v-image v-responsive black--text align-end theme--light" style="height: 200px;">
                            <div class="v-responsive__sizer" style="padding-bottom: 52.0312%;"></div>
                            <div class="v-image__image v-image__image--cover">
                                <div>
                                  <img class="img_logo" src="${item.image}">
                                </div>
                                <style>
                                  .img_logo{
                                    width: 60%;
                                    margin-left: 66px;
                                  }
                                </style>
                            </div>
                        </div>
                        <div class="v-responsive__content" style="width: 1280px;">
                            <div class="v-card__title">${item.nombre}</div>
                        </div>
                        <div class="v-card__subtitle pb-0">
                            Id: ${item.id}
                        </div>
                        <div class="v-card__text text--primary">
                          <div>Email: ${item.email}</div> 
                          <div>Rol: ${item.rol}</div> 
                        </div>
                    </div>
                </div>
                `
            }
        }
    }
}


