---
title: "Microcanonical entropy density"
description: "Thermodynamic-limit definition of microcanonical entropy per volume and its convex-analytic properties; links to ensemble (in)equivalence."
---

## Extension: entropy density in the thermodynamic limit

Let $\Lambda\subset\mathbb{Z}^d$ (or a region in $\mathbb{R}^d$) be a finite volume with $|\Lambda|$ degrees of freedom and Hamiltonian $H_\Lambda$. Write the energy density as $u=E/|\Lambda|$.

A common microcanonical entropy is the finite-volume Boltzmann form (see {{< knowl id="boltzmann-entropy-microcanonical" section="stat-mech" text="Boltzmann microcanonical entropy" >}}). The **microcanonical entropy density** is the thermodynamic-limit object
$$
s(u)=\lim_{\Lambda\uparrow\infty}\frac{1}{|\Lambda|}\,S_\Lambda(u),
$$

when the limit exists in an appropriate sense (often via upper/lower limits or regularizations), where $S_\Lambda(u)$ is a microcanonical entropy at energy density $u$.

### Basic properties and interpretation

- **Thermodynamic meaning:** $s(u)$ is the entropy per degree of freedom at fixed energy density, matching {{< knowl id="thermodynamic-entropy" section="thermodynamics" text="thermodynamic entropy" >}} after identifying $u$ with the thermodynamic {{< knowl id="internal-energy-thermo" section="thermodynamics" text="internal energy" >}} density.
- **Concavity and stability:** in many short-range systems, $s(u)$ is concave, reflecting {{< knowl id="thermodynamic-stability" section="thermodynamics" text="stability" >}}; nonconcavity is a hallmark of {{< knowl id="ensemble-equivalence-breakdown" section="stat-mech" text="ensemble equivalence breakdown" >}} and can coexist with {{< knowl id="microcanonical-negative-heat-capacity" section="stat-mech" text="negative heat capacity (microcanonical)" >}}.
- **Large deviations viewpoint:** for suitable macroscopic observables, $s(u)$ appears as (minus) a {{< knowl id="rate-function" section="large-deviations" text="rate function" >}} in a {{< knowl id="large-deviation-principle" section="large-deviations" text="large deviation principle" >}}.

### Duality with free energy (Legendre–Fenchel)

Let
$$
\psi(\beta)=\lim_{\Lambda\uparrow\infty}\frac{1}{|\Lambda|}\log Z_\Lambda(\beta)
$$

be the log-partition density (see {{< knowl id="pressure-log-partition-density" section="stat-mech" text="pressure (log-partition density)" >}}), where $Z_\Lambda(\beta)$ is the {{< knowl id="partition-function-canonical" section="stat-mech" text="canonical partition function" >}} at inverse temperature $\beta$.

Under standard hypotheses, $s$ and $\psi$ are related by convex duality:
$$
\psi(\beta)=\sup_{u}\,\bigl[s(u)-\beta u\bigr],
\qquad
s(u)=\inf_{\beta}\,\bigl[\psi(\beta)+\beta u\bigr].
$$
This is a Legendre–Fenchel transform (see {{< knowl id="convex-conjugate-fenchel" section="convex-analysis" text="Fenchel conjugate" >}} and {{< knowl id="legendre-transform" section="convex-analysis" text="Legendre transform" >}}) and is one of the equivalences packaged in {{< knowl id="tfae-legendre-duality-entropy-free-energy" section="stat-mech" text="Legendre duality (entropy/free energy)" >}}.

### Prerequisites / cross-links

- {{< knowl id="canonical-ensemble" section="stat-mech" text="canonical ensemble" >}}, {{< knowl id="free-energy-statistical" section="stat-mech" text="statistical free energy" >}}
- {{< knowl id="second-law-thermodynamics" section="thermodynamics" text="second law" >}} (for the macroscopic role of entropy)
