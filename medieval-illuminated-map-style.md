# 🎨 Średniowieczno-Słowiański Styl Mapy Iluminowanej

## Kompleksowy JSON dla Google Maps

### Główny Styl Mapy - Iluminowany Pergamin

```json
[
  {
    "elementType": "geometry",
    "stylers": [
      { "color": "#F8F1E4" }
    ]
  },
  {
    "elementType": "labels.text.fill",
    "stylers": [
      { "color": "#5D4E37" },
      { "weight": "bold" }
    ]
  },
  {
    "elementType": "labels.text.stroke",
    "stylers": [
      { "color": "#FCF5E5" },
      { "weight": 3 }
    ]
  },
  {
    "featureType": "road",
    "elementType": "geometry",
    "stylers": [
      { "color": "#D2B48C" },
      { "weight": 2 }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry",
    "stylers": [
      { "color": "#DAA520" },
      { "weight": 4 }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry.stroke",
    "stylers": [
      { "color": "#8B4513" },
      { "weight": 1 }
    ]
  },
  {
    "featureType": "road.local",
    "elementType": "geometry",
    "stylers": [
      { "color": "#CD853F" },
      { "weight": 1.5 }
    ]
  },
  {
    "featureType": "water",
    "elementType": "geometry",
    "stylers": [
      { "color": "#4682B4" }
    ]
  },
  {
    "featureType": "water",
    "elementType": "geometry.stroke",
    "stylers": [
      { "color": "#191970" },
      { "weight": 1 }
    ]
  },
  {
    "featureType": "landscape.natural",
    "elementType": "geometry",
    "stylers": [
      { "color": "#98FB98" }
    ]
  },
  {
    "featureType": "landscape.man_made",
    "elementType": "geometry",
    "stylers": [
      { "color": "#F5DEB3" }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "geometry",
    "stylers": [
      { "color": "#228B22" }
    ]
  },
  {
    "featureType": "poi.place_of_worship",
    "elementType": "geometry",
    "stylers": [
      { "color": "#DAA520" }
    ]
  },
  {
    "featureType": "poi.medical",
    "stylers": [
      { "visibility": "off" }
    ]
  },
  {
    "featureType": "poi.business",
    "stylers": [
      { "visibility": "off" }
    ]
  },
  {
    "featureType": "poi.government",
    "elementType": "geometry",
    "stylers": [
      { "color": "#8B0000" }
    ]
  },
  {
    "featureType": "administrative.country",
    "elementType": "geometry.stroke",
    "stylers": [
      { "color": "#8B0000" },
      { "weight": 3 }
    ]
  },
  {
    "featureType": "administrative.province",
    "elementType": "geometry.stroke",
    "stylers": [
      { "color": "#CD853F" },
      { "weight": 2 }
    ]
  },
  {
    "featureType": "administrative.locality",
    "elementType": "geometry.stroke",
    "stylers": [
      { "color": "#DAA520" },
      { "weight": 1 }
    ]
  },
  {
    "featureType": "transit",
    "stylers": [
      { "visibility": "off" }
    ]
  }
]
```

## Pergaminowe Nakładki CSS

### Tekstura Pergaminu

```css
.parchment-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: 
    radial-gradient(circle at 20% 30%, rgba(139, 69, 19, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(160, 82, 45, 0.08) 0%, transparent 40%),
    radial-gradient(circle at 40% 80%, rgba(205, 133, 63, 0.06) 0%, transparent 30%),
    linear-gradient(45deg, transparent 48%, rgba(139, 69, 19, 0.02) 49%, rgba(139, 69, 19, 0.02) 52%, transparent 53%),
    linear-gradient(-45deg, transparent 48%, rgba(160, 82, 45, 0.01) 49%, rgba(160, 82, 45, 0.01) 52%, transparent 53%);
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
      rgba(139, 69, 19, 0.03) 3px,
      rgba(139, 69, 19, 0.03) 4px
    ),
    repeating-linear-gradient(
      0deg,
      transparent,
      transparent 20px,
      rgba(160, 82, 45, 0.02) 21px,
      rgba(160, 82, 45, 0.02) 22px
    );
}
```

