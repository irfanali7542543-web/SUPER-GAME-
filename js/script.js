function triggerKillEffect(weaponName, weaponLevel) {
    // Determine Color and Glow based on Weapon/Upgrade
    let effectColor = "#ffffff"; // Default White
    let glowIntensity = "10px";

    if (weaponName.includes("Glacier")) {
        effectColor = "#00f2ff"; // Glacier Blue
        glowIntensity = "20px";
    } else if (weaponName.includes("Fire") || weaponName.includes("AKM")) {
        effectColor = "#ff0000"; // Red/Fire
        glowIntensity = "25px";
    }

    // Hit Flash Effect on Screen
    document.body.style.boxShadow = "inset 0 0 " + glowIntensity + " " + effectColor;
    
    // Show Kill Message
    showKillMessage(weaponName, effectColor);

    // Reset Flash after 0.5s
    setTimeout(() => {
        document.body.style.boxShadow = "none";
    }, 500);
}

function showKillMessage(weapon, color) {
    let msg = document.createElement("div");
    msg.style.position = "fixed";
    msg.style.right = "20px";
    msg.style.top = "100px";
    msg.style.color = color;
    msg.style.fontSize = "24px";
    msg.style.fontWeight = "bold";
    msg.style.textShadow = "0 0 10px " + color;
    msg.innerHTML = "ELIMINATED WITH " + weapon + " <span class='rotating-chicken'>🍗</span>";
    document.body.appendChild(msg);
    
    setTimeout(() => msg.remove(), 3000);
}
