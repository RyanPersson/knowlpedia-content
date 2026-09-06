+++
id = "operator-algebras/faithful-state-cstar-algebra"
title = "Faithful state on a C*-algebra"
kind = "definition"
summary = "A state that is strictly positive on every nonzero positive element."
aliases = ["faithful C*-state", "faithful positive normalized functional"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/state-cstar-algebra", "operator-algebras/positive-element", "operator-algebras/von-neumann-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
[[operator-algebras/state-cstar-algebra|state]] \(\varphi\) on \(A\) is
**faithful** if, for every [[operator-algebras/positive-element|positive
element]] \(a\in A\),
\[
\varphi(a)=0\quad\Longrightarrow\quad a=0.
\]
Equivalently, \(\varphi(a^*a)=0\) implies \(a=0\) for every \(a\in A\). Thus
faithfulness is a nondegeneracy condition on a state: no nonzero positive
element is invisible to it. It is independent of normality, which is a
continuity condition available when \(A\) is a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]], and it is also
independent of purity.

## Equivalent tests and representations

The two tests in the core agree because every positive element has a positive
square root. In the [[operator-algebras/gns-construction|GNS construction]],
faithfulness says that the [[operator-algebras/cyclic-vector|cyclic vector]]
has zero expectation on \(a^*a\) only when \(a=0\). It implies that the
associated GNS representation is faithful, but the converse can fail: a
faithful representation may have a cyclic vector whose
[[operator-algebras/vector-state|vector state]] vanishes on a nonzero positive
element.

## Examples and existence

On \(M_n(\mathbb C)\), a state has the form
\(\varphi(a)=\operatorname{Tr}(\rho a)\) for a positive matrix \(\rho\) of
trace one; it is faithful exactly when \(\rho\) is invertible. On \(C_0(X)\),
states correspond to probability Radon measures, and the state is faithful
exactly when the measure has full support. Not every \(C^*\)-algebra has a
faithful state, although every nonzero separable \(C^*\)-algebra does.

## Distinctions

**Warning.** A faithful state need not be pure, and a pure state need not be
faithful. On \(M_n(\mathbb C)\) with \(n>1\), pure states come from rank-one
density matrices and are therefore not faithful. If the ambient algebra is a
von Neumann algebra, a faithful [[operator-algebras/normal-state|normal state]]
imposes both faithfulness and ultraweak continuity; neither adjective includes
the other.

## References

1. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §3.3 on positive functionals, states, and faithfulness.
2. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter I, §9 on positive functionals and representations.
