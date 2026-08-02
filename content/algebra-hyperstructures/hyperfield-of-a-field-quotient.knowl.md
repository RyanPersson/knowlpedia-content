+++
id = "algebra-hyperstructures/hyperfield-of-a-field-quotient"
title = "Hyperfield of a field quotient"
kind = "construction"
summary = "The quotient hyperfield K/G formed from a field and a multiplicative subgroup."
aliases = ["quotient hyperfield", "factor hyperfield", "Krasner quotient hyperfield"]
domains = ["algebra-hyperstructures", "algebra-rings"]
section_mode = "progressive"
+++

Let \(K\) be a field and \(G\leq K^\times\) a multiplicative subgroup. The
orbit set
\[
K/G=\{0\}\sqcup K^\times/G
\]
is a **quotient hyperfield** with
\[
[a][b]=[ab],\qquad
[a]\boxplus[b]=\{[ag+bh]:g,h\in G\}.
\]
It is the hyperfield specialization of the
[[algebra-hyperstructures/quotient-hyperring|quotient-hyperring
construction]].

## Why this is a hyperfield

The formula is independent of the representatives because changing \(a\) or
\(b\) only changes the allowed factors from \(G\). Every nonzero orbit has
inverse \([a^{-1}]\), and distributivity follows from distributivity in
\(K\). The entire set of possible orbits is retained; no representative of a
hyper-sum is chosen.

The orbit map
\[
\pi:K\longrightarrow K/G
\]
is a weak hyperfield homomorphism and is generally not strong. A fixed sum
\(a+b\) has one orbit, while independently rescaling the two summands can
produce several orbits in \([a]\boxplus[b]\).

## Standard examples

- \(G=\{1\}\) recovers the original field with singleton-valued addition.
- If \(|K|\geq3\), then \(K/K^\times\) is the [[algebra-hyperstructures/krasner-hyperfield|Krasner hyperfield]]. For
  \(K=\mathbb F_2\), the same orbit construction recovers the ordinary field
  \(\mathbb F_2\), so the size hypothesis is real.
- \(\mathbb R/\mathbb R_{>0}\) is the [[algebra-hyperstructures/sign-hyperfield|sign hyperfield]].
- \(\mathbb C/\mathbb R_{>0}\) is the
  [[algebra-hyperstructures/phase-hyperfield|phase hyperfield]].

## Not every hyperfield is a field quotient

The quotient construction supplies many central examples, but it is not a
classification of hyperfields. Massouros constructed hyperfields not
isomorphic to \(K/G\) for any field \(K\) and multiplicative subgroup \(G\).
Consequently “hyperfield” and “quotient hyperfield” are not synonyms.

## References

1. Alain Connes and Caterina Consani, “The hyperring of adèle classes,” *Journal of Number Theory* 131 (2011), 159–194. [arXiv:1001.4260](https://arxiv.org/abs/1001.4260). Relevant: quotient hyperrings and hyperfields.
2. Matthew Baker and Nathan Bowler, “Matroids over partial hyperstructures,” *Advances in Mathematics* 343 (2019), 821–863. [arXiv:1709.09707](https://arxiv.org/abs/1709.09707). Relevant: Remark 2.7 and the standard quotient examples.
3. Christos G. Massouros, “Methods of constructing hyperfields,” *International Journal of Mathematics and Mathematical Sciences* 8 (1985), 725–728. [EuDML record and text](https://eudml.org/doc/46035). Relevant: non-quotient hyperfields.
