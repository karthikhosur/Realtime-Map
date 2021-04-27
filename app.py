from flask import Flask, render_template
from streamlit import get_all_records
from plot_map import basemap_layer, earthquake_plot

# instantiate a new Flash app
app = Flask(__name__)


@app.route('/')
def earthquake_data():
    # storing all data in a variable records
    earthquakes = get_all_records()
    map = basemap_layer()
    earthquake_plot(map=map, earthquakes=earthquakes)
    map.save('templates/map.html')
    return render_template('index.html')

if __name__ == "__main__":
    app.run() 