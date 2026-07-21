"""
Compositional Task Environment
Target: L+T pattern (must have BOTH L AND T present)
Not: "Learn L OR T"
But: "Learn L AND T simultaneously"

This tests when epigenomic write-back matters!
"""

import numpy as np


class CompositionTask:
    """
    Compositional task: Organism must learn both L and T patterns together
    Target: 10 cells forming L+T combination (5 cells L + 5 cells T)
    """

    def __init__(self):
        # L pattern (5 cells)
        self.L_target = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])

        # T pattern (5 cells)
        self.T_target = np.array([
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])

        # L+T composite target (BOTH must be present)
        self.composite_target = self.L_target | self.T_target

        print("\n" + "="*80)
        print("COMPOSITIONAL TASK ENVIRONMENT")
        print("="*80)
        print("\nTarget: L+T pattern (both L AND T must be present)")
        print(f"L target cells: {np.sum(self.L_target)}")
        print(f"T target cells: {np.sum(self.T_target)}")
        print(f"Composite target cells: {np.sum(self.composite_target)}")
        print("\nVisualization:")
        print("\nL pattern:")
        self._print_grid(self.L_target)
        print("\nT pattern:")
        self._print_grid(self.T_target)
        print("\nL+T Composite (target):")
        self._print_grid(self.composite_target)
        print("="*80 + "\n")

    @staticmethod
    def _print_grid(grid):
        """Print grid visualization"""
        for row in grid:
            print("  " + "".join(["█" if cell else "·" for cell in row]))

    def evaluate_fitness(self, phenotype):
        """
        Evaluate fitness on composite L+T task
        Must have BOTH L AND T cells correct

        Fitness = (L_intersection/L_cells + T_intersection/T_cells) / 2
        Both must be high!
        """
        L_intersection = np.sum(phenotype & self.L_target)
        T_intersection = np.sum(phenotype & self.T_target)

        L_recall = L_intersection / np.sum(self.L_target)
        T_recall = T_intersection / np.sum(self.T_target)

        # Must have BOTH L and T!
        # If missing either, fitness drops significantly
        composite_fitness = (L_recall + T_recall) / 2

        return composite_fitness

    def get_component_scores(self, phenotype):
        """Get separate L and T scores for analysis"""
        L_intersection = np.sum(phenotype & self.L_target)
        T_intersection = np.sum(phenotype & self.T_target)

        L_recall = L_intersection / np.sum(self.L_target)
        T_recall = T_intersection / np.sum(self.T_target)

        return {
            'L_score': L_recall,
            'T_score': T_recall,
            'both_present': (L_recall > 0.5) and (T_recall > 0.5),
        }


# Test the environment
if __name__ == "__main__":
    env = CompositionTask()

    # Test case 1: Perfect L+T
    test1 = env.composite_target
    print("Test 1: Perfect L+T composition")
    print(f"  Fitness: {env.evaluate_fitness(test1):.3f}")
    print(f"  Components: {env.get_component_scores(test1)}")

    # Test case 2: Only L (missing T)
    test2 = env.L_target
    print("\nTest 2: Only L (missing T)")
    print(f"  Fitness: {env.evaluate_fitness(test2):.3f}")
    print(f"  Components: {env.get_component_scores(test2)}")

    # Test case 3: Only T (missing L)
    test3 = env.T_target
    print("\nTest 3: Only T (missing L)")
    print(f"  Fitness: {env.evaluate_fitness(test3):.3f}")
    print(f"  Components: {env.get_component_scores(test3)}")

    # Test case 4: Random
    test4 = np.random.randint(0, 2, (10, 10))
    print("\nTest 4: Random")
    print(f"  Fitness: {env.evaluate_fitness(test4):.3f}")
    print(f"  Components: {env.get_component_scores(test4)}")

    print("\n" + "="*80)
    print("KEY INSIGHT:")
    print("="*80)
    print("Must learn BOTH L and T to get high fitness")
    print("- Only L: 50% fitness (missing T)")
    print("- Only T: 50% fitness (missing L)")
    print("- L+T: 100% fitness (perfect!)")
    print("\nBaldwin must learn L and T separately, then combine")
    print("Phenotype-First can inherit L, learn T, combine directly!")
    print("="*80)
