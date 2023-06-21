import numpy as np
import math
import random
import matplotlib.pyplot as plt

NUM_DIMENSIONS = 10
NUM_PARTICLES = 50
MAX_ITERATIONS = 100
INERTIA_WEIGHT = 0.729
COGNITIVE_WEIGHT = 1.49445
SOCIAL_WEIGHT = 1.49445
MIN_POSITION = -5.12
MAX_POSITION = 5.12

def f1(position: np.ndarray):
    fitness = np.sum(position**2 - 10 * np.cos(2 * math.pi * position) + 10)
    return fitness

class Particle:
    def __init__(self, num_dimensions: int):
        self.position = np.zeros(num_dimensions)
        self.velocity = np.zeros(num_dimensions)
        self.personal_best = np.zeros(num_dimensions)
        self.personal_best_fitness = float('inf')

def initialize_particle(particle: Particle, min_position: float, max_position: float, num_dimensions: int, evaluate_func: callable):
    particle.position = np.random.uniform(min_position, max_position, num_dimensions)
    particle.velocity = np.zeros(num_dimensions)
    particle.personal_best = particle.position
    particle.personal_best_fitness = evaluate_func(particle.position)

def update_particle(particle: Particle, global_best: np.ndarray, num_dimensions: int, min_position: float, max_position: float, inertia_weight: float, cognitive_weight: float, social_weight: float, evaluate_func: callable):
    for i in range(num_dimensions):
        r1 = random.random()
        r2 = random.random()
        particle.velocity[i] = (inertia_weight * particle.velocity[i] +
                                cognitive_weight * r1 * (particle.personal_best[i] - particle.position[i]) +
                                social_weight * r2 * (global_best[i] - particle.position[i]))
        particle.position[i] += particle.velocity[i]
        # Clamp position within the valid range
        particle.position[i] = max(min(particle.position[i], max_position), min_position)
    
    fitness = evaluate_func(particle.position)
    if fitness < particle.personal_best_fitness:
        particle.personal_best = particle.position
        particle.personal_best_fitness = fitness

def pso(num_dimensions: int, num_particles: int, max_iterations: int, min_position: float, max_position: float, inertia_weight: float, cognitive_weight: float, social_weight: float, evaluate_func: callable):
# PSO initialization
    particles = [Particle() for _ in range(num_particles)]
    global_best = np.zeros(num_dimensions)
    global_best_fitness = float('inf')

    # Initialize particles
    for particle in particles:
        initialize_particle(particle, min_position, max_position, num_dimensions, evaluate_func)
        if particle.personal_best_fitness < global_best_fitness:
            global_best = particle.personal_best
            global_best_fitness = particle.personal_best_fitness

    # PSO iterations
    convergence_data = []
    for _ in range(max_iterations):
        convergence_data.append(global_best_fitness)
        for particle in particles:
            update_particle(particle, global_best, num_dimensions, min_position, max_position, inertia_weight, cognitive_weight, social_weight, evaluate_func)
            if particle.personal_best_fitness < global_best_fitness:
                global_best = particle.personal_best
                global_best_fitness = particle.personal_best_fitness

    # Print global minimum
    print("Global Minimum Found:")
    for i, value in enumerate(global_best):
        print(f"x[{i}] = {value}")
    print("Minimum Fitness:", global_best_fitness)

    # Plot convergence graph
    plt.plot(range(max_iterations), convergence_data)
    plt.title("PSO Convergence")
    plt.xlabel("Iteration")
    plt.ylabel("Best Fitness")
    plt.show()

if __name__ == "__main__":
    pso(num_dimensions=10, num_particles=50, max_iterations=100, min_position=-5.12, max_position=5.12, inertia_weight=0.729, cognitive_weight=1.49445, social_weight=1.49445, evaluate_func=f1)