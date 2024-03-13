import heapq


def minimize_cable_costs(cables):
    heapq.heapify(cables)

    total_cost = 0
    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        merged_cable = cable1 + cable2
        total_cost += merged_cable
        heapq.heappush(cables, merged_cable)

    return total_cost


# Приклад використання
network_cables = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Network cables before: {network_cables}")
result = minimize_cable_costs(network_cables)
print(f"Total cost to merge: {result}")
print(f"Network cables now: {network_cables}")
