+++
id = "operator-algebras/vector-state"
title = "Vector state"
kind = "definition"
summary = "A state obtained by evaluating a represented algebra against a unit vector."
aliases = ["state induced by a unit vector"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(\pi:A\to\mathcal B(H)\) be a
[[operator-algebras/nondegenerate-cstar-representation|nondegenerate]]
[[operator-algebras/cstar-representation|representation of a
\(C^*\)-algebra]], and let \(\xi\in H\) be a unit vector. The **vector state**
determined by \(\xi\) is the [[operator-algebras/state-cstar-algebra|state]]
\[
\omega_\xi(a)=\langle\pi(a)\xi,\xi\rangle\qquad(a\in A).
\]
The representation is part of the ambient data, even when suppressed from the
notation. More generally, the same formula for an arbitrary vector gives a
positive vector functional. For a degenerate representation and a unit vector,
that functional can have norm less than one, so it need not be a state.

## Positivity and normalization

Positivity follows from
\[
\omega_\xi(a^*a)=\|\pi(a)\xi\|^2\geq0.
\]
Nondegeneracy implies that an
[[operator-algebras/approximate-identity|approximate identity]] converges
strongly to \(I_H\), which yields
\(\|\omega_\xi\|=\|\xi\|^2=1\). If \(\xi\) is cyclic, the given pointed
representation is unitarily equivalent to the GNS representation of
\(\omega_\xi\)
[Murphy, §3.3](https://doi.org/10.1016/C2009-0-22289-6).

## Concrete operator algebras

For \(A=\mathcal B(H)\) with its identity representation, every unit vector
defines a vector state. This state is normal, and its [[quantum-foundations/density-operator|density operator]] is the
rank-one projection onto \(\mathbb C\xi\). A general
[[operator-algebras/normal-state|normal state]] on \(\mathcal B(H)\) is instead
represented by a positive trace-class operator of trace one, and need not be a
single vector state.

## Dependence on representation

The same abstract state can appear as a vector state in different
representations. The [[operator-algebras/gns-construction|GNS construction]]
guarantees at least one cyclic-vector realization for every state. Purity is
not automatic: a vector state is pure exactly when its cyclic GNS
subrepresentation is irreducible, not merely because it is specified by one
vector.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §§3.2–3.3 on vector functionals, states, and GNS representations.
2. Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I*, American Mathematical Society, 1997. [DOI record](https://doi.org/10.1090/gsm/015). Relevant: Chapter 4 on positive functionals and vector states.
