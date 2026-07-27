+++
id = "operator-algebras/involutive-algebra"
title = "Involutive algebra"
kind = "definition"
summary = "A complex associative algebra equipped with a conjugate-linear involution reversing products."
aliases = ["*-algebra"]
domains = ["operator-algebras", "algebra-rings"]
section_mode = "progressive"
+++

An **involutive algebra**, or **\(*\)-algebra**, is a complex associative [[algebra-modules/algebra-over-ring|algebra]] \(A\) equipped with a map \(a\mapsto a^*\) such that for all \(a,b\in A\) and \(\lambda,\mu\in\mathbb C\),
\[
(\lambda a+\mu b)^*=\overline\lambda a^*+\overline\mu b^*,\qquad
(ab)^*=b^*a^*,\qquad
(a^*)^*=a.
\]
The operation is called an involution. If \(A\) is unital, one normally also requires \(1^*=1\), although this follows from the other axioms when the involution is bijective and \(1\) is a two-sided identity. No norm, topology, or completeness is part of this definition.

## Morphisms and distinguished elements

A \(*\)-homomorphism is an [[algebra-modules/algebra-homomorphism|algebra homomorphism]] \(\phi:A\to B\) satisfying \(\phi(a^*)=\phi(a)^*\). An element is self-adjoint when \(a=a^*\), normal when \(aa^*=a^*a\), and unitary in a unital algebra when \(a^*a=aa^*=1\). These algebraic notions become analytic only after a compatible norm or operator representation is supplied.

## Examples and additional structure

For a complex [[linear-algebra/hilbert-space|Hilbert space]] \(\mathcal H\), bounded operators form a unital \(*\)-algebra under the operator adjoint. Complex matrices use conjugate transpose. A [[operator-algebras/cstar-algebra|\(C^*\)-algebra]] is a norm-complete \(*\)-algebra satisfying \(\|a^*a\|=\|a\|^2\); an arbitrary involutive algebra need not admit any such norm.

## Conventions and scope

More generally, one may work over a field carrying a specified involution and require semilinearity with respect to it. Over \(\mathbb R\), the involution is linear. Some authors build a unit into “algebra” and others do not, so unitality must be stated separately. The symbols \(*\)-algebra and involutive algebra are synonymous here.

## References

1. Gerard J. Murphy, \(C^*\)-Algebras and Operator Theory, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.1 on involutions and \(C^*\)-algebras.
2. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §1.1 on \(*\)-algebra conventions.
