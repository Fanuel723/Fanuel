import plotly.graph_objects as go
import json

# Data from the provided JSON
data = {
    "categories": [
        {"name": "Kategorie Podstawowe", "count": 14, "color": "#DAA520"},
        {"name": "Podkategorie Uroczysk", "count": 4, "color": "#8B4513"},
        {"name": "Mniejszości Kulturowe", "count": 6, "color": "#FCF5E5"}
    ]
}

# Extract data for the pie chart
categories = [cat["name"] for cat in data["categories"]]
counts = [cat["count"] for cat in data["categories"]]
colors = [cat["color"] for cat in data["categories"]]

# Abbreviate category names to fit 15 character limit
abbreviated_names = [
    "Kat. Podstaw.",    # Kategorie Podstawowe
    "Podkat. Uroczy",   # Podkategorie Uroczysk  
    "Mniej. Kultur."    # Mniejszości Kulturowe
]

# Calculate percentages
total = sum(counts)
percentages = [count/total*100 for count in counts]

# Create labels with counts and percentages
labels = [f"{name}<br>{count} ({perc:.1f}%)" 
          for name, count, perc in zip(abbreviated_names, counts, percentages)]

# Create pie chart
fig = go.Figure(data=[go.Pie(
    labels=abbreviated_names,
    values=counts,
    textinfo='label+value+percent',
    texttemplate='%{label}<br>%{value} (%{percent})',
    marker=dict(colors=colors),
    textposition='inside'
)])

# Update layout
fig.update_layout(
    title="Podział Kategorii Ikon Kolberg 2.0",
    uniformtext_minsize=14, 
    uniformtext_mode='hide'
)

# Save the chart
fig.write_image("kolberg_categories_pie.png")