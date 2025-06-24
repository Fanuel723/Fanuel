# 🛠️ Instrukcja Wdrożenia Średniowieczno-Słowiańskiego Stylu Mapy

## Krok 1: Przygotowanie Google Cloud Console

### Konfiguracja Map Styles

1. **Wejdź do Google Cloud Console**
   - Otwórz [console.cloud.google.com](https://console.cloud.google.com)
   - Wybierz swój projekt lub utwórz nowy

2. **Przejdź do Map Styles**
   - W menu nawigacji wybierz "APIs & Services" > "Google Maps Platform"
   - Kliknij "Map Styles" w menu bocznym

3. **Utwórz nowy styl**
   - Kliknij "CREATE STYLE"
   - Wybierz "Import JSON"
   - Wklej JSON z pliku `medieval-illuminated-map-style.md`
   - Nadaj nazwę: "Średniowieczno-Słowiański Iluminowany"

4. **Opublikuj styl**
   - Kliknij "PUBLISH"
   - Skopiuj Style ID (będzie potrzebne w kodzie)

### Uzyskanie Map ID

1. **Utwórz Map ID**
   - W sekcji "Map IDs" kliknij "CREATE MAP ID"
   - Wybierz utworzony styl jako domyślny
   - Nadaj nazwę: "Szeptance-Medieval-Map"
   - Skopiuj Map ID

## Krok 2: Implementacja HTML i CSS

### Podstawowa struktura HTML

```html
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mapa Projektu Szeptańce - Średniowieczno-Słowiańska</title>
    
    <!-- Fonty Google -->
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
    
    <!-- Style własne -->
    <link rel="stylesheet" href="medieval-map-styles.css">
</head>
<body>
    <div class="map-container medieval-theme">
        <!-- Nawigacja z ornamentami -->
        <header class="medieval-header">
            <div class="header-ornament left">
                <div class="kolovrat"></div>
            </div>
            <h1 class="medieval-title">🏰 Mapa Projektu Szeptańce</h1>
            <div class="header-ornament right">
                <div class="zasiane-pole"></div>
            </div>
        </header>
        
        <!-- Główna mapa -->
        <div id="map" class="illuminated-map"></div>
        
        <!-- Nakładka pergaminowa -->
        <div class="parchment-overlay manuscript-texture"></div>
        
        <!-- Panel kontroli -->
        <div class="control-panel medieval-border">
            <h3>📜 Legendy Słowiańskie</h3>
            <div class="category-filters" id="categoryFilters">
                <!-- Filtry kategorii generowane dynamicznie -->
            </div>
        </div>
        
        <!-- Róża wiatrów -->
        <div class="compass-rose-container">
            <div class="compass-rose-medieval">
                <!-- SVG róży wiatrów -->
            </div>
        </div>
        
        <!-- Panel informacyjny -->
        <div class="info-panel medieval-scroll" id="infoPanel">
            <div class="panel-header">
                <h3>📖 Szczegóły Legendy</h3>
                <button class="close-btn" onclick="closeInfoPanel()">✕</button>
            </div>
            <div class="panel-content" id="legendDetails">
                <!-- Treść legendy -->
            </div>
        </div>
    </div>
    
    <!-- Skrypty -->
    <script src="https://maps.googleapis.com/maps/api/js?key=TWÓJ_API_KEY&map_ids=TWÓJ_MAP_ID&libraries=marker&callback=initMap" async defer></script>
    <script src="medieval-map-controller.js"></script>
</body>
</html>
```

### CSS - medieval-map-styles.css

```css
/* === ZMIENNE CSS === */
:root {
    /* Kolory pergaminowe */
    --pergamin-base: #FCF5E5;
    --pergamin-gradient: linear-gradient(45deg, #FCF5E5 0%, #F1D696 50%, #F8ECCD 100%);
    --pergamin-dark: #F5DEB3;
    
    /* Kolory złote */
    --zloto-slowianskie: #DAA520;
    --zloto-jasne: #FFD700;
    --zloto-ciemne: #B8860B;
    
    /* Kolory brązowe */
    --braz-ziemisty: #8B4513;
    --braz-jasny: #CD853F;
    --braz-ciemny: #654321;
    
    /* Kolory akcentowe */
    --czerwien-ochronna: #8B0000;
    --zielen-lesna: #228B22;
    --srebro-mistyczne: #C0C0C0;
    --niebieskie-misticum: #4682B4;
    
    /* Cienie i efekty */
    --cien-zloty: 0 4px 20px rgba(218, 165, 32, 0.3);
    --cien-sredniowieczny: 0 2px 15px rgba(139, 69, 19, 0.2);
    --blask-zloty: 0 0 20px rgba(255, 215, 0, 0.3);
    
    /* Typografia */
    --font-title: 'Cinzel', 'Times New Roman', serif;
    --font-body: 'Crimson Text', 'Georgia', serif;
    --font-ui: 'Open Sans', sans-serif;
}

/* === RESET I BAZOWE STYLE === */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: var(--font-body);
    background: var(--pergamin-gradient);
    min-height: 100vh;
    overflow-x: hidden;
}

/* === KONTENER MAPY === */
.map-container {
    position: relative;
    width: 100vw;
    height: 100vh;
    background: var(--pergamin-gradient);
}

.illuminated-map {
    width: 100%;
    height: 100%;
    position: relative;
    z-index: 1;
}

/* === NAKŁADKA PERGAMINOWA === */
.parchment-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(circle at 20% 30%, rgba(139, 69, 19, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 80% 70%, rgba(160, 82, 45, 0.06) 0%, transparent 40%),
        radial-gradient(circle at 40% 80%, rgba(205, 133, 63, 0.04) 0%, transparent 30%);
    pointer-events: none;
    z-index: 1000;
    mix-blend-mode: multiply;
}

.manuscript-texture {
    background-image: 
        repeating-linear-gradient(
            90deg,
            transparent,
            transparent 2px,
            rgba(139, 69, 19, 0.02) 3px,
            rgba(139, 69, 19, 0.02) 4px
        ),
        repeating-linear-gradient(
            0deg,
            transparent,
            transparent 20px,
            rgba(160, 82, 45, 0.015) 21px,
            rgba(160, 82, 45, 0.015) 22px
        );
}

/* === NAGŁÓWEK ŚREDNIOWIECZNY === */
.medieval-header {
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    gap: 20px;
    z-index: 2000;
    background: var(--pergamin-gradient);
    padding: 15px 30px;
    border: 3px solid var(--zloto-slowianskie);
    border-radius: 12px;
    box-shadow: var(--cien-sredniowieczny);
}

.medieval-title {
    font-family: var(--font-title);
    font-size: 2rem;
    font-weight: 700;
    color: var(--braz-ziemisty);
    text-shadow: 
        2px 2px 4px rgba(139, 69, 19, 0.3),
        0 0 10px rgba(218, 165, 32, 0.2);
    margin: 0;
}

.header-ornament {
    display: flex;
    align-items: center;
    justify-content: center;
}

/* === SŁOWIAŃSKIE ORNAMENTY === */
.kolovrat {
    width: 50px;
    height: 50px;
    background: conic-gradient(
        from 0deg,
        var(--zloto-slowianskie) 0deg 45deg,
        var(--braz-ziemisty) 45deg 90deg,
        var(--zloto-slowianskie) 90deg 135deg,
        var(--braz-ziemisty) 135deg 180deg,
        var(--zloto-slowianskie) 180deg 225deg,
        var(--braz-ziemisty) 225deg 270deg,
        var(--zloto-slowianskie) 270deg 315deg,
        var(--braz-ziemisty) 315deg 360deg
    );
    border-radius: 50%;
    animation: rotate 10s linear infinite;
    box-shadow: var(--blask-zloty);
    position: relative;
}

.kolovrat::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 20px;
    height: 20px;
    background: var(--zloto-jasne);
    border-radius: 50%;
    transform: translate(-50%, -50%);
}

@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.zasiane-pole {
    width: 40px;
    height: 40px;
    background: var(--braz-ziemisty);
    position: relative;
    transform: rotate(45deg);
    border: 2px solid var(--zloto-slowianskie);
}

.zasiane-pole::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 2px;
    height: 100%;
    background: var(--zloto-slowianskie);
    transform: translate(-50%, -50%);
}

.zasiane-pole::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 100%;
    height: 2px;
    background: var(--zloto-slowianskie);
    transform: translate(-50%, -50%);
}

/* === ŚREDNIOWIECZNE BORDERY === */
.medieval-border {
    border: 4px solid;
    border-image: linear-gradient(
        45deg,
        var(--zloto-slowianskie),
        var(--braz-ziemisty),
        var(--zloto-slowianskie),
        var(--braz-jasny),
        var(--zloto-slowianskie)
    ) 1;
    position: relative;
    background: var(--pergamin-gradient);
}

.medieval-border::before {
    content: '';
    position: absolute;
    top: -8px;
    left: -8px;
    right: -8px;
    bottom: -8px;
    border: 2px solid var(--braz-ziemisty);
    border-radius: 8px;
    z-index: -1;
}

/* === PANEL KONTROLI === */
.control-panel {
    position: absolute;
    top: 120px;
    left: 20px;
    width: 300px;
    max-height: 60vh;
    overflow-y: auto;
    padding: 20px;
    z-index: 1500;
    border-radius: 12px;
    box-shadow: var(--cien-sredniowieczny);
}

.control-panel h3 {
    font-family: var(--font-title);
    color: var(--braz-ziemisty);
    margin-bottom: 15px;
    text-align: center;
    font-size: 1.2rem;
}

.category-filters {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
    gap: 10px;
}

.category-filter {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 8px;
    background: var(--pergamin-base);
    border: 2px solid var(--zloto-slowianskie);
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.category-filter:hover {
    transform: translateY(-2px);
    box-shadow: var(--cien-zloty);
    background: linear-gradient(135deg, var(--zloto-jasne), var(--zloto-slowianskie));
}

.category-filter.active {
    background: linear-gradient(135deg, var(--zloto-slowianskie), var(--zloto-ciemne));
    color: white;
}

.category-emoji {
    font-size: 1.5rem;
    margin-bottom: 4px;
}

.category-name {
    font-size: 0.7rem;
    font-weight: 600;
    text-align: center;
    font-family: var(--font-ui);
}

/* === RÓŻA WIATRÓW === */
.compass-rose-container {
    position: absolute;
    top: 20px;
    right: 20px;
    z-index: 1500;
}

.compass-rose-medieval {
    width: 80px;
    height: 80px;
    background: var(--pergamin-gradient);
    border: 3px solid var(--braz-ziemisty);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: var(--cien-sredniowieczny);
    animation: gentleFloat 3s ease-in-out infinite;
}

@keyframes gentleFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-5px); }
}

/* === PANEL INFORMACYJNY === */
.info-panel {
    position: absolute;
    bottom: 20px;
    right: 20px;
    width: 350px;
    max-height: 400px;
    background: var(--pergamin-gradient);
    border-radius: 12px;
    z-index: 1500;
    transform: translateX(100%);
    transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: var(--cien-sredniowieczny);
    overflow: hidden;
}

.info-panel.open {
    transform: translateX(0);
}

.panel-header {
    background: linear-gradient(135deg, var(--zloto-slowianskie), var(--zloto-ciemne));
    padding: 15px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.panel-header h3 {
    font-family: var(--font-title);
    color: white;
    margin: 0;
}

.close-btn {
    background: none;
    border: none;
    color: white;
    font-size: 1.2rem;
    cursor: pointer;
    padding: 5px;
    border-radius: 3px;
    transition: background-color 0.2s;
}

.close-btn:hover {
    background-color: rgba(255, 255, 255, 0.2);
}

.panel-content {
    padding: 20px;
    overflow-y: auto;
    max-height: 300px;
}

/* === MARKERY MAP === */
.custom-marker {
    background: var(--pergamin-base);
    border: 2px solid var(--zloto-slowianskie);
    border-radius: 50%;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: var(--cien-sredniowieczny);
}

.custom-marker:hover {
    transform: scale(1.2);
    box-shadow: var(--blask-zloty);
    z-index: 1000;
}

.custom-marker.pulsing {
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}

/* === KOMBINOWANE MARKERY === */
.heraldical-shield {
    width: 32px;
    height: 32px;
    position: relative;
    border: 2px solid var(--braz-ziemisty);
    border-radius: 4px 4px 8px 8px;
    overflow: hidden;
    box-shadow: var(--cien-sredniowieczny);
    cursor: pointer;
    transition: all 0.3s ease;
}

.heraldical-shield:hover {
    transform: scale(1.15);
    box-shadow: var(--blask-zloty);
}

.heraldical-shield.per-pale {
    background: linear-gradient(90deg, 
        var(--category-a-color) 50%, 
        var(--category-b-color) 50%);
}

.heraldical-shield.per-fess {
    background: linear-gradient(180deg, 
        var(--category-a-color) 50%, 
        var(--category-b-color) 50%);
}

/* === RESPONSYWNOŚĆ === */
@media (max-width: 1200px) {
    .medieval-title {
        font-size: 1.5rem;
    }
    
    .control-panel {
        width: 250px;
    }
    
    .info-panel {
        width: 300px;
    }
}

@media (max-width: 768px) {
    .medieval-header {
        flex-direction: column;
        gap: 10px;
        padding: 10px 20px;
    }
    
    .medieval-title {
        font-size: 1.2rem;
    }
    
    .header-ornament {
        display: none;
    }
    
    .control-panel {
        width: 200px;
        left: 10px;
        top: 80px;
    }
    
    .info-panel {
        width: calc(100vw - 20px);
        right: 10px;
        bottom: 10px;
    }
    
    .custom-marker,
    .heraldical-shield {
        width: 24px;
        height: 24px;
    }
    
    .category-emoji {
        font-size: 1.2rem;
    }
    
    .kolovrat {
        width: 35px;
        height: 35px;
    }
    
    .zasiane-pole {
        width: 30px;
        height: 30px;
    }
}

@media (max-width: 480px) {
    .control-panel {
        width: 150px;
    }
    
    .category-filters {
        grid-template-columns: 1fr 1fr;
    }
    
    .medieval-title {
        font-size: 1rem;
    }
}

/* === ANIMACJE PRZEJŚĆ === */
.medieval-scroll-behavior {
    scroll-behavior: smooth;
    scroll-snap-type: y mandatory;
}

.legend-card {
    scroll-snap-align: start;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    background: var(--pergamin-base);
    border: 2px solid var(--zloto-slowianskie);
    border-radius: 8px;
    padding: 15px;
    margin: 10px 0;
}

.legend-card:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: var(--cien-zloty);
}

@keyframes manuscriptUnfold {
    0% { 
        transform: perspective(1000px) rotateX(90deg);
        opacity: 0;
    }
    50% { 
        transform: perspective(1000px) rotateX(45deg);
        opacity: 0.5;
    }
    100% { 
        transform: perspective(1000px) rotateX(0deg);
        opacity: 1;
    }
}

.unfold-animation {
    animation: manuscriptUnfold 1s ease-out;
}

/* === ZŁOTE EFEKTY TEKSTOWE === */
.gold-text {
    background: linear-gradient(
        135deg,
        #FFD700 0%,
        #DAA520 15%,
        #FFF8DC 30%,
        #DAA520 45%,
        #B8860B 60%,
        #DAA520 75%,
        #FFD700 100%
    );
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: goldShimmer 3s ease-in-out infinite;
}

@keyframes goldShimmer {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* === EFEKTY HOVER DLA DETALI === */
.terrain-detail {
    font-size: 0.8rem;
    background: rgba(252, 245, 229, 0.9);
    border: 1px solid var(--zloto-slowianskie);
    border-radius: 4px;
    padding: 2px 6px;
    color: var(--braz-ziemisty);
    font-weight: 600;
    text-shadow: 1px 1px 2px rgba(139, 69, 19, 0.3);
    box-shadow: 0 1px 4px rgba(139, 69, 19, 0.2);
}

.distance-marker {
    background: var(--czerwien-ochronna);
    color: var(--zloto-jasne);
    border-radius: 50%;
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7rem;
    font-weight: bold;
    border: 1px solid var(--zloto-slowianskie);
}
```

## Krok 3: JavaScript - medieval-map-controller.js

### Główny kontroler mapy

```javascript
// medieval-map-controller.js

class MedievalSlavicMap {
    constructor() {
        this.map = null;
        this.markers = [];
        this.infoWindow = null;
        this.categories = this.initializeCategories();
        this.activeFilters = new Set();
        this.shieldGenerator = new HeraldicalShieldGenerator();
        
        // Binding
        this.handleMarkerClick = this.handleMarkerClick.bind(this);
        this.handleCategoryFilter = this.handleCategoryFilter.bind(this);
    }
    
    // Inicjalizacja kategorii
    initializeCategories() {
        return {
            // Podstawowe kategorie
            duch: { emoji: "👻", color: "#E6E6FA", name: "Duch" },
            bestia: { emoji: "🐺", color: "#8B4513", name: "Bestia" },
            smok: { emoji: "🐉", color: "#DC143C", name: "Smok" },
            czart: { emoji: "😈", color: "#8B0000", name: "Czart" },
            skarb: { emoji: "💰", color: "#FFD700", name: "Skarb" },
            lokacja: { emoji: "🏰", color: "#228B22", name: "Lokacja" },
            straznik: { emoji: "⚔️", color: "#8FBC8F", name: "Strażnik" },
            zjawisko: { emoji: "✨", color: "#FF6347", name: "Zjawisko" },
            czar: { emoji: "🔮", color: "#4B0082", name: "Czar/Klątwa" },
            uroczysko: { emoji: "🌳", color: "#556B2F", name: "Uroczysko" },
            czarownik: { emoji: "🧙", color: "#2F4F4F", name: "Czarownik" },
            proces: { emoji: "⚖️", color: "#800000", name: "Proces" },
            zbrodnie: { emoji: "🔍", color: "#2C2C2C", name: "Zbrodnie" },
            wspolczesne: { emoji: "📱", color: "#00CED1", name: "Współczesne" },
            
            // Podkategorie uroczysk
            kurhany: { emoji: "⛰️", color: "#8B7D6B", name: "Kurhany" },
            swiate_gaje: { emoji: "🌲", color: "#228B22", name: "Święte Gaje" },
            oltarze: { emoji: "🗿", color: "#696969", name: "Ołtarze" },
            kregi_kamienne: { emoji: "⭕", color: "#A0522D", name: "Kręgi Kamienne" },
            
            // Mniejszości kulturowe
            zydowskie: { emoji: "✡️", color: "#4169E1", name: "Żydowskie" },
            lemkowskie: { emoji: "🏔️", color: "#FF8C00", name: "Łemkowskie" },
            huculsie: { emoji: "🎻", color: "#DA70D6", name: "Huculsie" },
            ormianskie: { emoji: "🕊️", color: "#CD853F", name: "Ormiańskie" },
            romskie: { emoji: "🎪", color: "#FF1493", name: "Romskie" },
            niemieckie: { emoji: "🍺", color: "#708090", name: "Niemieckie" }
        };
    }
    
    // Inicjalizacja mapy
    async initMap() {
        const { Map, InfoWindow } = await google.maps.importLibrary("maps");
        const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
        
        this.map = new Map(document.getElementById("map"), {
            zoom: 7,
            center: { lat: 52.0693, lng: 19.4803 }, // Centrum Polski
            mapId: "TWÓJ_MAP_ID", // Zastąp własnym Map ID
            disableDefaultUI: true,
            zoomControl: true,
            fullscreenControl: false,
            streetViewControl: false
        });
        
        this.infoWindow = new InfoWindow();
        
        // Inicjalizacja kontroli
        this.initializeCategoryFilters();
        this.initializeCompassRose();
        
        // Ładowanie legend
        await this.loadLegends();
        
        // Dodanie nasłuchiwaczy zdarzeń
        this.setupEventListeners();
    }
    
    // Inicjalizacja filtrów kategorii
    initializeCategoryFilters() {
        const container = document.getElementById('categoryFilters');
        
        Object.entries(this.categories).forEach(([key, category]) => {
            const filterElement = document.createElement('div');
            filterElement.className = 'category-filter';
            filterElement.dataset.category = key;
            
            filterElement.innerHTML = `
                <span class="category-emoji">${category.emoji}</span>
                <span class="category-name">${category.name}</span>
            `;
            
            filterElement.addEventListener('click', () => this.handleCategoryFilter(key));
            container.appendChild(filterElement);
        });
    }
    
    // Obsługa filtrów kategorii
    handleCategoryFilter(categoryKey) {
        const filterElement = document.querySelector(`[data-category="${categoryKey}"]`);
        
        if (this.activeFilters.has(categoryKey)) {
            this.activeFilters.delete(categoryKey);
            filterElement.classList.remove('active');
        } else {
            this.activeFilters.add(categoryKey);
            filterElement.classList.add('active');
        }
        
        this.updateMarkersVisibility();
    }
    
    // Aktualizacja widoczności markerów
    updateMarkersVisibility() {
        this.markers.forEach(markerData => {
            const { marker, legend } = markerData;
            
            if (this.activeFilters.size === 0) {
                marker.map = this.map;
            } else {
                const hasMatchingCategory = legend.categories.some(cat => 
                    this.activeFilters.has(cat)
                );
                marker.map = hasMatchingCategory ? this.map : null;
            }
        });
    }
    
    // Tworzenie markera
    createMarker(legend) {
        const categories = legend.categories.map(cat => this.categories[cat]).filter(Boolean);
        
        let markerContent;
        if (categories.length === 1) {
            markerContent = this.createSingleCategoryMarker(categories[0]);
        } else {
            markerContent = this.createCombinedMarker(categories, legend.shieldType || 'per-pale');
        }
        
        const marker = new google.maps.marker.AdvancedMarkerElement({
            map: this.map,
            position: { lat: legend.lat, lng: legend.lng },
            content: markerContent,
            title: legend.title
        });
        
        marker.addListener('click', () => this.handleMarkerClick(legend, marker));
        
        return marker;
    }
    
    // Marker pojedynczej kategorii
    createSingleCategoryMarker(category) {
        const markerDiv = document.createElement('div');
        markerDiv.className = 'custom-marker pulsing';
        markerDiv.style.backgroundColor = category.color;
        markerDiv.innerHTML = `<span class="category-emoji">${category.emoji}</span>`;
        
        return markerDiv;
    }
    
    // Marker kombinowany (tarcza heraldyczna)
    createCombinedMarker(categories, shieldType) {
        const markerDiv = document.createElement('div');
        markerDiv.className = `heraldical-shield ${shieldType}`;
        
        // Implementacja różnych typów tarcz
        switch (shieldType) {
            case 'per-pale':
                markerDiv.style.background = `linear-gradient(90deg, ${categories[0].color} 50%, ${categories[1].color} 50%)`;
                markerDiv.innerHTML = `
                    <span class="category-emoji left" style="position: absolute; left: 25%; top: 50%; transform: translate(-50%, -50%); font-size: 10px;">${categories[0].emoji}</span>
                    <span class="category-emoji right" style="position: absolute; right: 25%; top: 50%; transform: translate(50%, -50%); font-size: 10px;">${categories[1].emoji}</span>
                `;
                break;
                
            case 'per-fess':
                markerDiv.style.background = `linear-gradient(180deg, ${categories[0].color} 50%, ${categories[1].color} 50%)`;
                markerDiv.innerHTML = `
                    <span class="category-emoji top" style="position: absolute; left: 50%; top: 25%; transform: translate(-50%, -50%); font-size: 10px;">${categories[0].emoji}</span>
                    <span class="category-emoji bottom" style="position: absolute; left: 50%; bottom: 25%; transform: translate(-50%, 50%); font-size: 10px;">${categories[1].emoji}</span>
                `;
                break;
                
            case 'per-chevron':
                markerDiv.innerHTML = this.createChevronShield(categories);
                break;
                
            case 'quarterly':
                markerDiv.innerHTML = this.createQuarterlyShield(categories);
                break;
                
            default:
                markerDiv.innerHTML = this.createSingleCategoryMarker(categories[0]).innerHTML;
        }
        
        return markerDiv;
    }
    
    // Obsługa kliknięcia w marker
    handleMarkerClick(legend, marker) {
        const content = this.createInfoWindowContent(legend);
        
        this.infoWindow.setContent(content);
        this.infoWindow.open({
            anchor: marker,
            map: this.map
        });
        
        // Aktualizacja panelu bocznego
        this.updateInfoPanel(legend);
    }
    
    // Tworzenie contentu InfoWindow
    createInfoWindowContent(legend) {
        const categoriesHtml = legend.categories
            .map(cat => this.categories[cat])
            .filter(Boolean)
            .map(cat => `<span class="category-tag" style="background: ${cat.color}; color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.8rem; margin-right: 4px;">${cat.emoji} ${cat.name}</span>`)
            .join('');
        
        return `
            <div class="info-window-content" style="max-width: 300px; font-family: 'Crimson Text', serif;">
                <h3 style="margin: 0 0 10px 0; color: #8B4513; font-family: 'Cinzel', serif;">${legend.title}</h3>
                <div class="categories" style="margin-bottom: 10px;">${categoriesHtml}</div>
                <p style="margin: 0; line-height: 1.4; color: #5D4E37;">${legend.description}</p>
                <div style="margin-top: 10px; font-size: 0.8rem; color: #8B4513;">
                    <strong>Region:</strong> ${legend.region || 'Nieznany'}<br>
                    <strong>Źródło:</strong> ${legend.source || 'Tradycja ludowa'}
                </div>
            </div>
        `;
    }
    
    // Aktualizacja panelu informacyjnego
    updateInfoPanel(legend) {
        const panel = document.getElementById('infoPanel');
        const details = document.getElementById('legendDetails');
        
        const categoriesHtml = legend.categories
            .map(cat => this.categories[cat])
            .filter(Boolean)
            .map(cat => `
                <div class="category-detail" style="display: flex; align-items: center; margin-bottom: 8px;">
                    <span style="font-size: 1.2rem; margin-right: 8px;">${cat.emoji}</span>
                    <span style="color: ${cat.color}; font-weight: 600;">${cat.name}</span>
                </div>
            `)
            .join('');
        
        details.innerHTML = `
            <div class="legend-details">
                <h4 style="color: #8B4513; margin-bottom: 15px; font-family: 'Cinzel', serif;">${legend.title}</h4>
                
                <div class="categories-section" style="margin-bottom: 15px;">
                    <h5 style="color: #5D4E37; margin-bottom: 8px;">Kategorie:</h5>
                    ${categoriesHtml}
                </div>
                
                <div class="description-section" style="margin-bottom: 15px;">
                    <h5 style="color: #5D4E37; margin-bottom: 8px;">Opis:</h5>
                    <p style="line-height: 1.5; color: #654321;">${legend.description}</p>
                </div>
                
                <div class="metadata-section">
                    <h5 style="color: #5D4E37; margin-bottom: 8px;">Informacje:</h5>
                    <div class="metadata-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.9rem;">
                        <div><strong>Region:</strong><br>${legend.region || 'Nieznany'}</div>
                        <div><strong>Typ:</strong><br>${legend.type || 'Legenda'}</div>
                        <div><strong>Źródło:</strong><br>${legend.source || 'Tradycja ludowa'}</div>
                        <div><strong>Status:</strong><br>${legend.verified ? 'Zweryfikowana' : 'Oczekująca'}</div>
                    </div>
                </div>
            </div>
        `;
        
        panel.classList.add('open');
    }
    
    // Ładowanie legend z API lub pliku JSON
    async loadLegends() {
        try {
            // Przykładowe dane - zastąp właściwym API
            const legends = await this.fetchLegends();
            
            legends.forEach(legend => {
                const marker = this.createMarker(legend);
                this.markers.push({ marker, legend });
            });
            
        } catch (error) {
            console.error('Błąd ładowania legend:', error);
        }
    }
    
    // Symulacja pobierania legend
    async fetchLegends() {
        // W rzeczywistej aplikacji pobierz z API
        return [
            {
                id: 1,
                title: "Smok Wawelski",
                lat: 50.0647,
                lng: 19.9450,
                categories: ['smok', 'lokacja'],
                shieldType: 'per-pale',
                description: "Legenda o smoku mieszkającym w jaskini pod Wzgórzem Wawelskim, który terroryzował mieszkańców Krakowa.",
                region: "Małopolska",
                source: "Kronika Wincentego Kadłubka",
                verified: true
            },
            {
                id: 2,
                title: "Czarownica z Łysej Góry",
                lat: 50.8973,
                lng: 20.8937,
                categories: ['czarownik', 'uroczysko', 'zjawisko'],
                shieldType: 'per-chevron',
                description: "Opowieść o potężnej czarownicy, która przewodziła sabatom wiedźm na Łysej Górze.",
                region: "Świętokrzyskie",
                source: "Podania ludowe",
                verified: false
            }
            // Dodaj więcej legend...
        ];
    }
    
    // Inicjalizacja róży wiatrów
    initializeCompassRose() {
        const compass = document.querySelector('.compass-rose-medieval');
        if (compass) {
            compass.addEventListener('click', () => {
                this.map.setCenter({ lat: 52.0693, lng: 19.4803 });
                this.map.setZoom(7);
            });
        }
    }
    
    // Nasłuchiwacze zdarzeń
    setupEventListeners() {
        // Zamykanie panelu informacyjnego
        window.closeInfoPanel = () => {
            document.getElementById('infoPanel').classList.remove('open');
        };
        
        // Responsywność zoom
        this.map.addListener('zoom_changed', () => {
            const zoom = this.map.getZoom();
            const container = document.querySelector('.map-container');
            
            if (zoom >= 15) {
                container.setAttribute('data-zoom', 'close');
            } else if (zoom >= 10) {
                container.setAttribute('data-zoom', 'medium');
            } else {
                container.setAttribute('data-zoom', 'far');
            }
        });
        
        // Adaptacja do rozmiaru ekranu
        window.addEventListener('resize', () => {
            google.maps.event.trigger(this.map, 'resize');
        });
    }
    
    // Metody pomocnicze dla heraldycznych tarcz
    createChevronShield(categories) {
        return `
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 50%; background: ${categories[0].color}; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 8px;">${categories[0].emoji}</span>
            </div>
            <div style="position: absolute; bottom: 0; left: 0; width: 50%; height: 50%; background: ${categories[1].color}; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 8px;">${categories[1].emoji}</span>
            </div>
            <div style="position: absolute; bottom: 0; right: 0; width: 50%; height: 50%; background: ${categories[2].color}; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 8px;">${categories[2].emoji}</span>
            </div>
        `;
    }
    
    createQuarterlyShield(categories) {
        return `
            <div style="position: absolute; top: 0; left: 0; width: 50%; height: 50%; background: ${categories[0].color}; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 6px;">${categories[0].emoji}</span>
            </div>
            <div style="position: absolute; top: 0; right: 0; width: 50%; height: 50%; background: ${categories[1].color}; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 6px;">${categories[1].emoji}</span>
            </div>
            <div style="position: absolute; bottom: 0; left: 0; width: 50%; height: 50%; background: ${categories[2].color}; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 6px;">${categories[2].emoji}</span>
            </div>
            <div style="position: absolute; bottom: 0; right: 0; width: 50%; height: 50%; background: ${categories[3].color}; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 6px;">${categories[3].emoji}</span>
            </div>
        `;
    }
}

// Generator heraldycznych tarcz
class HeraldicalShieldGenerator {
    constructor() {
        this.shieldTypes = {
            'per-pale': this.generatePerPale,
            'per-fess': this.generatePerFess,
            'per-chevron': this.generatePerChevron,
            'quarterly': this.generateQuarterly
        };
    }
    
    generateCombinedMarker(categories, shieldType = 'per-pale') {
        if (categories.length === 1) {
            return this.generateSingleMarker(categories[0]);
        }
        
        const generator = this.shieldTypes[shieldType];
        if (!generator) {
            throw new Error(`Nieznany typ tarczy: ${shieldType}`);
        }
        
        return generator.call(this, categories);
    }
    
    generateSingleMarker(category) {
        return `
            <div class="single-category-marker" style="background-color: ${category.color};">
                <span class="category-emoji">${category.emoji}</span>
            </div>
        `;
    }
    
    // Implementacje różnych typów tarcz...
    generatePerPale(categories) {
        const [catA, catB] = categories;
        return `
            <div class="heraldical-shield per-pale" style="background: linear-gradient(90deg, ${catA.color} 50%, ${catB.color} 50%);">
                <span class="category-emoji left">${catA.emoji}</span>
                <span class="category-emoji right">${catB.emoji}</span>
            </div>
        `;
    }
    
    // Pozostałe metody generowania...
}

// Inicjalizacja po załadowaniu strony
let medievalMap;

window.initMap = async function() {
    medievalMap = new MedievalSlavicMap();
    await medievalMap.initMap();
};

// Export dla możliwości importu w innych modułach
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { MedievalSlavicMap, HeraldicalShieldGenerator };
}
```

## Krok 4: Implementacja dla Gier Terenowych

### Dodatkowe funkcjonalności

```javascript
// Rozszerzenia dla gier terenowych
class TerrainGameExtensions {
    constructor(map) {
        this.map = map;
        this.currentPosition = null;
        this.targetMarkers = [];
        this.gameMode = false;
    }
    
    // Aktywacja trybu gry terenowej
    activateGameMode() {
        this.gameMode = true;
        this.enableGeolocation();
        this.addGameControls();
        this.setupDistanceCalculation();
    }
    
    // Geolokalizacja
    enableGeolocation() {
        if (navigator.geolocation) {
            navigator.geolocation.watchPosition(
                (position) => this.updatePlayerPosition(position),
                (error) => console.error('Błąd geolokalizacji:', error),
                { enableHighAccuracy: true, timeout: 5000, maximumAge: 60000 }
            );
        }
    }
    
    // Aktualizacja pozycji gracza
    updatePlayerPosition(position) {
        const newPos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };
        
        if (this.currentPosition) {
            this.currentPosition.setMap(null);
        }
        
        this.currentPosition = new google.maps.Marker({
            position: newPos,
            map: this.map.map,
            icon: {
                path: google.maps.SymbolPath.CIRCLE,
                scale: 8,
                fillColor: '#FF0000',
                fillOpacity: 0.8,
                strokeWeight: 2,
                strokeColor: '#FFFFFF'
            },
            title: 'Twoja pozycja'
        });
        
        this.updateDistances(newPos);
    }
    
    // Aktualizacja dystansów do celów
    updateDistances(playerPos) {
        this.targetMarkers.forEach(target => {
            const distance = this.calculateDistance(playerPos, target.position);
            target.distanceElement.textContent = `${distance}m`;
            
            // Zmiana koloru w zależności od odległości
            if (distance < 50) {
                target.distanceElement.style.backgroundColor = '#00FF00';
            } else if (distance < 200) {
                target.distanceElement.style.backgroundColor = '#FFFF00';
            } else {
                target.distanceElement.style.backgroundColor = '#FF0000';
            }
        });
    }
    
    // Kalkulacja odległości
    calculateDistance(pos1, pos2) {
        const R = 6371e3; // Promień Ziemi w metrach
        const φ1 = pos1.lat * Math.PI/180;
        const φ2 = pos2.lat * Math.PI/180;
        const Δφ = (pos2.lat-pos1.lat) * Math.PI/180;
        const Δλ = (pos2.lng-pos1.lng) * Math.PI/180;
        
        const a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
                Math.cos(φ1) * Math.cos(φ2) *
                Math.sin(Δλ/2) * Math.sin(Δλ/2);
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
        
        return Math.round(R * c);
    }
    
    // Dodanie kontroli gry
    addGameControls() {
        const gamePanel = document.createElement('div');
        gamePanel.className = 'game-controls medieval-border';
        gamePanel.style.cssText = `
            position: absolute;
            bottom: 20px;
            left: 20px;
            padding: 15px;
            background: var(--pergamin-gradient);
            z-index: 1500;
            border-radius: 8px;
        `;
        
        gamePanel.innerHTML = `
            <h4 style="margin: 0 0 10px 0; color: #8B4513;">🎮 Tryb Gry Terenowej</h4>
            <button onclick="terrainGame.findNearestLegend()" class="game-btn">🎯 Znajdź Najbliższą Legendę</button>
            <button onclick="terrainGame.startQuest()" class="game-btn">⚔️ Rozpocznij Quest</button>
            <div id="gameStatus" style="margin-top: 10px; font-size: 0.9rem; color: #654321;"></div>
        `;
        
        document.querySelector('.map-container').appendChild(gamePanel);
    }
    
    // Znajdowanie najbliższej legendy
    findNearestLegend() {
        if (!this.currentPosition) {
            alert('Nie można określić Twojej pozycji');
            return;
        }
        
        let nearest = null;
        let minDistance = Infinity;
        
        this.map.markers.forEach(markerData => {
            const distance = this.calculateDistance(
                this.currentPosition.getPosition().toJSON(),
                markerData.marker.position
            );
            
            if (distance < minDistance) {
                minDistance = distance;
                nearest = markerData;
            }
        });
        
        if (nearest) {
            this.map.map.panTo(nearest.marker.position);
            this.map.handleMarkerClick(nearest.legend, nearest.marker);
            
            document.getElementById('gameStatus').innerHTML = 
                `🎯 Najbliższa legenda: <strong>${nearest.legend.title}</strong><br>
                📍 Odległość: <strong>${minDistance}m</strong>`;
        }
    }
    
    // Rozpoczęcie questa
    startQuest() {
        const gameStatus = document.getElementById('gameStatus');
        gameStatus.innerHTML = `
            ⚔️ <strong>Quest rozpoczęty!</strong><br>
            🎯 Cel: Odwiedź 3 legendy w promieniu 5km<br>
            📊 Postęp: 0/3
        `;
        
        // Logika questa...
    }
}

// CSS dla gier terenowych
const terrainGameCSS = `
.game-btn {
    background: linear-gradient(135deg, #DAA520, #B8860B);
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 5px;
    cursor: pointer;
    margin-right: 8px;
    margin-bottom: 5px;
    font-size: 0.8rem;
    transition: all 0.2s ease;
}

.game-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(218, 165, 32, 0.3);
}

.distance-indicator {
    position: absolute;
    top: -8px;
    right: -8px;
    background: #FF0000;
    color: white;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7rem;
    font-weight: bold;
    border: 1px solid #FFD700;
}

.quest-marker {
    animation: questPulse 2s infinite;
}

@keyframes questPulse {
    0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 215, 0, 0.7); }
    70% { transform: scale(1.1); box-shadow: 0 0 0 10px rgba(255, 215, 0, 0); }
    100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 215, 0, 0); }
}
`;

// Dodanie CSS do dokumentu
const terrainGameStyleSheet = document.createElement('style');
terrainGameStyleSheet.textContent = terrainGameCSS;
document.head.appendChild(terrainGameStyleSheet);
```

