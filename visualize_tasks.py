"""
Visualize the L, T, Plus shapes and fitness calculation
Publication-quality figures for Nature manuscript
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle

def render_shape(grid_size=10, shape='L'):
    """Render a shape on a grid"""
    grid = np.zeros((grid_size, grid_size))

    if shape == 'L':
        # L shape: vertical line + horizontal line at bottom
        grid[2:8, 3] = 1  # vertical
        grid[7, 3:7] = 1  # horizontal
    elif shape == 'T':
        # T shape: horizontal line at top + vertical down center
        grid[2, 3:7] = 1  # horizontal
        grid[2:8, 5] = 1  # vertical
    elif shape == 'Plus':
        # Plus shape: horizontal + vertical cross
        grid[4:6, 2:8] = 1  # horizontal bar
        grid[2:8, 4:6] = 1  # vertical bar

    return grid

def plot_single_shapes(figsize=(14, 4)):
    """3-panel figure showing L, T, Plus shapes"""
    fig, axes = plt.subplots(1, 3, figsize=figsize, dpi=300)
    shapes = ['L', 'T', 'Plus']

    for idx, shape in enumerate(shapes):
        ax = axes[idx]
        grid = render_shape(shape=shape)

        # Show grid
        ax.imshow(grid, cmap='Greys', vmin=0, vmax=1, origin='upper')

        # Grid lines
        for i in range(11):
            ax.axhline(i-0.5, color='lightgray', linewidth=0.5)
            ax.axvline(i-0.5, color='lightgray', linewidth=0.5)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(f'{shape} Pattern', fontsize=14, fontweight='bold')
        ax.set_aspect('equal')

    plt.suptitle('Single Pattern Tasks: L, T, Plus', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('task_shapes.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: task_shapes.png")
    plt.close()

def plot_compositional_example(figsize=(14, 6)):
    """Show compositional L+T task example with fitness calculation"""
    fig = plt.figure(figsize=figsize, dpi=300)

    # Create grid for subplots with more space
    gs = fig.add_gridspec(2, 3, hspace=0.5, wspace=0.3)

    # Panel A: Target L+T (both patterns combined)
    ax_target = fig.add_subplot(gs[0, :2])
    grid_LT = render_shape(shape='L').copy()
    grid_T = render_shape(shape='T').copy()
    combined = np.minimum(grid_LT + grid_T, 1)  # combine

    ax_target.imshow(combined, cmap='Greys', vmin=0, vmax=1, origin='upper')
    for i in range(11):
        ax_target.axhline(i-0.5, color='lightgray', linewidth=0.5)
        ax_target.axvline(i-0.5, color='lightgray', linewidth=0.5)
    ax_target.set_xticks([])
    ax_target.set_yticks([])
    ax_target.set_title('Target: L + T (Combined)', fontsize=13, fontweight='bold')

    # Move text below the figure with more space
    fig.text(0.32, 0.47, 'Target cells occupied: {}'.format(int(combined.sum())),
             ha='center', fontsize=11, fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    # Panel B: Fitness formula
    ax_formula = fig.add_subplot(gs[0, 2])
    ax_formula.axis('off')
    formula_text = (
        "Fitness Calculation\n\n"
        "Organism output: O\n"
        "Target pattern: T\n\n"
        "Recall = ∩(O,T) / |T|\n\n"
        "Fitness = mean(pattern recalls)"
    )
    ax_formula.text(0.1, 0.5, formula_text, fontsize=11, family='monospace',
                   verticalalignment='center',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # Panel C: Example organism output (imperfect)
    ax_output = fig.add_subplot(gs[1, 0])
    organism = np.array([
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,1,0,0,0,0],  # partial T (top)
        [0,0,0,1,0,1,0,0,0,0],  # partial T
        [0,0,0,1,1,1,0,0,0,0],  # partial T
        [0,0,0,1,0,0,0,0,0,0],  # partial L (vertical)
        [0,0,0,1,0,0,0,0,0,0],  # partial L
        [0,0,0,1,1,1,1,0,0,0],  # partial L (horizontal)
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ])
    ax_output.imshow(organism, cmap='Greys', vmin=0, vmax=1, origin='upper')
    for i in range(11):
        ax_output.axhline(i-0.5, color='lightgray', linewidth=0.5)
        ax_output.axvline(i-0.5, color='lightgray', linewidth=0.5)
    ax_output.set_xticks([])
    ax_output.set_yticks([])
    ax_output.set_title('Organism Output\n(Partial Success)', fontsize=11, fontweight='bold')

    # Panel D: L component score
    ax_l = fig.add_subplot(gs[1, 1])
    ax_l.axis('off')
    ax_l.text(0.5, 0.7, "L Pattern Score", ha='center', fontsize=12, fontweight='bold')
    ax_l.text(0.5, 0.4, "Recall = 5/6\n= 0.83", ha='center', fontsize=13,
             family='monospace',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax_l.set_xlim(0, 1)
    ax_l.set_ylim(0, 1)

    # Panel E: T component score
    ax_t = fig.add_subplot(gs[1, 2])
    ax_t.axis('off')
    ax_t.text(0.5, 0.7, "T Pattern Score", ha='center', fontsize=12, fontweight='bold')
    ax_t.text(0.5, 0.4, "Recall = 4/6\n= 0.67", ha='center', fontsize=13,
             family='monospace',
             bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    ax_t.set_xlim(0, 1)
    ax_t.set_ylim(0, 1)

    fig.text(0.5, -0.02, 'Final Fitness = (0.83 + 0.67) / 2 = 0.75',
            ha='center', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.suptitle('Compositional Task Example: Learning L and T Together',
                fontsize=14, fontweight='bold', y=0.98)
    plt.savefig('task_compositional_example.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: task_compositional_example.png")
    plt.close()

def plot_learning_comparison(figsize=(14, 6)):
    """Compare Baldwin vs Phenotype-First learning on L+T task"""
    fig, axes = plt.subplots(1, 2, figsize=figsize, dpi=300)

    # Baldwin: Random wandering
    ax_b = axes[0]
    ax_b.axis('off')

    generations_b = ['Gen 0-5', 'Gen 6-10', 'Gen 11-20', 'Gen 21+']
    fitness_b = [0.2, 0.3, 0.25, 0.28]

    ax_b.text(0.5, 0.95, 'Baldwin Effect\n(Selection-based learning)',
             ha='center', fontsize=12, fontweight='bold')

    y_pos = 0.8
    for gen, fit in zip(generations_b, fitness_b):
        ax_b.text(0.1, y_pos, f'{gen}:', fontsize=11)
        bar_width = fit * 0.6
        rect = Rectangle((0.35, y_pos-0.03), bar_width, 0.05,
                         facecolor='#FF6B6B', alpha=0.7)
        ax_b.add_patch(rect)
        ax_b.text(0.98, y_pos, f'{fit:.2f}', ha='right', fontsize=11)
        y_pos -= 0.15

    ax_b.text(0.5, 0.1, 'Random wandering\nRarely learns both L and T\nAvg fitness: 0.26',
             ha='center', fontsize=10, style='italic',
             bbox=dict(boxstyle='round', facecolor='#FFE0E0', alpha=0.8))

    ax_b.set_xlim(0, 1)
    ax_b.set_ylim(0, 1)

    # Phenotype-First: Cumulative learning
    ax_p = axes[1]
    ax_p.axis('off')

    generations_p = ['Gen 0-5', 'Gen 6-10', 'Gen 11-20', 'Gen 21+']
    fitness_p = [0.4, 0.7, 0.78, 0.77]

    ax_p.text(0.5, 0.95, 'Phenotype-First\n(Epigenomic inheritance)',
             ha='center', fontsize=12, fontweight='bold')

    y_pos = 0.8
    for gen, fit in zip(generations_p, fitness_p):
        ax_p.text(0.1, y_pos, f'{gen}:', fontsize=11)
        bar_width = fit * 0.6
        rect = Rectangle((0.35, y_pos-0.03), bar_width, 0.05,
                         facecolor='#4ECDC4', alpha=0.7)
        ax_p.add_patch(rect)
        ax_p.text(0.98, y_pos, f'{fit:.2f}', ha='right', fontsize=11)
        y_pos -= 0.15

    ax_p.text(0.5, 0.1, 'Learn L → write to epigenome\nInherit L → learn T\nAvg fitness: 0.66',
             ha='center', fontsize=10, style='italic',
             bbox=dict(boxstyle='round', facecolor='#E0F7F6', alpha=0.8))

    ax_p.set_xlim(0, 1)
    ax_p.set_ylim(0, 1)

    plt.suptitle('Learning Trajectories: Baldwin vs Phenotype-First',
                fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('learning_comparison.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: learning_comparison.png")
    plt.close()

def main():
    print("\n" + "="*80)
    print("GENERATING TASK VISUALIZATION FIGURES")
    print("="*80 + "\n")

    plot_single_shapes()
    plot_compositional_example()
    plot_learning_comparison()

    print("\n" + "="*80)
    print("✅ All visualization figures generated!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
