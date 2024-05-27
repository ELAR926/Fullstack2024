
// HEADER

const nav = document.querySelector("#nav");
const abrir = document.querySelector("#abrir");
const cerrar = document.querySelector("#cerrar");

abrir.addEventListener("click", () => {
    nav.classList.add("visible");
});

cerrar.addEventListener("click", () => {
    nav.classList.remove("visible"); 
});








//"Ver Mas" en pagina del inicio
let hideText_btn = document.getElementById('hideText_btn');

let hideText = document.getElementById('hideText');

hideText_btn.addEventListener('click', toggleText);

function toggleText(){
    hideText.classList.toggle('show');

    if(hideText.classList.contains('show')){
        hideText_btn.innerHTML = 'Ver menos'

    }
    else{
        hideText_btn.innerHTML = 'Mas fotos';
    }
}





 // VALIDACION DEL FORMULARIO

document.querySelector('.submit').addEventListener('click', function(event) {
    var form = document.getElementById('contactForm');
    var isValid = form.checkValidity();
    if (isValid) {
        var email = document.getElementById('email').value;
        if (email.trim() === '') {
            alert("Por favor, ingrese su correo electrónico.");
        } else {
            alert("¡Felicidades! Todos los datos serán enviados a su correo electrónico a la brevedad.");
        }
    } else {
        alert("Por favor, complete todos los campos obligatorios.");
    }
    event.preventDefault();
});




//API

fetch("https://hp-api.onrender.com/api/characters")
.then(response => response.json())
.then(data =>{
    console.log(data);
})
.catch(error => console.log("Ocurrio un error!"));