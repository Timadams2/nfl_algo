// Placeholder for future dashboard interactivity
function toggleBetInputs() {
    const betType = document.getElementById("betType").value;

    const spreadContainer = document.getElementById("spreadContainer");
    const totalContainer = document.getElementById("totalContainer");

    // Hide both by default
    spreadContainer.style.display = "none";
    totalContainer.style.display = "none";

    if (betType === "spread") {
        spreadContainer.style.display = "block";
    } else if (betType === "total") {
        totalContainer.style.display = "block";
    }
}

function updateSpreadValue(val) {
    document.getElementById("spreadValue").innerText = val;
}

function updateTotalValue(val) {
    document.getElementById("totalValue").innerText = val;
}
