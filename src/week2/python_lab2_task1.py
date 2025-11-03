"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.
"""

# 1. Create datasets
temperatures = [72, 75, 68, 70, 74, 77, 73]  # Example temperatures (°F) for one week
city_population = {
    "New York": 8_419_600,
    "Los Angeles": 3_980_400,
    "Chicago": 2_716_000,
    "Houston": 2_328_000,
    "Phoenix": 1_690_000
}

# 2. Compute aggregates

# Average temperature
average_temperature = sum(temperatures) / len(temperatures)

# Find largest city
largest_city = max(city_population, key=lambda k: city_population[k])
largest_population = city_population[largest_city]

# Find smallest city
smallest_city = min(city_population, key=lambda k: city_population[k])
smallest_population = city_population[smallest_city]

# Total population
total_population = sum(city_population.values())

# 3. Print results
print("=== Weekly Summary ===")
print(f"Average temperature: {average_temperature:.1f}°F")
print(f"Largest city: {largest_city} - {largest_population:,} people")
print(f"Smallest city: {smallest_city} - {smallest_population:,} people")
print(f"Total population: {total_population:,} people")

