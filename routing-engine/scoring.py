def score(node):
    """Return a routing cost for a node based on load and latency.

    Lower scores indicate a more attractive node. Load and latency are
    expected to be numeric values in the node mapping. Their values are
    combined with equal weights, so callers should provide consistently
    scaled measurements when comparing the two signals.
    """
    load = node["load"]
    latency = node["latency"]

    if not isinstance(load, (int, float)):
        raise TypeError("node load must be numeric")
    if not isinstance(latency, (int, float)):
        raise TypeError("node latency must be numeric")

    if load < 0:
        raise ValueError("node load must not be negative")
    if latency < 0:
        raise ValueError("node latency must not be negative")

    # Keep the calculation explicit so weights can be tuned independently.
    load_weight = 0.5
    latency_weight = 0.5

    load_cost = load * load_weight
    latency_cost = latency * latency_weight
    total_cost = load_cost + latency_cost

    return total_cost
