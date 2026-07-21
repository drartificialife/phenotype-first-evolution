import random
import numpy as np
from copy import deepcopy

class LamarckianOrganism:
    """
    Lamarckian Evolution: Learning + Slow Genetic Assimilation

    Key difference from Baldwin:
    - Like Baldwin: organisms learn during lifetime
    - Different: learned patterns slowly encode into genes over many generations
    - This creates "genetic memory" but SLOWLY (50-100 gens)

    Mechanism: If organism has learned pattern, offspring have small chance
    to inherit it encoded in genes. Over many gens, accumulates.
    """

    def __init__(self, genome=None, encoded_patterns=None):
        self.genome = genome if genome is not None else self._random_genome()
        # encoded_patterns: patterns that slowly accumulated via genetic assimilation
        self.encoded_patterns = encoded_patterns or {}
        # learned_this_gen: patterns learned THIS generation (not inherited)
        self.learned_this_gen = []
        self.fitness = 0.0

    @staticmethod
    def _random_genome():
        return np.random.randint(0, 2, 100)

    def phenotype_from_genome(self):
        """Decode genome to 10x10 grid"""
        grid = np.zeros((10, 10), dtype=int)

        primitives = [
            [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # L
            [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)],  # T
            [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],  # Cross
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],  # Line
            [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)],  # Block
        ]

        for prim_idx in range(5):
            start_bit = prim_idx * 20
            offset_x = int(self.genome[start_bit] * 5)
            offset_y = int(self.genome[start_bit + 1] * 5)
            scale = 1 + int(self.genome[start_bit + 2] * 2)
            active = self.genome[start_bit + 3] == 1

            if active:
                for dx, dy in primitives[prim_idx]:
                    x, y = offset_x + dx * scale, offset_y + dy * scale
                    if 0 <= x < 10 and 0 <= y < 10:
                        grid[x, y] = 1

        return grid

    def learn(self, target_grid, num_trials=20):
        """
        Learning phase: Try random compositions to find patterns.
        LAMARCKIAN ADVANTAGE: Inherited encoded patterns give head start!
        """
        best_fitness = 0.0
        best_pattern = None
        old_genome = self.genome.copy()

        # LAMARCKIAN FEATURE: First check if inherited patterns already solve it
        if self.encoded_patterns:
            inherited_phenotype = np.zeros((10, 10), dtype=int)
            for encoded_pattern in self.encoded_patterns.values():
                inherited_phenotype |= encoded_pattern

            fitness = self._evaluate_fitness(inherited_phenotype, target_grid)
            if fitness > 0.95:
                # Already solved via inheritance! Use inherited pattern
                best_fitness = fitness
                best_pattern = inherited_phenotype
                self.fitness = best_fitness
                self.genome = old_genome
                return

        # Learning phase: try to find new patterns
        for trial in range(num_trials):
            if trial < num_trials // 2 and self.encoded_patterns:
                # First half: combine inherited patterns with new genomes
                test_genome = self._random_genome()
                self.genome = test_genome
                phenotype = self.phenotype_from_genome()

                # Add inherited patterns
                for encoded_pattern in self.encoded_patterns.values():
                    phenotype |= encoded_pattern
            else:
                # Second half: pure random learning
                test_genome = self._random_genome()
                self.genome = test_genome
                phenotype = self.phenotype_from_genome()

            # Evaluate fitness
            fitness = self._evaluate_fitness(phenotype, target_grid)

            if fitness > best_fitness:
                best_fitness = fitness
                best_pattern = phenotype

        self.genome = old_genome

        # Store learned pattern
        if best_pattern is not None and best_fitness > 0.3:
            self.learned_this_gen.append({
                'pattern': best_pattern,
                'fitness': best_fitness,
            })

        # Fitness = best learned (with inheritance advantage)
        self.fitness = best_fitness

    @staticmethod
    def _evaluate_fitness(phenotype, target):
        """RECALL metric"""
        intersection = np.sum(phenotype & target)
        target_cells = np.sum(target)

        if target_cells == 0:
            return 0.0

        return intersection / target_cells

    def copy(self):
        """
        Reproduction with genetic assimilation.

        Key mechanism:
        - Inherited encoded patterns are ALWAYS copied
        - Learned patterns from this generation have small chance to encode
        - Over many gens, learned patterns slowly accumulate in encoded_patterns
        """
        # Copy and mutate genome
        child_genome = self.genome.copy()
        mutation_rate = 0.02
        for i in range(len(child_genome)):
            if random.random() < mutation_rate:
                child_genome[i] = 1 - child_genome[i]

        # GENETIC ASSIMILATION: Copy encoded patterns (inherited)
        child_encoded = deepcopy(self.encoded_patterns)

        # GENETIC ASSIMILATION: Small chance for learned patterns to encode
        # This simulates slow genetic assimilation over many generations
        assimilation_rate = 0.15  # 15% chance per pattern per generation (faster encoding)
        for learned in self.learned_this_gen:
            if random.random() < assimilation_rate:
                # This learned pattern becomes "encoded" for next generation
                pattern_key = random.randint(0, 1000000)  # Unique key
                child_encoded[pattern_key] = learned['pattern']

        child = LamarckianOrganism(child_genome, child_encoded)
        return child


