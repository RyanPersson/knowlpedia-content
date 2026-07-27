+++
id = "operator-algebras/essential-ideal"
title = "Essential ideal of a C*-algebra"
kind = "definition"
summary = "A closed two-sided ideal that meets every nonzero closed two-sided ideal nontrivially."
aliases = ["essential C*-ideal", "large ideal", "essential two-sided ideal"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) be a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. A
[[operator-algebras/closed-two-sided-ideal|closed two-sided ideal]]
\(I\triangleleft A\) is **essential** if
\[
I\cap J\ne\{0\}
\]
for every nonzero closed two-sided ideal \(J\triangleleft A\). Equivalently,
the annihilator
\[
I^\perp=\{a\in A:aI=\{0\}\}
\]
is zero; in a \(C^*\)-algebra this is also equivalent to
\(\{a\in A:Ia=\{0\}\}=\{0\}\). Thus essentiality says that no nonzero part of
\(A\) is disjoint from \(I\). It strengthens merely being a nonzero
[[algebra-rings/two-sided-ideal|two-sided ideal]].

## Equivalent characterizations

The following conditions are equivalent for a closed ideal \(I\):

1. \(I\) is essential;
2. \(I^\perp=\{0\}\);
3. the canonical \(*\)-homomorphism \(A\to M(I)\), obtained from left and
right multiplication on \(I\), is injective.

The \(C^*\)-identity is important here: it makes the left and right
annihilator conditions agree and converts a nonzero annihilating element into
a nonzero ideal disjoint from \(I\)
[Pedersen, §3.12](https://doi.org/10.1016/C2016-0-03431-9).

## Examples

Every \(C^*\)-algebra is an essential ideal in itself. The [[linear-algebra/compact-operator|compact operators]]
\(K(\mathcal H)\) form an essential ideal in \(B(\mathcal H)\) when
\(\mathcal H\ne0\). More generally, if \(X\) is locally compact Hausdorff and
\(U\subseteq X\) is open, the ideal \(C_0(U)\subseteq C_0(X)\) is essential
exactly when \(U\) is dense. By contrast, either coordinate summand in
\(A_1\oplus A_2\), with both summands nonzero, is not essential because it
has zero intersection with the other summand.

## Role in multiplier algebras

The [[operator-algebras/multiplier-algebra|multiplier algebra]] \(M(I)\) is the largest unital \(C^*\)-algebra in
which \(I\) sits as an essential ideal, in the sense that every
\(C^*\)-algebra containing \(I\) essentially acts faithfully on \(I\) by
multipliers. The essentiality hypothesis is exactly what prevents ambient
elements from disappearing under this action
[Lance, §2](https://doi.org/10.1017/CBO9780511526206).

## References

1. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §3.12 on essential ideals and multipliers.
2. E. Christopher Lance, *Hilbert \(C^*\)-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: §2 on multiplier algebras and essential ideals.
