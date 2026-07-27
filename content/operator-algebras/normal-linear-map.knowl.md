+++
id = "operator-algebras/normal-linear-map"
title = "Normal linear map"
kind = "definition"
summary = "A normal linear map between von Neumann algebras is a bounded linear map that is continuous for their ultraweak topologies."
aliases = ["ultraweakly continuous map", "order-continuous map"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(M\) and \(N\) be [[operator-algebras/von-neumann-algebra|von Neumann algebras]] with [[operator-algebras/predual|preduals]] \(M_*\) and \(N_*\). A bounded [[linear-algebra/linear-map|linear map]] \(\Phi:M\to N\) is **normal** when it is continuous from the [[operator-algebras/ultraweak-topology|ultraweak topology]] on \(M\) to the ultraweak topology on \(N\). Equivalently, there is a unique bounded linear preadjoint \(\Phi_*:N_*\to M_*\) such that
\[
\langle \Phi_*(\omega),x\rangle=\langle\omega,\Phi(x)\rangle
\]
for every \(x\in M\) and \(\omega\in N_*\). Thus normality records weak-star continuity, not norm continuity alone.

## Order characterization

If \(\Phi\) is additionally a [[operator-algebras/positive-linear-map|positive linear map]], normality is equivalent to preservation of bounded increasing suprema:
\[
\Phi\!\left(\sup_i x_i\right)=\sup_i\Phi(x_i)
\]
for every bounded increasing net \((x_i)\) in \(M_+\). Equivalently, this condition may be tested on increasing nets of projections. These order criteria, with positivity explicit, are standard in [Takesaki, chapter III, section 3](https://doi.org/10.1007/978-1-4612-6188-9).

## Stability and use

Composites of normal linear maps are normal. Normal unital positive maps preserve increasing limits of observables, while normal \(*\)-homomorphisms are the morphisms most compatible with the weak-star structure of von Neumann algebras. The preadjoint reverses composition: \((\Psi\circ\Phi)_*=\Phi_*\circ\Psi_*\).

## Conventions and scope

**Warning.** “Order-continuous map” is an equivalent description here only for positive maps. For a general bounded linear map, the unambiguous definition is ultraweak continuity. Normality also does not mean continuity for the norm topology, because every bounded linear map is norm-continuous whether or not it is normal.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: chapter III, sections 2–3 on preduals, ultraweak continuity, and normal maps.
