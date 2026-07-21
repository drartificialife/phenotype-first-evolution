#!/usr/bin/env python3
"""
Create publication-quality plots for Evolutionary Algorithms Paper
"""

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 11


def load_data():
    """Load experiment results"""
    results = []
    with open('experiment_results_detailed.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append({
                'method': row['method'],
                'shape': row['shape'],
                'run': int(row['run']),
                'fitness': float(row['fitness']),
                'convergence_gen': float(row['convergence_gen']),
            })

    return pd.DataFrame(results)


def plot_fitness_by_method(df):
    """Box plot of fitness by method"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Fitness Comparison Across Methods', fontsize=14, fontweight='bold')

    shapes = sorted(df['shape'].unique())
    methods = sorted(df['method'].unique())

    for idx, shape in enumerate(shapes):
        shape_data = df[df['shape'] == shape]

        # Box plot
        sns.boxplot(data=shape_data, x='method', y='fitness', ax=axes[idx],
                   palette='Set2', width=0.6)

        # Strip plot for individual points
        sns.stripplot(data=shape_data, x='method', y='fitness', ax=axes[idx],
                     color='black', alpha=0.3, size=4)

        axes[idx].set_title(f'{shape}-Shape', fontweight='bold')
        axes[idx].set_xlabel('Method')
        axes[idx].set_ylabel('Fitness' if idx == 0 else '')
        axes[idx].set_ylim(-0.05, 1.15)
        axes[idx].axhline(y=1.0, color='red', linestyle='--', alpha=0.3, label='Perfect')
        axes[idx].tick_params(axis='x', rotation=45)

        # Add mean line
        means = shape_data.groupby('method')['fitness'].mean().sort_index()
        positions = range(len(methods))
        axes[idx].plot(positions, [means.get(m, 0) for m in methods],
                      'o-', color='red', alpha=0.7, linewidth=2, markersize=8, label='Mean')

    plt.tight_layout()
    plt.savefig('plot_fitness_by_method.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: plot_fitness_by_method.png")
    plt.close()


def plot_convergence_by_method(df):
    """Box plot of convergence generations by method"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Convergence Speed Comparison (Generations to 95% Fitness)',
                fontsize=14, fontweight='bold')

    shapes = sorted(df['shape'].unique())
    methods = sorted(df['method'].unique())

    for idx, shape in enumerate(shapes):
        shape_data = df[df['shape'] == shape]

        # Box plot
        sns.boxplot(data=shape_data, x='method', y='convergence_gen', ax=axes[idx],
                   palette='Set2', width=0.6)

        # Strip plot
        sns.stripplot(data=shape_data, x='method', y='convergence_gen', ax=axes[idx],
                     color='black', alpha=0.3, size=4)

        axes[idx].set_title(f'{shape}-Shape', fontweight='bold')
        axes[idx].set_xlabel('Method')
        axes[idx].set_ylabel('Generations' if idx == 0 else '')
        axes[idx].tick_params(axis='x', rotation=45)

        # Add mean line
        means = shape_data.groupby('method')['convergence_gen'].mean().sort_index()
        positions = range(len(methods))
        axes[idx].plot(positions, [means.get(m, 0) for m in methods],
                      'o-', color='darkred', alpha=0.7, linewidth=2, markersize=8, label='Mean')

    plt.tight_layout()
    plt.savefig('plot_convergence_by_method.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: plot_convergence_by_method.png")
    plt.close()


def plot_violin_fitness(df):
    """Violin plot for fitness distribution"""
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.violinplot(data=df, x='shape', y='fitness', hue='method', ax=ax, split=False)

    ax.set_title('Fitness Distribution by Method and Shape', fontsize=14, fontweight='bold')
    ax.set_xlabel('Target Shape', fontsize=12)
    ax.set_ylabel('Fitness', fontsize=12)
    ax.set_ylim(-0.05, 1.15)
    ax.axhline(y=1.0, color='red', linestyle='--', alpha=0.3, label='Perfect')
    ax.legend(title='Method', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.savefig('plot_violin_fitness.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: plot_violin_fitness.png")
    plt.close()


def plot_violin_convergence(df):
    """Violin plot for convergence distribution"""
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.violinplot(data=df, x='shape', y='convergence_gen', hue='method', ax=ax, split=False)

    ax.set_title('Convergence Distribution by Method and Shape', fontsize=14, fontweight='bold')
    ax.set_xlabel('Target Shape', fontsize=12)
    ax.set_ylabel('Generations to 95% Fitness', fontsize=12)
    ax.legend(title='Method', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.savefig('plot_violin_convergence.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: plot_violin_convergence.png")
    plt.close()


def plot_mean_comparison(df):
    """Bar plot of mean fitness and convergence"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('Mean Performance Comparison', fontsize=14, fontweight='bold')

    methods = sorted(df['method'].unique())
    shapes = sorted(df['shape'].unique())

    # Fitness plot
    fitness_data = df.groupby('method')['fitness'].agg(['mean', 'std']).reindex(methods)
    x_pos = np.arange(len(methods))

    axes[0].bar(x_pos, fitness_data['mean'], yerr=fitness_data['std'],
               capsize=5, alpha=0.7, color=sns.color_palette('husl', len(methods)))
    axes[0].set_xlabel('Method', fontsize=12)
    axes[0].set_ylabel('Mean Fitness', fontsize=12)
    axes[0].set_title('Mean Fitness Across All Runs', fontweight='bold')
    axes[0].set_xticks(x_pos)
    axes[0].set_xticklabels(methods, rotation=45, ha='right')
    axes[0].set_ylim(0, 1.1)
    axes[0].axhline(y=1.0, color='red', linestyle='--', alpha=0.3)

    # Convergence plot
    conv_data = df.groupby('method')['convergence_gen'].agg(['mean', 'std']).reindex(methods)

    axes[1].bar(x_pos, conv_data['mean'], yerr=conv_data['std'],
               capsize=5, alpha=0.7, color=sns.color_palette('husl', len(methods)))
    axes[1].set_xlabel('Method', fontsize=12)
    axes[1].set_ylabel('Mean Generations', fontsize=12)
    axes[1].set_title('Mean Convergence Speed Across All Runs', fontweight='bold')
    axes[1].set_xticks(x_pos)
    axes[1].set_xticklabels(methods, rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig('plot_mean_comparison.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: plot_mean_comparison.png")
    plt.close()


def plot_scatter_fitness_vs_convergence(df):
    """Scatter plot showing tradeoff between fitness and convergence"""
    fig, ax = plt.subplots(figsize=(10, 8))

    methods = sorted(df['method'].unique())
    colors = sns.color_palette('husl', len(methods))
    method_colors = {method: colors[i] for i, method in enumerate(methods)}

    for method in methods:
        method_data = df[df['method'] == method]
        ax.scatter(method_data['convergence_gen'], method_data['fitness'],
                  label=method, alpha=0.6, s=80, color=method_colors[method])

    ax.set_xlabel('Convergence Generations (to 95% fitness)', fontsize=12)
    ax.set_ylabel('Final Fitness', fontsize=12)
    ax.set_title('Fitness-Convergence Tradeoff', fontsize=14, fontweight='bold')
    ax.legend(title='Method', loc='best', fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-0.05, 1.15)

    plt.tight_layout()
    plt.savefig('plot_fitness_vs_convergence.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: plot_fitness_vs_convergence.png")
    plt.close()


def plot_heatmap_fitness(df):
    """Heatmap of mean fitness by method and shape"""
    # Create pivot table
    pivot_data = df.pivot_table(values='fitness', index='method', columns='shape', aggfunc='mean')

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(pivot_data, annot=True, fmt='.3f', cmap='RdYlGn', vmin=0, vmax=1,
               cbar_kws={'label': 'Fitness'}, ax=ax, linewidths=0.5)

    ax.set_title('Mean Fitness Heatmap (Method × Shape)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Target Shape', fontsize=12)
    ax.set_ylabel('Method', fontsize=12)

    plt.tight_layout()
    plt.savefig('plot_heatmap_fitness.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: plot_heatmap_fitness.png")
    plt.close()


def plot_heatmap_convergence(df):
    """Heatmap of mean convergence by method and shape"""
    pivot_data = df.pivot_table(values='convergence_gen', index='method', columns='shape', aggfunc='mean')

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(pivot_data, annot=True, fmt='.1f', cmap='YlOrRd_r',
               cbar_kws={'label': 'Generations'}, ax=ax, linewidths=0.5)

    ax.set_title('Mean Convergence Heatmap (Method × Shape)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Target Shape', fontsize=12)
    ax.set_ylabel('Method', fontsize=12)

    plt.tight_layout()
    plt.savefig('plot_heatmap_convergence.png', dpi=300, bbox_inches='tight')
    print("✅ Saved: plot_heatmap_convergence.png")
    plt.close()


def main():
    print("\n" + "="*80)
    print("CREATING PUBLICATION-QUALITY PLOTS")
    print("="*80 + "\n")

    # Load data
    df = load_data()
    print(f"Loaded {len(df)} results from 30 runs × 4 methods × 3 shapes\n")

    # Create plots
    plot_fitness_by_method(df)
    plot_convergence_by_method(df)
    plot_violin_fitness(df)
    plot_violin_convergence(df)
    plot_mean_comparison(df)
    plot_scatter_fitness_vs_convergence(df)
    plot_heatmap_fitness(df)
    plot_heatmap_convergence(df)

    print("\n" + "="*80)
    print("PLOTS CREATED SUCCESSFULLY")
    print("="*80)
    print("\nGenerated files:")
    print("  1. plot_fitness_by_method.png")
    print("  2. plot_convergence_by_method.png")
    print("  3. plot_violin_fitness.png")
    print("  4. plot_violin_convergence.png")
    print("  5. plot_mean_comparison.png")
    print("  6. plot_fitness_vs_convergence.png")
    print("  7. plot_heatmap_fitness.png")
    print("  8. plot_heatmap_convergence.png")
    print("\nReady for publication!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
