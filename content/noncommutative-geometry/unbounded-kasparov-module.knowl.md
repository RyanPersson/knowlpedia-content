+++
id = "noncommutative-geometry/unbounded-kasparov-module"
title = "Unbounded Kasparov module"
kind = "definition"
summary = "A Hilbert C-star module cycle with a regular self-adjoint operator whose commutators are bounded and whose resolvent is locally compact."
aliases = ["unbounded KK-cycle", "Baaj–Julg cycle"]
domains = ["noncommutative-geometry", "operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) and \(B\) be
[[operator-algebras/graded-cstar-algebra|graded \(C^*\)-algebras]]. An
**unbounded Kasparov \(A\)-\(B\) module** is a graded,
[[operator-algebras/countably-generated-hilbert-cstar-module|countably
generated Hilbert \(B\)-module]] \(E\), a graded \(*\)-homomorphism
\(\pi:A\to\)
[[operator-algebras/adjointable-operator-hilbert-module|\(\mathcal L_B(E)\)]],
and an odd
[[operator-algebras/regular-operator-hilbert-cstar-module|regular
self-adjoint operator]] \(D\) on \(E\), together with a dense graded
\(*\)-subalgebra \(\mathcal A\subseteq A\), such that:

1. the graded commutator \([D,\pi(a)]\) extends to an adjointable operator for every \(a\in\mathcal A\); and
2. \(\pi(a)(1+D^2)^{-1}\in\mathcal K_B(E)\) for every \(a\in A\).

Here \(\mathcal K_B(E)\) is the algebra of [[operator-algebras/compact-operator-hilbert-module|compact module operators]].

## Bounded transform and KK-class

Functional calculus for regular self-adjoint operators defines
\[
F_D=D(1+D^2)^{-1/2}\in\mathcal L_B(E).
\]
The Baaj–Julg bounded-transform theorem shows that \((E,\pi,F_D)\) is a bounded Kasparov module and hence determines a class in \(KK(A,B)\). Local compactness gives compactness of \(\pi(a)(1-F_D^2)\); the bounded-commutator condition is what controls \([F_D,\pi(a)]\).

The construction generalizes the [[noncommutative-geometry/bounded-transform-spectral-triple|bounded transform of a spectral triple]]. Taking \(B=\mathbb C\) turns a Hilbert \(B\)-module into a [[linear-algebra/hilbert-space|Hilbert space]] and recovers an unbounded Fredholm-module cycle.

## Examples and variants

The [[noncommutative-geometry/dirac-operator|Dirac operator]] on a complete [[differential-geometry/riemannian-manifold|Riemannian manifold]], acting on an appropriate graded \(L^2\)-module with \(C_0(M)\) represented by multiplication, is the model example: commutators with compactly supported smooth functions are bounded, and multiplication by such functions makes the resolvent locally compact.

In the unital compact-resolvent case, it is enough to test local compactness at \(a=1\). For nonunital \(A\), requiring the bare resolvent to be compact is generally too strong; the factors \(\pi(a)\) are essential.

## Conventions and scope

Some authors put \(\mathcal A\), rather than its \(C^*\)-completion \(A\), into the notation for a cycle. Equivalent definitions may use \(\pi(a)(1+D^2)^{-1/2}\in\mathcal K_B(E)\); this stronger-looking formulation follows from the standard hypotheses in the usual Baaj–Julg framework. In the trivially graded case, an odd cycle is commonly expressed by adjoining the appropriate grading rather than deleting the parity condition.

Regular self-adjointness is the Hilbert-module condition that \(D\pm i\) have dense range. It is stronger than being a closed self-adjoint operator on an underlying [[linear-algebra/banach-space|Banach space]] and is needed for [[operator-algebras/continuous-functional-calculus|continuous functional calculus]].

## References

1. S. Baaj and P. Julg, “Théorie bivariante de Kasparov et opérateurs non bornés dans les \(C^*\)-modules hilbertiens,” *Comptes rendus de l’Académie des sciences, Série I* 296 (1983), 875–878. [zbMATH record](https://zbmath.org/0551.46041). Relevant: unbounded cycles and the bounded transform.
2. E. C. Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: Chapters 9–10 on unbounded regular operators and Kasparov theory.
