# Stworzę kompletny system ikon SVG dla wszystkich 24 kategorii

# Funkcja do generowania SVG ikon
def generate_category_icon_svg(category, emoji, color, size=32):
    """Generuje ikonę SVG dla danej kategorii z średniowieczno-słowiańskim stylem"""
    
    # Definicje gradientów dla różnych kategorii
    gradients = {
        'gold': f'url(#goldGradient)',
        'silver': f'url(#silverGradient)', 
        'bronze': f'url(#bronzeGradient)',
        'mystical': f'url(#mysticalGradient)',
        'forest': f'url(#forestGradient)',
        'fire': f'url(#fireGradient)',
        'water': f'url(#waterGradient)',
        'earth': f'url(#earthGradient)'
    }
    
    # Mapowanie kategorii do stylów
    style_mapping = {
        'skarb': 'gold',
        'lokacja': 'forest', 
        'czart': 'fire',
        'smok': 'fire',
        'duch': 'mystical',
        'bestia': 'earth',
        'uroczysko': 'forest',
        'czarownik': 'mystical',
        'straznik': 'bronze',
        'zjawisko': 'mystical',
        'czar': 'mystical',
        'proces': 'bronze',
        'zbrodnie': 'bronze',
        'wspolczesne': 'silver'
    }
    
    gradient_style = style_mapping.get(category, 'bronze')
    
    svg_content = f'''<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- Złoty gradient -->
        <linearGradient id="goldGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#DAA520;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#B8860B;stop-opacity:1" />
        </linearGradient>
        
        <!-- Srebrny gradient -->
        <linearGradient id="silverGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#C0C0C0;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#A9A9A9;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#808080;stop-opacity:1" />
        </linearGradient>
        
        <!-- Brązowy gradient -->
        <linearGradient id="bronzeGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#CD853F;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#8B4513;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#A0522D;stop-opacity:1" />
        </linearGradient>
        
        <!-- Mistyczny gradient -->
        <linearGradient id="mysticalGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#E6E6FA;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#9370DB;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#4B0082;stop-opacity:1" />
        </linearGradient>
        
        <!-- Leśny gradient -->
        <linearGradient id="forestGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#98FB98;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#228B22;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#006400;stop-opacity:1" />
        </linearGradient>
        
        <!-- Ognisty gradient -->
        <linearGradient id="fireGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FF6347;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#DC143C;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8B0000;stop-opacity:1" />
        </linearGradient>
        
        <!-- Wodny gradient -->
        <linearGradient id="waterGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#87CEEB;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#4682B4;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#191970;stop-opacity:1" />
        </linearGradient>
        
        <!-- Ziemisty gradient -->
        <linearGradient id="earthGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#D2B48C;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#8B4513;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#654321;stop-opacity:1" />
        </linearGradient>
        
        <!-- Filtry efektów -->
        <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="2" dy="2" stdDeviation="2" flood-color="#000000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- Tło ikony - heraldyczna tarcza -->
    <path d="M{size/2} 2 L{size-2} {size/4} L{size-2} {size*0.7} Q{size-2} {size-2} {size/2} {size-2} Q2 {size-2} 2 {size*0.7} L2 {size/4} Z" 
          fill="{gradients[gradient_style]}" 
          stroke="#8B4513" 
          stroke-width="1" 
          filter="url(#shadow)"/>
    
    <!-- Ornamentalne linie -->
    <line x1="4" y1="{size/4+2}" x2="{size-4}" y2="{size/4+2}" stroke="#DAA520" stroke-width="0.5"/>
    <line x1="4" y1="{size*0.7-2}" x2="{size-4}" y2="{size*0.7-2}" stroke="#DAA520" stroke-width="0.5"/>
    
    <!-- Emoji w centrum -->
    <text x="{size/2}" y="{size*0.6}" text-anchor="middle" font-size="{size*0.5}" font-family="Apple Color Emoji, Segoe UI Emoji">{emoji}</text>
    
    <!-- Dodatkowe ornamenty w rogach -->
    <circle cx="4" cy="4" r="1" fill="#DAA520"/>
    <circle cx="{size-4}" cy="4" r="1" fill="#DAA520"/>
</svg>'''
    
    return svg_content

# Generowanie wszystkich ikon
categories_data = {
    # Podstawowe kategorie
    "duch": {"emoji": "👻", "kolor": "#E6E6FA"},
    "bestia": {"emoji": "🐺", "kolor": "#8B4513"},
    "smok": {"emoji": "🐉", "kolor": "#DC143C"},
    "czart": {"emoji": "😈", "kolor": "#8B0000"},
    "skarb": {"emoji": "💰", "kolor": "#FFD700"},
    "lokacja": {"emoji": "🏰", "kolor": "#228B22"},
    "straznik": {"emoji": "⚔️", "kolor": "#8FBC8F"},
    "zjawisko": {"emoji": "✨", "kolor": "#FF6347"},
    "czar": {"emoji": "🔮", "kolor": "#4B0082"},
    "uroczysko": {"emoji": "🌳", "kolor": "#556B2F"},
    "czarownik": {"emoji": "🧙", "kolor": "#2F4F4F"},
    "proces": {"emoji": "⚖️", "kolor": "#800000"},
    "zbrodnie": {"emoji": "🔍", "kolor": "#2C2C2C"},
    "wspolczesne": {"emoji": "📱", "kolor": "#00CED1"},
    
    # Podkategorie uroczysk
    "kurhany": {"emoji": "⛰️", "kolor": "#8B7D6B"},
    "swiate_gaje": {"emoji": "🌲", "kolor": "#228B22"},
    "oltarze": {"emoji": "🗿", "kolor": "#696969"},
    "kregi_kamienne": {"emoji": "⭕", "kolor": "#A0522D"},
    
    # Mniejszości kulturowe
    "zydowskie": {"emoji": "✡️", "kolor": "#4169E1"},
    "lemkowskie": {"emoji": "🏔️", "kolor": "#FF8C00"},
    "huculsie": {"emoji": "🎻", "kolor": "#DA70D6"},
    "ormianskie": {"emoji": "🕊️", "kolor": "#CD853F"},
    "romskie": {"emoji": "🎪", "kolor": "#FF1493"},
    "niemieckie": {"emoji": "🍺", "kolor": "#708090"}
}

print("🎨 GENEROWANIE IKON SVG DLA WSZYSTKICH KATEGORII")
print("=" * 60)

# Tworzenie pliku z wszystkimi ikonami
svg_icons_content = "# 🎨 Ikony SVG dla Projektu Szeptańce\n\n"
svg_icons_content += "## Kompletny zestaw 24 ikon w stylu średniowieczno-słowiańskim\n\n"

for category, data in categories_data.items():
    emoji = data["emoji"]
    color = data["kolor"]
    
    # Generacja ikony
    icon_svg = generate_category_icon_svg(category, emoji, color, 32)
    
    svg_icons_content += f"### {category.upper()} {emoji}\n"
    svg_icons_content += f"**Kolor:** {color}\n\n"
    svg_icons_content += "```svg\n"
    svg_icons_content += icon_svg
    svg_icons_content += "\n```\n\n"
    
    print(f"✅ Wygenerowano ikonę: {category.upper()} {emoji} ({color})")

print(f"\n🎯 PODSUMOWANIE: Wygenerowano {len(categories_data)} ikon SVG")
print("📁 Ikony zostały przygotowane w formacie gotowym do implementacji")

# Zapisanie do pliku będzie w następnym kroku
with open("svg_icons_output.txt", "w", encoding="utf-8") as f:
    f.write(svg_icons_content)

print("💾 Ikony zapisane do pliku svg_icons_output.txt")