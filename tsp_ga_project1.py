import random
import math

# -----------------------------
# Data: city coordinates
# -----------------------------
CITIES = {
    "A": (100, 300),
    "B": (200, 130),
    "C": (300, 500),
    "D": (500, 390),
    "E": (700, 300),
    "F": (900, 600),
    "G": (800, 950),
    "H": (600, 560),
    "I": (350, 550),
    "J": (270, 350),
}

START_CITY = "A"

def euclidean(a, b):
    (x1, y1) = CITIES[a]
    (x2, y2) = CITIES[b]
    return math.hypot(x1 - x2, y1 - y2)

# Precompute distances (faster)
DIST = {}
for i in CITIES:
    for j in CITIES:
        if i != j:
            DIST[(i, j)] = euclidean(i, j)

def tour_distance(route):
    """route includes ONLY the non-start cities in visiting order.
       Full tour is A -> route -> A
    """
    total = 0.0
    prev = START_CITY
    for city in route:
        total += DIST[(prev, city)]
        prev = city
    total += DIST[(prev, START_CITY)]
    return total

def fitness(route):
    # smaller distance => higher fitness
    d = tour_distance(route)
    return 1.0 / (d + 1e-9)

# -----------------------------
# GA operators
# -----------------------------
def make_initial_population(pop_size, genes):
    population = []
    for _ in range(pop_size):
        r = genes[:]  # copy
        random.shuffle(r)
        population.append(r)
    return population

def tournament_selection(population, k=3):
    """Pick the best out of k random individuals."""
    contenders = random.sample(population, k)
    contenders.sort(key=tour_distance)
    return contenders[0][:]  # copy

def order_crossover(parent1, parent2):
    """Order crossover (OX) for permutations."""
    n = len(parent1)
    a, b = sorted(random.sample(range(n), 2))
    child = [None] * n

    # copy a slice from parent1
    child[a:b+1] = parent1[a:b+1]

    # fill the rest from parent2 in order
    p2_idx = 0
    for i in range(n):
        if child[i] is None:
            while parent2[p2_idx] in child:
                p2_idx += 1
            child[i] = parent2[p2_idx]
            p2_idx += 1

    return child

def swap_mutation(route, mutation_rate=0.2):
    """Swap two cities with probability mutation_rate."""
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]
    return route

# -----------------------------
# GA main loop
# -----------------------------
def genetic_algorithm(
    pop_size=300,
    generations=2000,
    crossover_rate=0.9,
    mutation_rate=0.2,
    elite_size=10,
    seed=42
):
    random.seed(seed)

    genes = [c for c in CITIES.keys() if c != START_CITY]  # 9 cities
    population = make_initial_population(pop_size, genes)

    best_route = None
    best_dist = float("inf")

    for gen in range(generations):
        # Sort population by distance (best first)
        population.sort(key=tour_distance)

        # Track global best
        current_best = population[0]
        current_best_dist = tour_distance(current_best)
        if current_best_dist < best_dist:
            best_dist = current_best_dist
            best_route = current_best[:]

        # Elitism: keep top elite_size
        new_population = population[:elite_size]

        # Create rest of next generation
        while len(new_population) < pop_size:
            p1 = tournament_selection(population, k=3)
            p2 = tournament_selection(population, k=3)

            if random.random() < crossover_rate:
                child = order_crossover(p1, p2)
            else:
                child = p1[:]  # no crossover

            child = swap_mutation(child, mutation_rate=mutation_rate)
            new_population.append(child)

        population = new_population

    return best_route, best_dist

if __name__ == "__main__":
    best_route, best_dist = genetic_algorithm()

    # Build full tour string
    full_tour = [START_CITY] + best_route + [START_CITY]

    # Print results
    print("Shortest distance value:", round(best_dist, 2), "miles")
    print("Sequence order of 10 cities:", " -> ".join(full_tour))

    # Write required output text file
    with open("tsp_result.txt", "w") as f:
        f.write(f"Shortest distance value: {best_dist:.2f} miles\n")
        f.write("Sequence order of 10 cities: " + " -> ".join(full_tour) + "\n")

    print("\nSaved output to tsp_result.txt")