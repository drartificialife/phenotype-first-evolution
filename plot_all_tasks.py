"""
Comparative Plots: All 3 Compositional Tasks
Publication-quality 300 DPI plots
"""

import csv
import numpy as np
import matplotlib.pyplot as plt


def load_results(csv_file='compositional_results_all_tasks.csv'):
    """Load results from CSV"""
    results = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)
    return results


def parse_data(results):
    """Extract data by task and method"""
    data = {}
    for task in ['L+T', 'L+Plus', 'T+Plus']:
        data[task] = {
            'Baldwin': {'fitness': []},
            'Phenotype-First': {'fitness': []},
        }

    for row in results:
        task = row['task']
        method = row['method']
        fitness = float(row['final_fitness'])
        data[task][method]['fitness'].append(fitness)

    return data


def plot_fitness_all_tasks(data):
    """3-panel plot: fitness for all tasks"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5), dpi=300)
    tasks = ['L+T', 'L+Plus', 'T+Plus']
    colors = ['#FF6B6B', '#4ECDC4']

    for idx, task in enumerate(tasks):
        ax = axes[idx]
        fitness_data = [data[task]['Baldwin']['fitness'],
                       data[task]['Phenotype-First']['fitness']]

        bp = ax.boxplot(fitness_data, labels=['Baldwin', 'Phenotype'],
                       patch_artist=True, widths=0.6)

        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

        ax.set_ylabel('Final Fitness', fontsize=11, fontweight='bold')
        ax.set_title(f'{task} Task', fontsize=12, fontweight='bold')
        ax.set_ylim([0, 1])
        ax.grid(axis='y', alpha=0.3, linestyle='--')

        # Add means
        for i, d in enumerate(fitness_data, 1):
            mean = np.mean(d)
            ax.plot(i, mean, 'D', color='black', markersize=8, zorder=3)

    plt.suptitle('Compositional Task Comparison: 3 Different Pairs',
                fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('compositional_all_tasks_fitness.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_all_tasks_fitness.png")
    plt.close()


def plot_fitness_by_task(data):
    """Bar plot: mean fitness across tasks"""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

    tasks = ['L+T', 'L+Plus', 'T+Plus']
    baldwin_means = [np.mean(data[t]['Baldwin']['fitness']) for t in tasks]
    phenotype_means = [np.mean(data[t]['Phenotype-First']['fitness']) for t in tasks]

    x = np.arange(len(tasks))
    width = 0.35

    bars1 = ax.bar(x - width/2, baldwin_means, width, label='Baldwin',
                  color='#FF6B6B', alpha=0.7)
    bars2 = ax.bar(x + width/2, phenotype_means, width, label='Phenotype-First',
                  color='#4ECDC4', alpha=0.7)

    ax.set_ylabel('Mean Fitness', fontsize=12, fontweight='bold')
    ax.set_xlabel('Compositional Task', fontsize=12, fontweight='bold')
    ax.set_title('Mean Fitness Across All Tasks', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(tasks)
    ax.legend(fontsize=11)
    ax.set_ylim([0, 1])
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig('compositional_all_tasks_means.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_all_tasks_means.png")
    plt.close()


def plot_advantage(data):
    """Bar plot: Phenotype advantage over Baldwin"""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

    tasks = ['L+T', 'L+Plus', 'T+Plus']
    advantages = []

    for task in tasks:
        b_mean = np.mean(data[task]['Baldwin']['fitness'])
        p_mean = np.mean(data[task]['Phenotype-First']['fitness'])
        if b_mean > 0:
            adv = p_mean / b_mean
        else:
            adv = 1.0 if p_mean == 0 else 999
        advantages.append(adv)

    colors_adv = ['#27AE60' if a > 1.5 else '#F39C12' if a > 1 else '#95A5A6'
                  for a in advantages]
    bars = ax.bar(tasks, advantages, color=colors_adv, alpha=0.7, width=0.6)

    ax.axhline(y=1.0, color='black', linestyle='--', linewidth=2, label='No difference')
    ax.set_ylabel('Advantage Factor (Phenotype / Baldwin)', fontsize=12, fontweight='bold')
    ax.set_title('Phenotype-First Advantage Across Tasks', fontsize=14, fontweight='bold')
    ax.set_ylim([0, max(advantages) * 1.2])
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.legend()

    # Add value labels
    for bar, adv in zip(bars, advantages):
        height = bar.get_height()
        label = f'{adv:.2f}x' if adv < 100 else '∞'
        ax.text(bar.get_x() + bar.get_width()/2., height,
               label, ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig('compositional_all_tasks_advantage.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_all_tasks_advantage.png")
    plt.close()


def plot_consistency(data):
    """Violin plot: consistency across runs"""
    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)

    tasks = ['L+T', 'L+Plus', 'T+Plus']
    positions = []
    pos_idx = 1

    for task in tasks:
        baldwin_data = data[task]['Baldwin']['fitness']
        phenotype_data = data[task]['Phenotype-First']['fitness']

        parts = ax.violinplot([baldwin_data, phenotype_data],
                             positions=[pos_idx, pos_idx+1],
                             showmeans=True, showmedians=True)
        positions.extend([pos_idx, pos_idx+1])
        pos_idx += 3

    ax.set_ylabel('Final Fitness', fontsize=12, fontweight='bold')
    ax.set_title('Fitness Distribution Across 3 Tasks', fontsize=14, fontweight='bold')
    ax.set_xticks([1.5, 4.5, 7.5])
    ax.set_xticklabels(tasks)
    ax.set_ylim([0, 1])
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='#FF6B6B', alpha=0.7, label='Baldwin'),
                      Patch(facecolor='#4ECDC4', alpha=0.7, label='Phenotype-First')]
    ax.legend(handles=legend_elements, loc='upper right')

    plt.tight_layout()
    plt.savefig('compositional_all_tasks_violin.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_all_tasks_violin.png")
    plt.close()


def main():
    print("\n" + "="*80)
    print("GENERATING COMPARATIVE PLOTS FOR ALL 3 TASKS")
    print("="*80 + "\n")

    results = load_results()
    data = parse_data(results)

    plot_fitness_all_tasks(data)
    plot_fitness_by_task(data)
    plot_advantage(data)
    plot_consistency(data)

    print("\n" + "="*80)
    print("✅ All comparative plots generated!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
