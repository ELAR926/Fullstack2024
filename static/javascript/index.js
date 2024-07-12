// Contenido de app.js
const url = '/api/tasks/reservas';
const method = 'POST';
const data = {
    nombre: 'Nombre Ejemplo',
    apellido: 'Apellido Ejemplo',
    email: 'correo@example.com',
    fecha_entrada: '2024-07-11',
    fecha_salida: '2024-07-13'
};

const callback = (data) => {
    console.log('Respuesta del servidor:', data);
    // Aquí puedes manejar la respuesta del servidor según tus necesidades
};

// Llamada a fetchData para realizar la solicitud
fetchData(url, method, callback, data);
