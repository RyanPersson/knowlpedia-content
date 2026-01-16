---
title: "Thermodynamic limit of the lattice pressure"
description: "Infinite-volume limit of the log partition function per site, yielding the bulk free-energy density (pressure) of a lattice spin system."
---

## Definition

Let $(\Lambda_n)_{n\ge 1}$ be an increasing sequence of finite regions exhausting the lattice (often boxes, as in {{< knowl id="finite-box-lattice" section="discrete-structures" text="finite boxes" >}}), and fix boundary conditions $\tau_n$ (e.g. free, fixed, or periodic; see {{< knowl id="boundary-condition-lattice" section="stat-mech-lattice" text="boundary conditions" >}}).

With $p_{\Lambda_n}(\beta,\tau_n)$ the {{< knowl id="pressure-lattice" section="stat-mech-lattice" text="finite-volume pressure" >}}, the **thermodynamic-limit pressure** (or **bulk pressure**) is the limit
$$
p(\beta)
=
\lim_{n\to\infty} p_{\Lambda_n}(\beta,\tau_n)
=
\lim_{n\to\infty} \frac{1}{|\Lambda_n|}\log Z_{\Lambda_n}(\beta,\tau_n),
$$
when this limit exists and is independent of the chosen exhausting sequence and boundary conditions.

This is the lattice counterpart of the {{< knowl id="thermodynamic-limit" section="thermodynamics" text="thermodynamic limit" >}} for macroscopic thermodynamic quantities.

## Key properties

- **Existence under standard hypotheses.** For many models defined by a {{< knowl id="translation-invariant-interaction" section="stat-mech-lattice" text="translation-invariant" >}}, {{< knowl id="finite-range-interaction-lattice" section="stat-mech-lattice" text="finite-range" >}} (or sufficiently fast decaying) {{< knowl id="interaction-potential-phi" section="stat-mech-lattice" text="interaction" >}}, the limit exists due to subadditivity-type arguments and boundary terms being negligible compared to volume.

- **Boundary-condition independence (bulk limit).** When the limit exists, dependence on $\tau_n$ typically disappears because boundary contributions scale like $|\partial\Lambda_n|$ while the normalization is by $|\Lambda_n|$.

- **Thermodynamic information.** The bulk Helmholtz free-energy density is
  $$
  f(\beta) = -\frac{1}{\beta}p(\beta),
  $$
  aligning with {{< knowl id="helmholtz-free-energy" section="thermodynamics" text="Helmholtz free energy" >}} per site.

- **Non-analyticity signals phase transitions.** Lack of differentiability or other singular behavior of $p(\beta)$ (as a function of parameters such as $\beta$ or an external field) is a standard signature of {{< knowl id="phase-transition-gibbs" section="stat-mech-lattice" text="phase transitions" >}}; it is closely tied to non-uniqueness of {{< knowl id="infinite-volume-gibbs-measure" section="stat-mech-lattice" text="infinite-volume Gibbs measures" >}}.

## Physical interpretation

$p(\beta)$ is the macroscopic (infinite-volume) free-energy density in units of $k_B T$. It determines equilibrium thermodynamic response: derivatives with respect to temperature-like or field-like parameters yield energy density, magnetization, and susceptibilities in the bulk. When multiple equilibrium phases coexist, $p(\beta)$ remains well-defined but can develop singularities reflecting competing phases.
