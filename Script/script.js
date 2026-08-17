// ambient starfield
(function () {
    const canvas = document.getElementById('stars');
    const ctx = canvas.getContext('2d');
    let stars = [];
 
    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        const count = Math.floor((canvas.width * canvas.height) / 9000);
        stars = Array.from({ length: count }, () => ({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: Math.random() * 1.3 + 0.2,
            phase: Math.random() * Math.PI * 2,
            speed: Math.random() * 0.015 + 0.005
        }));
    }
 
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 
    function draw(t) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (const s of stars) {
            const twinkle = reduceMotion ? 0.7 : 0.5 + 0.5 * Math.sin(t * s.speed + s.phase);
            ctx.globalAlpha = 0.25 + twinkle * 0.6;
            ctx.fillStyle = '#e9eaf6';
            ctx.beginPath();
            ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
            ctx.fill();
        }
        if (!reduceMotion) requestAnimationFrame(draw);
    }
 
    window.addEventListener('resize', resize);
    resize();
    requestAnimationFrame(draw);
})();
 
function sendMessage() {
    const input = document.getElementById("messageInput");
    const message = input.value.trim();
    if (!message) return;
    addMessage(message, "user");
    input.value = "";
    addTyping();
 
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
        .then(res => res.json())
        .then(data => {
            removeTyping();
            addMessage(data.response, "ai");
        })
        .catch(() => {
            removeTyping();
            addMessage("Lyra couldn't reach the server. Check the connection and try again.", "ai");
        });
}
 
function addMessage(text, type) {
    const messages = document.getElementById("messages");
    const row = document.createElement("div");
    row.classList.add("row", type);
 
    if (type === "ai") {
        const avatar = document.createElement("div");
        avatar.className = "avatar";
        avatar.textContent = "L";
        row.appendChild(avatar);
    }
 
    const bubble = document.createElement("div");
    bubble.classList.add("message");
    bubble.textContent = text;
    row.appendChild(bubble);
 
    messages.appendChild(row);
    messages.scrollTop = messages.scrollHeight;
}
 
function addTyping() {
    const messages = document.getElementById("messages");
    const row = document.createElement("div");
    row.classList.add("row", "ai");
    row.id = "typing-row";
 
    const avatar = document.createElement("div");
    avatar.className = "avatar";
    avatar.textContent = "L";
    row.appendChild(avatar);
 
    const bubble = document.createElement("div");
    bubble.classList.add("message");
    bubble.innerHTML = '<span class="typing"><span></span><span></span><span></span></span>';
    row.appendChild(bubble);
 
    messages.appendChild(row);
    messages.scrollTop = messages.scrollHeight;
}
 
function removeTyping() {
    const row = document.getElementById("typing-row");
    if (row) row.remove();
}
 
document.getElementById("messageInput").addEventListener("keydown", (e) => {
    if (e.key === "Enter") sendMessage();
});
