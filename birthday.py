import webbrowser
import os

html = """
<!DOCTYPE html>
<html>
<head>
<title>Birthday Surprise - DAX</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    background: linear-gradient(135deg, #090018, #251044, #090018);
    color: white;
    font-family: Arial;
    text-align: center;
    overflow-x: hidden;
}

.container {
    padding: 60px 15px;
}

h1 {
    font-size: 45px;
    color: gold;
    text-shadow: 0 0 20px orange;
}

.subtitle {
    font-size: 20px;
}

.gift {
    font-size: 100px;
    cursor: pointer;
    margin: 30px;
    animation: bounce 1.5s infinite;
}

@keyframes bounce {
    50% { transform: translateY(-20px); }
}

button {
    background: linear-gradient(45deg, #ff0080, #ff6600);
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 30px;
    font-size: 18px;
    cursor: pointer;
    margin: 15px;
}

button:hover {
    transform: scale(1.1);
}

#surprise {
    display: none;
    margin: 30px auto;
    max-width: 600px;
    padding: 25px;
    border: 2px solid gold;
    border-radius: 20px;
    background: rgba(255,255,255,0.08);
    animation: appear 1s;
}

@keyframes appear {
    from { opacity: 0; transform: scale(0.5); }
    to { opacity: 1; transform: scale(1); }
}

.message {
    font-size: 21px;
    line-height: 1.8;
}

.heart {
    position: fixed;
    bottom: -50px;
    animation: float 7s linear infinite;
    font-size: 25px;
    pointer-events: none;
}

@keyframes float {
    to {
        transform: translateY(-110vh) rotate(360deg);
    }
}

</style>
</head>

<body>

<div class="container">

<h1>🎉 HAPPY BIRTHDAY DAX 🎉</h1>

<p class="subtitle">
Today is not just a day, it's YOUR special day! ❤️
</p>

<div class="gift" onclick="openGift()">🎁</div>

<h2>Something Special Is Waiting For You!</h2>

<button onclick="openGift()">OPEN YOUR GIFT 🎁</button>

<div id="surprise">

<h1>❤️ DEAR DAX ❤️</h1>

<div class="message">

You are not just my brother,<br>
You are my best friend and my biggest support. ❤️<br><br>

May your life be filled with happiness,<br>
success, love and unforgettable memories.<br><br>

Never stop smiling and chasing your dreams!<br><br>

<strong>HAPPY BIRTHDAY ONCE AGAIN! 🎂</strong>

<h2>LOTS OF LOVE ❤️</h2>

</div>
</div>

</div>

<script>

function openGift() {
    document.getElementById("surprise").style.display = "block";

    for(let i = 0; i < 50; i++) {
        let confetti = document.createElement("div");
        confetti.innerHTML = ["🎉","✨","❤️","🎊"][Math.floor(Math.random()*4)];

        confetti.style.position = "fixed";
        confetti.style.left = Math.random()*100 + "vw";
        confetti.style.top = "-30px";
        confetti.style.fontSize = "25px";
        confetti.style.transition = "transform 3s linear";

        document.body.appendChild(confetti);

        setTimeout(() => {
            confetti.style.transform =
                "translateY(110vh) rotate(720deg)";
        }, 50);

        setTimeout(() => confetti.remove(), 3500);
    }
}

function createHeart() {
    let heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "❤️";
    heart.style.left = Math.random()*100 + "vw";
    document.body.appendChild(heart);

    setTimeout(() => heart.remove(), 7000);
}

setInterval(createHeart, 500);

</script>

</body>
</html>
"""

filename = "DAX_Birthday.html"

with open(filename, "w", encoding="utf-8") as f:
    f.write(html)

webbrowser.open("file://" + os.path.abspath(filename))

print("DAX Birthday Website Created Successfully!")