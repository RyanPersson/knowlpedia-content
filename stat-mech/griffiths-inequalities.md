---
title: "Griffiths inequalities"
description: "Positivity and monotonicity properties of spin correlations for the finite-volume ferromagnetic Ising model."
---

## Statement

Let $\Lambda$ be a finite set of sites with Ising spins $\sigma_i\in\{-1,+1\}$, and consider the finite-volume ferromagnetic {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}} with Hamiltonian
$$
H_\Lambda(\sigma)
= -\sum_{\{i,j\}\subset \Lambda} J_{ij}\,\sigma_i\sigma_j - \sum_{i\in\Lambda} h_i\,\sigma_i,
$$

where the couplings satisfy $J_{ij}\ge 0$ (ferromagnetic) and the external fields satisfy $h_i\ge 0$.

Let $\mu_\Lambda$ be the associated {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}} and write $\langle \cdot\rangle_\Lambda$ for expectation (see {{< knowl id="expectation" section="probability" text="expectation" >}}). For $A\subset\Lambda$, define the spin monomial $\sigma_A := \prod_{i\in A}\sigma_i$ (with $\sigma_\varnothing=1$).

**Griffiths inequalities:**
1. (**Griffiths I**) For every $A\subset\Lambda$,
   $$
   \langle \sigma_A\rangle_\Lambda \ge 0.
   $$

2. (**Griffiths II**) For every $A,B\subset\Lambda$,
   $$
   \langle \sigma_A\sigma_B\rangle_\Lambda - \langle \sigma_A\rangle_\Lambda\,\langle \sigma_B\rangle_\Lambda \ge 0.
   $$

Equivalently, all covariances of spin monomials are nonnegative.

## Key hypotheses and conclusions

### Hypotheses
- Finite volume $\Lambda$.
- Ising spins $\sigma_i\in\{-1,+1\}$ (context: {{< knowl id="ising-model" section="stat-mech-lattice" text="Ising model" >}}).
- Ferromagnetic couplings $J_{ij}\ge 0$.
- Nonnegative external fields $h_i\ge 0$.
- Gibbs measure $\mu_\Lambda$ (context: {{< knowl id="lattice-hamiltonian" section="stat-mech-lattice" text="lattice Hamiltonian" >}}, {{< knowl id="finite-volume-gibbs-measure" section="stat-mech-lattice" text="finite-volume Gibbs measure" >}}, {{< knowl id="partition-function-lattice" section="stat-mech-lattice" text="partition function" >}}).

### Conclusions
- **Positivity of moments:** $\langle\sigma_A\rangle_\Lambda\ge 0$ for all $A$.
- **Positive correlations:** $\mathrm{Cov}_\Lambda(\sigma_A,\sigma_B)\ge 0$ for all $A,B$.
- **Monotonicity (useful corollary):** differentiating expectations with respect to fields/couplings yields covariances, so Griffiths II implies monotonicity of $\langle\sigma_A\rangle_\Lambda$ in the parameters (a basic “ferromagnets align more when you increase $J$ or $h$” principle).

## Proof idea / significance

A common route is to express derivatives of the pressure $\log Z_\Lambda$ (see {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="pressure" >}}) in terms of truncated correlations and then prove these derivatives are nonnegative using ferromagnetic structure (e.g. random-current/high-temperature expansions or correlation-inequality arguments). In practice, Griffiths inequalities are often obtained as consequences of the stronger {{< knowl id="gks-inequalities" text="GKS inequalities" >}} (and, for monotone observables, the {{< knowl id="fkg-inequality" text="FKG inequality" >}}).

They are foundational for:
- comparison/monotonicity arguments in boundary conditions and fields,
- establishing existence and order properties of infinite-volume limits (see {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}),
- proving bounds on correlation functions (see {{< knowl id="correlation-function-two-point" section="stat-mech" text="two-point correlations" >}}).
