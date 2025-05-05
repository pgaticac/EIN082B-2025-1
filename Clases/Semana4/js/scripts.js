
function saludar(){
    var nombre = document.getElementById("txtNombre")
    var h1 = document.getElementById("titulo")
    h1.innerHTML = "Hola " + nombre.value
}

function restablecer(){
    document.getElementById("titulo").innerHTML = "Hola Mundo"
    document.getElementById("txtNombre").value = ""
}

function cerrarOjo(){
    var img = document.getElementById("ojo")
    img.src ="img/ojo-cerrado.png"    
}

function abrirOjo(){
    var img = document.getElementById("ojo")
    img.src ="img/vista.png"    
}