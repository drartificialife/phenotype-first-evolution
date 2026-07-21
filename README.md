# Phenotype-First Evolution: Epigenomic Inheritance in Computational Learning

Computational model testing Denis Noble's extended agency hypothesis through evolutionary learning experiments.

## Overview

This repository contains all code, data, and figures supporting the manuscript:

**"Organisms Write Evolution Through Epigenomic Inheritance"**

Testing whether organisms can directly write learned knowledge to heritable epigenomic form (Phenopoiesis) and whether this mechanism provides evolutionary advantage on compositional learning problems.

## Key Findings

- **Simple tasks**: Learning alone is sufficient; inheritance mechanism irrelevant (Baldwin Effect = Phenopoiesis)
- **Learnable compositional tasks**: Phenopoiesis provides 3-6× fitness advantage over selection-only learning
- **Incompatible compositional tasks**: Both mechanisms fail equally, revealing limits of extended agency

## Repository Structure

```
phenotype-first-evolution/
├── paper/                          # Manuscripts
│   ├── AMNAT_MANUSCRIPT.pdf       # Main paper (22 pages)
│   ├── AMNAT_SUPPLEMENTARY.pdf    # Supplementary figures (9 pages)
│   └── *.tex                      # LaTeX sources
├── code/                          # Python implementation
│   ├── phenopoiesis.py           # Phenotype-First algorithm
│   ├── ga_algorithms.py           # Gene-Centric & Baldwin Effect algorithms
│   ├── experiment.py              # Experimental pipeline
│   └── analysis.py                # Statistical analysis & visualization
├── data/                          # Experimental results
│   └── *.csv                      # 540 runs (30 reps × 6 tasks × 3 algorithms)
├── figures/                       # Generated visualizations
│   ├── task_environment_*.png     # Task definitions & fitness calculations
│   ├── simple_tasks_*.png         # Simple learning results
│   ├── compositional_*.png        # Compositional learning results
│   ├── learning_trajectories_*.png # Learning dynamics across generations
│   └── supplementary_*.png        # Additional analyses (variance, convergence, etc.)
└── README.md                      # This file
```

## Quick Start

### Requirements

- Python 3.9+
- NumPy, SciPy, Matplotlib, Pandas

```bash
pip install -r requirements.txt
```

### Running Experiments

```bash
python code/experiment.py
```

Runs all 540 experimental conditions (30 replicates × 6 tasks × 3 algorithms):
- **Algorithms**: Gene-Centric GA, Baldwin Effect, Phenotype-First (Phenopoiesis)
- **Tasks**: 
  - Simple: L alone, T alone, Plus alone
  - Compositional: L+T, T+Plus, L+Plus

### Generating Figures

```bash
python code/analysis.py
```

Generates all figures used in main manuscript and supplementary materials.

## Algorithms

### Gene-Centric GA (Baseline)
- Pure genetic evolution, no learning
- 100-bit genome, standard GA operators (tournament selection, crossover, mutation)

### Baldwin Effect
- Learning during lifetime (20 trials per organism)
- Learning influences selection (phenotypic selection)
- Learned knowledge NOT inherited (each generation learns from scratch)

### Phenotype-First (Phenopoiesis)
- Dual-layer inheritance: genetic (mutates) + epigenetic (inherited at 100% fidelity)
- Learning modifies epigenetic layer
- Offspring inherit both layers → learned patterns persist across generations
- Direct epigenomic write-back mechanism

## Tasks

All tasks on 10×10 grid:
- **L pattern**: 13 cells (angular shape)
- **T pattern**: 12 cells (symmetric T)
- **Plus pattern**: 15 cells (cross shape)

Simple tasks: Learn one pattern alone
Compositional tasks: Learn union of two patterns simultaneously

Fitness metric: (matched cells) / (target cells)

## Results Summary

| Task | Gene-Centric | Baldwin | Phenopoiesis | Advantage |
|------|--------------|---------|--------------|-----------|
| L alone | 57% | 100% | 100% | None (p=0.559) |
| T alone | 59% | 100% | 100% | None |
| Plus alone | 56% | 100% | 100% | None |
| L+T | Low | 25% | 77% | 3.0× (p<0.001) |
| T+Plus | Low | 9% | 52% | 6.0× (p<0.001) |
| L+Plus | Low | 18% | 19% | None (p=0.789) |

## Data Format

Each CSV file contains:
- Final fitness at generation 150
- Convergence time (generation reaching 80% final fitness)
- Component fitnesses (for compositional tasks)
- Summary statistics (mean, s.d. across 30 runs)

## Reproducibility

All experiments are deterministic with fixed random seeds. To reproduce:

```bash
python code/experiment.py --seed 42
```

Computational time: ~48 hours for full experiment suite on standard laptop (Intel Core i7, 8GB RAM).

## Citation

If you use this code or data, please cite the manuscript:

```bibtex
@article{phenotype-first-evolution,
  title={Organisms Write Evolution Through Epigenomic Inheritance},
  journal={The American Naturalist},
  year={2026}
}
```

## License

CC-BY-4.0 (Creative Commons Attribution)

## Contact

For questions about the code or data, please open an issue in this repository.

## Related Work

- Denis Noble, "The Music of Life" (2006)
- Extended Evolutionary Synthesis literature
- Epigenetic inheritance mechanisms

---

**Anonymous submission for peer review**
