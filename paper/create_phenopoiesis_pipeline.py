"""
Create Phenopoiesis Pipeline Figure
Shows: Genome + Epigenome + Learning + Inheritance across 2 generations
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig = plt.figure(figsize=(14, 10))
fig.suptitle('Phenopoiesis Pipeline: Epigenomic Inheritance Across Generations',
             fontsize=16, fontweight='bold', y=0.98)

# Color scheme
genome_color = '#FF6B6B'    # Red for genetic
epigenome_color = '#4ECDC4' # Teal for epigenetic
learning_color = '#FFE66D'  # Yellow for learning
offspring_color = '#95E1D3' # Light teal for inherited

# ===== GENERATION N (Parent) =====
ax1 = plt.subplot(2, 3, 1)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('Generation N: Birth', fontsize=12, fontweight='bold')

# Genome grid
genome_grid = np.random.randint(0, 2, (10, 10))
genome_grid[:5, :] = 0  # Make sparse
genome_grid[2:4, 2:4] = 1

ax1.imshow(genome_grid, cmap='Reds', alpha=0.7, extent=[0.5, 5, 0.5, 5])
ax1.text(2.75, -0.7, 'Genome\n(inherited)', ha='center', fontsize=10, fontweight='bold')

# Epigenome grid (empty at birth)
epigenome_grid = np.zeros((10, 10))
ax1.imshow(epigenome_grid, cmap='Blues', alpha=0.3, extent=[5.5, 10, 0.5, 5])
ax1.text(7.75, -0.7, 'Epigenome\n(empty)', ha='center', fontsize=10, fontweight='bold')

ax1.set_xticks([])
ax1.set_yticks([])

# ===== GENERATION N (Learning) =====
ax2 = plt.subplot(2, 3, 2)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')
ax2.set_title('Generation N: Learning', fontsize=12, fontweight='bold')

# Genome unchanged
ax2.imshow(genome_grid, cmap='Reds', alpha=0.7, extent=[0.5, 5, 0.5, 5])
ax2.text(2.75, -0.7, 'Genome\n(unchanged)', ha='center', fontsize=10, fontweight='bold')

# Epigenome modified by learning
learned_epigenome = np.zeros((10, 10))
# Add learned pattern
learned_epigenome[3:7, 3:7] = 1
learned_epigenome[2:8, 1:3] = 1

ax2.imshow(learned_epigenome, cmap='YlGn', alpha=0.8, extent=[5.5, 10, 0.5, 5])
ax2.text(7.75, -0.7, 'Epigenome\n(learned)', ha='center', fontsize=10, fontweight='bold')

# Learning arrow
arrow = FancyArrowPatch((3, 6.5), (3, 7.5),
                       arrowstyle='->', mutation_scale=30,
                       linewidth=2, color='#FFE66D')
ax2.add_patch(arrow)
ax2.text(3.8, 7, '20 trials', fontsize=9, style='italic', color='#FFE66D')

ax2.set_xticks([])
ax2.set_yticks([])

# ===== GENERATION N (Reproduction) =====
ax3 = plt.subplot(2, 3, 3)
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 10)
ax3.axis('off')
ax3.set_title('Generation N: Reproduction', fontsize=12, fontweight='bold')

# Genome with mutations
mutated_genome = genome_grid.copy()
mutated_genome[5, 5] = 1  # Add mutation
mutated_genome[1, 1] = 0  # Remove bit

ax3.imshow(mutated_genome, cmap='Reds', alpha=0.7, extent=[0.5, 5, 0.5, 5])
ax3.text(2.75, -0.7, 'Genome\n(+ mutations)', ha='center', fontsize=10, fontweight='bold')

# Epigenome: PERFECT COPY
ax3.imshow(learned_epigenome, cmap='YlGn', alpha=0.8, extent=[5.5, 10, 0.5, 5])
ax3.text(7.75, -0.7, 'Epigenome\n(PERFECT COPY)', ha='center', fontsize=10, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='#FFE66D', alpha=0.3))

# Inheritance arrows
arrow1 = FancyArrowPatch((2.75, -0.5), (2.75, -1.5),
                        arrowstyle='->', mutation_scale=25,
                        linewidth=2.5, color='#FF6B6B')
ax3.add_patch(arrow1)

arrow2 = FancyArrowPatch((7.75, -0.5), (7.75, -1.5),
                        arrowstyle='->', mutation_scale=25,
                        linewidth=2.5, color='#4ECDC4')
ax3.add_patch(arrow2)

ax3.set_xticks([])
ax3.set_yticks([])

# ===== GENERATION N+1 (Birth) =====
ax4 = plt.subplot(2, 3, 4)
ax4.set_xlim(0, 10)
ax4.set_ylim(0, 10)
ax4.axis('off')
ax4.set_title('Generation N+1: Birth', fontsize=12, fontweight='bold')

# Inherited genome (with mutations from parent)
ax4.imshow(mutated_genome, cmap='Reds', alpha=0.7, extent=[0.5, 5, 0.5, 5])
ax4.text(2.75, -0.7, 'Genome\n(inherited)', ha='center', fontsize=10, fontweight='bold')

# Inherited epigenome (EXACT COPY from parent)
ax4.imshow(learned_epigenome, cmap='YlGn', alpha=0.8, extent=[5.5, 10, 0.5, 5])
ax4.text(7.75, -0.7, 'Epigenome\n(inherited!)', ha='center', fontsize=10, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='#FFE66D', alpha=0.3))

# Highlight: offspring starts with parent's learned knowledge!
rect = FancyBboxPatch((5, 0), 5, 6, boxstyle="round,pad=0.1",
                      edgecolor='#4ECDC4', facecolor='none', linewidth=3, linestyle='--')
ax4.add_patch(rect)
ax4.text(7.5, 6.8, '← ACCUMULATED KNOWLEDGE', fontsize=9, fontweight='bold',
        ha='center', color='#4ECDC4')

ax4.set_xticks([])
ax4.set_yticks([])

# ===== GENERATION N+1 (Learning) =====
ax5 = plt.subplot(2, 3, 5)
ax5.set_xlim(0, 10)
ax5.set_ylim(0, 10)
ax5.axis('off')
ax5.set_title('Generation N+1: Learning', fontsize=12, fontweight='bold')

# Genome unchanged
ax5.imshow(mutated_genome, cmap='Reds', alpha=0.7, extent=[0.5, 5, 0.5, 5])
ax5.text(2.75, -0.7, 'Genome\n(unchanged)', ha='center', fontsize=10, fontweight='bold')

# Epigenome: inherited + new learning ON TOP
learned_epigenome_gen2 = learned_epigenome.copy()
learned_epigenome_gen2[1:3, 6:9] = 1  # Learn NEW pattern
learned_epigenome_gen2[6:9, 1:3] = 1

ax5.imshow(learned_epigenome_gen2, cmap='YlGn', alpha=0.8, extent=[5.5, 10, 0.5, 5])
ax5.text(7.75, -0.7, 'Epigenome\n(+ new learning)', ha='center', fontsize=10, fontweight='bold')

# Learning arrow
arrow = FancyArrowPatch((8, 6.5), (8, 7.5),
                       arrowstyle='->', mutation_scale=30,
                       linewidth=2, color='#FFE66D')
ax5.add_patch(arrow)
ax5.text(8.8, 7, 'Learn new', fontsize=9, style='italic', color='#FFE66D')

ax5.set_xticks([])
ax5.set_yticks([])

# ===== KEY INSIGHT =====
ax6 = plt.subplot(2, 3, 6)
ax6.set_xlim(0, 10)
ax6.set_ylim(0, 10)
ax6.axis('off')
ax6.set_title('Key Advantage', fontsize=12, fontweight='bold')

# Text summary
texts = [
    "🔴 GENOME: Standard mutation & selection",
    "     (slow genetic change, ~50-100 gens)",
    "",
    "🟢 EPIGENOME: Direct inheritance",
    "     (perfect copy, 100% fidelity)",
    "",
    "💡 RESULT: Knowledge accumulates",
    "     Offspring start with parent's learning",
    "     Can build on it in same generation",
    "",
    "⚡ SPEED: 1 generation (vs 6-7 gens)",
    "     3-6× fitness advantage on",
    "     compositional tasks"
]

y_pos = 9
for text in texts:
    if text == "":
        y_pos -= 0.3
    else:
        ax6.text(0.5, y_pos, text, fontsize=10, verticalalignment='top',
                family='monospace' if '🔴' in text or '🟢' in text or '💡' in text or '⚡' in text else 'sans-serif')
        y_pos -= 0.7

ax6.set_xticks([])
ax6.set_yticks([])

# Add legend at bottom
fig.text(0.5, 0.02,
         'Figure: Phenopoiesis Algorithm Pipeline. Organisms inherit both genome (red, subject to mutation) and epigenome (green, learned and inherited at 100% fidelity). ' +
         'Offspring begin generation with parent\'s accumulated knowledge, enabling rapid learning of compositional tasks.',
         ha='center', fontsize=10, style='italic', wrap=True)

plt.tight_layout(rect=[0, 0.05, 1, 0.96])
plt.savefig('algorithm_pipeline_phenopoiesis.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✅ Saved: algorithm_pipeline_phenopoiesis.png (300 DPI)")
plt.close()

# ===== SECOND FIGURE: Side-by-side comparison =====
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Three Approaches to Evolutionary Learning', fontsize=14, fontweight='bold')

approaches = [
    {
        'name': 'Gene-Centric GA',
        'subtitle': '(Baseline - No Learning)',
        'genome_text': 'Genome\n(static)',
        'epigenome_text': '(none)',
        'process': 'Selection only\nNo inheritance\nof learning',
        'advantage': 'Benchmark',
        'color_genome': '#FF6B6B',
        'color_process': '#CCCCCC'
    },
    {
        'name': 'Baldwin Effect',
        'subtitle': '(Learning + Selection)',
        'genome_text': 'Genome\n(unchanged)',
        'epigenome_text': 'Learning\n(not inherited)',
        'process': 'Selection pressure\nfrom learning\nNo inheritance',
        'advantage': 'Moderate\n(slow)',
        'color_genome': '#FF6B6B',
        'color_process': '#FFE66D'
    },
    {
        'name': 'Phenotype-First',
        'subtitle': '(Learning + Direct Write-back)',
        'genome_text': 'Genome\n(mutated)',
        'epigenome_text': 'Epigenome\n(inherited)',
        'process': 'Direct inheritance\n100% fidelity\n1 generation',
        'advantage': 'POWERFUL\n(3-6×)',
        'color_genome': '#FF6B6B',
        'color_process': '#4ECDC4'
    }
]

for idx, (ax, approach) in enumerate(zip(axes, approaches)):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Title
    ax.text(5, 11.5, approach['name'], ha='center', fontsize=12, fontweight='bold')
    ax.text(5, 11, approach['subtitle'], ha='center', fontsize=9, style='italic', color='gray')

    # Genome box
    rect_genome = FancyBboxPatch((1, 8.5), 8, 1.5, boxstyle="round,pad=0.1",
                                edgecolor=approach['color_genome'], facecolor=approach['color_genome'],
                                alpha=0.3, linewidth=2)
    ax.add_patch(rect_genome)
    ax.text(5, 9.25, approach['genome_text'], ha='center', va='center', fontsize=10, fontweight='bold')

    # Epigenome box
    rect_epi = FancyBboxPatch((1, 6.5), 8, 1.5, boxstyle="round,pad=0.1",
                             edgecolor=approach['color_process'], facecolor=approach['color_process'],
                             alpha=0.3, linewidth=2)
    ax.add_patch(rect_epi)
    ax.text(5, 7.25, approach['epigenome_text'], ha='center', va='center', fontsize=10, fontweight='bold')

    # Process box
    rect_process = FancyBboxPatch((1, 3.5), 8, 2.5, boxstyle="round,pad=0.1",
                                 edgecolor='#333333', facecolor='#F5F5F5',
                                 alpha=0.7, linewidth=2, linestyle='--')
    ax.add_patch(rect_process)
    ax.text(5, 4.75, approach['process'], ha='center', va='center', fontsize=9,
           style='italic', color='#333333')

    # Advantage box
    rect_adv = FancyBboxPatch((1.5, 0.5), 7, 2.5, boxstyle="round,pad=0.1",
                             edgecolor=approach['color_process'], facecolor=approach['color_process'],
                             alpha=0.4, linewidth=2.5)
    ax.add_patch(rect_adv)
    ax.text(5, 1.75, approach['advantage'], ha='center', va='center', fontsize=11, fontweight='bold',
           color=approach['color_process'] if idx == 2 else '#666666')

    # Arrows
    arrow1 = FancyArrowPatch((5, 8.4), (5, 8), arrowstyle='->', mutation_scale=20, linewidth=1.5, color='gray')
    ax.add_patch(arrow1)

    arrow2 = FancyArrowPatch((5, 6.4), (5, 6), arrowstyle='->', mutation_scale=20, linewidth=1.5, color='gray')
    ax.add_patch(arrow2)

plt.tight_layout()
plt.savefig('algorithm_comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✅ Saved: algorithm_comparison.png (300 DPI)")
plt.close()

print("\n✅ Generated 2 pipeline figures:")
print("   1. algorithm_pipeline_phenopoiesis.png - Detailed 2-generation pipeline")
print("   2. algorithm_comparison.png - Side-by-side algorithm comparison")
