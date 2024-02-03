import pandas as pd

class Hotspot:
    def __init__(self, hotspot_route_df_path):
        self.hot_spot_route_df = pd.read_excel(hotspot_route_df_path)
        self.hotspot_to_routes = self.map_hotspots()

    def map_hotspots(self):
        hotspot_to_routes = {}
        for _, row in self.hot_spot_route_df.iterrows():
            hotspot = row['HOTSPOTS']
            routes = [int(x) for x in str(row['HOTSPOT ROUTE']).split(',') if x]
            hotspot_to_routes[hotspot] = routes
        return hotspot_to_routes