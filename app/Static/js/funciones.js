//var userNameInput = document.formularioRegistro.username;
//window.status="Hola mundo";
function validar()
{
    var userNameInput = document.formularioregistro.usr_name;
    var passWordInput = document.formularioregistro.usr_password;
    var correoInput = document.formularioregistro.usr_email;

    var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;

    var swErrores=false;

    console.log(userNameInput.value + "-"+passWordInput.value+"-"+correoInput.value);

    if(userNameInput.value.length == 0 || userNameInput.value.length < 8)
    {
        //alert("El nombre de usuario debe tener mínimo 8 caracteres.");
        document.getElementById("errorUsername").innerHTML="El nombre de usuario debe tener mínimo 8 caracteres.";
        userNameInput.focus();
        //document.getElementById("botonEnviar").disabled=true;
        swErrores=true;
    }

    if(passWordInput.value.length == 0 || passWordInput.value.length < 8)
    {
        //alert("La clave debe tener mínimo 8 caracteres.");
        document.getElementById("errorPassword").innerHTML="La clave debe tener mínimo 8 caracteres.";
        passWordInput.focus();
        swErrores=true;
    }

    if(!correoInput.value.match(formato_email))
    {
        //alert("Por favor escriba un correo válido.");
        document.getElementById("errorMail").innerHTML="Por favor escriba un correo válido, gracias.";
        correoInput.focus();
        swErrores=true;
    }

    if( swErrores==true)
    {
        return false;
    }
    else{
        return true;
    }  
}

function verClave()
{
    console.log('Mostrar clave');

    var passWordInput = document.formularioregistro.usr_password;
    passWordInput.type="text";
}

function ocultarClave()
{
    console.log('Ocultar clave');
    var passWordInput = document.formularioregistro.usr_password;
    passWordInput.type="password";

    
}

function ocultarVerClave()
{
    var passWordInput = document.formularioregistro.usr_password;
    var tipo = passWordInput.type;

    console.log(tipo);

    if(tipo=="text")
    {
        passWordInput.type="password";
    }

    if(tipo == "password")
    {
        passWordInput.type="text";
    }
}


function verClave_Log()
{
    console.log('Mostrar clave');

    var passWordInput = document.formulariologin.usr_password;
    passWordInput.type="text";
}

function ocultarClave_Log()
{
    console.log('Ocultar clave');
    var passWordInput = document.formulariologin.usr_password;
    passWordInput.type="password";
}

function ocultarVerClave_Log()
{
    var passWordInput = document.formulariologin.usr_password;
    var tipo = passWordInput.type;
    console.log(tipo);
    if(tipo=="text")
    {
        passWordInput.type="password";
    }

    if(tipo == "password")
    {
        passWordInput.type="text";
    }
}

// formatea un numero según una mascara dada ej: "-$###,###,##0.00"
//
// elm   = elemento html <input> donde colocar el resultado
// n     = numero a formatear
// mask  = mascara ej: "-$###,###,##0.00"
// force = formatea el numero aun si n es igual a 0
//
//
//ingresar un valor numero (o formula) formatear con -$##,###,##0.00<br>
//<input onchange="MASK(this,this.value,'-$##,###,##0.00',1)"><br>
//<br>
//ingresar un valor numero (o formula) formatear con 00/00/0000<br>
//<input onchange="MASK(this,this.value,'00/00/0000',1)"><br></br>
// La función devuelve el numero formateado

function MASK(form, n, mask, format) {
    if (format == "undefined") format = false;
    if (format || NUM(n)) {
      dec = 0, point = 0;
      x = mask.indexOf(".")+1;
      if (x) { dec = mask.length - x; }
  
      if (dec) {
        n = NUM(n, dec)+"";
        x = n.indexOf(".")+1;
        if (x) { point = n.length - x; } else { n += "."; }
      } else {
        n = NUM(n, 0)+"";
      } 
      for (var x = point; x < dec ; x++) {
        n += "0";
      }
      x = n.length, y = mask.length, XMASK = "";
      while ( x || y ) {
        if ( x ) {
          while ( y && "#0.".indexOf(mask.charAt(y-1)) == -1 ) {
            if ( n.charAt(x-1) != "-")
              XMASK = mask.charAt(y-1) + XMASK;
            y--;
          }
          XMASK = n.charAt(x-1) + XMASK, x--;
        } else if ( y && "$0".indexOf(mask.charAt(y-1))+1 ) {
          XMASK = mask.charAt(y-1) + XMASK;
        }
        if ( y ) { y-- }
      }
    } else {
       XMASK="";
    }
    if (form) { 
      form.value = XMASK;
      if (NUM(n)<0) {
        form.style.color="#FF0000";
      } else {
        form.style.color="#000000";
      }
    }
    return XMASK;
  }
  
  // Convierte una cadena alfanumérica a numérica (incluyendo formulas aritméticas)
  //
  // s   = cadena a ser convertida a numérica
  // dec = numero de decimales a redondear
  //
  // La función devuelve el numero redondeado
  
  function NUM(s, dec) {
    for (var s = s+"", num = "", x = 0 ; x < s.length ; x++) {
      c = s.charAt(x);
      if (".-+/*".indexOf(c)+1 || c != " " && !isNaN(c)) { num+=c; }
    }
    if (isNaN(num)) { num = eval(num); }
    if (num == "")  { num=0; } else { num = parseFloat(num); }
    if (dec != undefined) {
      r=.5; if (num<0) r=-r;
      e=Math.pow(10, (dec>0) ? dec : 0 );
      return parseInt(num*e+r) / e;
    } else {
      return num;
    }
  }

