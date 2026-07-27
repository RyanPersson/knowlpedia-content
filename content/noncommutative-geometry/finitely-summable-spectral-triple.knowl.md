+++
id = "noncommutative-geometry/finitely-summable-spectral-triple"
title = "Finitely summable spectral triple"
kind = "definition"
summary = "A spectral triple that is strictly p-summable for at least one finite exponent."
aliases = ["finite summability", "finitely summable triple"]
domains = ["noncommutative-geometry", "functional-analysis"]
section_mode = "progressive"
+++

A [[noncommutative-geometry/spectral-triple|spectral triple]] \((\mathcal A,H,D)\) is **finitely summable** if it is [[noncommutative-geometry/p-summable-spectral-triple|\(p\)-summable]] for at least one finite exponent \(p>0\); explicitly, there exists \(p<\infty\) such that
\[
\operatorname{Tr}\!\left((1+D^2)^{-p/2}\right)<\infty.
\]
Equivalently, the eigenvalue counting function of \(|D|\) has sufficiently slow polynomial growth for some finite power of its regularized inverse to be trace class. The exponent is not part of the data of finite summability. Once one exponent works, every larger exponent works as well.

## What the condition controls

Finite summability is stronger than
[[functional-analysis/compact-resolvent|compact resolvent]]: an arbitrary compact
operator can have singular values that fail to belong to every finite
Schatten class. It is also stronger than
[[noncommutative-geometry/theta-summable-spectral-triple|theta summability]],
because polynomial summability implies convergence of every positive-time
heat trace, while the converse need not hold.

The condition supplies finite-degree trace cocycles. If the commutators of
the associated [[noncommutative-geometry/fredholm-module|bounded Fredholm module]]
lie in \(\mathcal L^p\), then products
of sufficiently many commutators are trace class and define its cyclic Chern
character [Connes, Chapter IV, §1](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf).

## Examples and non-examples

Every [[noncommutative-geometry/canonical-spin-spectral-triple|canonical Dirac spectral triple]]
on a closed finite-dimensional manifold
is finitely summable, by Weyl asymptotics. A diagonal operator on
\(\ell^2(\mathbb N)\) with eigenvalues growing like \(\log(n+1)\) has compact
resolvent but is not finitely summable, since
\[
\sum_n\bigl(1+\log^2(n+1)\bigr)^{-p/2}
\]
diverges for every finite \(p\). This example isolates the failed property:
compactness holds, but no polynomial trace-ideal bound does.

Finite-dimensional spectral triples are automatically finitely summable for
every \(p\), but finite summability does not mean that \(H\), \(\mathcal A\),
or the spectrum is finite.

## Conventions and scope

Some sources use “finite summability” for the weaker assertion that the
regularized inverse lies in a
[[operator-algebras/weak-schatten-ideal|weak Schatten ideal]] of finite order. The core
uses strict trace-class powers, in agreement with the linked
\(p\)-summability convention. When only weak endpoint behavior is known, the
ideal and exponent should be stated.

Finite summability says nothing by itself about regularity, dimension
spectrum, or meromorphic continuation of zeta functions. Those are separate
hypotheses in the local index formula.

## References

1. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter IV, §§1–2 on finite summability and the cyclic character.
2. J. M. Gracia-Bondía, J. C. Várilly, and H. Figueroa, *Elements of Noncommutative Geometry*, Birkhäuser, 2001. [DOI record](https://doi.org/10.1007/978-1-4612-0005-5). Relevant: §10.1 on spectral triples and finite summability.
