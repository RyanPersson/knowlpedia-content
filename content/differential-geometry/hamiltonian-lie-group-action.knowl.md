+++
id = "differential-geometry/hamiltonian-lie-group-action"
title = "Hamiltonian Lie group action"
kind = "definition"
summary = "A symplectic Lie group action equipped with a compatible equivariant moment map."
aliases = ["Hamiltonian action"]
domains = ["differential-geometry", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] acting by a [[differential-geometry/symplectic-lie-group-action|symplectic Lie group action]] on \((M,\omega)\). With the convention \(\iota_{X_f}\omega=df\), the action is **Hamiltonian** if it admits a [[fiber-bundles/moment-map|moment map]] \(\mu:M\to\mathfrak g^*\) such that
\[
d\langle\mu,\xi\rangle=\iota_{\xi_M}\omega
\]
for every \(\xi\in\mathfrak g\), and \(\mu(gx)=\operatorname{Ad}_g^*\mu(x)\) for every \(g\in G\). The triple \((M,\omega,\mu)\), together with the \(G\)-action, is a Hamiltonian \(G\)-space. Thus Hamiltonianity requires compatible global Hamiltonians for all infinitesimal generators, not merely preservation of \(\omega\). Equivariance couples those Hamiltonians to the full [[algebra-groups/group-action|group action]].

## Infinitesimal characterization

Symplecticity gives \(d(\iota_{\xi_M}\omega)=0\). A moment map exists only if these closed one-forms are exact and their primitives can be chosen linearly in \(\xi\). Equivariance further requires
\[
\{\langle\mu,\xi\rangle,\langle\mu,\eta\rangle\}
=\langle\mu,[\xi,\eta]\rangle
\]
with the compatible Poisson-bracket convention. For connected \(G\), this infinitesimal bracket identity is equivalent to global coadjoint equivariance [Ortega and Ratiu, §4.2](https://doi.org/10.1007/978-1-4757-3811-7).

## Examples and non-examples

The standard counterclockwise rotation action of \(S^1\) on \(\mathbb R^2\) with \(\omega=dx\wedge dy\) is Hamiltonian; a moment map is \((x,y)\mapsto -(x^2+y^2)/2\), after identifying \(\mathfrak{s}^1{}^*\) with \(\mathbb R\). Cotangent-lifted actions provide a canonical family of examples.

Translations on a symplectic torus preserve its symplectic form but need not be Hamiltonian: contraction with a generating translation field can be a closed nonexact one-form. The failed condition is global exactness, not symplecticity.

## Conventions and scope

**Warning.** Some authors call an action Hamiltonian as soon as it has a not-necessarily-equivariant moment map, while others include equivariance in the definition. This knowl adopts the latter convention, standard in reduction theory; under the former convention, “Hamiltonian with an [[differential-geometry/equivariant-moment-map|equivariant moment map]]” names the notion defined here [Guillemin and Sternberg, Chapter 3](https://doi.org/10.1017/CBO9780511624110).

## References

1. Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1984. [DOI record](https://doi.org/10.1017/CBO9780511624110). Relevant: Chapter 3, Hamiltonian group actions and moment maps.
2. Juan-Pablo Ortega and Tudor S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Birkhäuser, 2004. [DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: §4.2, momentum maps and equivariance.
