# ⚔️ System Heraldycznych Tarcz dla Kombinacji Kategorii

## Tarcze dla Wielokategorialnych Legend

### Podział Per Pale (Pionowy) - 2 kategorie

```svg
<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="shieldGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#DAA520;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8B4513;stop-opacity:1" />
        </linearGradient>
        
        <filter id="medievalShadow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="2" dy="2" stdDeviation="2" flood-color="#000000" flood-opacity="0.4"/>
        </filter>
    </defs>
    
    <!-- Tło tarczy -->
    <path d="M20 2 L38 10 L38 28 Q38 38 20 38 Q2 38 2 28 L2 10 Z" 
          fill="url(#shieldGradient)" 
          stroke="#654321" 
          stroke-width="1" 
          filter="url(#medievalShadow)"/>
    
    <!-- Linia podziału -->
    <line x1="20" y1="2" x2="20" y2="38" stroke="#654321" stroke-width="1"/>
    
    <!-- Ornamenty -->
    <circle cx="6" cy="6" r="1" fill="#FFD700"/>
    <circle cx="34" cy="6" r="1" fill="#FFD700"/>
    <circle cx="20" cy="35" r="1" fill="#FFD700"/>
    
    <!-- Placeholder dla kategorii A (lewa strona) -->
    <text x="10" y="22" text-anchor="middle" font-size="12" font-family="Apple Color Emoji">{categoryA}</text>
    
    <!-- Placeholder dla kategorii B (prawa strona) -->
    <text x="30" y="22" text-anchor="middle" font-size="12" font-family="Apple Color Emoji">{categoryB}</text>
</svg>
```

### Podział Per Fess (Poziomy) - 2 kategorie

```svg
<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="shieldGradient2" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#CD853F;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#A0522D;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <!-- Tło tarczy -->
    <path d="M20 2 L38 10 L38 28 Q38 38 20 38 Q2 38 2 28 L2 10 Z" 
          fill="url(#shieldGradient2)" 
          stroke="#654321" 
          stroke-width="1" 
          filter="url(#medievalShadow)"/>
    
    <!-- Linia podziału -->
    <line x1="2" y1="20" x2="38" y2="20" stroke="#654321" stroke-width="1"/>
    
    <!-- Ornamenty -->
    <circle cx="6" cy="6" r="1" fill="#FFD700"/>
    <circle cx="34" cy="6" r="1" fill="#FFD700"/>
    <circle cx="20" cy="35" r="1" fill="#FFD700"/>
    
    <!-- Placeholder dla kategorii A (góra) -->
    <text x="20" y="14" text-anchor="middle" font-size="12" font-family="Apple Color Emoji">{categoryA}</text>
    
    <!-- Placeholder dla kategorii B (dół) -->
    <text x="20" y="30" text-anchor="middle" font-size="12" font-family="Apple Color Emoji">{categoryB}</text>
</svg>
```

### Podział Per Chevron (Trójkątny) - 3 kategorie

```svg
<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="shieldGradient3" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#B8860B;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#DAA520;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8B4513;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <!-- Tło tarczy -->
    <path d="M20 2 L38 10 L38 28 Q38 38 20 38 Q2 38 2 28 L2 10 Z" 
          fill="url(#shieldGradient3)" 
          stroke="#654321" 
          stroke-width="1" 
          filter="url(#medievalShadow)"/>
    
    <!-- Linie podziału chevron -->
    <path d="M2 22 L20 12 L38 22 L38 28 Q38 38 20 38 Q2 38 2 28 Z" 
          fill="none" 
          stroke="#654321" 
          stroke-width="1"/>
    
    <!-- Ornamenty -->
    <circle cx="10" cy="8" r="1" fill="#FFD700"/>
    <circle cx="30" cy="8" r="1" fill="#FFD700"/>
    <circle cx="20" cy="35" r="1" fill="#FFD700"/>
    
    <!-- Placeholder dla kategorii A (góra) -->
    <text x="20" y="10" text-anchor="middle" font-size="10" font-family="Apple Color Emoji">{categoryA}</text>
    
    <!-- Placeholder dla kategorii B (lewy dół) -->
    <text x="12" y="30" text-anchor="middle" font-size="10" font-family="Apple Color Emoji">{categoryB}</text>
    
    <!-- Placeholder dla kategorii C (prawy dół) -->
    <text x="28" y="30" text-anchor="middle" font-size="10" font-family="Apple Color Emoji">{categoryC}</text>
</svg>
```

