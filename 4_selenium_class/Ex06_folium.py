import folium

map_osm = folium.Map(location=[37.572807,126.975918],
                     zoom_start=18
                     )
folium.Marker(location=[37.572807,126.975918],
              popup='세종문화회관',
              icon=folium.Icon(color='green',icon='info-sign')
              ).add_to(map_osm)
# 지도 스타일 주기 >>> tiles='Stamen Terrain / Stamen Toner / Mapbox Bright'
map_osm.save('./map/map3.html')
