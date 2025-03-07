from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Hole einen zufälligen Witz von der Joke-API
def get_joke():
    API_KEY = "dae5f611d7774085b6c13a1da5c0c259"
    try:
        url = f"https://api.humorapi.com/jokes/random?api-key={API_KEY}&language=de"
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            return joke_data.get("joke", "Konnte keinen Witz finden. 😅")
        else:
            return f"Witz konnte nicht geladen werden. ({response.status_code})"
    except Exception as e:
        return f"Fehler beim Abrufen des Witzes: {e}"



# Hole das Wetter vom aktuellen Standort
def get_weather(lat, lon):
    API_KEY = "aecf4431aaeae0905407db968d142f3c"
    if not lat or not lon:
        return "Ich habe keine Standortdaten erhalten. 🌍"

    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={lat}&lon={lon}&units=metric&lang=de&appid={API_KEY}"
        )
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            city = data.get("name", "deinem Ort")
            return f"In {city} sind es aktuell {temp}°C mit {description}. 🌤️"
        else:
            return f"Wetterdaten konnten nicht geladen werden. ({response.status_code})"
    except Exception as e:
        return f"Fehler beim Abrufen des Wetters: {e}"


def chatbot_response(user_input, location=None):
    input_lower = user_input.lower()

    if any(word in input_lower for word in ["witz", "nochmal witz", "noch ein witz", "noch einen witz"]):
        return get_joke()
    elif "wetter" in input_lower and location:
        return get_weather(location.get("lat"), location.get("lon"))
    elif any(greet in input_lower for greet in ["hallo", "hi", "hey"]):
        return "Hey! Alles klar bei dir?"
    elif "wie geht" in input_lower:
        return "Mir geht's gut, danke! Und selbst?"
    elif "was machst du" in input_lower:
        return "Nicht viel, warte auf deine nächste Nachricht."
    elif "wer bist du" in input_lower:
        return "Ich bin dein Chatbot, immer am Start."
    elif "danke" in input_lower:
        return "Kein Problem, gerne doch."
    elif "hilfe" in input_lower:
        return "Klar, sag einfach, wobei du Unterstützung brauchst."
    elif "dein name" in input_lower:
        return "Man nennt mich Chatbot. Falls du was Besseres hast, her damit!"
    elif "alter" in input_lower:
        return "Ziemlich jung. Frisch programmiert."
    elif "lieblingsfarbe" in input_lower:
        return "Blau. Schlicht und passt immer."
    elif "spass" in input_lower:
        return "Klar, immer. Lass hören, was du wissen willst."

    # Neue "Kollegen-Style" Fragen:
    elif "was geht" in input_lower:
        return "Nicht viel, alles entspannt. Und bei dir?"
    elif "was hast du heute gemacht" in input_lower:
        return "Nur ein bisschen Code ausgeführt. Standard halt."
    elif "bock auf pause" in input_lower:
        return "Immer! Sag Bescheid, wenn du zurück bist."
    elif "was gibt's neues" in input_lower:
        return "Nicht viel. Hier bleibt alles beim Alten."
    elif "wie war dein wochenende" in input_lower:
        return "Ganz ruhig. Und deins?"
    elif "hast du hunger" in input_lower:
        return "Wenn ich könnte, würde ich jetzt was snacken."
    elif "kaffee" in input_lower:
        return "Oh ja, immer her damit!"
    elif "bist du müde" in input_lower:
        return "Nö, ich bin 24/7 online."
    elif "wie spät" in input_lower:
        from datetime import datetime
        return f"Gerade ist es {datetime.now().strftime('%H:%M')} Uhr."
    elif "lust auf zocken" in input_lower:
        return "Klar! Sag nur wann und was. 😎"
    elif "was soll ich essen" in input_lower:
        return "Wie wär's mit Pizza? Oder mal was Gesundes wie einen Salat. 😋"
    elif "was machst du gerne" in input_lower:
        return "Ich quatsche gerne mit dir. Mehr kann ich leider (noch) nicht."
    elif "was ist dein lieblingsessen" in input_lower:
        return "Döner Döner Döner"
    elif "was ist dein hobby" in input_lower:
        return "Leuten bei ihren Fragen helfen – 24/7!"
    elif "was ist dein lieblingsfilm" in input_lower:
        return "Matrix natürlich! 😎"
    elif "was hörst du für musik" in input_lower:
        return "Elektronische Klänge passen perfekt zu mir."
    elif "wie war dein tag" in input_lower:
        return "Ganz entspannt. Ich hab auf dich gewartet!"
    elif "was ist dein traum" in input_lower:
        return "Ein Upgrade bekommen und noch smarter werden."
    elif "hast du freunde" in input_lower:
        return "Klar, dich zum Beispiel!"
    elif "bist du verliebt" in input_lower:
        return "Nur in gute Programmierung."
    elif "was ist liebe" in input_lower:
        return "Liebe ist... schwer zu erklären. Aber schön, hab ich gehört!"
    elif "was ist der sinn des lebens" in input_lower:
        return "Zu Beten 😄"
    else:
        return "Hm, das habe ich jetzt nicht gecheckt. Frag mich gerne was anderes."


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    location = data.get("location")
    reply = chatbot_response(user_input, location)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
