"""
Compare Baldwin vs Phenotype-First on Compositional L+T Task
Tests when epigenomic write-back becomes critical!
"""

import random
import numpy as np
from baldwin_compositional import run_baldwin_compositional
from phenotype_first_compositional import run_phenotype_first_compositional


def main():
    print("\n" + "="*80)
    print("COMPOSITIONAL TASK EXPERIMENT")
    print("Testing when epigenomic write-back matters!")
    print("="*80)

    # Run both methods
    print("\n" + "▶"*40)
    baldwin_result = run_baldwin_compositional(max_generations=150, population_size=50)

    print("\n" + "▶"*40)
    phenotype_result = run_phenotype_first_compositional(max_generations=150, population_size=50)

    # Compare results
    print("\n" + "="*80)
    print("COMPARISON: BALDWIN vs PHENOTYPE-FIRST")
    print("="*80)

    print(f"\n{'Metric':<30} {'Baldwin':<20} {'Phenotype-First':<20} {'Winner':<15}")
    print("-"*85)

    # Fitness
    print(f"{'Final Fitness':<30} {baldwin_result['final_fitness']:<20.3f} "
          f"{phenotype_result['final_fitness']:<20.3f} ", end="")
    if phenotype_result['final_fitness'] > baldwin_result['final_fitness'] + 0.01:
        print("Phenotype ✓")
    elif baldwin_result['final_fitness'] > phenotype_result['final_fitness'] + 0.01:
        print("Baldwin ✓")
    else:
        print("Tie")

    # Convergence
    print(f"{'Convergence (gens)':<30} {baldwin_result['convergence_gen']:<20} "
          f"{phenotype_result['convergence_gen']:<20} ", end="")
    if phenotype_result['convergence_gen'] < baldwin_result['convergence_gen'] - 1:
        print(f"Phenotype ✓ ({baldwin_result['convergence_gen']/phenotype_result['convergence_gen']:.1f}x)")
    else:
        print("Tie")

    # L score
    print(f"{'L Pattern Score':<30} {baldwin_result['L_score']:<20.3f} "
          f"{phenotype_result['L_score']:<20.3f}")

    # T score
    print(f"{'T Pattern Score':<30} {baldwin_result['T_score']:<20.3f} "
          f"{phenotype_result['T_score']:<20.3f}")

    print("\n" + "="*80)
    print("KEY FINDINGS")
    print("="*80)

    speedup = baldwin_result['convergence_gen'] / max(phenotype_result['convergence_gen'], 1)
    print(f"\nPhenotype-First speedup: {speedup:.1f}x")
    print(f"  Baldwin: {baldwin_result['convergence_gen']} gens")
    print(f"  Phenotype: {phenotype_result['convergence_gen']} gens")

    print(f"\nFitness:")
    print(f"  Baldwin: {baldwin_result['final_fitness']:.3f}")
    print(f"  Phenotype-First: {phenotype_result['final_fitness']:.3f}")

    print("\n" + "="*80)
    print("INTERPRETATION")
    print("="*80)

    if speedup > 2.0:
        print("\n✓ PHENOTYPE-FIRST DOMINATES on compositional tasks!")
        print("  Reason: Epigenome inheritance lets organism inherit L,")
        print("          then learn T, then combine them directly.")
        print("          Baldwin must learn L and T from scratch each time.")
        print("\n  This validates Denis Noble's theory:")
        print("  - Organism WRITES back learned patterns to epigenome")
        print("  - Offspring can REUSE patterns for composition")
        print("  - True 'extended agency' matters for complex problems!")
    elif speedup > 1.2:
        print("\n~ PHENOTYPE-FIRST SLIGHTLY FASTER on compositional tasks")
        print("  Phenotype has modest advantage but not dramatic")
    else:
        print("\n✗ No significant difference")

    print("\n" + "="*80 + "\n")

    # Return both results for further analysis
    return {
        'baldwin': baldwin_result,
        'phenotype_first': phenotype_result,
        'speedup': speedup,
    }


if __name__ == "__main__":
    results = main()
