+++
id = "operator-algebras/nondegenerate-star-homomorphism"
title = "Nondegenerate *-homomorphism"
kind = "definition"
summary = "A C*-algebra homomorphism whose image acts densely on the target algebra or representation space."
aliases = ["non-degenerate representation", "essential *-homomorphism", "nondegenerate representation", "nondegenerate C*-homomorphism"]
domains = ["operator-algebras"]
prerequisites = ["operator-algebras/cstar-algebra", "operator-algebras/star-homomorphism", "operator-algebras/multiplier-algebra"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(A\) and \(B\) be
[[operator-algebras/cstar-algebra|\(C^*\)-algebras]]. A
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]]
\(\varphi:A\to M(B)\) is **nondegenerate** if
\[
\overline{\operatorname{span}}\{\varphi(a)b:a\in A,\ b\in B\}=B.
\]
Here \(M(B)\) acts canonically on \(B\). A representation
\(\pi:A\to B(H)\) is nondegenerate when
\(\overline{\pi(A)H}=H\). These conditions exclude a nonzero summand on which
the image acts as zero and remain meaningful when \(A\) or \(B\) is
nonunital. Nondegeneracy is the morphism hypothesis that permits canonical
extensions to [[operator-algebras/multiplier-algebra|multiplier algebras]].

## Approximate-identity criteria

If \((e_i)\) is an
[[operator-algebras/approximate-identity|approximate identity]] for \(A\),
then \(\varphi\) is nondegenerate exactly when
\(\varphi(e_i)b\to b\) for every \(b\in B\). Equivalently,
\(\varphi(e_i)\to1_{M(B)}\) strictly. For a representation, the corresponding
criterion is strong convergence \(\pi(e_i)\xi\to\xi\) for every \(\xi\in H\).
These criteria are independent of the chosen approximate identity.

## Multiplier extension

Every nondegenerate \(\varphi:A\to M(B)\) has a unique unital strictly
continuous extension
\[
\overline{\varphi}:M(A)\longrightarrow M(B)
\]
that agrees with \(\varphi\) on \(A\). Conversely, the restriction of such an
extension is nondegenerate. This is why nondegenerate homomorphisms, rather
than arbitrary \(*\)-homomorphisms, are used for multiplier-algebra functoriality,
correspondences, and covariant representations.

## Unital and degenerate cases

If \(A\) is unital, nondegeneracy is equivalent to
\(\varphi(1_A)=1_{M(B)}\). A representation is degenerate precisely when the
[[linear-algebra/orthogonal-complement|orthogonal complement]] of \(\overline{\pi(A)H}\) is nonzero; restricting to the
essential subspace \(\overline{\pi(A)H}\) produces a nondegenerate
representation. A zero map into a nonzero target is degenerate, while a map
into the zero algebra is sensitive to the convention adopted for its identity.

## References

1. E. Christopher Lance, *Hilbert C*-Modules: A Toolkit for Operator Algebraists*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511526206). Relevant: §2 on nondegenerate homomorphisms and multiplier extensions.
2. Gert K. Pedersen, *C*-Algebras and Their Automorphism Groups*, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §3.12 on approximate identities and nondegenerate representations.
3. Dana P. Williams, *Crossed Products of C*-Algebras*, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Appendix A on multiplier algebras and nondegenerate homomorphisms.