### Podział Quarterly (Krzyżowy) - 4 kategorie

```svg
<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="shieldGradient4" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#C0C0C0;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#A9A9A9;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#696969;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <!-- Tło tarczy -->
    <path d="M20 2 L38 10 L38 28 Q38 38 20 38 Q2 38 2 28 L2 10 Z" 
          fill="url(#shieldGradient4)" 
          stroke="#654321" 
          stroke-width="1" 
          filter="url(#medievalShadow)"/>
    
    <!-- Linie podziału krzyżowego -->
    <line x1="20" y1="2" x2="20" y2="38" stroke="#654321" stroke-width="1"/>
    <line x1="2" y1="20" x2="38" y2="20" stroke="#654321" stroke-width="1"/>
    
    <!-- Ornamenty środkowe -->
    <circle cx="20" cy="20" r="2" fill="#FFD700" stroke="#654321" stroke-width="0.5"/>
    
    <!-- Placeholder dla kategorii A (lewy górny) -->
    <text x="10" y="14" text-anchor="middle" font-size="8" font-family="Apple Color Emoji">{categoryA}</text>
    
    <!-- Placeholder dla kategorii B (prawy górny) -->
    <text x="30" y="14" text-anchor="middle" font-size="8" font-family="Apple Color Emoji">{categoryB}</text>
    
    <!-- Placeholder dla kategorii C (lewy dolny) -->
    <text x="10" y="30" text-anchor="middle" font-size="8" font-family="Apple Color Emoji">{categoryC}</text>
    
    <!-- Placeholder dla kategorii D (prawy dolny) -->
    <text x="30" y="30" text-anchor="middle" font-size="8" font-family="Apple Color Emoji">{categoryD}</text>
</svg>
```

## Słowiańskie Symbole Dekoracyjne

### Kolovrat (Koło Słońca)

```svg
<svg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <radialGradient id="sunGradient" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
            <stop offset="70%" style="stop-color:#DAA520;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#B8860B;stop-opacity:1" />
        </radialGradient>
        
        <filter id="sunGlow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    
    <!-- Zewnętrzny krąg -->
    <circle cx="30" cy="30" r="28" fill="none" stroke="url(#sunGradient)" stroke-width="2" filter="url(#sunGlow)"/>
    
    <!-- Środkowy krąg -->
    <circle cx="30" cy="30" r="15" fill="url(#sunGradient)" stroke="#8B4513" stroke-width="1"/>
    
    <!-- 8 ramion słońca -->
    <g transform="translate(30,30)">
        <line x1="0" y1="-25" x2="0" y2="-18" stroke="url(#sunGradient)" stroke-width="3" stroke-linecap="round"/>
        <line x1="17.7" y1="-17.7" x2="12.7" y2="-12.7" stroke="url(#sunGradient)" stroke-width="3" stroke-linecap="round"/>
        <line x1="25" y1="0" x2="18" y2="0" stroke="url(#sunGradient)" stroke-width="3" stroke-linecap="round"/>
        <line x1="17.7" y1="17.7" x2="12.7" y2="12.7" stroke="url(#sunGradient)" stroke-width="3" stroke-linecap="round"/>
        <line x1="0" y1="25" x2="0" y2="18" stroke="url(#sunGradient)" stroke-width="3" stroke-linecap="round"/>
        <line x1="-17.7" y1="17.7" x2="-12.7" y2="12.7" stroke="url(#sunGradient)" stroke-width="3" stroke-linecap="round"/>
        <line x1="-25" y1="0" x2="-18" y2="0" stroke="url(#sunGradient)" stroke-width="3" stroke-linecap="round"/>
        <line x1="-17.7" y1="-17.7" x2="-12.7" y2="-12.7" stroke="url(#sunGradient)" stroke-width="3" stroke-linecap="round"/>
    </g>
    
    <!-- Środkowy punkt -->
    <circle cx="30" cy="30" r="4" fill="#FFD700"/>
</svg>
```

