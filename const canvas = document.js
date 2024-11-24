const canvas = document.getElementById('simulationCanvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// ตัวอย่างโครงสร้างไม้กระดก
function drawSeesaw() {
    ctx.fillStyle = '#D2B48C'; // สีน้ำตาลอ่อน
    ctx.fillRect(canvas.width / 2 - 150, canvas.height / 2, 300, 10); // ไม้กระดก
    ctx.fillStyle = '#000'; // สีดำ (จุดหมุน)
    ctx.beginPath();
    ctx.arc(canvas.width / 2, canvas.height / 2 + 5, 10, 0, Math.PI * 2);
    ctx.fill();
}

// วาดกราฟิก
function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawSeesaw();
    requestAnimationFrame(render);
}

render();
