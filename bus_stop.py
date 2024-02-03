import pandas as pd
class BusStop:
    def __init__(self, bus_stops_df_path):
        self.bus_stops_df = pd.read_excel(bus_stops_df_path)
        self.routes, self.stop_to_route = self.map_routes_and_stops_to_routes()

    def map_routes_and_stops_to_routes(self):
        routes = {row['ROUTES']: [] for index, row in self.bus_stops_df.iterrows()}
        stop_to_route = {}
        for index, row in self.bus_stops_df.iterrows():
            routes[row['ROUTES']].extend([int(x) for x in str(row['CONNECTED STOPS']).split(',') if x])
            stop_to_route[row['BUSSTOPS']] = row['ROUTES']
        return routes, stop_to_route