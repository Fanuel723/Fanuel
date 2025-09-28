from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
import json
import random
import os
import signal
import dropbox
from werkzeug.utils import secure_filename
import traceback
import logging

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'a-fallback-secret-key-for-development')

# --- Konfiguracja z użyciem zmiennych środowiskowych ---
# Użytkownik powinien ustawić te zmienne w swoim środowisku.
# Przykład: export GOOGLE_MAPS_API_KEY='TwojKluczAPI'
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
DROPBOX_ACCESS_TOKEN = os.getenv('DROPBOX_ACCESS_TOKEN')

IS_DROPBOX_CONFIGURED = bool(DROPBOX_ACCESS_TOKEN)
IS_MAPS_CONFIGURED = bool(GOOGLE_MAPS_API_KEY)

# --- Logowanie ---
logging.basicConfig(filename='flask_app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

def load_larp_data():
    try:
        with open('larp_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        app.logger.error(f"Nie udało się wczytać pliku larp_data.json: {e}")
        return []

larp_locations = load_larp_data()

def generate_larp_scenario(location):
    roles = [
        {"role": "Strażnik/czka Tajemnicy", "description": "Osoba, która od pokoleń strzeże sekretu tego miejsca."},
        {"role": "Badacz/ka Zjawisk Paranormalnych", "description": "Naukowiec, który przybył tu, aby zbadać legendę."},
        {"role": "Potomek/Potomkini Dawnych Mieszkańców", "description": "Osoba czująca emocjonalną więź z tym miejscem."},
        {"role": "Sceptyk/Sceptyczka", "description": "Dziennikarz/ka szukający/a racjonalnego wyjaśnienia."},
        {"role": "Zbłąkany/a Wędrowiec/Wędrowniczka", "description": "Osoba, która trafiła tu przypadkiem."}
    ]
    conflicts = [
        "Odkrycie prawdy i zdecydowanie, co z nią zrobić.",
        "Spór między wierzącymi w legendę a sceptykami.",
        "Uspokojenie ducha nawiedzającego to miejsce.",
        "Ochrona miejsca przed zewnętrznym zagrożeniem (np. deweloperami)."
    ]
    goals = [
        "Zrozumienie, jak przeszłość wpływa na teraźniejszość.",
        "Skłonienie do współpracy pomimo różnych celów.",
        "Zachęcenie do kreatywnego rozwiązywania problemów.",
        "Refleksja nad wartościami takimi jak prawda, pamięć i dziedzictwo."
    ]

    k = min(random.randint(3, 4), len(roles))
    selected_roles = random.sample(roles, k=k)

    scenario_details = {
        "Tytuł Scenariusza": f"Szepty w {location.get('name')}",
        "Kontekst Fabularny": location.get('description', 'Brak opisu.'),
        "Proponowane Role": selected_roles,
        "Zarys Konfliktu": random.choice(conflicts),
        "Cele Dramy": random.choice(goals)
    }

    return {
        "name": location.get("name"),
        "coordinates": location.get("coordinates"),
        "image_url": location.get("image_url"),
        "scenario_details": scenario_details
    }

@app.route('/')
def index():
    return render_template('index.html',
                           dropbox_configured=IS_DROPBOX_CONFIGURED,
                           maps_configured=IS_MAPS_CONFIGURED,
                           google_maps_api_key=GOOGLE_MAPS_API_KEY)

@app.route('/api/scenario')
def get_scenario():
    try:
        if not larp_locations:
            return jsonify({"error": "Brak danych o lokalizacjach."}), 404
        location = random.choice(larp_locations)
        scenario = generate_larp_scenario(location)
        return jsonify(scenario)
    except Exception:
        app.logger.error("Błąd w get_scenario:\n" + traceback.format_exc())
        return jsonify({"error": "Wystąpił wewnętrzny błąd serwera."}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    if not IS_DROPBOX_CONFIGURED:
        flash('Integracja z Dropbox nie jest skonfigurowana. Administrator musi ustawić zmienną środowiskową DROPBOX_ACCESS_TOKEN.', 'error')
        return redirect(url_for('index'))

    if 'file' not in request.files or request.files['file'].filename == '':
        flash('Nie wybrano żadnego pliku.', 'error')
        return redirect(request.referrer or url_for('index'))

    file = request.files['file']
    scenario_name = request.form.get('scenario_name', 'BezNazwy')
    filename = secure_filename(file.filename)
    folder_name = "".join(c for c in scenario_name if c.isalnum() or c in (' ', '_')).rstrip()
    dropbox_path = f'/Szeptańce/{folder_name}/{filename}'

    try:
        dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
        dbx.files_upload(file.read(), dropbox_path, mode=dropbox.files.WriteMode('overwrite'))
        flash(f'Plik "{filename}" został pomyślnie przesłany do folderu "{folder_name}" na Dropboxie.', 'success')
    except dropbox.exceptions.AuthError:
        app.logger.error("Błąd autoryzacji Dropbox. Sprawdź poprawność tokena.")
        flash('Błąd autoryzacji z Dropbox. Sprawdź konfigurację serwera.', 'error')
    except Exception as e:
        app.logger.error("Błąd przesyłania do Dropbox:\n" + traceback.format_exc())
        flash('Wystąpił nieoczekiwany błąd podczas przesyłania pliku.', 'error')

    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=False)