import streamlit as st
import folium
from streamlit_folium import st_folium

# Sidebar for User Input
st.sidebar.header("Customize Your Interactive Map")
selected_city = st.sidebar.selectbox("Select a City in India", ["Delhi", "Mumbai", "Bangalore", "Kolkata", "Chennai", "Hyderabad"])
zoom_level = st.sidebar.slider("Select Zoom Level", min_value=5, max_value=18, value=12)
map_type = st.sidebar.selectbox("Select Map Type", ["OpenStreetMap", "Stamen Terrain", "Stamen Toner", "CartoDB positron", "CartoDB dark_matter"])

# Mapping City Names to Coordinates
city_coordinates = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
    "Kolkata": (22.5726, 88.3639),
    "Chennai": (13.0827, 80.2707),
    "Hyderabad": (17.3850, 78.4867)
}

# Define tile attributions
tile_attributions = {
    "OpenStreetMap": "© OpenStreetMap contributors",
    "Stamen Terrain": "Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors",
    "Stamen Toner": "Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors",
    "CartoDB positron": "© CartoDB - Map data © OpenStreetMap contributors",
    "CartoDB dark_matter": "© CartoDB - Map data © OpenStreetMap contributors"
}

# Generate Map with attribution
st.title(f":rainbow[Interactive Map of {selected_city}]")
m = folium.Map(location=city_coordinates[selected_city], zoom_start=zoom_level, tiles=map_type, attr=tile_attributions[map_type])

# Adding a marker for the selected city
folium.Marker(city_coordinates[selected_city], popup=f"{selected_city}", tooltip="Click for info").add_to(m)

# Display Map in Streamlit
st_folium(m, width=700, height=500)

st.sidebar.markdown("Built with ❤️ using Streamlit & Folium")
