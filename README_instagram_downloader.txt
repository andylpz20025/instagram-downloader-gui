📄 README.md – Instagram Downloader Tool (Fotos, Reels, Alben, Videos)

📌 Beschreibung
Dieses Tool ist eine grafische Benutzeroberfläche (GUI), mit der du Instagram-Fotos, -Videos, -Reels und Alben herunterladen kannst.
Es basiert auf Python + PyQt6 und nutzt Instaloader, um Inhalte von Instagram zu laden.

💡 Hinweis:
- Funktioniert ohne Login für öffentliche Profile und Inhalte.
- Für private Inhalte (oder öffentliche Inhalte, die nur für eingeloggte Nutzer sichtbar sind) ist ein einmaliger Login nötig. Die Login-Session wird gespeichert.

🚀 Funktionen
- 📷 Download von Fotos
- 🎥 Download von Videos
- 🎬 Download von Reels
- 📚 Download von Alben/Karussells
- 🖱 Benutzerfreundliche GUI (kein Terminal nötig)
- 📂 Auswahl des Speicherorts vor jedem Download
- 🔑 Option zum Einloggen und Speichern der Session

📥 Installation
1. Python installieren
   Lade dir Python 3.10+ von python.org herunter und installiere es.
   ✅ Achte darauf, beim Installieren "Add to PATH" zu aktivieren.

2. Projekt-Ordner erstellen
   Lade den Quellcode in einen Ordner, z. B.  
   C:\Users\DeinName\Desktop\insta_downloader

3. Benötigte Pakete installieren
   Öffne in diesem Ordner ein Terminal (Eingabeaufforderung) und führe aus:
   pip install PyQt6 instaloader

4. Tool starten
   python insta_gui.py

🛠 Nutzung

🔓 Ohne Login (nur öffentliche Inhalte)
1. Starte das Programm.
2. Gib die vollständige URL des Instagram-Posts ein (Foto, Reel oder Album).
3. Wähle einen Speicherort.
4. Drücke "Download starten".

Beispiele für gültige URLs:
https://www.instagram.com/p/ABC123xyz/
https://www.instagram.com/reel/XYZ456abc/

🔑 Mit Login (auch für private Inhalte)
1. Starte das Programm.
2. Drücke "Login" und gib deinen Instagram-Benutzernamen & Passwort ein.
3. Die Session wird gespeichert (session.txt im Programmordner).
4. Du kannst nun auch Inhalte von privaten Profilen herunterladen (wenn dein Account Zugriff hat).

⚠️ Einschränkungen
- Kein Download von Storys oder Live-Videos in dieser Version.
- Private Inhalte nur mit Login und gültiger Berechtigung.
- Instagram kann seine API ändern – dann muss ggf. Instaloader aktualisiert werden:
  pip install --upgrade instaloader

📂 Projektstruktur
insta_downloader/
│
├── insta_gui.py       # Hauptprogramm (GUI)
├── README.md          # Diese Anleitung
└── session.txt        # (optional) Gespeicherte Login-Session

🔄 Updates
Falls Instagram etwas ändert und das Tool nicht mehr funktioniert:
pip install --upgrade instaloader

📝 Lizenz
Dieses Tool ist nur für persönliche, nicht-kommerzielle Nutzung gedacht.
Respektiere die Urheberrechte der Inhalte, die du herunterlädst.
