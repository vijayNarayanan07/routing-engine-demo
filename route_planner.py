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


if __name__ == "__main__":
    main()
