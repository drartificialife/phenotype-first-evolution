"""
Generate Task Environment Figure: Task Shapes and Fitness Calculation
Shows L, T, Plus patterns and how fitness is calculated for simple vs compositional tasks
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle

def create_task_shapes_and_fitness():
    """
    4-panel figure:
    (A) Three basic patterns: L, T, Plus
    (B) Simple task example: fitness calculation for L alone
    (C) Compositional task example: L+T union
    (D) Fitness calculation explanation
    """

    fig = plt.figure(figsize=(14, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.3)

    grid_size = 10

    # Define patterns
    patterns = {
        'L': np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
        'T': np.array([[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]),
        'Plus': np.array([[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    }

    # Panel A: Three basic patterns
    ax_a = fig.add_subplot(gs[0, 0])
    combined = np.zeros((10, 30))
    combined[:, 0:10] = patterns['L']
    combined[:, 10:20] = patterns['T']
    combined[:, 20:30] = patterns['Plus']

    ax_a.imshow(combined, cmap='Blues', aspect='auto')
    ax_a.set_xticks([5, 15, 25])
    ax_a.set_xticklabels(['L\n(13 cells)', 'T\n(12 cells)', 'Plus\n(15 cells)'], fontsize=10)
    ax_a.set_yticks([])
    ax_a.set_title('(A) Basic Patterns on 10×10 Grid', fontsize=11, fontweight='bold')

    # Panel B: Simple task - L alone
    ax_b = fig.add_subplot(gs[0, 1])
    target = patterns['L']
    organism = patterns['L'].copy()
    organism[0, 0] = 0  # Organism missed one cell
    organism[7, 0] = 1  # Organism added one extra cell

    combined_simple = np.zeros((10, 20))
    combined_simple[:, 0:10] = target
    combined_simple[:, 10:20] = organism

    ax_b.imshow(combined_simple, cmap='Blues', aspect='auto')
    ax_b.set_xticks([5, 15])
    ax_b.set_xticklabels(['Target L', 'Organism\nActivation'], fontsize=10)
    ax_b.set_yticks([])
    ax_b.set_title('(B) Simple Task: L Alone\nFitness = Matched cells / 13 = 11/13 = 85%',
                  fontsize=11, fontweight='bold')

    # Panel C: Compositional task - L+T
    ax_c = fig.add_subplot(gs[1, 0])
    target_lt = np.maximum(patterns['L'], patterns['T'])  # Union
    organism_lt = target_lt.copy()
    organism_lt[3, 4] = 0  # Missed one cell from T

    combined_comp = np.zeros((10, 20))
    combined_comp[:, 0:10] = target_lt
    combined_comp[:, 10:20] = organism_lt

    ax_c.imshow(combined_comp, cmap='Blues', aspect='auto')
    ax_c.set_xticks([5, 15])
    ax_c.set_xticklabels(['Target L+T\n(Union)', 'Organism\nActivation'], fontsize=10)
    ax_c.set_yticks([])
    ax_c.set_title('(C) Compositional Task: L+T\nFitness = Matched cells / 25 = 24/25 = 96%',
                  fontsize=11, fontweight='bold')

    # Panel D: Fitness calculation explanation
    ax_d = fig.add_subplot(gs[1, 1])
    ax_d.axis('off')

    text_content = """
FITNESS CALCULATION

Simple Tasks (L alone, T alone, Plus alone):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fitness = # cells matched / # cells in pattern
• L alone: 13 target cells
• T alone: 12 target cells
• Plus alone: 15 target cells
Maximum fitness: 1.0 (perfect match)

Compositional Tasks (L+T, T+Plus, L+Plus):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fitness = # cells matched / # cells in union
• L+T: Union = 25 cells (L + T - overlap)
• T+Plus: Union = 27 cells
• L+Plus: Union = 28 cells
  (cells overlap; perfect 1.0 hard to achieve)

Component Fitness (Compositional Only):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
L component = matched L cells / 13
T component = matched T cells / 12
Plus component = matched Plus cells / 15
"""

    ax_d.text(0.05, 0.95, text_content, transform=ax_d.transAxes,
             fontsize=9.5, verticalalignment='top', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.savefig('task_environment_fitness.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: task_environment_fitness.png")
    plt.close()


if __name__ == '__main__':
    print("Generating task environment and fitness calculation figure...\n")
    create_task_shapes_and_fitness()
    print("\n✓ Figure generated successfully!")
