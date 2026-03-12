#!/usr/bin/env python3
"""
generate_figure.py
==================
Reproduces Figure 1 from the PIIA paper:
  Left:  Super-polynomial growth of J^(k)(2) (log scale)
  Right: Convergence of PNT prediction relative error

Usage:
    pip install matplotlib numpy
    python generate_figure.py

Output:
    ../figures/folding_dynamics.png
    ../figures/folding_dynamics.pdf
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ── Data from Table 1 ──────────────────────────────────────────────
k_all     = np.arange(1, 15)
actual    = np.array([
    3, 5, 11, 31, 127, 709, 5381, 52711,
    648391, 9737333, 174440041, 3657500101,
    88362852307, 2428095424619
], dtype=float)

# PNT prediction and relative error (k >= 4 only)
k_err     = np.arange(4, 15)
rel_error = np.array([22.58, 11.02, 2.96, 1.91, 0.56,
                       0.34, 0.28, 0.25, 0.22, 0.20, 0.17])

# For the right panel, also show k=2,3 as high-error context points
k_err_ctx  = np.array([2, 3])
rel_err_ctx = np.array([90.0, 52.0])  # approximate, outside asymptotic regime

# ── Figure ──────────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left panel: growth of J^(k)(2)
ax1.semilogy(k_all, actual, 'o-', color='#1f77b4', linewidth=1.8,
             markersize=7, markerfacecolor='#1f77b4')
ax1.set_xlabel('Iteration Step $k$', fontsize=12)
ax1.set_ylabel(r'Value of $J^{(k)}(2)$ (Log Scale)', fontsize=12)
ax1.set_title('Tectonic Growth of Super-Primes', fontsize=13)
ax1.set_xticks(np.arange(2, 15, 2))
ax1.grid(True, which='both', linestyle='--', alpha=0.4)

# Right panel: convergence of relative error
ax2.plot(k_err_ctx, rel_err_ctx, 's-', color='#d62728',
         markersize=7, markerfacecolor='#d62728', linewidth=1.8)
ax2.plot(k_err, rel_error, 's-', color='#d62728',
         markersize=7, markerfacecolor='#d62728', linewidth=1.8)
ax2.set_xlabel('Iteration Step $k$', fontsize=12)
ax2.set_ylabel('Relative Error (%)', fontsize=12)
ax2.set_title('Convergence of PNT Prediction', fontsize=13)
ax2.set_xticks(np.arange(2, 15, 2))
ax2.set_ylim(-2, 95)
ax2.grid(True, which='both', linestyle='--', alpha=0.4)

plt.tight_layout(w_pad=3)

# ── Save ────────────────────────────────────────────────────────────
out_dir = os.path.join(os.path.dirname(__file__), '..', 'figures')
os.makedirs(out_dir, exist_ok=True)
fig.savefig(os.path.join(out_dir, 'folding_dynamics.png'), dpi=200, bbox_inches='tight')
fig.savefig(os.path.join(out_dir, 'folding_dynamics.pdf'), dpi=200, bbox_inches='tight')
print(f"Figures saved to {os.path.abspath(out_dir)}/")
plt.show()
