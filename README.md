# Prime-Universe-OS

**Algebraic framework and computational tools for Prime-Index Isomorphic Arithmetic (PIIA)**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## Overview

This repository accompanies the research program on **Prime-Index Isomorphic Arithmetic (PIIA)**, which constructs an ordered commutative rig (semiring without zero) $(\mathbb{P}, \oplus, \otimes)$ isomorphic to $(\mathbb{Z}^+, +, \times)$ via the prime-enumeration bijection $f(n) = p_n$.

Key results include:

- **Super-primes as algebraic atoms**: The $\otimes$-irreducible elements of $(\mathbb{P}, \otimes)$ correspond exactly to primes with prime indices (OEIS [A006450](https://oeis.org/A006450)).
- **Fundamental Theorem of PIIA**: Every prime admits a unique $\otimes$-factorization into super-primes, mirroring the classical Fundamental Theorem of Arithmetic.
- **Asymptotic expansion of the folding operator**: The self-referential map $J(p_n) = p_{p_n}$ satisfies

$$J(p_n) = n(\ln n)^2 + 3n \ln n \,\ln \ln n - 2n \ln n + 2n(\ln \ln n)^2 + O(n \ln \ln n)$$

validated empirically up to the $10^{12}$ index scale.

## Repository Structure

```
Prime-Universe-OS/
├── papers/
│   ├── Preface_The_Language_of_Primes.tex    # Philosophical preface
│   ├── Preface_The_Language_of_Primes.pdf
│   ├── PIIA_Algebraic_Structures.tex         # Main paper (proofs + experiments)
│   └── PIIA_Algebraic_Structures.pdf
├── figures/
│   └── folding_dynamics.png                  # Figure 1: growth + convergence
├── data/
│   └── folding_sequence.csv                  # J^(k)(2) data for k=1..14
├── scripts/
│   ├── prime_calculator_en.py                # Interactive PIIA calculator (English)
│   ├── prime_calculator_cn.py                # Interactive PIIA calculator (中文)
│   └── generate_figure.py                    # Reproduces Figure 1
├── README.md
├── LICENSE
└── .gitignore
```

## Quick Start

### Prerequisites

```bash
pip install sympy matplotlib numpy
```

### Run the Interactive Calculator

```bash
# English version
python scripts/prime_calculator_en.py

# 中文版
python scripts/prime_calculator_cn.py
```

The calculator supports four PIIA operations:

| Operation | Symbol | Definition | Example |
|-----------|--------|------------|---------|
| Prime Addition | $\oplus$ | $p_i \oplus p_j = p_{i+j}$ | $5 \oplus 7 = p_{3+4} = p_7 = 17$ |
| Prime Multiplication | $\otimes$ | $p_i \otimes p_j = p_{i \cdot j}$ | $5 \otimes 7 = p_{3 \times 4} = p_{12} = 37$ |
| Prime Subtraction | $\ominus$ | $p_i \ominus p_j = p_{i-j}$ (partial) | $11 \ominus 3 = p_{5-2} = p_3 = 5$ |
| Self-Reference Fold | $J$ | $J(p_n) = p_{p_n}$ | $J(5) = p_5 = 11$ |

### Reproduce Figure 1

```bash
python scripts/generate_figure.py
```

### Compile Papers

```bash
cd papers
pdflatex PIIA_Algebraic_Structures.tex
pdflatex PIIA_Algebraic_Structures.tex   # second pass for references
pdflatex Preface_The_Language_of_Primes.tex
pdflatex Preface_The_Language_of_Primes.tex
```

## Data

`data/folding_sequence.csv` contains the complete iterative folding sequence $J^{(k)}(2)$ for $k = 1, \ldots, 14$, including:

- Exact values computed via SymPy's Meissel–Lehmer implementation
- Localized PNT predictions $\tilde{p}_m = \lfloor m(\ln m + \ln\ln m - 1) \rfloor$
- Relative errors (monotonically decreasing from 22.58% at $k=4$ to 0.17% at $k=14$)

## Citation

If you use this framework in your research, please cite:

```bibtex
@misc{chen2026piia,
  author       = {Ruqing Chen},
  title        = {Prime-Index Isomorphic Arithmetic: Algebraic Structures,
                  Asymptotic Dynamics, and $\otimes$-Irreducible Elements
                  in the Prime Space},
  year         = {2026},
  howpublished = {\url{https://github.com/Ruqing1963/Prime-Universe-OS}},
}
```

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

## Author

**Ruqing Chen**
GUT Geoservice Inc., Montreal, Canada
📧 ruqing@hotmail.com