def run_lamarckian_ga(target_shape, max_generations=150, population_size=50):
    """Run Lamarckian GA on a single target shape"""

    population = [LamarckianOrganism() for _ in range(population_size)]

    target_shapes = {
        'L': np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
        'T': np.array([[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
        'Plus': np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    }

    target = target_shapes[target_shape]
    convergence_gen = None

    for generation in range(max_generations):
        # Learning phase
        for organism in population:
            organism.learn(target, num_trials=20)

        # Evaluate fitness (already set during learning)
        for organism in population:
            phenotype = organism.phenotype_from_genome()
            organism.fitness = organism._evaluate_fitness(phenotype, target)

        # Check convergence
        best_fitness = max(org.fitness for org in population)
        avg_fitness = np.mean([org.fitness for org in population])

        if generation % 20 == 0:
            total_encoded = sum(len(org.encoded_patterns) for org in population)
            print(f"  Gen {generation:3d}: Best={best_fitness:.3f}, Avg={avg_fitness:.3f}, "
                  f"Encoded patterns in pop={total_encoded}")

        if best_fitness >= 0.95 and convergence_gen is None:
            convergence_gen = generation
            print(f"  ✓ Converged at generation {generation}!")

        # Selection and reproduction
        sorted_pop = sorted(population, key=lambda x: x.fitness, reverse=True)
        elite = sorted_pop[:10]

        new_population = elite[:]
        while len(new_population) < population_size:
            parent = random.choice(sorted_pop[:25])
            child = parent.copy()
            new_population.append(child)

        population = new_population[:population_size]

    # Final results
    best_organism = max(population, key=lambda x: x.fitness)
    phenotype = best_organism.phenotype_from_genome()
    final_fitness = best_organism._evaluate_fitness(phenotype, target)

    if convergence_gen is None:
        convergence_gen = max_generations

    return {
        'shape': target_shape,
        'final_fitness': final_fitness,
        'convergence_gen': convergence_gen,
        'final_phenotype': phenotype,
        'best_organism': best_organism
    }


if __name__ == "__main__":
    print("=" * 80)
    print("LAMARCKIAN GA: Learning + Slow Genetic Assimilation")
    print("=" * 80)
    print()

    shapes = ['L', 'T', 'Plus']
    results = {}

    for shape in shapes:
        print(f"\n{'='*80}")
        print(f"Testing {shape} shape...")
        print(f"{'='*80}")
        result = run_lamarckian_ga(shape)
        results[shape] = result
        print(f"\nFinal fitness: {result['final_fitness']:.3f}")
        print(f"Convergence: Generation {result['convergence_gen']}")

    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    for shape in shapes:
        print(f"{shape:5s}: Fitness={results[shape]['final_fitness']:.1%}, "
              f"Convergence={results[shape]['convergence_gen']} gens")

    avg_fitness = np.mean([results[s]['final_fitness'] for s in shapes])
    avg_convergence = np.mean([results[s]['convergence_gen'] for s in shapes])

    print(f"\nAverage fitness: {avg_fitness:.1%}")
    print(f"Average convergence: {avg_convergence:.1f} gens")
    print(f"\nNote: Lamarckian should be SLOWER than Baldwin (15.7 gens)")
    print(f"      Because genetic assimilation takes ~50-100 generations!")
