+++
id = "langlands/affine-springer-fiber"
title = "Affine Springer fiber"
kind = "definition"
summary = "The locus of affine-Grassmannian lattices on which a fixed loop-Lie-algebra element becomes integral."
aliases = ["affine Springer fibre", "Kazhdan-Lusztig affine Springer fiber", "affine Springer variety"]
domains = ["langlands", "algebraic-geometry-foundations", "algebra-representation-theory"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "langlands/strongly-regular-semisimple-element", "lie-groups/lie-algebra", "langlands/affine-grassmannian"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(k\) be a field, put \(F=k((t))\) and \(\mathcal O=k[[t]]\), and let \(G\)
be a [[algebraic-geometry-foundations/reductive-algebraic-group|reductive
group]]. For a
regular semisimple element \(\gamma\) of its
[[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g(F)\) whose Lie-algebra
centralizer is a maximal torus (the Lie-algebra analogue of a
[[langlands/strongly-regular-semisimple-element|strongly regular semisimple
element]]),
the **affine Springer fiber** is the subspace

\[
\mathcal M_\gamma=
\left\{
gG(\mathcal O)\in G(F)/G(\mathcal O):
\operatorname{Ad}(g^{-1})\gamma\in\mathfrak g(\mathcal O)
\right\}
\]

of the [[langlands/affine-grassmannian|affine Grassmannian]].

## Interpretation and group version

It parametrizes
integral \(G\)-lattices preserved by \(\gamma\).

There is also a group version in which
\(\gamma\in G(F)\) and the integrality condition is
\(g^{-1}\gamma g\in G(\mathcal O)\).

## Geometry

Affine Springer fibers are usually infinite-dimensional as ambient
[[langlands/ind-scheme|ind-scheme]] loci but have finite-dimensional reduced
pieces under standard
regularity hypotheses.  They can be singular, reducible, and nonproper.  A
lattice in the loop [[algebra-groups/centralizer|centralizer]] of \(\gamma\)
acts on them, often with a
projective quotient.

## Orbital integrals

Point counts and
[[algebraic-geometry-foundations/compactly-supported-etale-cohomology|compactly
supported \(\ell\)-adic cohomology]] of affine Springer fibers encode
[[langlands/orbital-integral|orbital integrals]].  The
[[langlands/hitchin-fibration|Hitchin fibration]] places these local fibers
inside a global family, allowing geometric comparison with endoscopic fibers
in the proof of the [[langlands/fundamental-lemma|fundamental lemma]].

## References

1. David Kazhdan and George Lusztig, “Fixed point varieties on affine flag
   manifolds,” *Israel Journal of Mathematics* 62 (1988), 129–168.
2. Ngô Bảo Châu, “Survey on the fundamental lemma,” 2010, §§3–4.
   [Author PDF](https://math.uchicago.edu/~ngo/survey.pdf).
