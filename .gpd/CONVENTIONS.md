# Conventions: Experiential Measure Formalization

## Information-Theoretic Conventions

| Convention | Definition | Test Value |
| ---------- | ---------- | ---------- |
| Entropy base | Nats (natural logarithm, ln) | H(uniform over 4 states) = ln(4) = 1.386 nats |
| Mutual information | I(B;M) = H(B) + H(M) - H(B,M) | I = 0 for independent B,M; I = H(B) for M = f(B) |
| Von Neumann entropy | S_vN(rho) = -Tr(rho ln rho) | S_vN(I/d) = ln(d) for maximally mixed state |
| Experiential density | rho(p) = I(B;M) * (1 - I(B;M)/H(B)) | rho = 0 at I=0 and I=H(B); peak H(B)/4 at I=H(B)/2 |
| Trajectory functional | mu([0,T]) = integral_0^T rho(p_t) dt | Units: nat-seconds. At stationarity: mu = T * rho(pi) |
| Quantum experiential density | rho_Q = I_vN(B;M) * (1 - I_vN(B;M)/S_vN(B)) | Same form as classical; Shannon -> von Neumann |
| Born-Fisher target | I_vN(B;M) / S_vN(B) = 1/2 conjectured for Born-rule | Falsification: ratio != 1/2 |

## Markov Process Conventions

| Convention | Definition | Test Value |
| ---------- | ---------- | ---------- |
| State space | Omega = B x M (product space) | Toy model: \|B\| = \|M\| = 4, \|Omega\| = 16 |
| Discrete-time kernel | P row-stochastic: rows sum to 1 | \|\|P\|\|_inf = 1 |
| Continuous-time generator | Q with zero row sums; dp/dt = pQ | Probabilist's convention (row-vector left, generator right) |
| Stationary distribution | pi satisfying pi*P = pi (left eigenvector) | pi_i >= 0, sum pi_i = 1 |
| Factorization condition | P((b',m')\|(b,m)) = P_B(b'\|b,m) * P_M(m'\|b',m) | Observe-then-update: M' depends on B' (new), not B (old) |
| Spectral gap (discrete) | gap(P) = 1 - \|lambda_2\| | Larger gap = faster mixing |
| Spectral gap (CTMC) | gap(Q) = -Re(lambda_2) | gap > 0 iff irreducible |
| Matrix norm | \|\|P\|\|_inf = max_i sum_j \|P_ij\| | Sup-norm on rows; used in Lipschitz bound |

## Metastability Conventions

| Convention | Definition |
| ---------- | ---------- |
| Communication height | Delta_s, Delta_b in Freidlin-Wentzell sense |
| Basin ordering | Delta_s > Delta_b (stable observer deeper than BB) |
| Noise parameter | epsilon -> 0 (low-noise limit) |
| Rate scaling | Transition rates ~ exp(-V/epsilon) for potential V |

## Cross-Convention Interactions

| Conv A | Conv B | Interaction |
| ------ | ------ | ----------- |
| Entropy base (nats) | Von Neumann entropy | Must use ln in S_vN = -Tr(rho ln rho) |
| Entropy base (nats) | Trajectory functional | mu has units nat-seconds |
| Entropy base (nats) | rho_max | H(B)/4 in nats (ln(4)/4 = 0.347 for 4-state body) |
| Matrix norm (inf) | Lipschitz bound | \|rho(P) - rho(P')\| <= L * \|\|P - P'\|\|_inf |
| Stationary dist convention | Generator convention | dp/dt = pQ: Q acts on right of row-vector p |

## Not Applicable

QFT-standard conventions not used: metric signature, Fourier convention, gauge choice, regularization, renormalization, covariant derivative sign, gamma matrices, Levi-Civita sign, generator normalization, creation/annihilation order, coupling convention, spin basis, QFT state normalization, index positioning, commutation relations, time ordering, coordinate system.

---

_Established: 2026-03-15 during project initialization_
