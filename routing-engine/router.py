def route(request, nodes):
    best = None
    for node in nodes:
        if node["healthy"] and (
            best is None
            or node["load"] < best["load"]
            or (node["load"] == best["load"] and node["latency"] < best["latency"])
        ):
            best = node
    return best
