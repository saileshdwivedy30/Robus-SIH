import random

class Bus:
    def __init__(self, routes):
        self.bus_info = self.generate_current_bus_info(routes)

    def generate_current_bus_info(self, routes):
        bus_info = {}
        for route_label, stops in routes.items():
            current_stop = random.choice(stops)
            current_occupancy = random.randint(0, 50)
            bus_info[route_label] = {'current_stop': current_stop, 'current_occupancy': current_occupancy, 'route': stops}
        return bus_info
