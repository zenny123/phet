const canvas = document.getElementById("simulationCanvas");
const context = canvas.getContext("2d");
canvas.width = 800;
canvas.height = 400;

const beam = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    length: 300,
    thickness: 10,
    pivot: 0.5,
};

const weights = [];
const colors = ["#FF1493", "#32CD32", "#FF4500", "#000000"];
let torqueLeft = 0, torqueRight = 0;


function calculateTorque() {
    torqueLeft = 0;
    torqueRight = 0;

    weights.forEach(w => {
        const distance = w.x - beam.x;
        const torque = distance * w.weight;

        if (distance < 0) {
            torqueLeft += Math.abs(torque);
        } else {
            torqueRight += Math.abs(torque);
        }
    });
}


function drawBeam() {
    const pivotX = beam.x + beam.length * (beam.pivot - 0.5);
    context.fillStyle = "saddlebrown";
    context.fillRect(beam.x - beam.length / 2, beam.y, beam.length, beam.thickness);

    context.beginPath();
    context.arc(pivotX, beam.y + beam.thickness / 2, 10, 0, Math.PI * 2);
    context.fillStyle = "black";
    context.fill();
}


function drawWeights() {
    weights.forEach(w => {
        context.beginPath();
        context.arc(w.x, w.y, 10, 0, Math.PI * 2);
        context.fillStyle = w.color;
        context.fill();
        context.closePath();
    });
}


function updateCanvas() {
    context.clearRect(0, 0, canvas.width, canvas.height);

    const tiltAngle = (torqueRight - torqueLeft) / 1000; 
    context.save();
    context.translate(beam.x, beam.y);
    context.rotate(tiltAngle);
    context.translate(-beam.x, -beam.y);

    drawBeam();
    drawWeights();
    context.restore();

    document.getElementById("torqueLeft").innerText = torqueLeft.toFixed(2);
    document.getElementById("torqueRight").innerText = torqueRight.toFixed(2);
}

canvas.addEventListener("click", event => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = beam.y;

    const weightValue = Math.floor(Math.random() * 50);
    weights.push({ x, y, weight: weightValue, color: colors[Math.floor(Math.random() * colors.length)] });

    calculateTorque();
    updateCanvas();
});

updateCanvas();
