"""
Create algorithm pipeline figure for Phenotype-First (Phenopoiesis)
Shows the flow of learning and inheritance through generations
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

def create_phenopoiesis_pipeline():
    """Create visual pipeline of phenotype-first learning and inheritance"""
    fig, ax = plt.subplots(figsize=(14, 10), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Title
    fig.text(0.5, 0.98, 'Phenopoiesis: Direct Epigenomic Inheritance Pipeline',
             ha='center', fontsize=16, fontweight='bold')
    fig.text(0.5, 0.95, 'How organisms compose their own evolution through learned patterns',
             ha='center', fontsize=12, style='italic')

    # Color scheme
    color_genome = '#FFE0E0'
    color_epigenome = '#E0F0FF'
    color_learning = '#E0FFE0'
    color_inheritance = '#FFF0E0'

    # ═══════════════════════════════════════════════════════════════════
    # GENERATION 0: Initial organism
    # ═══════════════════════════════════════════════════════════════════
    y_start = 10.5

    # Gen 0 label
    ax.text(0.5, y_start + 0.5, 'GENERATION 0', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))

    # Genome box
    genome_box_0 = FancyBboxPatch((0.2, y_start - 0.8), 1.5, 1,
                                   boxstyle="round,pad=0.1",
                                   edgecolor='black', facecolor=color_genome, linewidth=2)
    ax.add_patch(genome_box_0)
    ax.text(0.95, y_start - 0.3, 'Genome\n(Random)', ha='center', va='center',
            fontsize=10, fontweight='bold')

    # Epigenome box (empty)
    epigenome_box_0 = FancyBboxPatch((2.2, y_start - 0.8), 1.5, 1,
                                      boxstyle="round,pad=0.1",
                                      edgecolor='black', facecolor=color_epigenome,
                                      linewidth=2, linestyle='--')
    ax.add_patch(epigenome_box_0)
    ax.text(2.95, y_start - 0.3, 'Epigenome\n(Empty)', ha='center', va='center',
            fontsize=10, fontweight='bold')

    # Arrow: Learning
    arrow_learn_0 = FancyArrowPatch((0.95, y_start - 0.9), (0.95, y_start - 1.8),
                                    arrowstyle='->', mutation_scale=30, linewidth=2.5,
                                    color='green')
    ax.add_patch(arrow_learn_0)
    ax.text(1.8, y_start - 1.35, 'LEARNING\n(20 trials)', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=color_learning, alpha=0.8))

    # ═══════════════════════════════════════════════════════════════════
    # GENERATION 0: After learning
    # ═══════════════════════════════════════════════════════════════════
    y_learn = y_start - 2.3

    # Genome (unchanged)
    genome_box_0l = FancyBboxPatch((0.2, y_learn - 0.8), 1.5, 1,
                                    boxstyle="round,pad=0.1",
                                    edgecolor='black', facecolor=color_genome, linewidth=2)
    ax.add_patch(genome_box_0l)
    ax.text(0.95, y_learn - 0.3, 'Genome\n(Unchanged)', ha='center', va='center',
            fontsize=10, fontweight='bold')

    # Epigenome (learned L pattern)
    epigenome_box_0l = FancyBboxPatch((2.2, y_learn - 0.8), 1.5, 1,
                                       boxstyle="round,pad=0.1",
                                       edgecolor='darkblue', facecolor=color_epigenome,
                                       linewidth=2.5)
    ax.add_patch(epigenome_box_0l)
    ax.text(2.95, y_learn - 0.3, 'Epigenome\n(Learned L)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='darkblue')

    # Phenotype (genome ∪ epigenome)
    phenotype_box_0 = FancyBboxPatch((4.2, y_learn - 0.8), 1.5, 1,
                                      boxstyle="round,pad=0.1",
                                      edgecolor='darkgreen', facecolor='#FFFFCC',
                                      linewidth=2.5)
    ax.add_patch(phenotype_box_0)
    ax.text(4.95, y_learn - 0.3, 'Phenotype\n(G ∪ E = L)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='darkgreen')

    # Arrows
    arrow_g_to_p = FancyArrowPatch((1.7, y_learn - 0.3), (4.2, y_learn - 0.3),
                                   arrowstyle='->', mutation_scale=20, linewidth=1.5,
                                   color='gray', linestyle=':')
    ax.add_patch(arrow_g_to_p)
    arrow_e_to_p = FancyArrowPatch((3.7, y_learn - 0.3), (4.2, y_learn - 0.3),
                                   arrowstyle='->', mutation_scale=20, linewidth=1.5,
                                   color='gray', linestyle=':')
    ax.add_patch(arrow_e_to_p)

    # Selection box
    fitness_box_0 = FancyBboxPatch((4.2, y_learn - 1.8), 1.5, 0.8,
                                    boxstyle="round,pad=0.05",
                                    edgecolor='red', facecolor='#FFE0E0', linewidth=2)
    ax.add_patch(fitness_box_0)
    ax.text(4.95, y_learn - 1.4, 'Fitness\n(L learned)', ha='center', va='center',
            fontsize=9, fontweight='bold')

    arrow_pheno_to_fit = FancyArrowPatch((4.95, y_learn - 0.8), (4.95, y_learn - 1.0),
                                        arrowstyle='->', mutation_scale=15, linewidth=1.5,
                                        color='red')
    ax.add_patch(arrow_pheno_to_fit)

    # Arrow: Selection & Inheritance
    arrow_inherit_0 = FancyArrowPatch((4.95, y_learn - 1.8), (4.95, y_learn - 2.7),
                                      arrowstyle='->', mutation_scale=30, linewidth=2.5,
                                      color='#FF8800')
    ax.add_patch(arrow_inherit_0)
    ax.text(6.2, y_learn - 2.25, 'INHERITANCE\n(Direct copy of\nepigenome)',
            fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=color_inheritance, alpha=0.8))

    # ═══════════════════════════════════════════════════════════════════
    # GENERATION 1: Inherited state
    # ═══════════════════════════════════════════════════════════════════
    y_gen1 = y_learn - 3.5

    # Gen 1 label
    ax.text(0.5, y_gen1 + 0.5, 'GENERATION 1', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))

    # Genome (slightly mutated)
    genome_box_1 = FancyBboxPatch((0.2, y_gen1 - 0.8), 1.5, 1,
                                   boxstyle="round,pad=0.1",
                                   edgecolor='black', facecolor=color_genome, linewidth=2)
    ax.add_patch(genome_box_1)
    ax.text(0.95, y_gen1 - 0.3, 'Genome\n(Mutated)', ha='center', va='center',
            fontsize=10, fontweight='bold')

    # Epigenome (INHERITED L!)
    epigenome_box_1 = FancyBboxPatch((2.2, y_gen1 - 0.8), 1.5, 1,
                                      boxstyle="round,pad=0.1",
                                      edgecolor='darkblue', facecolor=color_epigenome,
                                      linewidth=2.5)
    ax.add_patch(epigenome_box_1)
    ax.text(2.95, y_gen1 - 0.3, 'Epigenome\n(Inherited L)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='darkblue')

    # Phenotype includes inherited L
    phenotype_box_1 = FancyBboxPatch((4.2, y_gen1 - 0.8), 1.5, 1,
                                      boxstyle="round,pad=0.1",
                                      edgecolor='darkgreen', facecolor='#FFFFCC',
                                      linewidth=2.5)
    ax.add_patch(phenotype_box_1)
    ax.text(4.95, y_gen1 - 0.3, 'Phenotype\n(G ∪ E = L)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='darkgreen')

    # Arrows to phenotype
    arrow_g_to_p1 = FancyArrowPatch((1.7, y_gen1 - 0.3), (4.2, y_gen1 - 0.3),
                                    arrowstyle='->', mutation_scale=20, linewidth=1.5,
                                    color='gray', linestyle=':')
    ax.add_patch(arrow_g_to_p1)
    arrow_e_to_p1 = FancyArrowPatch((3.7, y_gen1 - 0.3), (4.2, y_gen1 - 0.3),
                                    arrowstyle='->', mutation_scale=20, linewidth=1.5,
                                    color='gray', linestyle=':')
    ax.add_patch(arrow_e_to_p1)

    # Arrow: NEW learning on top of inherited L
    arrow_learn_1 = FancyArrowPatch((0.95, y_gen1 - 0.9), (0.95, y_gen1 - 1.8),
                                    arrowstyle='->', mutation_scale=30, linewidth=2.5,
                                    color='green')
    ax.add_patch(arrow_learn_1)
    ax.text(1.8, y_gen1 - 1.35, 'LEARNING\n(Learn T on top\nof inherited L)',
            fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor=color_learning, alpha=0.8))

    # ═══════════════════════════════════════════════════════════════════
    # GENERATION 1: After learning (combined L+T)
    # ═══════════════════════════════════════════════════════════════════
    y_gen1_learn = y_gen1 - 2.3

    # Genome (unchanged again)
    genome_box_1l = FancyBboxPatch((0.2, y_gen1_learn - 0.8), 1.5, 1,
                                    boxstyle="round,pad=0.1",
                                    edgecolor='black', facecolor=color_genome, linewidth=2)
    ax.add_patch(genome_box_1l)
    ax.text(0.95, y_gen1_learn - 0.3, 'Genome\n(Still Unchanged)', ha='center', va='center',
            fontsize=10, fontweight='bold')

    # Epigenome (NOW has both L and T!)
    epigenome_box_1l = FancyBboxPatch((2.2, y_gen1_learn - 0.8), 1.5, 1,
                                       boxstyle="round,pad=0.1",
                                       edgecolor='darkblue', facecolor='#0066FF',
                                       linewidth=2.5)
    ax.add_patch(epigenome_box_1l)
    ax.text(2.95, y_gen1_learn - 0.3, 'Epigenome\n(L + T)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # Phenotype (COMBINED L+T!)
    phenotype_box_1l = FancyBboxPatch((4.2, y_gen1_learn - 0.8), 1.5, 1,
                                       boxstyle="round,pad=0.1",
                                       edgecolor='darkgreen', facecolor='#00FF00',
                                       linewidth=2.5)
    ax.add_patch(phenotype_box_1l)
    ax.text(4.95, y_gen1_learn - 0.3, 'Phenotype\n(L + T!)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='darkgreen')

    # Arrows
    arrow_g_to_p1l = FancyArrowPatch((1.7, y_gen1_learn - 0.3), (4.2, y_gen1_learn - 0.3),
                                     arrowstyle='->', mutation_scale=20, linewidth=1.5,
                                     color='gray', linestyle=':')
    ax.add_patch(arrow_g_to_p1l)
    arrow_e_to_p1l = FancyArrowPatch((3.7, y_gen1_learn - 0.3), (4.2, y_gen1_learn - 0.3),
                                     arrowstyle='->', mutation_scale=20, linewidth=1.5,
                                     color='gray', linestyle=':')
    ax.add_patch(arrow_e_to_p1l)

    # Fitness
    fitness_box_1 = FancyBboxPatch((4.2, y_gen1_learn - 1.8), 1.5, 0.8,
                                    boxstyle="round,pad=0.05",
                                    edgecolor='darkgreen', facecolor='#E0FFE0', linewidth=2)
    ax.add_patch(fitness_box_1)
    ax.text(4.95, y_gen1_learn - 1.4, 'Fitness\n(L + T!)', ha='center', va='center',
            fontsize=9, fontweight='bold', color='darkgreen')

    arrow_pheno_to_fit1 = FancyArrowPatch((4.95, y_gen1_learn - 0.8), (4.95, y_gen1_learn - 1.0),
                                         arrowstyle='->', mutation_scale=15, linewidth=1.5,
                                         color='darkgreen')
    ax.add_patch(arrow_pheno_to_fit1)

    # ═══════════════════════════════════════════════════════════════════
    # Summary box
    # ═══════════════════════════════════════════════════════════════════
    summary_y = 0.8
    summary_text = (
        "KEY INSIGHT: Phenopoiesis (Organism Composing Evolution)\n\n"
        "Generation 0: Learn L → write to epigenome → fitness improved\n"
        "Generation 1: INHERIT L → learn T on top → combine both → even higher fitness\n"
        "Generation 2+: Have L+T inherited → continue refining or learn new patterns\n\n"
        "Advantage: Cumulative, compositional learning. Each generation builds on parent's knowledge.\n"
        "NOT selection reshaping genes (slow, 50-100 gens). NOT learning starting from scratch each gen.\n"
        "DIRECT: Organism writes learned patterns to epigenome → offspring inherit → accelerated adaptation."
    )

    ax.text(0.5, summary_y, summary_text, ha='center', va='center', fontsize=9.5,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, pad=1),
            family='monospace', transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig('algorithm_pipeline_phenopoiesis.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: algorithm_pipeline_phenopoiesis.png")
    plt.close()

def create_algorithm_comparison():
    """Create comparison of all 4 algorithms"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12), dpi=300)
    fig.suptitle('Four Evolutionary Algorithms: Mechanism Comparison',
                 fontsize=16, fontweight='bold', y=0.98)

    algorithms = [
        {
            'name': 'Gene-Centric (Baseline)',
            'ax': axes[0, 0],
            'color': '#CCCCCC',
            'description': (
                'No Learning | No Inheritance\n\n'
                'Pure mutation only:\n'
                '• Genome → random mutation\n'
                '• No learning trials\n'
                '• No inheritance structure\n\n'
                'Result: Baseline performance\n'
                'Learning essential? YES'
            )
        },
        {
            'name': 'Baldwin Effect',
            'ax': axes[0, 1],
            'color': '#FF6B6B',
            'description': (
                'Learning Without Inheritance\n\n'
                'Selection-based evolution:\n'
                '• Each organism learns (20 trials)\n'
                '• Good learners selected for breeding\n'
                '• Offspring get genome only (no learned knowledge)\n'
                '• Must learn from scratch\n\n'
                'Result: Learning works but slow\n'
                'Inheritance mechanism: Selection pressure (50-100 gens)'
            )
        },
        {
            'name': 'Lamarckian GA',
            'ax': axes[1, 0],
            'color': '#FFB347',
            'description': (
                'Slow Genetic Assimilation\n\n'
                'Learned patterns slowly encode genes:\n'
                '• Organisms learn (20 trials)\n'
                '• 15% of learned info encodes per generation\n'
                '• Offspring inherit partially-encoded genes\n'
                '• Full encoding takes ~6-7 generations\n\n'
                'Result: Faster than Baldwin, slower than write-back\n'
                'Inheritance mechanism: Genetic assimilation (slow encoding)'
            )
        },
        {
            'name': 'Phenotype-First (Phenopoiesis)',
            'ax': axes[1, 1],
            'color': '#4ECDC4',
            'description': (
                'Direct Epigenomic Inheritance\n\n'
                'Organisms compose their evolution:\n'
                '• Organism learns (modifies epigenome)\n'
                '• 100% fidelity copy to offspring\n'
                '• Offspring inherit learned patterns immediately\n'
                '• Can learn NEW patterns on top\n\n'
                'Result: FAST, compositional learning\n'
                'Inheritance mechanism: Direct copy (1 generation)'
            )
        }
    ]

    for algo in algorithms:
        ax = algo['ax']
        ax.axis('off')

        # Title box
        title_box = FancyBboxPatch((0.05, 0.85), 0.9, 0.12,
                                    boxstyle="round,pad=0.02",
                                    edgecolor='black', facecolor=algo['color'],
                                    linewidth=2, transform=ax.transAxes)
        ax.add_patch(title_box)
        ax.text(0.5, 0.91, algo['name'], ha='center', va='center',
               fontsize=13, fontweight='bold', transform=ax.transAxes)

        # Description
        ax.text(0.5, 0.45, algo['description'], ha='center', va='center',
               fontsize=10, family='monospace', transform=ax.transAxes,
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.9, pad=0.5))

    plt.tight_layout()
    plt.savefig('algorithm_comparison.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: algorithm_comparison.png")
    plt.close()

if __name__ == "__main__":
    print("\n" + "="*80)
    print("GENERATING ALGORITHM PIPELINE FIGURES")
    print("="*80 + "\n")

    create_phenopoiesis_pipeline()
    create_algorithm_comparison()

    print("\n" + "="*80)
    print("✅ Algorithm pipeline figures generated!")
    print("="*80 + "\n")
