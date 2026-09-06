+++
id = "langlands/regular-singular-connection"
title = "Regular-singular connection"
kind = "definition"
summary = "A flat connection on a punctured curve that has at worst logarithmic poles after extension across the punctures."
aliases = ["regular singular connection", "regular singularity"]
domains = ["langlands", "algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/algebraic-curve"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(U=X\setminus D\) be the complement of finitely many points in a smooth
complex [[algebraic-geometry-foundations/algebraic-curve|algebraic curve]]. A flat connection \((V,\nabla)\) on \(U\) is
**regular singular along \(D\)** if, locally at every \(x\in D\), there is a
locally free extension \(\overline V\) across \(x\) for which
\[
\nabla:\overline V\longrightarrow
\overline V\otimes\Omega_X^1(D)
\]
has at most a logarithmic pole. Equivalently, its horizontal sections have
moderate growth near each puncture.

For a principal \(G\)-connection, regular singularity can be tested after a
faithful linear representation of \(G\).

## Riemann–Hilbert consequence

Regular-singular algebraic flat connections correspond analytically to
[[fiber-bundles/local-system|local systems]] on \(U\). Thus ordinary monodromy records the connection on the
[[algebraic-geometry-foundations/punctured-algebraic-curve|punctured curve]], although choosing a logarithmic extension across \(D\) may
require additional extension data.

## References

1. Pierre Deligne, *Équations différentielles à points singuliers réguliers*,
   Lecture Notes in Mathematics 163, Springer, 1970.
   [DOI](https://doi.org/10.1007/BFb0061194).
