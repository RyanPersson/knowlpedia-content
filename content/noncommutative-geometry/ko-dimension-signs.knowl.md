+++
id = "noncommutative-geometry/ko-dimension-signs"
title = "KO-dimension sign table for a real spectral triple"
kind = "definition"
summary = "The mod-eight rule assigning the commutation signs of the real structure with the Dirac operator and grading."
aliases = ["KO-dimension modulo 8", "epsilon signs", "real parity signs"]
domains = ["noncommutative-geometry"]
section_mode = "progressive"
+++

For a [[noncommutative-geometry/real-structure-spectral-triple|real structure]] \(J\), the **KO-dimension sign table** assigns signs to
\[
J^2=\varepsilon,\qquad JD=\varepsilon'DJ,\qquad
J\Gamma=\varepsilon''\Gamma J
\]
as a function of \(n\in\mathbb Z/8\mathbb Z\). In the Connes–Marcolli convention the eight sign pairs \((\varepsilon,\varepsilon')\), for \(n=0,\ldots,7\), are
\[
(+,+),(+,-),(-,+),(-,+),(-,+),(-,-),(+,+),(+,+).
\]
The grading sign \(\varepsilon''\) exists only in even dimension and equals \(+,-,+,-\) for \(n=0,2,4,6\), respectively. Thus KO-dimension is discrete real-parity data; it is independent of the metric or [[noncommutative-geometry/metric-dimension|spectral dimension]] of the triple.

## Expanded lookup

The convention above gives the following complete lookup:

- \(n=0\): \((\varepsilon,\varepsilon',\varepsilon'')=(+,+,+)\).
- \(n=1\): \((\varepsilon,\varepsilon')=(+,-)\).
- \(n=2\): \((\varepsilon,\varepsilon',\varepsilon'')=(-,+,-)\).
- \(n=3\): \((\varepsilon,\varepsilon')=(-,+)\).
- \(n=4\): \((\varepsilon,\varepsilon',\varepsilon'')=(-,+,+)\).
- \(n=5\): \((\varepsilon,\varepsilon')=(-,-)\).
- \(n=6\): \((\varepsilon,\varepsilon',\varepsilon'')=(+,+,-)\).
- \(n=7\): \((\varepsilon,\varepsilon')=(+,+)\).

This is [Connes and Marcolli, Definition 1.124](https://doi.org/10.1090/coll/055).

## Conventions and use

The table packages the real Clifford-algebra periodicity behind KO-homology. In particular, KO-dimension \(2\) gives \(J^2=-1\), \(JD=DJ\), and \(J\Gamma=-\Gamma J\), while KO-dimension \(6\) changes only \(J^2\) among these three relations.

**Warning.** Alternative definitions of the [[noncommutative-geometry/dirac-operator|Dirac operator]] or charge-conjugation operator can shift the displayed signs, especially the \(JD\) relation. A source using a different convention must not be combined entrywise with this table.

## References

1. A. Connes and M. Marcolli, *Noncommutative Geometry, Quantum Fields and Motives*, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/coll/055). Relevant: Definition 1.124, especially equation (1.470) and its mod-eight table.
2. A. Connes, “Noncommutative Geometry and Reality,” *Journal of Mathematical Physics* 36 (1995), 6194–6231. [DOI record](https://doi.org/10.1063/1.531241). Relevant: §2 on real K-cycles and dimension-dependent sign relations.
