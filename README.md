# 🧬 Traveling Salesman Problem: Genetic Algorithm

A Python implementation of a **genetic algorithm (GA)** that finds the shortest round-trip route through 10 cities, starting and ending at city A.

Built for **CIS 561 – Artificial Intelligence** at UMass Dartmouth.

---

## 🧩 The Problem

The Traveling Salesman Problem (TSP) asks: given a set of cities, what is the shortest route that visits each one exactly once and returns to the start? Checking every possible route quickly becomes impractical, so this project uses a genetic algorithm to evolve a near-optimal route instead.

---

## ⚙️ How It Works

Each possible route is treated as an "individual" in a population, and routes evolve over generations:

- **Representation:** a route is a permutation of the 9 non-start cities (the tour always begins and ends at A)
- **Fitness:** inverse of total Euclidean distance, so shorter routes score higher
- **Selection:** tournament selection (best of 3 random routes)
- **Crossover:** Order Crossover (OX), which keeps every city exactly once
- **Mutation:** swap mutation, which randomly exchanges two cities
- **Elitism:** the top 10 routes carry over unchanged to each new generation
- **Optimization:** pairwise distances are precomputed for faster evaluation

### Parameters

| Parameter | Value |
|---|---|
| Population size | 300 |
| Generations | 2,000 |
| Crossover rate | 0.9 |
| Mutation rate | 0.2 |
| Elite size | 10 |
| Random seed | 42 (for reproducible results) |

---

## 🚀 How to Run

No external libraries needed, just Python 3.

```bash
python tsp_ga_project1.py
```

The program prints the shortest distance found and the city order, and saves both to `tsp_result.txt`.

---

## 📁 Files

| File | Description |
|---|---|
| `tsp_ga_project1.py` | Genetic algorithm implementation |
| `tsp_result.txt` | Output: shortest distance and best route found |

---

## 🛠️ Skills Demonstrated

Python · Genetic Algorithms · Optimization · Search Heuristics · Algorithm Design
