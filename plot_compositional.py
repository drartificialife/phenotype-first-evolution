"""
Publication-Quality Plots for Compositional Task Experiment
30-run comparison of Baldwin vs Phenotype-First on L+T task
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats


def load_results(csv_file='compositional_results_30runs.csv'):
    """Load results from CSV"""
    results = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)
    return results


def parse_data(results):
    """Extract data by method"""
    data = {
        'Baldwin': {
            'fitness': [],
            'L_score': [],
            'T_score': [],
            'convergence': [],
        },
        'Phenotype-First': {
            'fitness': [],
            'L_score': [],
            'T_score': [],
            'convergence': [],
        }
    }

    for row in results:
        method = row['method']
        data[method]['fitness'].append(float(row['final_fitness']))
        data[method]['L_score'].append(float(row['L_score']))
        data[method]['T_score'].append(float(row['T_score']))
        data[method]['convergence'].append(float(row['convergence_gen']))

    return data


def plot_fitness_comparison(data):
    """Box plot of final fitness"""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

    methods = ['Baldwin', 'Phenotype-First']
    fitness_data = [data[m]['fitness'] for m in methods]

    bp = ax.boxplot(fitness_data, labels=methods, patch_artist=True, widths=0.6)

    colors = ['#FF6B6B', '#4ECDC4']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    ax.set_ylabel('Final Fitness', fontsize=12, fontweight='bold')
    ax.set_xlabel('Method', fontsize=12, fontweight='bold')
    ax.set_title('Compositional L+T Task: Final Fitness Comparison (30 runs)',
                 fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Add mean markers
    for i, d in enumerate(fitness_data, 1):
        mean = np.mean(d)
        ax.plot(i, mean, 'D', color='black', markersize=8, zorder=3)

    plt.tight_layout()
    plt.savefig('compositional_fitness_boxplot.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_fitness_boxplot.png")
    plt.close()


def plot_violin_fitness(data):
    """Violin plot of fitness"""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

    methods = ['Baldwin', 'Phenotype-First']
    fitness_data = [data[m]['fitness'] for m in methods]

    parts = ax.violinplot(fitness_data, positions=[1, 2], showmeans=True, showmedians=True)

    ax.set_ylabel('Final Fitness', fontsize=12, fontweight='bold')
    ax.set_xlabel('Method', fontsize=12, fontweight='bold')
    ax.set_title('Fitness Distribution: Baldwin vs Phenotype-First',
                 fontsize=14, fontweight='bold')
    ax.set_xticks([1, 2])
    ax.set_xticklabels(methods)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig('compositional_fitness_violin.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_fitness_violin.png")
    plt.close()


def plot_component_scores(data):
    """Bar plot of L and T scores"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), dpi=300)

    methods = ['Baldwin', 'Phenotype-First']
    L_means = [np.mean(data[m]['L_score']) for m in methods]
    L_stds = [np.std(data[m]['L_score']) for m in methods]
    T_means = [np.mean(data[m]['T_score']) for m in methods]
    T_stds = [np.std(data[m]['T_score']) for m in methods]

    x = np.arange(len(methods))
    width = 0.35

    # L score
    ax1.bar(x - width/2, L_means, width, yerr=L_stds, label='L Score',
            color='#4ECDC4', alpha=0.7, capsize=5)
    ax1.set_ylabel('Score', fontsize=11, fontweight='bold')
    ax1.set_title('L Pattern Score', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(methods)
    ax1.set_ylim([0, 1])
    ax1.grid(axis='y', alpha=0.3, linestyle='--')

    # T score
    ax2.bar(x - width/2, T_means, width, yerr=T_stds, label='T Score',
            color='#FF6B6B', alpha=0.7, capsize=5)
    ax2.set_ylabel('Score', fontsize=11, fontweight='bold')
    ax2.set_title('T Pattern Score', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(methods)
    ax2.set_ylim([0, 1])
    ax2.grid(axis='y', alpha=0.3, linestyle='--')

    plt.suptitle('Component-Wise Performance: L and T Pattern Recognition',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('compositional_component_scores.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_component_scores.png")
    plt.close()


def plot_both_present_rate(data):
    """Bar plot showing when both L and T are present"""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

    methods = ['Baldwin', 'Phenotype-First']
    both_present_rates = []

    for method in methods:
        L_scores = data[method]['L_score']
        T_scores = data[method]['T_score']
        both_present = sum(1 for l, t in zip(L_scores, T_scores) if l >= 0.5 and t >= 0.5) / len(L_scores) * 100
        both_present_rates.append(both_present)

    colors = ['#FF6B6B', '#4ECDC4']
    bars = ax.bar(methods, both_present_rates, color=colors, alpha=0.7, width=0.6)

    # Add value labels
    for bar, rate in zip(bars, both_present_rates):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{rate:.1f}%',
                ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax.set_ylabel('Percent of Runs (%)', fontsize=12, fontweight='bold')
    ax.set_title('Compositional Success: Both L and T Present (≥0.5)',
                 fontsize=14, fontweight='bold')
    ax.set_ylim([0, 110])
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig('compositional_both_present_rate.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_both_present_rate.png")
    plt.close()


def plot_scatter_LT(data):
    """Scatter plot: L vs T score"""
    fig, ax = plt.subplots(figsize=(10, 8), dpi=300)

    methods = ['Baldwin', 'Phenotype-First']
    colors = ['#FF6B6B', '#4ECDC4']

    for method, color in zip(methods, colors):
        L_scores = data[method]['L_score']
        T_scores = data[method]['T_score']
        ax.scatter(L_scores, T_scores, s=100, alpha=0.6, label=method, color=color)

    ax.set_xlabel('L Pattern Score', fontsize=12, fontweight='bold')
    ax.set_ylabel('T Pattern Score', fontsize=12, fontweight='bold')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_aspect('equal')

    # Target region (both >= 0.5)
    target = mpatches.Rectangle((0.5, 0.5), 0.5, 0.5, linewidth=2,
                                 edgecolor='green', facecolor='green', alpha=0.1)
    ax.add_patch(target)
    ax.text(0.75, 0.75, 'Target Region\n(both ≥ 0.5)', ha='center', va='center',
            fontsize=11, fontweight='bold', color='darkgreen')

    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(fontsize=11, loc='upper left')
    ax.set_title('Compositional Task: L vs T Pattern Achievement',
                 fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('compositional_scatter_LT.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_scatter_LT.png")
    plt.close()


def plot_convergence(data):
    """Convergence generation comparison"""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

    methods = ['Baldwin', 'Phenotype-First']
    convergence_data = [data[m]['convergence'] for m in methods]

    bp = ax.boxplot(convergence_data, labels=methods, patch_artist=True, widths=0.6)

    colors = ['#FF6B6B', '#4ECDC4']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    ax.set_ylabel('Convergence Generation', fontsize=12, fontweight='bold')
    ax.set_xlabel('Method', fontsize=12, fontweight='bold')
    ax.set_title('Convergence Speed: Baldwin vs Phenotype-First',
                 fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig('compositional_convergence.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_convergence.png")
    plt.close()


def plot_summary_heatmap(data):
    """Heatmap of all metrics"""
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)

    methods = ['Baldwin', 'Phenotype-First']
    metrics = ['Fitness', 'L Score', 'T Score']

    values = np.array([
        [np.mean(data['Baldwin']['fitness']), np.mean(data['Baldwin']['L_score']),
         np.mean(data['Baldwin']['T_score'])],
        [np.mean(data['Phenotype-First']['fitness']), np.mean(data['Phenotype-First']['L_score']),
         np.mean(data['Phenotype-First']['T_score'])],
    ])

    im = ax.imshow(values, cmap='RdYlGn', aspect='auto', vmin=0, vmax=1)

    ax.set_xticks(np.arange(len(metrics)))
    ax.set_yticks(np.arange(len(methods)))
    ax.set_xticklabels(metrics, fontsize=11)
    ax.set_yticklabels(methods, fontsize=11)

    # Add text annotations
    for i in range(len(methods)):
        for j in range(len(metrics)):
            text = ax.text(j, i, f'{values[i, j]:.3f}',
                          ha="center", va="center", color="black", fontsize=12, fontweight='bold')

    ax.set_title('Performance Heatmap: All Metrics', fontsize=14, fontweight='bold')
    fig.colorbar(im, ax=ax, label='Score')

    plt.tight_layout()
    plt.savefig('compositional_heatmap.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: compositional_heatmap.png")
    plt.close()


def main():
    """Generate all plots"""
    print("\n" + "="*80)
    print("GENERATING PUBLICATION-QUALITY PLOTS")
    print("Compositional L+T Task: 30-Run Experiment")
    print("="*80 + "\n")

    results = load_results()
    data = parse_data(results)

    plot_fitness_comparison(data)
    plot_violin_fitness(data)
    plot_component_scores(data)
    plot_both_present_rate(data)
    plot_scatter_LT(data)
    plot_convergence(data)
    plot_summary_heatmap(data)

    print("\n" + "="*80)
    print("✅ All plots generated successfully!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
