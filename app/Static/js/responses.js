function clear_all(){
    users_edited = [];
    let res = document.querySelector("#content");
    res.innerHTML="";
}

function eliminar(){
    var id = document.getElementById("btn_id").textContent;
    const table = document.getElementById("table").value;
    let xml = new XMLHttpRequest();

    console.log("Ejecutando eliminar" + id);
    xml.open("POST", "/eliminar/", true);
    xml.setRequestHeader("Content-type","application/json");
    xml.onload = function(evt){
      if (this.readyState == 4 && this.status == 200){      
        var dataReply = JSON.parse(this.response);
        console.log("RESPONSE: ",dataReply.status );
        switch (table) {
          case 'users': window.location.href = "/adm/users/"
            break;
          case 'rooms': window.location.href = "/adm/habitaciones/"
            break;
        
          default: window.location.href = "/"
            break;
        }
        
      }
    }

    data = JSON.stringify({
        'id': id, 
        'table': table
    });
    xml.send(data);

};


// FUNCION PARA EDITAR
function edit(){
  var formulario=document;
  const table = formulario.getElementById('table').value;
  var valid = true;

  if (table == 'users'){
    var nombre = formulario.getElementById("name").value;
    var email = formulario.getElementById("email").value;
    var rol = formulario.getElementById("role").value;
    if (nombre != '' && email != '' && rol != ''){
      valid = false;
    }
  }else if(table == 'rooms'){
    var number = formulario.getElementById("number").value;
    var price = formulario.getElementById("price").value;
    var description = formulario.getElementById("description").value;
    if (number != '' && price != '' && description != ''){
      valid = false;
    }
  }
  
  

  if (valid){
    console.log("aquí")
    let id = formulario.getElementById('btn_id').textContent;
    
    switch (table) {
      case 'users':
        nombre = nombre != '' ? nombre :  formulario.getElementById('btn_name').textContent;
        email = email != '' ? email :  formulario.getElementById('btn_email').value;
        rol = rol != '' ? rol :  formulario.getElementById("btn_rol").textContent;

        data = JSON.stringify({
          'id': id,
          'nombre': nombre,
          'email': email,
          'rol': rol,
          'table': table
        });
        break;

      case 'rooms':
        number = number != '' ? number :  formulario.getElementById('btn_number').textContent;
        price = price != '' ? price :  formulario.getElementById('hidden_price').value;
        description = description != '' ? description :  formulario.getElementById("hidden_description").value;

        data = JSON.stringify({
          'id': id,
          'number': number,
          'price': price,
          'descriptions': description,
          'table': table
        });

        break;
    
      default:
        break;
    }

    let xml = new XMLHttpRequest();
    xml.open("POST", "/update/", true);
    xml.setRequestHeader("Content-type","application/json");
    console.log(data);
    xml.send(data)

    // Cuando se reciba la respuesta
    xml.onload = function(evt){
      if (this.readyState == 4 && this.status == 200){      
        var dataReply = JSON.parse(this.response);
        console.log("RESPONSE: ",dataReply.status );

        switch (table) {
          case 'users': window.location.href = "/adm/users/"
            break;
          case 'rooms': window.location.href = "/adm/habitaciones/"
            break;
        
          default: window.location.href = "/"
            break;
        }
      }
    }

  }
}

//ENVIAR A LA VISTA DE CONFIG
function config(ide){
  console.log("Ejecutando configurar");
  var id = ide
  var table = document.getElementById("table").value;
  let xml = new XMLHttpRequest();
  xml.open("POST", "/adm/config", true);
  xml.setRequestHeader("Content-type","application/json");

  data = JSON.stringify({
      'id': id, 
      'table': table,
  });
  console.log("SOLICITUD: ", data);
  xml.send(data);

  xml.onload = function(evt){
    if (this.readyState == 4 && this.status == 200){      
      var dataReply = JSON.parse(this.response);
      console.log("RESPONSE: ", dataReply.res );
      switch (table) {
        case 'users': window.location.href += 'config_u?' + 'data=' + dataReply.res + dataReply.module;
          break;

        case 'rooms': window.location.href += 'config_r?' + 'data=' + dataReply.res +','+ dataReply.module;
          break;

        default: window.location.reload()
          break;
      }
    }
  }
};


//FUNCION PARA INCLUIR PARAMETROS EN LA URL
function params(){
  //console.log("Obteniendo datos")
  const valores = window.location.search;
  //console.log(valores);

  const urlParams = new URLSearchParams(valores);
  var url = urlParams.get('data').split(",");
  index = (url.length -1)
  module = url[index]
  console.log(url);

  switch (module) {
    case 'users':
      window.document.getElementById('btn_id').textContent = url['0'];
      window.document.getElementById('btn_name').textContent = url['1'];
      window.document.getElementById('btn_email').value = url['2'];
      window.document.getElementById('btn_rol').textContent = url['3']; 
      break;

    case 'rooms':
      window.document.getElementById('btn_id').textContent = url['0'];
      window.document.getElementById('btn_number').textContent = url['1'];
      window.document.getElementById('btn_enabled').textContent = url['6'];
      window.document.getElementById('description').value = url['2'];  
      window.document.getElementById('hidden_price').value = url['5']; 
      break;


    default:
      break;
  }
  
}


// FUNCION PARA BUSCAR USUARIO
function search(act){

  var xml = new XMLHttpRequest();
  xml.open("POST", "/adm/get_users/", true);
  xml.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  var data = '';

  if(act == 'unique'){
    var seeker = document.getElementById("search").value;
    var table = document.getElementById("table").value;

    if (!isNaN(parseInt(seeker))){
      seeker = parseInt(seeker);
      data = JSON.stringify({
        'action': act,
        'parameter': seeker,
        'search': 'number',
        'table': table
      });

    }else{
      data = JSON.stringify({
        'action': act,
        'parameter': seeker,
        'search': 'str',
        'table': table
      });
    }

  }else{
    window.location.reload();
  }
  console.log(data)
  xml.send(data);

}


function confirm_check(id){
  var xml = new XMLHttpRequest();
  const table = document.getElementById("table").value;
  var data = ''
  xml.open("POST", "/checked/", true);


  data = JSON.stringify({
    'table': table,
    'id': id,
    'state': 1
  });

  console.log(data)
  xml.send(data)

  xml.onload = function(evt){
    if (this.readyState == 4 && this.status == 200){      
      window.location.reload();
    }
  }

}

function delete_check(id){
  var xml = new XMLHttpRequest();
  const table = document.getElementById("table").value;
  var data = ''
  xml.open("POST", "/checked/", true);


  data = JSON.stringify({
    'table': table,
    'id': id,
    'state': -1
  });

  console.log(data)
  xml.send(data)

  xml.onload = function(evt){
    if (this.readyState == 4 && this.status == 200){      
      window.location.reload();
    }
  }

}
