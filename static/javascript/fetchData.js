// function fetchData(url, method, callback, data = null) {
//     const options = {
//         method: method,
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: data ? JSON.stringify(data) : null,
//     };

//     fetch(url, options)
//         .then(response => response.json()) // Convertir respuesta a JSON
//         .then(data => {
//             callback(data); // Llama a la función de devolución de llamada con los datos obtenidos
//         })
//         .catch(error => console.log("Ocurrió un error! " + error));
// }
