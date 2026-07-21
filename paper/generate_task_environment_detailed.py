"""
Generate detailed Task Environment Figure with clear grid cell visualization
Shows patterns with actual grid squares and cell counting
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle

def draw_grid_with_cells(ax, pattern, title, difference_pattern=None, show_counts=False):
    """
    Draw grid with actual cell rectangles
    pattern: 10x10 binary array (1 = occupied, 0 = empty)
    difference_pattern: 10x10 binary array showing missed cells (1 = should be filled but isn't)
    """
    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(-0.5, 9.5)
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.set_xticks(range(10))
    ax.set_yticks(range(10))
    ax.set_xticklabels(range(10), fontsize=7)
    ax.set_yticklabels(range(10), fontsize=7)
    ax.grid(True, which='major', color='gray', linewidth=0.5, alpha=0.3)

    # Draw cells
    for i in range(10):
        for j in range(10):
            if difference_pattern is not None and difference_pattern[i, j] == 1:
                # Missed cell - RED with X
                rect = Rectangle((j-0.4, i-0.4), 0.8, 0.8,
                               linewidth=2, edgecolor='red',
                               facecolor='#ffcccc', alpha=0.9)
                ax.add_patch(rect)
                # Add X mark
                ax.plot([j-0.3, j+0.3], [i-0.3, i+0.3], 'r-', linewidth=2)
                ax.plot([j-0.3, j+0.3], [i+0.3, i-0.3], 'r-', linewidth=2)
            elif pattern[i, j] == 1:
                rect = Rectangle((j-0.4, i-0.4), 0.8, 0.8,
                               linewidth=1.5, edgecolor='darkblue',
                               facecolor='lightblue', alpha=0.8)
                ax.add_patch(rect)
            else:
                rect = Rectangle((j-0.4, i-0.4), 0.8, 0.8,
                               linewidth=0.5, edgecolor='lightgray',
                               facecolor='white', alpha=0.3)
                ax.add_patch(rect)

    ax.set_title(title, fontsize=10, fontweight='bold')
    ax.set_xlabel('Column', fontsize=8)
    ax.set_ylabel('Row', fontsize=8)

def create_detailed_task_environment():
    """
    4-panel figure with detailed grid visualization
    """
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(2, 4, hspace=0.4, wspace=0.35)

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

    # Panel A1: L pattern
    ax_a1 = fig.add_subplot(gs[0, 0])
    draw_grid_with_cells(ax_a1, patterns['L'], '(A1) L Pattern\n13 cells')

    # Panel A2: T pattern
    ax_a2 = fig.add_subplot(gs[0, 1])
    draw_grid_with_cells(ax_a2, patterns['T'], '(A2) T Pattern\n12 cells')

    # Panel A3: Plus pattern
    ax_a3 = fig.add_subplot(gs[0, 2])
    draw_grid_with_cells(ax_a3, patterns['Plus'], '(A3) Plus Pattern\n15 cells')

    # Panel A4: Info panel
    ax_a4 = fig.add_subplot(gs[0, 3])
    ax_a4.axis('off')
    info_text = """BASIC PATTERNS

L pattern (13 cells):
• 5 vertical cells (left edge)
• 5 horizontal cells (bottom)
• Shared corner cell

T pattern (12 cells):
• 5 horizontal cells (top)
• 6 vertical cells (middle)
• Shared top-center cell

Plus pattern (15 cells):
• 7 horizontal cells (center)
• 5 vertical cells (center)
• Shared center cell
"""
    ax_a4.text(0.05, 0.95, info_text, transform=ax_a4.transAxes,
              fontsize=8.5, verticalalignment='top', fontfamily='monospace',
              bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # Panel B: Simple task - L alone
    ax_b1 = fig.add_subplot(gs[1, 0])
    target = patterns['L']
    draw_grid_with_cells(ax_b1, target, '(B) Simple Task: L Alone\nTarget (13 cells)')

    # Panel C1: Compositional target (L+T)
    ax_c1 = fig.add_subplot(gs[1, 1])
    target_lt = np.maximum(patterns['L'], patterns['T'])
    draw_grid_with_cells(ax_c1, target_lt, '(C1) L+T Compositional\nTarget Union (25 cells)')

    # Panel C2: Organism response (realistic learning - automatically calculate match)
    ax_c2 = fig.add_subplot(gs[1, 2])

    # Create realistic organism response by modifying target
    organism_lt = target_lt.copy()
    # Organism misses 1 cell from the pattern
    organism_lt[5, 1] = 0  # Missed one cell from L pattern

    # Automatically calculate mismatches: cells in target but not in organism
    missed_cells = np.logical_and(target_lt == 1, organism_lt == 0).astype(int)

    # Calculate fitness
    target_count = np.sum(target_lt)  # Total cells in target = 25
    matched_count = np.sum(np.logical_and(target_lt == 1, organism_lt == 1))  # Cells that match
    fitness_value = matched_count / target_count

    title_str = f'(C2) L+T Organism Response\nMatched {matched_count}/{target_count} = {fitness_value*100:.0f}%'
    draw_grid_with_cells(ax_c2, organism_lt, title_str, difference_pattern=missed_cells)

    # Panel D: Fitness calculation (using actual computed values)
    ax_d = fig.add_subplot(gs[1, 3])
    ax_d.axis('off')

    # Calculate L and T components separately
    l_target = patterns['L']
    t_target = patterns['T']
    l_organism = organism_lt.copy()
    l_organism = np.logical_and(l_organism, l_target).astype(int)  # Only L cells
    t_organism = organism_lt.copy()
    t_organism = np.logical_and(t_organism, t_target).astype(int)  # Only T cells

    l_matched = np.sum(l_organism)
    l_total = np.sum(l_target)
    t_matched = np.sum(t_organism)
    t_total = np.sum(t_target)

    calc_text = f"""FITNESS CALCULATION

Simple Task (L alone):
━━━━━━━━━━━━━━━━━━━━━━
Fitness = Matched / Target
Fitness = 13 / 13 = 1.0 (100%)

Compositional Task (L+T):
━━━━━━━━━━━━━━━━━━━━━━
Union size = {target_count} cells
Matched = {matched_count} cells
Fitness = {matched_count} / {target_count} = {fitness_value:.2f} ({fitness_value*100:.0f}%)

RED X = {target_count - matched_count} cell(s) missed

Component Fitness:
━━━━━━━━━━━━━━━━━━━━━━
L component: {l_matched}/{l_total}
T component: {t_matched}/{t_total}
Overall: {matched_count}/{target_count} = {fitness_value:.2f}
"""
    ax_d.text(0.05, 0.95, calc_text, transform=ax_d.transAxes,
             fontsize=8, verticalalignment='top', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='lightcyan', alpha=0.8))

    plt.suptitle('Task Environment and Fitness Calculation - Detailed Grid View',
                fontsize=14, fontweight='bold', y=0.995)

    plt.savefig('task_environment_detailed.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: task_environment_detailed.png")
    plt.close()


if __name__ == '__main__':
    print("Generating detailed task environment figure with grid cells...\n")
    create_detailed_task_environment()
    print("\n✓ Figure generated successfully!")
    print("Note: Shows actual grid squares so cells can be individually counted")
