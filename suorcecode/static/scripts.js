document
  .getElementById("prediction-form")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    // Gather input data into an object
    const data = {
      open: formData.get("open"),
      high: formData.get("high"),
      low: formData.get("low"),
      vol: formData.get("vol"),
      change: formData.get("change"),
      model: formData.get("model"),
    };

    // Send data to the server
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await response.json();
    const resultDiv = document.getElementById("result");

    if (result.success) {
      resultDiv.innerHTML = `<div class="result-card">
        Predicted Price: $${result.predicted_price.toFixed(2)}
      </div>`;
    } else {
      resultDiv.innerHTML = `<p class="error"><i class="fas fa-exclamation-circle"></i> Error: ${result.error}</p>`;
    }
  });