### Topór Peruna

```svg
<svg width="40" height="50" viewBox="0 0 40 50" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="axeGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#C0C0C0;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#A9A9A9;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#696969;stop-opacity:1" />
        </linearGradient>
        
        <linearGradient id="handleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#8B4513;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#A0522D;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#654321;stop-opacity:1" />
        </linearGradient>
        
        <filter id="lightningGlow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    
    <!-- Trzonek topora -->
    <rect x="18" y="15" width="4" height="33" fill="url(#handleGradient)" rx="2"/>
    
    <!-- Głowica topora -->
    <path d="M8 8 L32 8 L35 12 L35 18 L32 22 L8 22 L5 18 L5 12 Z" 
          fill="url(#axeGradient)" 
          stroke="#2F4F4F" 
          stroke-width="1" 
          filter="url(#lightningGlow)"/>
    
    <!-- Ostrze -->
    <path d="M8 10 L8 20 L2 15 Z" 
          fill="url(#axeGradient)" 
          stroke="#2F4F4F" 
          stroke-width="1"/>
    <path d="M32 10 L32 20 L38 15 Z" 
          fill="url(#axeGradient)" 
          stroke="#2F4F4F" 
          stroke-width="1"/>
    
    <!-- Runy Peruna -->
    <line x1="12" y1="13" x2="16" y2="17" stroke="#FFD700" stroke-width="1"/>
    <line x1="16" y1="13" x2="12" y2="17" stroke="#FFD700" stroke-width="1"/>
    
    <line x1="24" y1="13" x2="28" y2="17" stroke="#FFD700" stroke-width="1"/>
    <line x1="28" y1="13" x2="24" y2="17" stroke="#FFD700" stroke-width="1"/>
    
    <!-- Błyskawica na trzonku -->
    <path d="M19 20 L21 25 L19.5 25 L21.5 30 L19 28 L20 26 L19 26 Z" 
          fill="#FFD700" 
          stroke="#FFA500" 
          stroke-width="0.5"/>
</svg>
```

### Zasiane Pole

```svg
<svg width="40" height="40" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="fieldGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#8B4513;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#A0522D;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#654321;stop-opacity:1" />
        </linearGradient>
        
        <filter id="fieldGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="1" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    
    <!-- Romb zasianego pola (obrócony kwadrat) -->
    <rect x="20" y="20" width="20" height="20" 
          fill="url(#fieldGradient)" 
          stroke="#DAA520" 
          stroke-width="2" 
          transform="rotate(45 20 20)"
          filter="url(#fieldGlow)"/>
    
    <!-- Linie podziału na 4 części -->
    <line x1="20" y1="6" x2="20" y2="34" stroke="#DAA520" stroke-width="1"/>
    <line x1="6" y1="20" x2="34" y2="20" stroke="#DAA520" stroke-width="1"/>
    
    <!-- Nasiona w każdej części (kropki) -->
    <!-- Górna część -->
    <circle cx="16" cy="12" r="1.5" fill="#FFD700"/>
    <circle cx="24" cy="12" r="1.5" fill="#FFD700"/>
    <circle cx="20" cy="8" r="1.5" fill="#FFD700"/>
    
    <!-- Prawa część -->
    <circle cx="28" cy="16" r="1.5" fill="#FFD700"/>
    <circle cx="28" cy="24" r="1.5" fill="#FFD700"/>
    <circle cx="32" cy="20" r="1.5" fill="#FFD700"/>
    
    <!-- Dolna część -->
    <circle cx="16" cy="28" r="1.5" fill="#FFD700"/>
    <circle cx="24" cy="28" r="1.5" fill="#FFD700"/>
    <circle cx="20" cy="32" r="1.5" fill="#FFD700"/>
    
    <!-- Lewa część -->
    <circle cx="12" cy="16" r="1.5" fill="#FFD700"/>
    <circle cx="12" cy="24" r="1.5" fill="#FFD700"/>
    <circle cx="8" cy="20" r="1.5" fill="#FFD700"/>
</svg>
```

