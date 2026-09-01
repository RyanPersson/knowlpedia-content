+++
id = "harmonic-analysis/integrated-form-unitary-representation"
title = "Integrated form of a unitary representation"
kind = "construction"
summary = "The representation of a group convolution algebra obtained by integrating a strongly continuous unitary representation."
aliases = ["integrated representation", "pi(f)", "integrated group representation", "operator pi(f)", "Convolution operator associated to a representation"]
domains = ["harmonic-analysis", "lie-groups", "operator-algebras"]
prerequisites = ["topology/locally-compact-group", "harmonic-analysis/haar-measure", "lie-groups/strongly-continuous-unitary-representation", "harmonic-analysis/l1-group-algebra", "harmonic-analysis/coefficient-function"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact group]] with left
[[harmonic-analysis/haar-measure|Haar measure]], and let
\(\pi:G\to\mathcal U(H)\) be a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous
unitary representation]]. Its **integrated form** assigns to each
[[harmonic-analysis/l1-group-algebra|\(f\in L^1(G)\)]] the bounded operator
\[
\pi(f)\xi=\int_G f(x)\pi(x)\xi\,dx,\qquad \xi\in H.
\]
The integral is a Bochner integral in \(H\), equivalently characterized
weakly by integrating
[[harmonic-analysis/coefficient-function|matrix coefficients]]. It satisfies
\(\|\pi(f)\|\leq\|f\|_1\), and the assignment
\(f\mapsto\pi(f)\) is a nondegenerate \(*\)-representation of the Banach
\(*\)-algebra \(L^1(G)\).

## Algebraic compatibility

For \(f,h\in L^1(G)\),
[[measure-theory/fubinis-theorem|Fubini's theorem]] and the representation
identity give
\[
\pi(f*h)=\pi(f)\pi(h).
\]
With the [[harmonic-analysis/convolution-involution|group-algebra
involution]]
\[
f^*(x)=\Delta_G(x^{-1})\overline{f(x^{-1})},
\]
where \(\Delta_G\) is the
[[harmonic-analysis/modular-function|modular function]], one also has
\(\pi(f^*)=\pi(f)^*\). The modular factor is indispensable for a general
nonunimodular group; omitting it breaks the \(*\)-identity.

## Nondegeneracy and recovery of the group action

If \((u_i)\) is an
[[harmonic-analysis/approximate-identity-l1-group-algebra|approximate identity
in \(L^1(G)\)]], then \(\pi(u_i)\xi\to\xi\) for every \(\xi\in H\). Thus the
integrated form is nondegenerate. Conversely, a nondegenerate
\(*\)-representation of \(L^1(G)\) determines a unique strongly continuous
unitary representation of \(G\). This is why integrated forms are the bridge
between [[algebra-representation-theory/group-representation|group representations]] and representations of group
\(C^*\)-algebras.

## Smoothing and examples

When \(G\) is a [[fiber-bundles/lie-group|Lie group]] and \(f\) is smooth and compactly supported,
\(\pi(f)\) often maps arbitrary vectors into
[[lie-groups/smooth-vector-unitary-representation|smooth vectors]]. For the
left [[algebra-representation-theory/regular-representation|regular representation]], \(\pi(f)\) is left convolution by \(f\) on
\(L^2(G)\). For a discrete group, Haar integration becomes summation and
\(\pi(f)=\sum_{x\in G}f(x)\pi(x)\), with convergence in [[linear-algebra/operator-norm|operator norm]] for
\(f\in\ell^1(G)\).

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [Publisher record](https://www.routledge.com/A-Course-in-Abstract-Harmonic-Analysis/Folland/p/book/9781498727136). Relevant: §§3.2 and 7.1 on integrated representations and group \(C^*\)-algebras.
2. Dana P. Williams, *Crossed Products of C*-Algebras*, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: §2 and Appendix B on integrated forms and vector-valued integration.
