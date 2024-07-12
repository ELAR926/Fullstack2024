document.getElementById('formularioReserva').addEventListener('submit', function(event) {
    event.preventDefault();  // Evita que el formulario se envíe automáticamente

    const nombre = document.getElementById('nombre').value;
    const fecha = document.getElementById('fecha').value;
    // Otros campos del formulario según lo necesites

    const datos = {
        nombre: nombre,
        fecha: fecha,
        // Otros campos del formulario según lo necesites
    };

    axios.post('http://localhost:5000/api/tasks/reservas', datos)
        .then(function(response) {
            // Manejar la respuesta del backend
            document.getElementById('mensaje').innerText = response.data.mensaje;
            // Podrías redirigir a otra página o hacer algo más después de procesar la reserva
        })
        .catch(function(error) {
            console.error('Error al enviar la reserva:', error);
            document.getElementById('mensaje').innerText = 'Error al enviar la reserva. Por favor, inténtalo de nuevo.';
        });
});