### Róża Wiatrów Średniowieczna

```svg
<svg width="80" height="80" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <radialGradient id="compassGradient" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FCF5E5;stop-opacity:1" />
            <stop offset="70%" style="stop-color:#F5DEB3;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#D2B48C;stop-opacity:1" />
        </radialGradient>
        
        <linearGradient id="needleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#8B0000;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#DC143C;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#FF6347;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <!-- Zewnętrzny pierścień -->
    <circle cx="40" cy="40" r="38" fill="none" stroke="#8B4513" stroke-width="2"/>
    <circle cx="40" cy="40" r="35" fill="url(#compassGradient)" stroke="#654321" stroke-width="1"/>
    
    <!-- Główne kierunki -->
    <g transform="translate(40,40)">
        <!-- Północ -->
        <path d="M0,-30 L5,-20 L0,-25 L-5,-20 Z" fill="url(#needleGradient)"/>
        <text x="0" y="-32" text-anchor="middle" font-size="8" font-family="serif" fill="#8B4513">N</text>
        
        <!-- Wschód -->
        <path d="M30,0 L20,5 L25,0 L20,-5 Z" fill="#DAA520"/>
        <text x="32" y="3" text-anchor="middle" font-size="8" font-family="serif" fill="#8B4513">E</text>
        
        <!-- Południe -->
        <path d="M0,30 L5,20 L0,25 L-5,20 Z" fill="#DAA520"/>
        <text x="0" y="35" text-anchor="middle" font-size="8" font-family="serif" fill="#8B4513">S</text>
        
        <!-- Zachód -->
        <path d="M-30,0 L-20,5 L-25,0 L-20,-5 Z" fill="#DAA520"/>
        <text x="-32" y="3" text-anchor="middle" font-size="8" font-family="serif" fill="#8B4513">W</text>
        
        <!-- Kierunki pośrednie -->
        <line x1="21" y1="-21" x2="17" y2="-17" stroke="#8B4513" stroke-width="1"/>
        <line x1="21" y1="21" x2="17" y2="17" stroke="#8B4513" stroke-width="1"/>
        <line x1="-21" y1="21" x2="-17" y2="17" stroke="#8B4513" stroke-width="1"/>
        <line x1="-21" y1="-21" x2="-17" y2="-17" stroke="#8B4513" stroke-width="1"/>
    </g>
    
    <!-- Środkowy punkt -->
    <circle cx="40" cy="40" r="3" fill="#8B0000"/>
    
    <!-- Ozdobne linie -->
    <circle cx="40" cy="40" r="20" fill="none" stroke="#8B4513" stroke-width="0.5" stroke-dasharray="2,2"/>
    <circle cx="40" cy="40" r="10" fill="none" stroke="#8B4513" stroke-width="0.5"/>
</svg>
```

## JavaScript dla Dynamicznego Generowania Tarcz

### Generator Kombinowanych Markerów