### Złote Efekty Iluminacji

```css
.gold-illumination {
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
  animation: goldShimmer 4s ease-in-out infinite;
  text-shadow: 
    0 0 10px rgba(255, 215, 0, 0.5),
    0 0 20px rgba(218, 165, 32, 0.3),
    0 0 30px rgba(255, 215, 0, 0.2);
}

@keyframes goldShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
```

### Średniowieczne Bordery

```css
.medieval-border {
  border: 4px solid;
  border-image: linear-gradient(
    45deg,
    #DAA520,
    #8B4513,
    #DAA520,
    #CD853F,
    #DAA520
  ) 1;
  position: relative;
}

.medieval-border::before {
  content: '';
  position: absolute;
  top: -8px;
  left: -8px;
  right: -8px;
  bottom: -8px;
  border: 2px solid #8B4513;
  border-radius: 8px;
  z-index: -1;
}

.medieval-border::after {
  content: '';
  position: absolute;
  top: -12px;
  left: -12px;
  right: -12px;
  bottom: -12px;
  background: linear-gradient(45deg, 
    rgba(218, 165, 32, 0.2), 
    rgba(139, 69, 19, 0.2)
  );
  border-radius: 12px;
  z-index: -2;
}
```

## Ornamentalne Elementy

### Słowiańskie Symbole Dekoracyjne

```css
.kolovrat {
  width: 60px;
  height: 60px;
  background: conic-gradient(
    from 0deg,
    #DAA520 0deg 45deg,
    #8B4513 45deg 90deg,
    #DAA520 90deg 135deg,
    #8B4513 135deg 180deg,
    #DAA520 180deg 225deg,
    #8B4513 225deg 270deg,
    #DAA520 270deg 315deg,
    #8B4513 315deg 360deg
  );
  border-radius: 50%;
  animation: rotate 10s linear infinite;
  box-shadow: 
    0 0 20px rgba(218, 165, 32, 0.4),
    inset 0 0 20px rgba(139, 69, 19, 0.3);
}

@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.zasiane-pole {
  width: 40px;
  height: 40px;
  background: #8B4513;
  position: relative;
  transform: rotate(45deg);
}

.zasiane-pole::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 2px;
  height: 100%;
  background: #DAA520;
  transform: translate(-50%, -50%);
}

.zasiane-pole::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 2px;
  background: #DAA520;
  transform: translate(-50%, -50%);
}
```

### Responsywny Zoom z Preservacją Detali

```css
.map-container {
  position: relative;
  overflow: hidden;
}

.detail-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
  pointer-events: none;
}

.map-container[data-zoom="close"] .detail-layer.high-detail {
  opacity: 1;
}

.map-container[data-zoom="medium"] .detail-layer.medium-detail {
  opacity: 1;
}

.map-container[data-zoom="far"] .detail-layer.low-detail {
  opacity: 1;
}

@media (max-width: 768px) {
  .medieval-border {
    border-width: 2px;
  }
  
  .kolovrat {
    width: 40px;
    height: 40px;
  }
  
  .zasiane-pole {
    width: 30px;
    height: 30px;
  }
}
```

## Integracja z Google Maps

### Implementacja JavaScript

