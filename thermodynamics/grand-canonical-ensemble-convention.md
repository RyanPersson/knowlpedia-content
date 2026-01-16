---
title: "Grand canonical ensemble convention"
description: "The convention that a system in contact with a heat and particle bath is described by the grand canonical ensemble."
---

The **grand canonical ensemble** describes a system in thermal and chemical equilibrium with a reservoir at fixed {{< knowl id="temperature-thermo" text="temperature" >}} $T$ and {{< knowl id="chemical-potential-thermo" text="chemical potential" >}} $\mu$. The system can exchange both energy and particles with the reservoir.

## Probability distribution

In the grand canonical ensemble, the probability of finding the system with $N$ particles in {{< knowl id="microstate-classical" section="stat-mech" text="microstate" >}} $(q, p)$ is
$$
\rho_N(q, p) = \frac{1}{\Xi} e^{-\beta (H_N(q, p) - \mu N)},
$$

where:
- $\beta = 1/(k_B T)$ is the {{< knowl id="inverse-temperature-beta" text="inverse temperature" >}}
- $H_N$ is the {{< knowl id="hamiltonian-function-classical" section="stat-mech" text="Hamiltonian" >}} for $N$ particles
- $\Xi$ is the {{< knowl id="grand-partition-function" section="stat-mech" text="grand partition function" >}}

## Related concepts

- {{< knowl id="grand-canonical-ensemble" section="stat-mech" text="Grand canonical ensemble" >}} (detailed definition)
- {{< knowl id="grand-potential" text="Grand potential" >}}: the thermodynamic potential natural to this ensemble
- {{< knowl id="particle-reservoir" section="stat-mech" text="Particle reservoir" >}}
