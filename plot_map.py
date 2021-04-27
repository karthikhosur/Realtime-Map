
import folium

def basemap_layer():
    map = folium.Map(location=[12.971,77.5946],min_zoom=2)

    return map

def earthquake_plot(map, earthquakes):
    for earthquake in earthquakes:
        folium.Marker(location=[earthquake['Latitude'],
                                earthquake['Longitude']],
                        popup=folium.Popup("<b>Information: </b>{}".format(
                          earthquake['Magnitude'])
                          )
                        ).add_to(map)