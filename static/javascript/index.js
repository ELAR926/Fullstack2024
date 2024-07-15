// Ejemplo de JavaScript para manejar el envío del formulario y la redirección
document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('miFormulario'); // Reemplaza con el ID de tu formulario

    formulario.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevenir el comportamiento predeterminado de envío del formulario

        const formData = new FormData(formulario); // Obtener los datos del formulario

        try {
            // Enviar los datos del formulario al backend usando fetch
            const response = await fetch('http://127.0.0.1:5000/api/Form/reserva', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Error al procesar el formulario');
            }

            const responseData = await response.json();
            console.log('Datos recibidos correctamente:', responseData);

            // 
            window.location.href = 'http://127.0.0.1:5500/static/html/reservas.html'; 

        } catch (error) {
            console.error('Error al enviar formulario:', error);
            // Manejar el error si es necesario
        }
    });
});
