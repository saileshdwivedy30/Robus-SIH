class Message:
    def __init__(self, route_label, current_stop, subsequent_stops, cumulative_demand, remaining_capacity, additional_buses_needed, nearest_hotspot):
        self.route_label = route_label
        self.current_stop = current_stop
        self.subsequent_stops = subsequent_stops
        self.cumulative_demand = cumulative_demand
        self.remaining_capacity = remaining_capacity
        self.additional_buses_needed = additional_buses_needed
        self.nearest_hotspot = nearest_hotspot