# Projekt-Dokumentation

Mirhan Özden

| Datum | Version | Zusammenfassung                                              |
| ----- | ------- | ------------------------------------------------------------ |
|       | 0.0.1   | ✍️ Jedes Mal, wenn Sie an dem Projekt arbeiten, fügen Sie hier eine neue Zeile ein und beschreiben in *einem* Satz, was Sie erreicht haben. |
|       | ...     |                                                              |
|       | 1.0.0   |                                                              |

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
| 1.A  |       | Mirhan Özden          |  Grundstruktur der Website machen.            |               |
| 2.A  |       | Mirhan Özden          |  Eingabefeld implementieren.            |               |
|3.A||Mirhan Özden|Eingegebene Nachricht wird angezeigt.||
|4.A||Mirhan Özden|Nachricht wird an Server geschickt.||
|5.A||Mirhan Özden|Auf gesendete Nachricht wird sinnvoll geantwortet.||
|6.A||Mirhan Özden|Die Antwort des Bots wird angezeigt.||
|7.A||Mirhan Özden|Layout ist für verschiedene Geräten anders.||
|8.A||Mirhan Özden|Fehlerhinweise bei Fehler in der Kommunikation.||
|9.A||Mirhan Özden|Vorschläge für Fragen anzeigen lassen||



## 3 Entscheiden

✍️ Dokumentieren Sie hier Ihre Entscheidungen und Annahmen, die Sie im Bezug auf Ihre User Stories und die Implementierung getroffen haben.

## 4 Realisieren

| AP-№ | Datum | Zuständig | geplante Zeit | tatsächliche Zeit |
| ---- | ----- | --------- | ------------- | ----------------- |
| 1.A  |       |           |               |                   |
| ...  |       |           |               |                   |

✍️ Tragen Sie jedes Mal, wenn Sie ein Arbeitspaket abschließen, hier ein, wie lang Sie effektiv dafür hatten.

## 5 Kontrollieren

| TC-№ | Datum | Resultat | Tester |
| ---- | ----- | -------- | ------ |
| 1.1  |       |          |        |
| ...  |       |          |        |

✍️ Vergessen Sie nicht, ein Fazit hinzuzufügen, welches das Test-Ergebnis einordnet.

