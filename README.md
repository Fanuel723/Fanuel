# Generator Scenariuszy Gier LARP "Szeptańce"

Generator Scenariuszy Gier LARP to aplikacja webowa stworzona w celu inspirowania i wspierania mistrzów gry w tworzeniu unikalnych przygód fabularnych. Aplikacja bazuje na bogatych legendach i historiach związanych z konkretnymi lokalizacjami z mapy projektu "Szeptańce".

Każdy wygenerowany scenariusz opiera się na założeniach **dramy pedagogicznej**, dostarczając nie tylko kontekst fabularny, ale także gotowe role, zarys konfliktu i cele edukacyjne, które mają na celu pobudzenie kreatywności i współpracy między graczami.

## Funkcjonalności

- **Dynamiczne generowanie scenariuszy**: Każde kliknięcie tworzy nową, unikalną historię opartą na prawdziwych legendach.
- **Integracja z mapą**: Każdy scenariusz jest powiązany z konkretną lokalizacją, która jest wyświetlana na osadzonej mapie Google.
- **Elementy dramy pedagogicznej**: Scenariusze zawierają gotowe propozycje ról, konfliktów i celów, które pomagają w prowadzeniu gry nastawionej na rozwój i współpracę.
- **Integracja z Dropbox**: Umożliwia użytkownikom przesyłanie własnych materiałów (zdjęć, dokumentów) do dedykowanych folderów na Dropboxie, aby wzbogacić scenariusz.

## Instalacja i uruchomienie

### 1. Wymagania wstępne

- Python 3.x
- `pip` (menedżer pakietów Pythona)

### 2. Instalacja zależności

Projekt korzysta z kilku bibliotek Pythona. Możesz je zainstalować za pomocą przygotowanego pliku `requirements.txt`.

Najpierw utwórz plik `requirements.txt`:
```bash
echo "Flask" > requirements.txt
echo "dropbox" >> requirements.txt
echo "werkzeug" >> requirements.txt
```

Następnie zainstaluj zależności:
```bash
pip install -r requirements.txt
```

### 3. Konfiguracja zmiennych środowiskowych

Aplikacja wymaga dwóch kluczy API do pełnego działania: jeden dla Google Maps i jeden dla Dropbox. Należy je ustawić jako zmienne środowiskowe.

**Dla systemów Linux/macOS:**
```bash
export GOOGLE_MAPS_API_KEY="Twoj_Klucz_API_Google_Maps"
export DROPBOX_ACCESS_TOKEN="Twoj_Token_Dostepowy_Dropbox"
```

**Dla systemu Windows (w Command Prompt):**
```cmd
set GOOGLE_MAPS_API_KEY="Twoj_Klucz_API_Google_Maps"
set DROPBOX_ACCESS_TOKEN="Twoj_Token_Dostepowy_Dropbox"
```

**Uwaga:**
- **Klucz Google Maps API** możesz uzyskać z [Google Cloud Console](https://console.cloud.google.com/google/maps-apis/overview). Upewnij się, że masz włączone **Maps Embed API**.
- **Token dostępowy Dropbox** możesz wygenerować, tworząc nową aplikację w [panelu deweloperskim Dropbox](https://www.dropbox.com/developers). Wybierz typ dostępu "App folder" i uprawnienia `files.content.write`.

Jeśli klucze nie zostaną ustawione, aplikacja uruchomi się, ale funkcje mapy i przesyłania plików będą nieaktywne (zostanie wyświetlony odpowiedni komunikat).

### 4. Przygotowanie danych

Aplikacja korzysta z danych o lokalizacjach zapisanych w pliku `larp_data.json`. Plik ten jest generowany na podstawie danych KML z mapy projektu.

Aby wygenerować lub zaktualizować dane, upewnij się, że plik `Projekt SzeptańceThe Susurrers Project – kopia (3).kml` znajduje się w głównym katalogu projektu, a następnie uruchom skrypt:
```bash
python3 parse_kml.py
```
Spowoduje to utworzenie lub nadpisanie pliku `larp_data.json`.

### 5. Uruchomienie aplikacji

Po zainstalowaniu zależności i skonfigurowaniu zmiennych środowiskowych, uruchom aplikację za pomocą polecenia:
```bash
python3 app.py
```
Serwer zostanie uruchomiony na porcie 5001. Otwórz przeglądarkę i wejdź na adres `http://127.0.0.1:5001`, aby rozpocząć korzystanie z generatora.