## Krok 5: Testowanie i Optymalizacja

### Lista kontrolna wdrożenia

```markdown
## ✅ Lista Kontrolna Wdrożenia

### Google Cloud Console
- [ ] Utworzono styl mapy w Map Styles
- [ ] Wygenerowano Map ID
- [ ] Skonfigurowano klucz API z odpowiednimi uprawnieniami
- [ ] Przetestowano styl na różnych poziomach zoom

### Pliki CSS i JavaScript
- [ ] Zaimplementowano wszystkie style średniowieczne
- [ ] Dodano animacje i efekty
- [ ] Przetestowano responsywność na różnych urządzeniach
- [ ] Zoptymalizowano wydajność (lazy loading, kompresja)

### Funkcjonalności
- [ ] Wszystkie 24 kategorie ikon działają poprawnie
- [ ] System heraldycznych tarcz funkcjonuje
- [ ] Filtry kategorii reagują prawidłowo
- [ ] InfoWindow i panel boczny wyświetlają się correctly
- [ ] Geolokalizacja dla gier terenowych działa

### Testowanie
- [ ] Przetestowano na Chrome, Firefox, Safari, Edge
- [ ] Sprawdzono na urządzeniach mobilnych (iOS, Android)
- [ ] Zweryfikowano działanie w trybie offline (PWA)
- [ ] Przetestowano wydajność przy dużej liczbie markerów

### Optymalizacja
- [ ] Kompresja plików CSS i JavaScript
- [ ] Optymalizacja obrazów SVG
- [ ] Cache'owanie zasobów
- [ ] Lazy loading dla dużych zestawów danych
```