```javascript
class IlluminatedMedievalMap {
  constructor(mapId, center, zoom) {
    this.map = new google.maps.Map(document.getElementById(mapId), {
      center: center,
      zoom: zoom,
      styles: this.getMedievalStyle(),
      mapTypeControl: false,
      streetViewControl: false,
      fullscreenControl: false
    });
    
    this.addParchmentOverlay();
    this.addMedievalControls();
    this.setupResponsiveDetails();
  }
  
  getMedievalStyle() {
    // Zwraca JSON styl zdefiniowany powyżej
    return medievalMapStyle;
  }
  
  addParchmentOverlay() {
    const overlay = document.createElement('div');
    overlay.className = 'parchment-overlay manuscript-texture';
    this.map.getDiv().appendChild(overlay);
  }
  
  addMedievalControls() {
    const compassRose = document.createElement('div');
    compassRose.className = 'compass-rose';
    compassRose.innerHTML = `
      <div class="kolovrat"></div>
      <div class="cardinal-points">
        <div class="north">⬆️</div>
        <div class="east">➡️</div>
        <div class="south">⬇️</div>
        <div class="west">⬅️</div>
      </div>
    `;
    
    this.map.controls[google.maps.ControlPosition.TOP_RIGHT].push(compassRose);
  }
  
  setupResponsiveDetails() {
    this.map.addListener('zoom_changed', () => {
      const zoom = this.map.getZoom();
      const container = this.map.getDiv().parentElement;
      
      if (zoom >= 15) {
        container.setAttribute('data-zoom', 'close');
      } else if (zoom >= 10) {
        container.setAttribute('data-zoom', 'medium');
      } else {
        container.setAttribute('data-zoom', 'far');
      }
    });
  }
}
```

## Właściwości dla Gier Terenowych

### Wysokiej Rozdzielczości Detale

```css
.terrain-game-details {
  font-family: 'Cinzel', 'Times New Roman', serif;
  font-size: 14px;
  font-weight: 600;
  text-shadow: 
    1px 1px 2px rgba(139, 69, 19, 0.8),
    0 0 5px rgba(218, 165, 32, 0.3);
  color: #5D4E37;
}

.landmark-label {
  background: linear-gradient(135deg, 
    rgba(248, 248, 255, 0.9) 0%,
    rgba(252, 245, 229, 0.9) 100%
  );
  border: 2px solid #DAA520;
  border-radius: 8px;
  padding: 4px 8px;
  box-shadow: 
    0 2px 10px rgba(139, 69, 19, 0.3),
    inset 0 1px 3px rgba(255, 255, 255, 0.5);
}

.distance-marker {
  font-size: 12px;
  background: rgba(139, 69, 19, 0.8);
  color: #FFD700;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #DAA520;
}
```

### Adaptacyjne Skalowanie

```css
@media (max-width: 1200px) {
  .terrain-game-details { font-size: 12px; }
  .landmark-label { padding: 3px 6px; }
  .distance-marker { 
    width: 20px; 
    height: 20px; 
    font-size: 10px; 
  }
}

@media (max-width: 768px) {
  .terrain-game-details { font-size: 11px; }
  .landmark-label { 
    padding: 2px 4px;
    font-size: 10px;
  }
  .distance-marker { 
    width: 18px; 
    height: 18px; 
    font-size: 9px; 
  }
}
```

## Nowoczesność w Średniowiecznym Stylu

### GPS i Współczesne Funkcje

```css
.modern-medieval-gps {
  background: linear-gradient(135deg,
    rgba(0, 206, 209, 0.1) 0%,
    rgba(70, 130, 180, 0.1) 100%
  );
  border: 2px solid #4682B4;
  border-radius: 8px;
  padding: 8px;
  font-family: 'Cinzel', serif;
  color: #2F4F4F;
  box-shadow: 
    0 0 15px rgba(70, 130, 180, 0.3),
    inset 0 1px 3px rgba(255, 255, 255, 0.2);
}

.satellite-view-medieval {
  filter: sepia(20%) contrast(110%) brightness(95%) hue-rotate(15deg);
  border: 3px solid #8B4513;
  border-radius: 12px;
}

.qr-code-medieval {
  background: #FCF5E5;
  border: 4px solid #DAA520;
  border-radius: 8px;
  padding: 8px;
  position: relative;
}

.qr-code-medieval::before {
  content: "🏰";
  position: absolute;
  top: -10px;
  left: -10px;
  background: #8B4513;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
}
```

### Scroll i Animacje

```css
.medieval-scroll-behavior {
  scroll-behavior: smooth;
  scroll-snap-type: y mandatory;
}

.legend-card {
  scroll-snap-align: start;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.legend-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 
    0 15px 30px rgba(139, 69, 19, 0.3),
    0 0 20px rgba(218, 165, 32, 0.2);
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
```
