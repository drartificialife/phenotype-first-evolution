"""
Generate fitness comparison plot for SIMPLE TASKS ONLY
Shows all 3 algorithms (Gene-Centric, Baldwin, Phenopoiesis) on L, T, Plus
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Publication style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")

# Color scheme for algorithms
colors = {
    'Gene-Centric': '#E74C3C',      # Red
    'Baldwin': '#F39C12',            # Orange
    'Phenopoiesis': '#27AE60'        # Green
}

def create_simple_tasks_fitness_plot():
    """
    Simple tasks fitness comparison: L alone, T alone, Plus alone
    All 3 algorithms across all 3 simple tasks

    Expected results:
    - Gene-Centric: ~57-59% fitness (no learning)
    - Baldwin: ~100% fitness (learning, no inheritance)
    - Phenopoiesis: ~100% fitness (learning + inheritance, but inheritance irrelevant here)
    - No significant difference between Baldwin and Phenopoiesis (p = 0.559)
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    # Simple tasks
    tasks = ['L alone', 'T alone', 'Plus alone']

    # Simulated data (replace with actual experimental results)
    # Each value is mean ± s.d. from 30 runs
    results = {
        'Gene-Centric': {
            'L alone': (0.57, 0.28),
            'T alone': (0.59, 0.31),
            'Plus alone': (0.56, 0.25),
        },
        'Baldwin': {
            'L alone': (1.00, 0.00),
            'T alone': (1.00, 0.00),
            'Plus alone': (1.00, 0.00),
        },
        'Phenopoiesis': {
            'L alone': (1.00, 0.00),
            'T alone': (1.00, 0.00),
            'Plus alone': (1.00, 0.00),
        }
    }

    # Plot parameters
    x = np.arange(len(tasks))
    width = 0.25
    algorithms = ['Gene-Centric', 'Baldwin', 'Phenopoiesis']

    # Create bars for each algorithm
    for idx, algo in enumerate(algorithms):
        means = [results[algo][task][0] for task in tasks]
        stds = [results[algo][task][1] for task in tasks]

        position = x + (idx - 1) * width
        bars = ax.bar(position, means, width, label=algo,
                      color=colors[algo], alpha=0.8, capsize=5)

        # Add error bars
        ax.errorbar(position, means, yerr=stds, fmt='none',
                   ecolor='black', capsize=3, capthick=1, alpha=0.6)

    # Formatting
    ax.set_ylabel('Fitness', fontsize=12, fontweight='bold')
    ax.set_title('Simple Learning Tasks: Algorithm Comparison\n(L alone, T alone, Plus alone)',
                fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(tasks, fontsize=11)
    ax.set_ylim(-0.05, 1.15)
    ax.legend(fontsize=11, loc='upper right', framealpha=0.95)
    ax.grid(True, alpha=0.3, axis='y')

    # Add horizontal line at 100%
    ax.axhline(y=1.0, color='gray', linestyle='--', linewidth=1, alpha=0.5)

    # Add statistical annotation
    ax.text(0.5, 0.95, 'Baldwin vs Phenopoiesis: p = 0.559 (no difference)',
           transform=ax.transAxes, fontsize=10, ha='center',
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.savefig('simple_tasks_fitness_comparison.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: simple_tasks_fitness_comparison.png")
    plt.close()

if __name__ == '__main__':
    print("Generating simple tasks fitness comparison plot...\n")
    create_simple_tasks_fitness_plot()
    print("\n✓ Figure generated successfully!")
