import heapq


class RoutePlanner:
    def __init__(self):
        self.routes = {}

    def add_route(self, start, end, distance, bidirectional=True):
        if distance < 0:
            raise ValueError("Route distance cannot be negative")
        self.routes.setdefault(start, []).append((end, distance))
        self.routes.setdefault(end, [])
        if bidirectional:
            self.routes[end].append((start, distance))

    def shortest_route(self, origin, destination):
        if origin not in self.routes or destination not in self.routes:
            return None

        distances = {origin: 0}
        previous = {}
        pending = [(0, origin)]

        while pending:
            distance, place = heapq.heappop(pending)
            if distance != distances.get(place):
                continue
            if place == destination:
                break

            for neighbor, cost in self.routes[place]:
                candidate = distance + cost
                if candidate < distances.get(neighbor, float("inf")):
                    distances[neighbor] = candidate
                    previous[neighbor] = place
                    heapq.heappush(pending, (candidate, neighbor))

        if destination not in distances:
            return None

        path = []
        current = destination
        while current != origin:
            path.append(current)
            current = previous[current]
        path.append(origin)
        path.reverse()
        return path, distances[destination]

    def routes_within_stops(self, origin, destination, max_stops):
        if max_stops < 0:
            raise ValueError("Maximum stops cannot be negative")
        if origin not in self.routes or destination not in self.routes:
            return []

        found = []
        pending = [(origin, [origin], 0)]
        while pending:
            place, path, distance = pending.pop()
            if place == destination and len(path) > 1:
                found.append((path, distance))
                continue
            if len(path) - 1 == max_stops:
                continue

            for neighbor, cost in self.routes[place]:
                if neighbor not in path:
                    pending.append((neighbor, path + [neighbor], distance + cost))

        found.sort(key=lambda route: (route[1], len(route[0]), route[0]))
        return found

    def reachable_within_distance(self, origin, max_distance):
        if max_distance < 0:
            raise ValueError("Maximum distance cannot be negative")
        if origin not in self.routes:
            return {}

        distances = {origin: 0}
        pending = [(0, origin)]
        while pending:
            distance, place = heapq.heappop(pending)
            if distance != distances[place]:
                continue

            for neighbor, cost in self.routes[place]:
                candidate = distance + cost
                if candidate <= max_distance and candidate < distances.get(
                    neighbor, float("inf")
                ):
                    distances[neighbor] = candidate
                    heapq.heappush(pending, (candidate, neighbor))

        return dict(sorted(distances.items(), key=lambda item: (item[1], item[0])))

    def route_distance(self, path):
        if not path:
            raise ValueError("A route must include at least one location")

        total = 0
        for start, end in zip(path, path[1:]):
            legs = [
                distance
                for neighbor, distance in self.routes.get(start, [])
                if neighbor == end
            ]
            if not legs:
                return None
            total += min(legs)
        return total

    @staticmethod
    def format_route(route):
        if route is None:
            return "No route found."
        path, distance = route
        return f"{' -> '.join(path)} ({distance})"

    def locations(self):
        return sorted(self.routes)


def build_sample_planner():
    planner = RoutePlanner()
    planner.add_route("Central", "Museum", 4)
    planner.add_route("Central", "Harbor", 7)
    planner.add_route("Museum", "Garden", 3)
    planner.add_route("Garden", "Harbor", 2)
    planner.add_route("Harbor", "Airport", 8)
    return planner


def main():
    planner = build_sample_planner()
    result = planner.shortest_route("Central", "Airport")
    if result is None:
        print("No route found.")
        return

    path, distance = result
    print("Locations:", ", ".join(planner.locations()))
    print("Best route:", " -> ".join(path))
    print("Total distance:", distance)
    alternatives = planner.routes_within_stops("Central", "Airport", 3)
    print("Routes within 3 stops:")
    for route in alternatives:
        print(" -", planner.format_route(route))

    nearby = planner.reachable_within_distance("Central", 10)
    print("Reachable within distance 10:")
    for place, cost in nearby.items():
        print(f" - {place}: {cost}")
    sample_path = ["Central", "Museum", "Garden"]
    print("Sample route distance:", planner.route_distance(sample_path))


if __name__ == "__main__":
    main()
