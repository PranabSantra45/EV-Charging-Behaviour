function predictEnergy() {

    let data = {
        time: document.getElementById("time").value,
        duration: document.getElementById("duration").value,
        battery_capacity: document.getElementById("battery").value,
        soc_start: document.getElementById("soc_start").value,
        soc_end: document.getElementById("soc_end").value,
        charging_rate: document.getElementById("charging_rate").value,
        temperature: document.getElementById("temperature").value,
        day: document.getElementById("day").value,
        charger_type: document.getElementById("charger_type").value,
        location_type: document.getElementById("location_type").value,
        vehicle_model: document.getElementById("vehicle_model").value
    };

    fetch("http://127.0.0.1:5000/predict_energy", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        if (result.error) {
            document.getElementById("result").innerText = "Error: " + result.error;
        } else {
            document.getElementById("result").innerText =
                "⚡ Predicted Energy: " + result.energy + " kWh";
        }
    })
    .catch(() => {
        document.getElementById("result").innerText = "Server Error";
    });
}