+++
id = "operator-algebras/completely-positive-contraction"
title = "Completely positive contraction"
kind = "definition"
summary = "A completely positive linear map whose operator norm is at most one."
aliases = ["CP contraction", "CPC map"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) and \(B\) be [[operator-algebras/cstar-algebra|\(C^*\)-algebras]].
A **completely positive
contraction**, often abbreviated **CPC map**, is a
[[operator-algebras/completely-positive-map|completely positive map]]
\(\phi:A\to B\) satisfying
\[
\|\phi\|\leq 1.
\]
Thus every matrix amplification
\(\phi^{(n)}:M_n(A)\to M_n(B)\) is positive, while the contraction condition
is imposed on the ordinary
[[linear-algebra/operator-norm|operator norm]]. Complete positivity then implies
\(\|\phi\|_{\mathrm{cb}}=\|\phi\|\), in the sense of the
[[operator-algebras/completely-bounded-map|completely bounded norm]], so every
CPC map is completely contractive. Neither multiplicativity nor unitality is
required. In particular, a unital CPC map need not preserve products.

## Norm tests

If \(A\) is unital and \(\phi\) is completely positive, then
\[
\|\phi\|=\|\phi\|_{\mathrm{cb}}=\|\phi(1_A)\|.
\]
Consequently such a map is CPC exactly when
\(\phi(1_A)\leq 1_B\), provided \(B\) is unital. A unital completely positive
map is automatically contractive. For a nonunital domain, the definition
still uses \(\|\phi\|\leq1\); one may test it after passing to an appropriate
unitization [Brown–Ozawa, §1.5](https://doi.org/10.1090/gsm/088).

## Examples and boundary cases

Every contractive
[[operator-algebras/star-homomorphism|\(*\)-homomorphism]] is CPC. If
\(V:K\to H\) is a contraction, the compression
\(\phi(T)=V^*TV\) from \(B(H)\) to \(B(K)\) is CPC; it is unital exactly when
\(V\) is an isometry. Multiplying the identity map by a scalar
\(\lambda>1\) preserves complete positivity but fails the contraction
condition, so it is not CPC.

## Role in approximation

Finite-dimensional approximation properties are commonly formulated using
CPC maps because positivity controls order at every matrix level while
contractivity prevents norms from growing during composition. Nuclearity, for
example, can be expressed through point-norm approximations of the identity
by CPC maps factoring through matrix algebras
[Brown–Ozawa, §2.3](https://doi.org/10.1090/gsm/088).

## References

1. Nathanial P. Brown and Narutaka Ozawa, *C*-Algebras and Finite-Dimensional Approximations*, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [AMS DOI record](https://doi.org/10.1090/gsm/088). Relevant: §1.5 on completely positive maps and §2.3 on nuclear approximation.
