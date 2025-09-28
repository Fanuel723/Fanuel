import xml.etree.ElementTree as ET
import json
import re

def clean_html(raw_html):
    """Removes HTML tags from a string."""
    if not raw_html:
        return ""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext.strip()

def parse_kml(kml_file_path):
    """Parses a KML file and extracts Placemark data."""
    # The KML file has a default namespace. We need to handle it.
    # The namespace is 'http://www.opengis.net/kml/2.2'
    namespaces = {'kml': 'http://www.opengis.net/kml/2.2'}

    try:
        tree = ET.parse(kml_file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing KML file: {e}")
        return []

    placemarks_data = []

    # Using the registered namespace to find elements
    for placemark in root.findall('.//kml:Placemark', namespaces):
        name_element = placemark.find('kml:name', namespaces)
        name = name_element.text if name_element is not None else "Brak nazwy"

        description_element = placemark.find('kml:description', namespaces)
        description_html = description_element.text if description_element is not None else ""

        coordinates_element = placemark.find('.//kml:coordinates', namespaces)
        coordinates_text = coordinates_element.text if coordinates_element is not None else "0,0,0"

        image_url = None
        if description_html:
            match = re.search(r'<img src="([^"]+)"', description_html)
            if match:
                image_url = match.group(1)

        # Clean up coordinates: "lon,lat,alt" -> [lon, lat]
        try:
            lon, lat, _ = map(float, coordinates_text.strip().split(','))
            coords = [lon, lat]
        except (ValueError, IndexError):
            coords = [0.0, 0.0]

        placemarks_data.append({
            'name': name.strip(),
            'description': clean_html(description_html),
            'coordinates': coords,
            'image_url': image_url
        })

    return placemarks_data

def main():
    kml_file = 'Projekt SzeptańceThe Susurrers Project – kopia (3).kml'
    output_json_file = 'larp_data.json'

    parsed_data = parse_kml(kml_file)

    if parsed_data:
        with open(output_json_file, 'w', encoding='utf-8') as f:
            json.dump(parsed_data, f, ensure_ascii=False, indent=4)

        print(f"Dane zostały pomyślnie przetworzone i zapisane w pliku {output_json_file}")
        print(f"Przetworzono {len(parsed_data)} miejsc.")
    else:
        print("Nie udało się przetworzyć danych z pliku KML.")

if __name__ == '__main__':
    main()