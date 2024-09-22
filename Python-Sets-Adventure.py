# Task: Flight Route Comparison:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
# 1. Destinations that both airlines fly to.
shared_routes = our_routes.intersection(competitor_routes)
print(f"Destinations both airlines fly to: {shared_routes}")

# 2. Destinations unique to your airline.
unique_routes = our_routes.difference(competitor_routes)
print(f"Destinations unique to our airline: {unique_routes}")

#3. Whether there are any destinations that neither airline shares.
neither_shared = our_routes.symmetric_difference(competitor_routes)
print(f"Destinations neither airline shares: {neither_shared}")
