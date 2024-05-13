const header = document.querySelector('header');
header.innerHTML = `
<div id="Logo">
    <img src="../Recursos/Img/logo.png" alt="Imagen de logo" width="100px">
</div>
<h1>RESERVA NATURAL "LOS ROBLES"</h1>`;





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