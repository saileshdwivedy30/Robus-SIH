import pandas as pd
import math
from hot_spot import Hotspot
from message import Message
class Monitor:
    def __init__(self, bus_stop_demand_df_path, hot_spot_route_df_path):
        self.bus_stop_demand_df = pd.read_excel(bus_stop_demand_df_path)
        self.bus_stop_demand_dict = self.bus_stop_demand_df.set_index('BUSSTOPS')['DEMAND'].to_dict()
        self.hotspot = Hotspot(hot_spot_route_df_path)

    def evaluate_demand_from_current_stop(self, bus_info):
        dispatch_messages = []
        total_bus_capacity = 50
        for route_label, info in bus_info.items():
            current_stop = info['current_stop']
            current_route = info['route']
            current_occupancy = info['current_occupancy']
            current_index = current_route.index(current_stop)
            subsequent_stops = current_route[current_index + 1:]
            cumulative_demand = self.bus_stop_demand_dict.get(current_stop, 0) + sum(
                self.bus_stop_demand_dict.get(stop, 0) for stop in subsequent_stops)
            remaining_capacity = total_bus_capacity - current_occupancy
            excess_demand = max(0, cumulative_demand - remaining_capacity)
            additional_buses_needed = math.ceil(excess_demand / total_bus_capacity)
            if additional_buses_needed > 0:
                message = Message(route_label, current_stop, subsequent_stops, cumulative_demand, remaining_capacity,
                                  additional_buses_needed, None)
                dispatch_messages.append(message)
        return dispatch_messages

    def find_nearest_hotspot(self, dispatch_messages):
        updated_dispatch_messages = []
        for message in dispatch_messages:
            route_label = message.route_label
            route_stops = [message.current_stop] + message.subsequent_stops
            nearest_hotspot = None
            min_distance = float('inf')
            for hotspot, routes in self.hotspot.hotspot_to_routes.items():
                for stop in route_stops:
                    if stop in routes:
                        stop_index = routes.index(stop)
                        if stop_index < min_distance:
                            nearest_hotspot = hotspot
                            min_distance = stop_index
                            break
            message.nearest_hotspot = nearest_hotspot if nearest_hotspot is not None else "not available"
            updated_dispatch_messages.append(message)
        return updated_dispatch_messages