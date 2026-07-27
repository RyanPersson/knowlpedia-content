+++
id = "operator-algebras/tracial-state"
title = "Tracial state"
kind = "definition"
summary = "A normalized positive functional invariant under cyclic interchange of two factors."
aliases = ["trace state"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
**tracial state** is a
[[operator-algebras/state-cstar-algebra|state]] \(\tau:A\to\mathbb C\)
satisfying
\[
\tau(ab)=\tau(ba)\qquad\text{for all }a,b\in A.
\]
Equivalently, it is a [[operator-algebras/trace-cstar-algebra|bounded trace]]
of norm one. If \(A\) is unital, normalization is
\(\tau(1)=1\). For a nonunital algebra, norm one is the defining
normalization. The tracial identity is additional to positivity and
normalization: a general state need not be tracial. It makes the value of a
two-factor product independent of cyclic interchange of its factors.

## Equivalent invariance

On a unital \(C^*\)-algebra, a state is tracial exactly when it is invariant
under every inner unitary conjugation:
\[
\tau(uau^*)=\tau(a).
\]
It then takes equal values on
[[operator-algebras/murray-von-neumann-equivalence|Murray--von Neumann equivalent projections]].
The
set of tracial states is a convex weak-star closed subset of the state space
[Blackadar, treatment of traces and tracial states](https://doi.org/10.1007/3-540-28517-2).

## Examples and non-existence

The normalized matrix trace
\(\tau(a)=n^{-1}\operatorname{Tr}(a)\) is the unique tracial state on
\(M_n(\mathbb C)\). Every state on a
[[operator-algebras/commutative-cstar-algebra|commutative \(C^*\)-algebra]] is
tracial.
By contrast, \(B(H)\) has no tracial state when \(H\) is infinite-dimensional:
two isometries with orthogonal ranges would force the state of the identity to
equal twice itself.

## Bounded and unbounded notions

**Warning.** An extended-valued [[operator-algebras/tracial-weight|tracial weight]] on \(A_+\) is often also called
a trace. Such a weight may be unbounded and may require lower
semicontinuity, density, semifiniteness, or normality hypotheses. A tracial
state is always a bounded everywhere-defined functional, so those extended
notions are not synonyms.

## References

1. Bruce Blackadar, *Operator Algebras: Theory of \(C^*\)-Algebras and von Neumann Algebras*, Springer, 2006. [DOI record](https://doi.org/10.1007/3-540-28517-2). Relevant: the treatment of bounded traces, tracial states, and finite algebras.
2. Nathanial P. Brown and Narutaka Ozawa, *\(C^*\)-Algebras and Finite-Dimensional Approximations*, American Mathematical Society, 2008. [AMS DOI record](https://doi.org/10.1090/gsm/088). Relevant: the chapters using tracial states in finite and stably finite \(C^*\)-algebras.
