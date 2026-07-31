+++
id = "algebra-fields-galois/valuation-ring"
title = "Valuation ring of a valued field"
kind = "definition"
summary = "The local subring of elements having nonnegative valuation."
aliases = ["valuation ring associated with a valuation"]
domains = ["algebra-fields-galois", "algebra-commutative"]
section_mode = "progressive"
+++

For a [[algebra-fields-galois/valuation-on-a-field|valued field]]
\((K,v)\), its **valuation ring** is
\[
\mathcal O_v=\{x\in K:v(x)\geq0\}.
\]
Its group of units and maximal ideal are
\[
\mathcal O_v^\times=\{x\in K:v(x)=0\},
\qquad
\mathfrak m_v=\{x\in K:v(x)>0\}.
\]
Consequently \(\mathcal O_v\) is a
[[algebra-commutative/local-ring|local ring]], and
\(\mathcal O_v/\mathfrak m_v\) is its
[[algebra-commutative/residue-field|residue field]].

## Characterizing property

For every \(x\in K^\times\), totality of the value-group order gives
\[
x\in\mathcal O_v\quad\text{or}\quad x^{-1}\in\mathcal O_v.
\]
Conversely, a subring \(R\subseteq K\) with this property is a valuation ring
of \(K\) for a suitable ordered value group.

## References
Irving Kaplansky, “Maximal fields with valuations,” *Duke Mathematical
Journal* 9 (1942), 303–321.
[DOI](https://doi.org/10.1215/S0012-7094-42-00922-0).
