import folium

def plot_hops(hops):
    # Create a map centered at the first hop
    base_map = folium.Map(location=hops[0], zoom_start=4)

    # Add markers for each hop
    for index, (lat, lon) in enumerate(hops, start=1):
        if lat and lon:
            folium.Marker(
                location=(lat, lon),
                popup=f"Hop {index}",
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(base_map)

    # Save map to HTML
    base_map.save("traceroute_map.html")

