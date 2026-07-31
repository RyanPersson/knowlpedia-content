+++
id = "operator-algebras/state-cstar-algebra"
title = "State on a C*-algebra"
kind = "definition"
summary = "A norm-one positive linear functional on a C*-algebra."
aliases = ["C*-state", "algebraic state", "normalized positive functional"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
**state on \(A\)** is a
[[operator-algebras/positive-linear-functional|positive linear functional]]
\(\varphi:A\to\mathbb C\) satisfying \(\|\varphi\|=1\). Thus a state is
bounded and norm-continuous by definition, and positivity means
\(\varphi(a^*a)\geq0\) for every \(a\in A\). If \(A\) is unital, the
normalization is equivalent to \(\varphi(1)=1\). For a nonunital algebra the
norm condition remains the definition; no multiplier-unit value is silently
assumed. The set of all states is denoted \(S(A)\). Normality is additional
data available when \(A\) is a
[[operator-algebras/von-neumann-algebra|von Neumann algebra]], not part of a
general \(C^*\)-state.

## Convex structure

The state space \(S(A)\) is convex: if \(\varphi,\psi\in S(A)\) and
\(0\leq t\leq1\), then \(t\varphi+(1-t)\psi\) is again a state. A state is
[[operator-algebras/pure-state-cstar-algebra|pure]] when it is an extreme point
of this [[convex-analysis/convex-set|convex set]]. Purity is therefore not
part of the definition of a state. For unital \(A\), the state space is
weak-star compact in \(A^*\); for nonunital \(A\), states may have weak-star
limits of norm less than one, so \(S(A)\) need not be weak-star closed.

## Representation-theoretic meaning

The [[operator-algebras/gns-construction|GNS construction]] writes every state
as a vector functional
\[
\varphi(a)=\langle\pi_\varphi(a)\xi_\varphi,\xi_\varphi\rangle
\]
for a cyclic representation with \(\|\xi_\varphi\|=1\). The state is pure
exactly when its GNS representation is irreducible
[Murphy, §3.3]. Faithfulness of a
state and irreducibility of its representation are different properties:
neither implies the other in general.

## Examples and distinctions

For \(A=B(H)\), each unit vector \(\xi\in H\) defines the
[[operator-algebras/vector-state|vector state]]
\(\varphi_\xi(T)=\langle T\xi,\xi\rangle\). A
[[quantum-foundations/density-operator|density operator]] \(\rho\) defines the
[[operator-algebras/normal-state|normal state]]
\(\varphi_\rho(T)=\operatorname{Tr}(\rho T)\). On a commutative unital algebra
\(C(X)\), evaluation \(f\mapsto f(x)\) is a pure state, whereas integration
against a [[probability/probability-measure|probability measure]] is a general
state. A [[operator-algebras/tracial-state|tracial state]] additionally
satisfies \(\varphi(ab)=\varphi(ba)\); most states are not tracial.

## References

1. Gerard J. Murphy, \(C^*\)-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §§3.2–3.3 on states, pure states, and GNS representations.
2. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: the chapter on positive functionals and state spaces.
