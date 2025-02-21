import streamlit as st
import random

# Datenbank mit Mathe-Spielen
mathe_spiele = [
    {"name": "Zahlen-Bingo", "category": "Grundrechenarten", "grades": [5, 6], "instructions": "Die Lehrkraft ruft Rechenaufgaben auf, die Schüler markieren die Lösungen auf ihren Bingo-Karten."},
    {"name": "Blitzrechnen", "category": "Grundrechenarten", "grades": [5, 6, 7], "instructions": "Schüler lösen in kurzer Zeit möglichst viele Kopfrechenaufgaben."},
    {"name": "Mathe-Staffellauf", "category": "Bewegung", "grades": [5, 6, 7, 8], "instructions": "Teams lösen eine Matheaufgabe, bevor sie zur nächsten Station laufen dürfen."},
    {"name": "Zahlen-Memory", "category": "Denken & Logik", "grades": [5, 6, 7], "instructions": "Paare von Karten mit passenden Rechnungen und Ergebnissen finden."},
    {"name": "Würfel-Duell", "category": "Zufall & Wahrscheinlichkeiten", "grades": [5, 6, 7, 8], "instructions": "Zwei Schüler würfeln und müssen schnellstmöglich die Augensumme oder ein Produkt berechnen."},
    {"name": "Kettenrechnen", "category": "Grundrechenarten", "grades": [6, 7, 8], "instructions": "Jeder Schüler nennt das Ergebnis der vorherigen Rechnung und ergänzt eine neue Rechenoperation."},
    {"name": "Schätzmeister", "category": "Messen & Schätzen", "grades": [5, 6, 7, 8], "instructions": "Schüler schätzen Längen, Gewichte oder Volumina und vergleichen mit der tatsächlichen Messung."},
    {"name": "Bruch-Puzzle", "category": "Brüche & Prozente", "grades": [6, 7, 8], "instructions": "Passende Brüche, Dezimalzahlen und Prozente zuordnen."},
    {"name": "Zahlenrätsel", "category": "Denken & Logik", "grades": [5, 6, 7, 8], "instructions": "Schüler lösen knifflige Zahlenrätsel oder Sudoku-ähnliche Aufgaben."},
    {"name": "Flächenjagd", "category": "Geometrie", "grades": [6, 7, 8, 9], "instructions": "Schüler berechnen die Flächen von zufällig gezogenen geometrischen Formen."},
    {"name": "Würfelwahrscheinlichkeit", "category": "Zufall & Wahrscheinlichkeiten", "grades": [7, 8, 9, 10], "instructions": "Schüler berechnen Wahrscheinlichkeiten für verschiedene Würfelwürfe."},
    {"name": "Dreisatz-Duell", "category": "Brüche & Prozente", "grades": [7, 8, 9, 10], "instructions": "Schüler treten gegeneinander an, um Dreisatzaufgaben schneller zu lösen."},
    {"name": "Koordinaten-Schlacht", "category": "Geometrie", "grades": [6, 7, 8, 9], "instructions": "Schüler platzieren Schiffe auf einem Koordinatensystem und müssen sie durch gezielte Angriffe versenken."},
    {"name": "Fibonacci-Fieber", "category": "Denken & Logik", "grades": [7, 8, 9], "instructions": "Schüler müssen die nächste Zahl in einer Fibonacci-Folge erraten."},
    {"name": "Graphen-Rennen", "category": "Funktionen & Algebra", "grades": [8, 9, 10], "instructions": "Schüler müssen Graphen korrekt zeichnen und interpretieren."},
    {"name": "Schnelles Gleichungslösen", "category": "Funktionen & Algebra", "grades": [8, 9, 10], "instructions": "Schüler treten gegeneinander an, um Gleichungen möglichst schnell zu lösen."},
    {"name": "Formel-Domino", "category": "Geometrie", "grades": [7, 8, 9, 10], "instructions": "Schüler legen Karten mit Formeln passend aneinander."},
    {"name": "Zahlenmauern", "category": "Denken & Logik", "grades": [5, 6, 7], "instructions": "Schüler müssen die fehlenden Zahlen in Zahlenmauern ergänzen."},
    {"name": "Peng!", "category": "Grundrechenarten", "grades": [5, 6, 7, 8], "instructions": "Schüler zählen reihum, ersetzen aber bestimmte Zahlen (z. B. Vielfache von 3) durch 'Peng!'."}
]

# Streamlit UI
st.set_page_config(page_title="Mathe-Spiele-Generator", layout="centered")
st.title("🎲 Mathe-Spiele-Generator")

# Zentrierte Auswahlfelder
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
selected_grade = st.selectbox("Wähle die Klassenstufe:", [5, 6, 7, 8, 9, 10], index=0)
selected_category = st.selectbox("Wähle die Kategorie:", ["Alle", "Grundrechenarten", "Denken & Logik", "Geometrie", "Brüche & Prozente", "Funktionen & Algebra", "Messen & Schätzen", "Zufall & Wahrscheinlichkeiten", "Bewegung"], index=0)
st.markdown("</div>", unsafe_allow_html=True)

# Spielauswahl per Knopfdruck
def get_random_mathe_spiel():
    filtered_spiele = [s for s in mathe_spiele if selected_grade in s["grades"] and (selected_category == "Alle" or s["category"] == selected_category)]
    return random.choice(filtered_spiele) if filtered_spiele else None

# Zentrierter Button
if st.button("Spiel generieren", key="generate_button"):
    spiel = get_random_mathe_spiel()
    if spiel:
        st.markdown(f"<h3 style='text-align: center;'>{spiel['name']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'><strong>Kategorie:</strong> {spiel['category']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'><strong>Anleitung:</strong> {spiel['instructions']}</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='text-align: center;'>Kein passendes Spiel gefunden.</p>", unsafe_allow_html=True)

# Hinweis ganz unten
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Fügt Platz ein
st.markdown("<p style='text-align: center; font-size: smaller;'>created by Mr Übach in collaboration with ChatGPT</p>", unsafe_allow_html=True)

# Schul-Logo hinzufügen, zentriert und klein
st.markdown(
    "<div style='text-align: center;'><img src='main/school_logo.png' style='max-width: 100px; width: auto; height: auto;'></div>",
    unsafe_allow_html=True
)
