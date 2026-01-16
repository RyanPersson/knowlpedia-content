---
title: "Crooks fluctuation theorem"
description: "Exact relation between forward and reverse work distributions, linking nonequilibrium work fluctuations to equilibrium free-energy differences."
---

## Setup (forward vs. reverse driving)

Consider a system coupled to a heat bath at temperature $T$ (inverse temperature $\beta = 1/(k_B T)$), initially prepared in equilibrium for a control parameter value $\lambda_0$. The system is then driven by an externally prescribed protocol $\lambda_t$ from $t=0$ to $t=\tau$ (the **forward** process). Define the time-reversed protocol $\tilde\lambda_t := \lambda_{\tau-t}$ (the **reverse** process), with the reverse experiment initialized in equilibrium at $\lambda_\tau$.

- Equilibrium initialization and free energy: {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}, {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}}, {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}, {{< knowl id="temperature-thermo" section="thermodynamics" text="temperature" >}}.
- Nonequilibrium work viewpoint: {{< knowl id="work-distribution-nonequilibrium" text="work distribution" >}}, {{< knowl id="free-energy-difference-nonequilibrium" text="free-energy difference from nonequilibrium work" >}}.

Let $W$ denote the work performed on the system during a single realization of the forward protocol, and let $P_F(W)$ be its probability density. Let $P_R(W)$ be the work density in the reverse protocol (defined with the same sign convention for work on the system).

## Theorem (Crooks fluctuation theorem)

Assume **microreversibility** (time-reversal symmetry of the underlying dynamics) and consistent thermal contact with the bath (e.g., Markovian dynamics satisfying local detailed balance; see {{< knowl id="detailed-balance" text="detailed balance" >}}). Then the forward and reverse work distributions satisfy
$$
\frac{P_F(W)}{P_R(-W)} \;=\; e^{\beta\,(W-\Delta F)} ,
$$

where $\Delta F := F(\lambda_\tau)-F(\lambda_0)$ is the equilibrium Helmholtz free-energy difference.

Equivalently, in terms of **dissipated work** $W_{\mathrm{diss}} := W-\Delta F$,
$$
\frac{P_F(W)}{P_R(-W)} \;=\; e^{\beta\,W_{\mathrm{diss}}}.
$$

## Key consequences

### 1) Jarzynski equality (corollary)
Integrating the Crooks relation over $W$ yields
$$
\left\langle e^{-\beta W}\right\rangle_F \;=\; e^{-\beta \Delta F},
$$
which is the {{< knowl id="jarzynski-equality-theorem" text="Jarzynski equality" >}} (see also {{< knowl id="jarzynski-equality" text="Jarzynski equality (concept)" >}}).

### 2) Crossing criterion for estimating $\Delta F$
The forward and reverse distributions cross at the reversible work value:
$$
P_F(W) = P_R(-W) \quad \Longleftrightarrow \quad W=\Delta F.
$$

This gives an operational way to extract $\Delta F$ from nonequilibrium sampling.

### 3) Second-law inequality from convexity
By Jensen’s inequality applied to the Jarzynski equality,
$$
\langle W\rangle_F \;\ge\; \Delta F,
$$
consistent with {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="the second law" >}} and the role of dissipation.

## Proof idea (path probabilities; sketch)

A standard route compares the probability of a **forward trajectory** $\Gamma$ to its time-reversed counterpart $\tilde\Gamma$ under the reverse protocol:
1. Use microreversibility plus local detailed balance (or Hamiltonian time-reversal symmetry for system+bath) to relate the ratio of path probabilities to entropy flow into the bath.
2. Identify the bath entropy flow with $\beta Q$ (heat $Q$ absorbed by the bath), and combine with the first-law form $W = \Delta E + Q$.
3. Use equilibrium initial distributions to produce the boundary term $-\beta\Delta F$, yielding a relation of the form
   $$
   \frac{\mathbb P_F(\Gamma)}{\mathbb P_R(\tilde\Gamma)} = e^{\beta(W(\Gamma)-\Delta F)}.
   $$
4. Push forward from trajectories to work values to obtain the work-distribution identity above.

Information-theoretic refinements often express average dissipation as a relative entropy between forward and reverse path measures (see {{< knowl id="relative-entropy-kl-divergence" section="probability" text="relative entropy (KL divergence)" >}}).

## Prerequisites (minimal)

- Equilibrium ensembles and free energy: {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}, {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}}.
- Nonequilibrium work notions: {{< knowl id="work-distribution-nonequilibrium" text="work distribution" >}}.
- Microscopic reversibility / balance conditions: {{< knowl id="detailed-balance" text="detailed balance" >}}.
- Basic probability language: {{< knowl id="probability-measure" section="probability" text="probability measure" >}}, {{< knowl id="expectation" section="probability" text="expectation" >}}.
