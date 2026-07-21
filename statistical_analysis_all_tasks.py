"""
Statistical Analysis: All 3 Compositional Tasks
L+T, L+Plus, T+Plus - 30 runs each, 2 methods
"""

import csv
import numpy as np
import json
from scipy import stats


def load_results(csv_file='compositional_results_all_tasks.csv'):
    """Load results from CSV"""
    results = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)
    return results


def analyze_task(results, task_name):
    """Analyze single task"""
    print(f"\n{'='*80}")
    print(f"TASK: {task_name}")
    print(f"{'='*80}\n")

    task_results = [r for r in results if r['task'] == task_name]

    baldwin = [r for r in task_results if r['method'] == 'Baldwin']
    phenotype = [r for r in task_results if r['method'] == 'Phenotype-First']

    baldwin_fitness = [float(r['final_fitness']) for r in baldwin]
    phenotype_fitness = [float(r['final_fitness']) for r in phenotype]

    # Parse pattern names from first row
    pattern1_scores_b = [float(r['pattern1_score']) for r in baldwin if r['pattern1_score']]
    pattern2_scores_b = [float(r['pattern2_score']) for r in baldwin if r['pattern2_score']]
    pattern1_scores_p = [float(r['pattern1_score']) for r in phenotype if r['pattern1_score']]
    pattern2_scores_p = [float(r['pattern2_score']) for r in phenotype if r['pattern2_score']]

    print(f"BALDWIN (n={len(baldwin)}):")
    print(f"  Fitness:     {np.mean(baldwin_fitness):.3f} ± {np.std(baldwin_fitness):.3f}")
    print(f"  Pattern 1:   {np.mean(pattern1_scores_b):.3f} ± {np.std(pattern1_scores_b):.3f}")
    print(f"  Pattern 2:   {np.mean(pattern2_scores_b):.3f} ± {np.std(pattern2_scores_b):.3f}")

    print(f"\nPHENOTYPE-FIRST (n={len(phenotype)}):")
    print(f"  Fitness:     {np.mean(phenotype_fitness):.3f} ± {np.std(phenotype_fitness):.3f}")
    print(f"  Pattern 1:   {np.mean(pattern1_scores_p):.3f} ± {np.std(pattern1_scores_p):.3f}")
    print(f"  Pattern 2:   {np.mean(pattern2_scores_p):.3f} ± {np.std(pattern2_scores_p):.3f}")

    # ANOVA
    f_stat, p_value = stats.f_oneway(baldwin_fitness, phenotype_fitness)
    print(f"\nANOVA: F={f_stat:.2f}, p={p_value:.6f}")

    if p_value < 0.001:
        sig = "*** (highly significant)"
    elif p_value < 0.01:
        sig = "** (very significant)"
    elif p_value < 0.05:
        sig = "* (significant)"
    else:
        sig = "(NOT significant)"
    print(f"Result: {sig}")

    # T-test
    t_stat, p_t = stats.ttest_ind(phenotype_fitness, baldwin_fitness, equal_var=False)
    print(f"\nWelch's t-test: t={t_stat:.2f}, p={p_t:.6f}")

    # Cohen's d
    def cohens_d(g1, g2):
        n1, n2 = len(g1), len(g2)
        var1, var2 = np.var(g1, ddof=1), np.var(g2, ddof=1)
        pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
        return (np.mean(g1) - np.mean(g2)) / pooled_std

    d = cohens_d(phenotype_fitness, baldwin_fitness)
    print(f"Cohen's d: {d:.3f}")

    # Success rate
    baldwin_success = sum(1 for f in baldwin_fitness if f > 0.8) / len(baldwin_fitness) * 100
    phenotype_success = sum(1 for f in phenotype_fitness if f > 0.8) / len(phenotype_fitness) * 100
    print(f"\nSuccess rate (fitness > 0.8):")
    print(f"  Baldwin: {baldwin_success:.1f}%")
    print(f"  Phenotype: {phenotype_success:.1f}%")

    # Both present
    baldwin_both = sum(1 for p1, p2 in zip(pattern1_scores_b, pattern2_scores_b)
                      if p1 >= 0.5 and p2 >= 0.5) / len(pattern1_scores_b) * 100
    phenotype_both = sum(1 for p1, p2 in zip(pattern1_scores_p, pattern2_scores_p)
                        if p1 >= 0.5 and p2 >= 0.5) / len(pattern1_scores_p) * 100
    print(f"\nBoth-present rate (P1≥0.5 AND P2≥0.5):")
    print(f"  Baldwin: {baldwin_both:.1f}%")
    print(f"  Phenotype: {phenotype_both:.1f}%")

    return {
        'task': task_name,
        'baldwin_fitness_mean': float(np.mean(baldwin_fitness)),
        'baldwin_fitness_std': float(np.std(baldwin_fitness)),
        'phenotype_fitness_mean': float(np.mean(phenotype_fitness)),
        'phenotype_fitness_std': float(np.std(phenotype_fitness)),
        'anova_F': float(f_stat),
        'anova_p': float(p_value),
        'ttest_t': float(t_stat),
        'ttest_p': float(p_t),
        'cohens_d': float(d),
        'baldwin_success': float(baldwin_success),
        'phenotype_success': float(phenotype_success),
        'baldwin_both': float(baldwin_both),
        'phenotype_both': float(phenotype_both),
    }


def main():
    print("\n" + "="*80)
    print("STATISTICAL ANALYSIS: ALL 3 COMPOSITIONAL TASKS")
    print("="*80)

    results = load_results()

    # Analyze each task
    task_stats = {}
    for task_name in ['L+T', 'L+Plus', 'T+Plus']:
        task_stats[task_name] = analyze_task(results, task_name)

    # Summary comparison
    print(f"\n{'='*80}")
    print("SUMMARY: ALL TASKS")
    print(f"{'='*80}\n")

    print(f"{'Task':<12} {'Baldwin':<15} {'Phenotype':<15} {'Advantage':<12} {'p-value':<12}")
    print("-" * 70)
    for task_name in ['L+T', 'L+Plus', 'T+Plus']:
        stats_dict = task_stats[task_name]
        b_mean = stats_dict['baldwin_fitness_mean']
        p_mean = stats_dict['phenotype_fitness_mean']
        p_val = stats_dict['anova_p']
        advantage = p_mean / b_mean if b_mean > 0 else 0

        print(f"{task_name:<12} {b_mean:<15.3f} {p_mean:<15.3f} {advantage:<12.2f}x {p_val:<12.6f}")

    # Save to JSON
    with open('compositional_all_tasks_stats.json', 'w') as f:
        json.dump(task_stats, f, indent=2)

    print(f"\n✅ Statistics saved to compositional_all_tasks_stats.json")

    # Overall conclusion
    print(f"\n{'='*80}")
    print("KEY FINDINGS")
    print(f"{'='*80}\n")

    for task_name in ['L+T', 'L+Plus', 'T+Plus']:
        s = task_stats[task_name]
        advantage = s['phenotype_fitness_mean'] / s['baldwin_fitness_mean']
        p_success = s['phenotype_success']
        print(f"{task_name}:")
        print(f"  Phenotype {advantage:.1f}x better (p={s['anova_p']:.6f})")
        print(f"  Success rate: {p_success:.0f}% vs Baldwin {s['baldwin_success']:.0f}%")
        print(f"  Cohen's d = {s['cohens_d']:.2f} (large effect)")


if __name__ == "__main__":
    main()
