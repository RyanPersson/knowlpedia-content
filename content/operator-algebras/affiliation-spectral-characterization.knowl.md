+++
id = "operator-algebras/affiliation-spectral-characterization"
title = "Spectral characterization of affiliation"
kind = "theorem"
summary = "Affiliation is equivalent to membership of the polar partial isometry and all absolute-value spectral projections in the von Neumann algebra."
aliases = ["affiliation by spectral projections"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

Let \(M\subseteq B(H)\) be a [[operator-algebras/von-neumann-algebra|von Neumann algebra]] and let \(T\) be a closed [[functional-analysis/densely-defined-operator|densely defined operator]] on \(H\), with polar decomposition \(T=v|T|\). Then \(T\) is [[operator-algebras/affiliated-operator|affiliated with \(M\)]] if and only if the [[functional-analysis/partial-isometry|partial isometry]] \(v\) belongs to \(M\) and every [[functional-analysis/spectral-projection|spectral projection]]
\[
E^{|T|}(\Delta)=\mathbf 1_\Delta(|T|)
\]
belongs to \(M\) for every Borel set \(\Delta\subseteq[0,\infty)\). Equivalently, \(v\in M\) and \((|T|+i)^{-1}\in M\). For self-adjoint \(T\), affiliation is equivalent to all spectral projections of \(T\) lying in \(M\).

## Why the criteria agree

The defining commutation relation for affiliation says that \(T\) commutes,
as an unbounded operator, with every unitary in \(M'\). Uniqueness of polar
decomposition then forces both \(v\) and the spectral measure of \(|T|\) to
commute with \(M'\); the bicommutant theorem places them in \(M\). Conversely,
these bounded data reconstruct \(T\) by spectral integration and make it
commute with \(M'\).

## Self-adjoint and positive cases

For positive self-adjoint \(T\), the polar partial isometry is the support
projection of \(T\), so membership of the spectral projections alone is
sufficient. For self-adjoint \(T\), the bounded resolvent
\((T-i)^{-1}\) generates the same von Neumann algebra as the spectral
projections, giving a concise resolvent criterion for affiliation.

## Scope and cautions

**Warning.** Affiliation does not assert that an unbounded \(T\) is an element
of \(M\), nor does it imply measurability or integrability with respect to a
trace or weight. The polar decomposition needed here is the one for arbitrary
closed densely defined operators; a result stated only for invertible bounded
operators is not sufficient. For a merely
[[functional-analysis/closable-operator|closable operator]], the criterion
applies to its closure.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter V, §5 on closed operators affiliated with von Neumann algebras and their polar and spectral data.
2. Edward Nelson, “Notes on Non-Commutative Integration,” *Journal of Functional Analysis* 15 (1974), 103–116. [DOI record](https://doi.org/10.1016/0022-1236%2874%2990014-7). Relevant: §§1–2 on affiliated operators and spectral truncations.
