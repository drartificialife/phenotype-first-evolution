"""
Comprehensive 30-Run Compositional Task Experiment
Tests Baldwin vs Phenotype-First on L+T composition
30 runs × 2 algorithms = 60 total experiments
"""

import random
import numpy as np
import csv
from datetime import datetime
from baldwin_compositional import run_baldwin_compositional
from phenotype_first_compositional import run_phenotype_first_compositional


def run_comprehensive_experiment(num_runs=30):
    """Run 30 experiments with different seeds"""

    results = []

    print("\n" + "="*80)
    print("COMPREHENSIVE 30-RUN COMPOSITIONAL TASK EXPERIMENT")
    print("="*80)
    print(f"Methods: Baldwin, Phenotype-First")
    print(f"Runs: {num_runs} per method (total: {num_runs*2})")
    print(f"Task: L+T Compositional (must learn both patterns together)")
    print("="*80 + "\n")

    # Run Baldwin 30 times with different seeds
    print("▶ Running BALDWIN (30 runs with different seeds)...\n")
    for run_id in range(1, num_runs + 1):
        # Set seed for reproducibility
        seed = run_id * 42  # Different seed each run
        random.seed(seed)
        np.random.seed(seed)

        try:
            result = run_baldwin_compositional(max_generations=150, population_size=50)
            result['run'] = run_id
            result['seed'] = seed
            results.append(result)

            print(f"  Run {run_id:2d}/30: Fitness={result['final_fitness']:.3f}, "
                  f"L={result['L_score']:.3f}, T={result['T_score']:.3f}")
        except Exception as e:
            print(f"  Run {run_id:2d}/30: ERROR - {str(e)}")

    # Run Phenotype-First 30 times with different seeds
    print("\n▶ Running PHENOTYPE-FIRST (30 runs with different seeds)...\n")
    for run_id in range(1, num_runs + 1):
        # Set seed for reproducibility
        seed = run_id * 42  # Different seed each run
        random.seed(seed)
        np.random.seed(seed)

        try:
            result = run_phenotype_first_compositional(max_generations=150, population_size=50)
            result['run'] = run_id
            result['seed'] = seed
            results.append(result)

            print(f"  Run {run_id:2d}/30: Fitness={result['final_fitness']:.3f}, "
                  f"L={result['L_score']:.3f}, T={result['T_score']:.3f}")
        except Exception as e:
            print(f"  Run {run_id:2d}/30: ERROR - {str(e)}")

    # Save results to CSV
    csv_file = 'compositional_results_30runs.csv'
    with open(csv_file, 'w', newline='') as f:
        fieldnames = ['method', 'run', 'seed', 'final_fitness', 'convergence_gen',
                     'L_score', 'T_score', 'patterns_inherited']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✅ Results saved to: {csv_file}")

    # Print summary
    print("\n" + "="*80)
    print("SUMMARY STATISTICS")
    print("="*80)

    baldwin_results = [r for r in results if r['method'] == 'Baldwin']
    phenotype_results = [r for r in results if r['method'] == 'Phenotype-First']

    print(f"\nBALDWIN ({len(baldwin_results)} runs):")
    print(f"  Fitness:      {np.mean([r['final_fitness'] for r in baldwin_results]):.3f} ± {np.std([r['final_fitness'] for r in baldwin_results]):.3f}")
    print(f"  L score:      {np.mean([r['L_score'] for r in baldwin_results]):.3f} ± {np.std([r['L_score'] for r in baldwin_results]):.3f}")
    print(f"  T score:      {np.mean([r['T_score'] for r in baldwin_results]):.3f} ± {np.std([r['T_score'] for r in baldwin_results]):.3f}")
    print(f"  Convergence:  {np.mean([r['convergence_gen'] for r in baldwin_results]):.1f} ± {np.std([r['convergence_gen'] for r in baldwin_results]):.1f} gens")

    print(f"\nPHENOTYPE-FIRST ({len(phenotype_results)} runs):")
    print(f"  Fitness:      {np.mean([r['final_fitness'] for r in phenotype_results]):.3f} ± {np.std([r['final_fitness'] for r in phenotype_results]):.3f}")
    print(f"  L score:      {np.mean([r['L_score'] for r in phenotype_results]):.3f} ± {np.std([r['L_score'] for r in phenotype_results]):.3f}")
    print(f"  T score:      {np.mean([r['T_score'] for r in phenotype_results]):.3f} ± {np.std([r['T_score'] for r in phenotype_results]):.3f}")
    print(f"  Convergence:  {np.mean([r['convergence_gen'] for r in phenotype_results]):.1f} ± {np.std([r['convergence_gen'] for r in phenotype_results]):.1f} gens")
    print(f"  Avg patterns: {np.mean([r.get('patterns_inherited', 0) for r in phenotype_results]):.1f}")

    print("\n" + "="*80)
    print(f"Total experiments completed: {len(results)}")
    print("="*80 + "\n")

    return results


if __name__ == "__main__":
    results = run_comprehensive_experiment(num_runs=30)
    print("✅ Experiment complete! Results saved to compositional_results_30runs.csv")
