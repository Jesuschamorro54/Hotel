var users_edited = [];

function clear_all(){
    users_edited = [];
    let res = document.querySelector("#content_users");
    res.innerHTML="";
}


function get_one(){
    let seeker = document.getElementById("search").value;
    document.getElementById("search").value = "";
    users_edited =[];
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
                console.log("Buscando con el seeker", seeker)
                if (seeker.toLowerCase() == item.nombre.toLowerCase() || seeker == String(item.id) || seeker == item.email){
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
                            <div>
                                <input  class="v-card__title name="email" padding = "5px" id="email" type="text" value = "${item.nombre}" style="left: 60px; right: auto; padding-left: 8px;">
                            </div>
                        </div>
                        <div class="v-card__subtitle pb-0">
                            Id: ${item.id}
                        </div>
                        <div class="v-card__text text--primary">
                          <div>
                            <label for="email" class="v-label v-label--active theme--light" style="left: 15px; right: auto;">Email: </label>
                            <input name="email" padding = "5px" id="email" type="text" value = "${item.email}" style="width: 100% left: 60px; right: auto; padding-left: 8px;">
                          </div>
                          <div>
                            <label for="email" class="v-label v-label--active theme--light" style="left: 15px; right: auto;">Rol: </label>
                            <input name="email" padding = "5px" id="email" type="text" value = "${item.rol}" style="left: 60px; right: auto; padding-left: 8px;">
                          </div>  
                        </div>
                        <div class="v-card__actions">
                          <button type="button" class="v-btn v-btn--text theme--light v-size--default green--text" title="Editar" onclick = edit(${item.id})>
                            <span class="v-btn__content">Editar</span>
                          </button>
                          <button type="button" class="v-btn v-btn--text theme--light v-size--default red--text" title="Eliminar" onclick = edit(${item.id})>
                            <span class="v-btn__content">Eliminar</span>
                          </button>
                        </div>
                    </div>
                </div>
                    `
                }
            }
        }
    }
}

function get_data(){
    users_edited =[];
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
                            <div>
                                <input  class="v-card__title name="email" padding = "5px" id="email" type="text" value = "${item.nombre}" style="left: 60px; right: auto; padding-left: 8px;">
                            </div>
                        </div>
                        <div class="v-card__subtitle pb-0">
                            Id: ${item.id}
                        </div>
                        <div class="v-card__text text--primary">
                          <div>
                            <label for="email" class="v-label v-label--active theme--light" style="left: 15px; right: auto;">Email: </label>
                            <input name="email" padding = "5px" id="email" type="text" value = "${item.email}" style="width: 100% left: 60px; right: auto; padding-left: 8px;">
                          </div>
                          <div>
                            <label for="email" class="v-label v-label--active theme--light" style="left: 15px; right: auto;">Rol: </label>
                            <input name="email" padding = "5px" id="email" type="text" value = "${item.rol}" style="left: 60px; right: auto; padding-left: 8px;">
                          </div>  
                        </div>
                        <div class="v-card__actions">
                          <button type="button" class="v-btn v-btn--text theme--light v-size--default green--text" title="Editar" onclick = edit(${item.id})>
                            <span class="v-btn__content">Editar</span>
                          </button>
                          <button type="button" class="v-btn v-btn--text theme--light v-size--default red--text" title="Eliminar" onclick = edit(${item.id})>
                            <span class="v-btn__content">Eliminar</span>
                          </button>
                        </div>
                    </div>
                </div>
                `
            }
        }
    }
}
function edit(id){
    console.log("Editando")
    const xhttp = new XMLHttpRequest();
    xhttp.open('GET', '/static/js/users.json', true)
    xhttp.send();
    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            let datos = JSON.parse(this.responseText)
            console.log(datos)
            let res = document.querySelector("#content_users");
            res.innerHTML="";
            users_edited.push(id);
            for (let item of datos){
                if (!search(item.id, users_edited)){
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
                            <div>
                                <input  class="v-card__title name="email" padding = "5px" id="email" type="text" value = "${item.nombre}" style="left: 60px; right: auto; padding-left: 8px;">
                            </div>
                        </div>
                        <div class="v-card__subtitle pb-0">
                            Id: ${item.id}
                        </div>
                        <div class="v-card__text text--primary">
                          <div>
                            <label for="email" class="v-label v-label--active theme--light" style="left: 15px; right: auto;">Email: </label>
                            <input name="email" padding = "5px" id="email" type="text" value = "${item.email}" style="width: 100% left: 60px; right: auto; padding-left: 8px;">
                          </div>
                          <div>
                            <label for="email" class="v-label v-label--active theme--light" style="left: 15px; right: auto;">Rol: </label>
                            <input name="email" padding = "5px" id="email" type="text" value = "${item.rol}" style="left: 60px; right: auto; padding-left: 8px;">
                          </div>  
                        </div>
                        <div class="v-card__actions">
                          <button type="button" class="v-btn v-btn--text theme--light v-size--default green--text" title="Editar" onclick = edit(${item.id})>
                            <span class="v-btn__content">Editar</span>
                          </button>
                          <button type="button" class="v-btn v-btn--text theme--light v-size--default red--text" title="Eliminar" onclick = edit(${item.id})>
                            <span class="v-btn__content">Eliminar</span>
                          </button>
                        </div>
                    </div>
                </div>
                    `
                }
            }
        }
    }

}

function search(ide, array){
    for(i=0; i<array.length; i++){
        if(ide == array[i]){
            return true
        }
    }
}

