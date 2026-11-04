def route(request, nodes):
    best = None
    for node in nodes:
        if node["healthy"] and (best is None or node["load"] < best["load"]):
            best = node
    return best
