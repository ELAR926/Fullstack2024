document.addEventListener("DOMContentLoaded", () => {
    const apiKey = "3edd9a8a2f8d53cb34bd595eaf9dc73d"; 
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=Paso%20del%20Rey&appid=${apiKey}&lang=es`;

    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error("No se pudo obtener los datos del clima");
        }
        return response.json();
      })
      .then(data => {
        displayWeatherData(data);
      })
      .catch(error => {
        console.error("Error:", error);
        displayErrorMessage("Hubo un error al obtener los datos del clima.");
      });
  });
  
  function displayWeatherData(data) {
    const weatherDataElement = document.getElementById("weather-data");
    weatherDataElement.innerHTML = `
      <p><strong>Ciudad:</strong> ${data.name}</p>
      <p><strong>Descripción:</strong> ${data.weather[0].description}</p>
      <p><strong>Temperatura:</strong> ${data.main.temp} K</p>
      <p><strong>Presión:</strong> ${data.main.pressure} hPa</p>
      <p><strong>Humedad:</strong> ${data.main.humidity}%</p>
    `;
  }
  
  function displayErrorMessage(message) {
    const weatherDataElement = document.getElementById("weather-data");
    weatherDataElement.textContent = message;
  }
