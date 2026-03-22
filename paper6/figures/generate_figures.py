#!/usr/bin/env python3
"""Generate publication-quality figures for Paper 6, Section VI.

Reads Phase 11 data from:
  - data/benchmarks/benchmark_results.json
  - data/area_law/area_law_results.json
  - data/modular_hamiltonian/modular_hamiltonian_results.json

Produces:
  - paper6/figures/fig_cc_fit.pdf      (1D Calabrese-Cardy fit)
  - paper6/figures/fig_2d_scatter.pdf   (2D boundary vs volume)
  - paper6/figures/fig_ka_locality.pdf  (K_A locality decay)
  - paper6/figures/fig_mveh_check.pdf   (MVEH delta_S check)
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Shared style
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.labelsize': 10,
    'legend.fontsize': 8,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,
})

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIG_DIR = os.path.join(BASE, 'paper6', 'figures')

# Load data
with open(os.path.join(BASE, 'data', 'benchmarks', 'benchmark_results.json')) as f:
    benchmarks = json.load(f)
with open(os.path.join(BASE, 'data', 'area_law', 'area_law_results.json')) as f:
    area_law = json.load(f)
with open(os.path.join(BASE, 'data', 'modular_hamiltonian', 'modular_hamiltonian_results.json')) as f:
    mod_ham = json.load(f)


# ============================================================
# Figure 1: 1D Calabrese-Cardy fit
# ============================================================
def fig_cc_fit():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.8))

    # Panel (a): S(L) with CC fits for multiple N
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    markers = ['o', 's', '^', 'D']
    sizes_data = area_law['1d_afm']['system_sizes']

    for i, (key, color, marker) in enumerate(zip(
            ['N=8', 'N=12', 'N=16', 'N=20'], colors, markers)):
        data = sizes_data[key]
        N = int(key.split('=')[1])
        S_L = data['S_L']
        L_vals = np.arange(1, len(S_L) + 1)

        # CC scaling variable: (N/pi) sin(pi L / N) for PBC
        x_cc = (N / np.pi) * np.sin(np.pi * L_vals / N)

        c = data['cc_fit']['c']
        c1 = data['cc_fit']['c_1']

        # Plot data
        ax1.plot(x_cc, S_L, marker=marker, color=color, markersize=4,
                 linestyle='none', label=f'$N={N}$, $c={c:.3f}$')

        # Plot CC fit
        x_fit = np.linspace(min(x_cc) * 0.9, max(x_cc) * 1.05, 100)
        S_fit = (c / 3.0) * np.log(x_fit) + c1
        ax1.plot(x_fit, S_fit, color=color, linestyle='-', linewidth=0.8,
                 alpha=0.7)

    ax1.set_xlabel(r'$(N/\pi)\sin(\pi L/N)$')
    ax1.set_ylabel(r'$S(L)$ [nats]')
    ax1.legend(loc='lower right', framealpha=0.9, fontsize=7)
    ax1.set_title('(a) AFM Heisenberg, CC fit', fontsize=9)

    # Panel (b): Finite-size scaling of c
    c_vals = area_law['1d_afm']['finite_size_trend']['c_values']
    N_vals = area_law['1d_afm']['finite_size_trend']['N_values']

    ax2.plot(N_vals, c_vals, 'ko-', markersize=5)
    ax2.axhline(y=1.0, color='gray', linestyle='--', linewidth=0.8,
                label='$c=1$ (exact)')
    ax2.set_xlabel('$N$')
    ax2.set_ylabel('Extracted $c$')
    ax2.legend(loc='upper right', fontsize=8)
    ax2.set_title('(b) Central charge convergence', fontsize=9)
    ax2.set_ylim(0.95, 1.15)
    ax2.xaxis.set_major_locator(MaxNLocator(integer=True))

    plt.tight_layout()
    out = os.path.join(FIG_DIR, 'fig_cc_fit.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'Saved: {out}')


# ============================================================
# Figure 2: 2D boundary vs volume scatter
# ============================================================
def fig_2d_scatter():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.8))

    # Collect all subregion data (rectangular + non-rectangular)
    rect_data = area_law['2d_afm']['subregions']
    nonrect_data = area_law['2d_afm']['non_rectangular_subregions']['data']

    # Use independent rectangular + all non-rectangular
    indep_rect = [d for d in rect_data if d.get('independent', False)]
    all_data = indep_rect + nonrect_data

    boundaries = [d['boundary'] for d in all_data]
    volumes = [d['volume'] for d in all_data]
    entropies = [d['S'] for d in all_data]

    # Panel (a): S vs boundary
    ax1.plot(boundaries, entropies, 'ko', markersize=5)

    # Regression line (9 independent rectangular only)
    reg_bd = area_law['2d_afm']['regression_boundary_9indep']
    x_fit = np.linspace(3, 13, 50)
    y_fit = reg_bd['slope'] * x_fit + reg_bd['intercept']
    ax1.plot(x_fit, y_fit, 'r-', linewidth=1.2,
             label=f'$R^2 = {reg_bd["R2"]:.3f}$')

    ax1.set_xlabel(r'$|\partial A|$ (boundary)')
    ax1.set_ylabel(r'$S(A)$ [nats]')
    ax1.legend(loc='lower right', fontsize=8)
    ax1.set_title(r'(a) $S$ vs boundary, 4$\times$4 PBC', fontsize=9)

    # Panel (b): S vs volume
    ax2.plot(volumes, entropies, 'ko', markersize=5)

    reg_vol = area_law['2d_afm']['regression_volume_9indep']
    x_fit = np.linspace(0.5, 13, 50)
    y_fit = reg_vol['slope'] * x_fit + reg_vol['intercept']
    ax2.plot(x_fit, y_fit, 'b-', linewidth=1.2,
             label=f'$R^2 = {reg_vol["R2"]:.3f}$')

    ax2.set_xlabel(r'$|A|$ (volume)')
    ax2.set_ylabel(r'$S(A)$ [nats]')
    ax2.legend(loc='lower right', fontsize=8)
    ax2.set_title(r'(b) $S$ vs volume, 4$\times$4 PBC', fontsize=9)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, 'fig_2d_scatter.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'Saved: {out}')


# ============================================================
# Figure 3: K_A locality (operator weight vs range)
# ============================================================
def fig_ka_locality():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.8))

    # Panel (a): Pauli coefficient decay for Heisenberg AFM
    heis = mod_ham['modular_hamiltonian']['heisenberg_afm']
    decay = heis['decay_profile']
    ranges = [d['range'] for d in decay]
    max_coeffs = [d['max_abs_coeff'] for d in decay]
    sum_sqs = [d['sum_sq'] for d in decay]

    # Use sum of squares as operator weight
    total_sq = sum(sum_sqs)
    frac_sq = [s / total_sq for s in sum_sqs]

    ax1.semilogy(ranges, max_coeffs, 'ko-', markersize=5, label='max $|c|$')
    ax1.set_xlabel('Interaction range')
    ax1.set_ylabel('Max Pauli coefficient $|c|$')
    ax1.set_title('(a) Coefficient decay', fontsize=9)
    ax1.legend(fontsize=8)
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Remove range-0 (on-site, which is ~0 for Heisenberg due to SU(2))
    # and show range 1, 2, 3
    ranges_nonzero = ranges[1:]
    max_coeffs_nonzero = max_coeffs[1:]

    # Highlight the dominant nearest-neighbor contribution
    ax1.annotate(f'SRF = {heis["short_range_fraction"]:.4f}',
                 xy=(1, max_coeffs[1]), xytext=(1.5, max_coeffs[1] * 0.3),
                 fontsize=8, arrowprops=dict(arrowstyle='->', color='gray'))

    # Panel (b): Short-range fraction comparison
    models = ['TFI\ngapped', 'TFI\ncritical', 'Heisenberg\nAFM']
    srfs = [
        mod_ham['modular_hamiltonian']['tfi_gapped']['short_range_fraction'],
        mod_ham['modular_hamiltonian']['tfi_critical']['short_range_fraction'],
        mod_ham['modular_hamiltonian']['heisenberg_afm']['short_range_fraction'],
    ]

    bars = ax2.bar(models, srfs, color=['#7f7f7f', '#bcbd22', '#1f77b4'],
                   edgecolor='black', linewidth=0.5)
    ax2.axhline(y=0.5, color='red', linestyle='--', linewidth=0.8,
                label='Threshold')
    ax2.set_ylabel('Short-range fraction')
    ax2.set_title('(b) $K_A$ locality', fontsize=9)
    ax2.set_ylim(0, 1.05)
    ax2.legend(fontsize=8)

    # Add value labels
    for bar, srf in zip(bars, srfs):
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                 f'{srf:.3f}', ha='center', va='bottom', fontsize=7)

    plt.tight_layout()
    out = os.path.join(FIG_DIR, 'fig_ka_locality.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'Saved: {out}')


# ============================================================
# Figure 4: MVEH check (delta_S vs epsilon)
# ============================================================
def fig_mveh_check():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 2.8))

    mveh = mod_ham['mveh']

    # Panel (a): delta_S distribution at epsilon=0.1
    eps_data = mveh['results']['epsilon_0.1']
    per_site = eps_data['per_site']
    sites_not_in_A = [s for s in per_site if not s['in_A']]
    delta_S_vals = [s['mean_delta_S'] for s in sites_not_in_A]

    ax1.bar(range(len(delta_S_vals)), delta_S_vals,
            color='#1f77b4', edgecolor='black', linewidth=0.5)
    ax1.axhline(y=0, color='red', linestyle='-', linewidth=0.8)
    ax1.set_xlabel('Site index ($x \\notin A$)')
    ax1.set_ylabel(r'$\langle\delta S\rangle$')
    ax1.set_title(r'(a) $\delta S$ per site, $\epsilon=0.1$', fontsize=9)
    ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

    # Panel (b): Quadratic scaling
    qs = mveh['quadratic_scaling']
    epsilons = np.array(qs['epsilon_values'])
    mean_abs = np.array(qs['mean_abs_delta_S'])

    ax2.loglog(epsilons, mean_abs, 'ko', markersize=6, label='Data')

    # Quadratic fit line
    eps_fit = np.linspace(0.03, 0.3, 50)
    # Fit coefficient from the middle point
    coeff = mean_abs[1] / epsilons[1]**2
    ax2.loglog(eps_fit, coeff * eps_fit**2, 'r--', linewidth=1.0,
               label=r'$\propto \epsilon^2$')

    ax2.set_xlabel(r'$\epsilon$')
    ax2.set_ylabel(r'$\langle|\delta S|\rangle$')
    ax2.set_title('(b) Quadratic scaling', fontsize=9)
    ax2.legend(fontsize=8)

    # Annotate scaling ratios
    r1 = qs['ratio_0p2_to_0p1']
    r2 = qs['ratio_0p1_to_0p05']
    ax2.text(0.05, 0.15, f'Ratios: {r1:.2f}, {r2:.2f}\n(expected: 4.0)',
             transform=ax2.transAxes, fontsize=7,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    out = os.path.join(FIG_DIR, 'fig_mveh_check.pdf')
    fig.savefig(out)
    plt.close(fig)
    print(f'Saved: {out}')


if __name__ == '__main__':
    fig_cc_fit()
    fig_2d_scatter()
    fig_ka_locality()
    fig_mveh_check()
    print('All figures generated.')
