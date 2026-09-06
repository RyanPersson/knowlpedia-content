+++
id = "algebraic-geometry-foundations/perfectoid-field"
title = "Perfectoid field"
kind = "definition"
summary = "A complete nondiscretely valued nonarchimedean field whose residue-level Frobenius is surjective."
aliases = ["perfectoid nonarchimedean field", "perfectoid field of mixed characteristic"]
domains = ["algebraic-geometry-foundations", "number-theory", "langlands"]
prerequisites = ["algebra-fields-galois/valuation-on-a-field", "algebra-fields-galois/frobenius-endomorphism", "algebra-fields-galois/perfect-field"]
dependency_review_count = 1
section_mode = "progressive"
+++

A **perfectoid field** is a complete nonarchimedean field \(K\) with a
nondiscrete rank-one
[[algebra-fields-galois/valuation-on-a-field|valuation]], residue
characteristic \(p>0\), and surjective
[[algebra-fields-galois/frobenius-endomorphism|Frobenius]]

\[
\varphi:\mathcal O_K/p\longrightarrow\mathcal O_K/p,
\qquad x\longmapsto x^p.
\]

In characteristic \(p\), this says that \(K\) is
[[algebra-fields-galois/perfect-field|perfect]] in addition to being
complete and nondiscretely valued.  In mixed characteristic, the condition
forces \(K\) to contain elements with arbitrarily deep compatible \(p\)-power
roots in a valuation-theoretic sense.

## Examples

- The completion of \(\mathbb Q_p(p^{1/p^\infty})\) is perfectoid.
- The completed [[algebra-fields-galois/algebraic-closure|algebraic closure]]
  \(\mathbb C_p\) is perfectoid.
- A discretely valued
  [[langlands-letter/knowls/p-adic-field|\(p\)-adic field]] is not perfectoid.

## Tilt

Every perfectoid field \(K\) has a
[[algebraic-geometry-foundations/tilt-and-untilt|tilt]] \(K^\flat\) of
characteristic \(p\). Their
[[langlands-letter/knowls/galois-extension-and-group|absolute Galois groups]]
are canonically isomorphic,
and finite étale extensions correspond.  The tilting operation is the basic
bridge between mixed- and equal-characteristic perfectoid geometry.

## References

1. Peter Scholze, “Perfectoid spaces,” *Publications Mathématiques de l'IHÉS*
   116 (2012), 245–313. [arXiv](https://arxiv.org/abs/1111.4914).
2. Peter Scholze, “Perfectoid spaces: a survey,” in *Current Developments in
   Mathematics 2012*, International Press, 2013, 193–227.