### Przykładowe dane testowe

```javascript
// test-data.js - Przykładowe legendy do testowania
const testLegends = [
    {
        id: 1,
        title: "Smok Wawelski",
        lat: 50.0647,
        lng: 19.9450,
        categories: ['smok', 'lokacja'],
        shieldType: 'per-pale',
        description: "Legenda o smoku mieszkającym w jaskini pod Wzgórzem Wawelskim.",
        region: "Małopolska",
        verified: true
    },
    {
        id: 2,
        title: "Bazyliszek Warszawski",
        lat: 52.2297,
        lng: 21.0122,
        categories: ['bestia', 'zbrodnie'],
        shieldType: 'per-fess',
        description: "Potwór z żółwią skorupą i kogucim grzebieniem terroryzujący Warszawę.",
        region: "Mazowsze",
        verified: false
    },
    // Dodaj więcej przykładów...
];
```

## Krok 6: Dokumentacja dla Użytkowników

### Instrukcja użytkowania

1. **Nawigacja po mapie**
   - Użyj gestów/myszki do przesuwania mapy
   - Scroll/pinch do zmiany poziomu przybliżenia
   - Kliknij Różę Wiatrów aby wrócić do centrum Polski

2. **Filtrowanie legend**
   - Kliknij kategorie w panelu po lewej stronie
   - Aktywne filtry są podświetlone złotym kolorem
   - Kliknij ponownie aby wyłączyć filtr

3. **Przeglądanie szczegółów**
   - Kliknij marker aby zobaczyć podstawowe informacje
   - Panel po prawej stronie zawiera szczegółowe dane
   - Użyj przycisku X aby zamknąć panel

4. **Tryb gry terenowej**
   - Włącz lokalizację w przeglądarce
   - Kliknij "Tryb Gry Terenowej" aby aktywować
   - Śledź swoją pozycję i odległości do legend

Ta kompletna instrukcja wdrożenia zapewnia wszystkie niezbędne elementy do stworzenia w pełni funkcjonalnej średniowieczno-słowiańskiej mapy iluminowanej z 24 kategoriami ikon zgodnie z Protokołem Kolberg 2.0.