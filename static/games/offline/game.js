cat << 'EOF' > static/games/offline/game.js
console.log("Offline game loaded");
let score = 0;
function increaseScore() {
    score++;
    document.getElementById('score').innerText = "Score: " + score;
}
EOF