```javascript
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
    
    generatePerPale(categories) {
        const [catA, catB] = categories;
        return `
            <div class="heraldical-shield per-pale" style="background: linear-gradient(90deg, ${catA.color} 50%, ${catB.color} 50%);">
                <span class="category-emoji left">${catA.emoji}</span>
                <span class="category-emoji right">${catB.emoji}</span>
            </div>
        `;
    }
    
    generatePerFess(categories) {
        const [catA, catB] = categories;
        return `
            <div class="heraldical-shield per-fess" style="background: linear-gradient(180deg, ${catA.color} 50%, ${catB.color} 50%);">
                <span class="category-emoji top">${catA.emoji}</span>
                <span class="category-emoji bottom">${catB.emoji}</span>
            </div>
        `;
    }
    
    generatePerChevron(categories) {
        const [catA, catB, catC] = categories;
        return `
            <div class="heraldical-shield per-chevron">
                <div class="chevron-top" style="background-color: ${catA.color};">
                    <span class="category-emoji">${catA.emoji}</span>
                </div>
                <div class="chevron-bottom">
                    <div class="chevron-left" style="background-color: ${catB.color};">
                        <span class="category-emoji">${catB.emoji}</span>
                    </div>
                    <div class="chevron-right" style="background-color: ${catC.color};">
                        <span class="category-emoji">${catC.emoji}</span>
                    </div>
                </div>
            </div>
        `;
    }
    
    generateQuarterly(categories) {
        const [catA, catB, catC, catD] = categories;
        return `
            <div class="heraldical-shield quarterly">
                <div class="quarter top-left" style="background-color: ${catA.color};">
                    <span class="category-emoji">${catA.emoji}</span>
                </div>
                <div class="quarter top-right" style="background-color: ${catB.color};">
                    <span class="category-emoji">${catB.emoji}</span>
                </div>
                <div class="quarter bottom-left" style="background-color: ${catC.color};">
                    <span class="category-emoji">${catC.emoji}</span>
                </div>
                <div class="quarter bottom-right" style="background-color: ${catD.color};">
                    <span class="category-emoji">${catD.emoji}</span>
                </div>
            </div>
        `;
    }
    
    generateSingleMarker(category) {
        return `
            <div class="single-category-marker" style="background-color: ${category.color};">
                <span class="category-emoji">${category.emoji}</span>
            </div>
        `;
    }
}
```

### CSS dla Tarcz Heraldycznych

```css
.heraldical-shield {
    width: 32px;
    height: 32px;
    position: relative;
    border: 2px solid #8B4513;
    border-radius: 4px 4px 8px 8px;
    overflow: hidden;
    box-shadow: 
        0 2px 8px rgba(139, 69, 19, 0.4),
        inset 0 1px 2px rgba(255, 255, 255, 0.2);
}

.heraldical-shield.per-pale .category-emoji.left {
    position: absolute;
    left: 25%;
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 10px;
}

.heraldical-shield.per-pale .category-emoji.right {
    position: absolute;
    right: 25%;
    top: 50%;
    transform: translate(50%, -50%);
    font-size: 10px;
}

.heraldical-shield.per-fess .category-emoji.top {
    position: absolute;
    left: 50%;
    top: 25%;
    transform: translate(-50%, -50%);
    font-size: 10px;
}

.heraldical-shield.per-fess .category-emoji.bottom {
    position: absolute;
    left: 50%;
    bottom: 25%;
    transform: translate(-50%, 50%);
    font-size: 10px;
}

.heraldical-shield.per-chevron {
    display: flex;
    flex-direction: column;
}

.chevron-top {
    height: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.chevron-bottom {
    height: 50%;
    display: flex;
}

.chevron-left,
.chevron-right {
    width: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.heraldical-shield.quarterly {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
}

.quarter {
    display: flex;
    align-items: center;
    justify-content: center;
}

.quarter .category-emoji {
    font-size: 8px;
}

.single-category-marker {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #8B4513;
    box-shadow: 
        0 2px 8px rgba(139, 69, 19, 0.4),
        inset 0 1px 2px rgba(255, 255, 255, 0.2);
}

.single-category-marker .category-emoji {
    font-size: 16px;
}

/* Hover efekty */
.heraldical-shield:hover,
.single-category-marker:hover {
    transform: scale(1.1);
    transition: transform 0.2s ease-in-out;
    z-index: 1000;
}

/* Responsywność */
@media (max-width: 768px) {
    .heraldical-shield,
    .single-category-marker {
        width: 24px;
        height: 24px;
    }
    
    .heraldical-shield .category-emoji,
    .quarter .category-emoji {
        font-size: 6px;
    }
    
    .single-category-marker .category-emoji {
        font-size: 12px;
    }
}
```