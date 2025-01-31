const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Ajustar tamaño del canvas
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

const points = [];
const numPoints = 200;
const attractionRadius = 100;
const attractionForce = 0.05;

for (let i = 0; i < numPoints; i++) {
    points.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 3 + 2,
        speedX: (Math.random() - 0.5) * 2,
        speedY: (Math.random() - 0.5) * 2,
    });
}

let mouseX = null;
let mouseY = null;

canvas.addEventListener('mousemove', event => {
    mouseX = event.clientX;
    mouseY = event.clientY;
});

canvas.addEventListener('mouseleave', () => {
    mouseX = null;
    mouseY = null;
});

function updatePoints() {
    points.forEach(point => {
        point.x += point.speedX;
        point.y += point.speedY;

        if (point.x < 0 || point.x > canvas.width) point.speedX *= -1;
        if (point.y < 0 || point.y > canvas.height) point.speedY *= -1;

        if (mouseX !== null && mouseY !== null) {
            const dx = mouseX - point.x;
            const dy = mouseY - point.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < attractionRadius) {
                point.x += dx * attractionForce;
                point.y += dy * attractionForce;
            }
        }
    });
}

function drawPoints() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    points.forEach(point => {
        ctx.beginPath();
        ctx.arc(point.x, point.y, point.radius, 0, Math.PI * 2);
        ctx.fillStyle = '#172540'; // Color de los puntos
        ctx.fill();
    });
}

function animate() {
    updatePoints();
    drawPoints();
    requestAnimationFrame(animate);
}

animate();