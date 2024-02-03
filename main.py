from bus_stop import BusStop
from bus import Bus
from monitor import Monitor


bus_stop = BusStop('path_to_bus_route copy.xlsx')
bus = Bus(bus_stop.routes)
monitor = Monitor('bus_stop_demand.xlsx', 'path_to_hot_spot_route.xlsx')
dispatch_messages_current_stop = monitor.evaluate_demand_from_current_stop(bus.bus_info)
updated_dispatch_messages_current_stop = monitor.find_nearest_hotspot(dispatch_messages_current_stop)
for message in updated_dispatch_messages_current_stop:
    subsequent_stops_str = ', '.join(map(str, message.subsequent_stops)) if message.subsequent_stops else "none"
    stops_message = "have" if message.subsequent_stops else "has"
    bus_noun = "bus" if message.additional_buses_needed == 1 else "buses"
    subsequent_stops_message = f"and the subsequent stops {subsequent_stops_str} " if message.subsequent_stops else ""
    formatted_message = (
        f"\nBus(es) need to be dispatched to route {message.route_label} starting at stop {message.current_stop}.\n"
        f"Bus stop {message.current_stop} {subsequent_stops_message} {stops_message} a total demand of {message.cumulative_demand}.\n"
        f"The buses in the route have a remaining capacity of {message.remaining_capacity}.\n"
        f"{message.additional_buses_needed} additional {bus_noun} needed.\n"
        f"Nearest Hotspot for dispatch is {message.nearest_hotspot}."

    )
    print(formatted_message)