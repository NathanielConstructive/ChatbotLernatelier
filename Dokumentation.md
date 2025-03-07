# Projekt-Dokumentation

Mirhan Özden

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
| 14.02      | 0.0.1   | Frontend ist implementiert, man kann dort Sachen eingeben und es ist eine ansichtliche Website. |
|  28.02     | 1.0.0     |  Auf die Texte, die man eingibt wird eingegangen und eine KI antwortet dementsprechend                                                            |

## 1 Informieren

### 1.1 Ihr Projekt

Mein Projekt beinhaltet ein Chatbot welches gewisse Fragen beantworten kann. 


Mein Chatbot ist mit HTML, CSS, JavaScript und Python programmiert worden. Ich habe zwei APIs genutzt, damit mein Chatbot auf gewisse Sachen antworten kann. Der Bot kann beispielsweise das Wetter anzeigen und Witze erzählen.

### 1.2 User Stories

| US-№ | Verbindlichkeit | Typ  | Beschreibung                       |
| ---- | --------------- | ---- | ---------------------------------- |
| 1    |  Muss               | Funktional     |Als Benutzer möchte ich eine Grundstruktur auf der Website haben, damit ich die Chatbox und Eingabefelder klar erkenne. |
| 2  |    Muss             | Funktional     | Als Benutzer möchte ich meine Nachricht in ein Eingabefeld eingeben können, damit ich mit dem Chatbot kommunizieren kann.|
|3|Muss|Funktional|Als Benutzer möchte ich, dass meine eingegebene Nachricht in der Chatbox angezeigt wird, damit ich meinen Input und den Chatverlauf sehe.	|
|4|Muss|Funktional|Als Benutzer möchte ich, dass meine Nachricht an den Server geschickt wird, damit der Chatbot darauf antworten kann.	|
|5|Muss|Funktional|Als Benutzer möchte ich, dass der Chatbot meine Nachricht verarbeitet und sinnvoll darauf antwortet.	|
|6|Muss|Funktional|Als Benutzer möchte ich, dass die Antwort des Chatbots in der Chatbox angezeigt wird, damit ich die Unterhaltung nachvollziehen kann.	|
|7|Kann|Qualität|Als Benutzer möchte ich, dass die Website auf verschiedenen Geräten gut aussieht, damit ich sie überall nutzen kann. 	|
|8|Kann|Qualität|Als Benutzer möchte ich Fehlerhinweise erhalten, wenn die Kommunikation mit dem Chatbot fehlschlägt, damit ich weiss, was schiefgelaufen ist.|
|9|Kann|Qualität|Als Benutzer möchte ich Vorschläge kriegen, wenn ich nichts eingebe, damit ich weiss, worauf der Bot antworten kann.|


### 1.3 Testfälle

| TC-№ | Ausgangslage | Eingabe | Erwartete Ausgabe |
| ---- | ------------ | ------- | ----------------- |
| 1.1  |  Website wird gestartet            | -        |    Struktur der Website wird angezeigt.               |
| 2.1  |  Website wurde aufgerufen            | Links klick auf das Eingabefeld und Drücken einer Taste        |  Text im Textfeld                 |
|3.1|Text wurde in Textfeld eingegeben|Es wird auf "senden" gedrückt|Der Text wird im Chat angezeigt|
|4.1|Eine Nachricht wurde verfasst und auf "senden" gedrückt.|-|-|
|5.1|Nachricht wurde gesendet|-|Passende Antwort wurde gesendet.|
|6.1|Passende Antwort wurde gesendet|-|Die Antwort des Bots wird angezeigt.|
|7.1|Website wird auf einem anderen Handy aufgerufen|-|Layout der Website ändert sich.|
|8.1|Etwas falsches wird eingegeben|Auf senden drücken|"Hm, das habe ich jetzt nicht gecheckt. Frag mich gerne was anderes."|
|9.1|Man hat linksklick auf das Eingabefeld gedrückt.|-|Feld mit verschiedenen Vorschlägen die gefragt werden können.|



## 2 Planen

| AP-№ | Frist | Zuständig | Beschreibung | geplante Zeit |
| ---- | ----- | --------- | ------------ | ------------- |
| 1.A  | 17.1      | Mirhan Özden          |  Grundstruktur der Website machen.            | 90 Minuten              |
| 2.A  | 17.1      | Mirhan Özden          |  Eingabefeld implementieren.            |  45 Minuten             |
|3.A|24.1|Mirhan Özden|Eingegebene Nachricht wird angezeigt.|90 Minuten|
|4.A|24.1|Mirhan Özden|Nachricht wird an Server geschickt.|180 Minuten|
|5.A|14.2|Mirhan Özden|Auf gesendete Nachricht wird sinnvoll geantwortet.|225|
|6.A|14.2|Mirhan Özden|Die Antwort des Bots wird angezeigt.|90|
|7.A|20.1|Mirhan Özden|Layout ist für verschiedene Geräten anders.|90|
|8.A|20.1|Mirhan Özden|Fehlerhinweise bei Fehler in der Kommunikation.|90|
|9.A|28.1|Mirhan Özden|Vorschläge für Fragen anzeigen lassen|135|



## 3 Entscheiden

Ich habe mich dazu entschieden, eine Website zu machen, wo man einen Chat mit einem Bot führen kann. Man kann in einem Eingabefeld Fragen schreiben und senden, welche direkt über dem Feld angezeigt und beantwortet werden. Die KI kann Sachen wie Wetter anzeigen und Witze erzählen. Dazu kann es zu anderen Standartfragen antworten. Wenn man nichts gerade im Kopf hat, werden Vorschläge angezeigt. Zudem ist das Layout dynamisch, spricht, es ändert sich je nach Gerät.ö

## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| 1.A  | 17.1  | Mirhan Özden | 90 Minuten | 110 Minuten |
| 2.A  | 17.1  | Mirhan Özden | 45 Minuten | 65 Minuten |
| 3.A  | 24.1  | Mirhan Özden | 90 Minuten | 110 Minuten |
| 4.A  | 24.1  | Mirhan Özden | 180 Minuten | 200 Minuten |
| 5.A  | 28.1  | Mirhan Özden | 225 Minuten | 275 Minuten |
| 6.A  | 14.2  | Mirhan Özden | 90 Minuten | 110 Minuten |
| 7.A  | 20.1  | Mirhan Özden | 90 Minuten | 110 Minuten |
| 8.A  | 28.1  | Mirhan Özden | 90 Minuten | 110 Minuten |
| 9.A  | 28.1  | Mirhan Özden | 135 Minuten | 155 Minuten |



## 5 Kontrollieren

| TC-№ | Datum  | Resultat  | Tester        |
| ---- | ------ | --------- | ------------- |
| 1.1  | 28.02 | erfolgreich | Mirhan Özden |
| 1.2  | 28.02 | erfolgreich | Mirhan Özden |
| 1.3  | 28.02 | erfolgreich | Mirhan Özden |
| 1.4  | 28.02 | erfolgreich | Mirhan Özden |
| 1.5  | 28.02 | erfolgreich | Mirhan Özden |
| 1.6  | 28.02 | erfolgreich | Mirhan Özden |
| 1.7  | 28.02 | erfolgreich | Mirhan Özden |
| 1.8  | 28.02 | erfolgreich | Mirhan Özden |
| 1.9  | 28.02 | erfolgreich | Mirhan Özden |


Jedes Test ist erfolgreich gewesen,
