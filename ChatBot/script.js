let inactivityTimer;
let inactivityTime = 3000; // 3 Sekunden Inaktivität
const helpMessage = [
    "Wie geht's?",
    "Was machst du gerade?",
    "Erzähl mir einen Witz!",
    "Wie wird das Wetter?",
    "Was hast du heute gemacht?",
    "Wer bist du?",
    "Hast du Hunger?",
    "Was gibt's Neues?",
    "Lust auf eine Pause?",
    "Bist du müde?"
];

const helpBox = document.getElementById('help-box');
let selectedIndex = -1; // Index des aktuell ausgewählten Vorschlags

// Mausbewegung oder Tastendruck setzt den Inaktivität-Timer zurück
document.addEventListener('mousemove', startInactivityTimer);
document.addEventListener('keypress', startInactivityTimer);
document.getElementById("user-input").addEventListener('input', hideHelpMessage);

// Wenn der Benutzer die Maus bewegt, wird die Hilfe-Box ausgeblendet
document.addEventListener('mousemove', hideHelpMessage);

// Vorschläge anzeigen
function showHelpMessage() {
    helpBox.innerHTML = ""; // Leeren, bevor neue Vorschläge hinzugefügt werden
    helpMessage.forEach((message, index) => {
        const div = document.createElement('div');
        div.textContent = message;
        div.addEventListener('click', () => selectHelpMessage(index));
        helpBox.appendChild(div);
    });
    helpBox.style.display = 'block'; // Zeigt das Hilfefenster an
}

// Pfeiltasten für Navigation
document.getElementById("user-input").addEventListener('keydown', (event) => {
    if (event.key === "ArrowDown") {
        selectedIndex = Math.min(helpMessage.length - 1, selectedIndex + 1);
        highlightHelpMessage();
    } else if (event.key === "ArrowUp") {
        selectedIndex = Math.max(-1, selectedIndex - 1);
        highlightHelpMessage();
    } else if (event.key === "Enter" && selectedIndex !== -1) {
        document.getElementById("user-input").value = helpMessage[selectedIndex];
        hideHelpMessage(); // Vorschläge ausblenden, wenn eine Auswahl getroffen wurde
    }
});

// Helfen mit der Auswahl eines Vorschlags
function highlightHelpMessage() {
    const items = helpBox.querySelectorAll('div');
    items.forEach((item, index) => {
        if (index === selectedIndex) {
            item.classList.add('selected');
        } else {
            item.classList.remove('selected');
        }
    });
}

// Auswahl eines Vorschlags durch Klick
function selectHelpMessage(index) {
    document.getElementById("user-input").value = helpMessage[index];
    hideHelpMessage(); // Vorschläge ausblenden
}

// Hilfefenster ausblenden
function hideHelpMessage() {
    helpBox.style.display = 'none'; // Hilfe-Box ausblenden
    selectedIndex = -1; // Rücksetzen der Auswahl
}

// Inaktivitätstimer starten
function startInactivityTimer() {
    clearTimeout(inactivityTimer);
    inactivityTimer = setTimeout(showHelpMessage, inactivityTime);
}

// Nachricht senden
async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><b>Du:</b> ${userInput}</p>`;
    document.getElementById("user-input").value = "";

    const location = await getLocation();

    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userInput, location })
        });

        if (!response.ok) throw new Error(`Server-Fehler: ${response.status}`);

        const data = await response.json();
        chatBox.innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;
    } catch (error) {
        chatBox.innerHTML += `<p style="color:red;"><b>Fehler:</b> ${error.message}</p>`;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
    hideHelpMessage(); // Vorschläge ausblenden, wenn Nachricht gesendet wird
}

// Standort ermitteln
async function getLocation() {
    return new Promise((resolve) => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    resolve({
                        lat: position.coords.latitude,
                        lon: position.coords.longitude,
                    });
                },
                () => resolve(null)
            );
        } else {
            resolve(null);
        }
    });
}

// Timer starten
startInactivityTimer();
