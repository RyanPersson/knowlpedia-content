+++
id = "noncommutative-geometry/delta-derivation"
title = "Derivation δ(T) = [|D|, T]"
kind = "definition"
summary = "The closed commutator derivation with the absolute value of the Dirac operator in a spectral triple."
aliases = ["absolute-Dirac derivation", "delta derivation", "smoothness derivation"]
domains = ["noncommutative-geometry", "functional-analysis"]
section_mode = "progressive"
+++

Let \((\mathcal A,H,D)\) be a
[[noncommutative-geometry/spectral-triple|spectral triple]]. The **delta
derivation** is the generally unbounded derivation on \(B(H)\) defined by
\[
\delta(T)=[|D|,T].
\]
Its domain consists of bounded operators \(T\) that preserve
\(\operatorname{Dom}|D|\) and for which this
[[functional-analysis/operator-commutator|operator commutator]], initially
defined on \(\operatorname{Dom}|D|\), extends to a bounded operator on \(H\).
The bounded extension is by definition \(\delta(T)\). With the
[[linear-algebra/operator-norm|operator norm]] on \(B(H)\), \(\delta\) is a
closed derivation and satisfies
\(\delta(ST)=\delta(S)T+S\delta(T)\) whenever \(S\) and \(T\) lie in its domain.

## Iterated domains and regularity

Define
\[
\operatorname{Dom}\delta^\infty
=\bigcap_{k\geq1}\operatorname{Dom}\delta^k.
\]
A spectral triple is regular when every represented \(a\in\mathcal A\) and
every [[functional-analysis/bounded-commutator|bounded commutator]] \([D,a]\)
belongs to \(\operatorname{Dom}\delta^\infty\). Thus regularity means
boundedness of every iterated commutator with \(|D|\), not merely boundedness
of \([D,a]\). This condition supplies the operator analogue of smooth
coefficients needed by the pseudodifferential calculus in the local index formula
[Connes–Moscovici, §II].

## Graph norms and smooth operator algebra

The [[functional-analysis/graph-norm|graph-norm]] seminorms
\[
q_k(T)=\|\delta^k(T)\|,\qquad k\geq0,
\]
give \(\operatorname{Dom}\delta^\infty\) a natural Fréchet algebra topology.
Closedness of \(\delta\) makes the successive graph norms complete. This
topology records more information than the ambient operator norm and is the
appropriate home for asymptotic expansions involving repeated commutators.

## Conventions and scope

**Warning.** Some treatments replace \(|D|\) by
\(\langle D\rangle=(1+D^2)^{1/2}\), especially to avoid behavior at the kernel
of \(D\). The resulting smooth domains agree in many standard settings, but
that agreement is a theorem with hypotheses, not a change to the displayed
definition. One must also distinguish \(\delta\) from the bounded commutator
\(a\mapsto[D,a]\) appearing in the basic spectral-triple axioms.

## References

1. A. Connes and H. Moscovici, “The Local Index Formula in Noncommutative Geometry,” *Geometric and Functional Analysis* 5 (1995), 174–243. [DOI record](https://doi.org/10.1007/BF01895667). Relevant: §II on regular spectral triples and the derivation by \(|D|\).
2. N. Higson, “The Local Index Formula in Noncommutative Geometry,” in *Contemporary Developments in Algebraic K-Theory*, ICTP Lecture Notes 15, 2004. [Author-hosted manuscript](https://nigel.higson.ca/uploads/1/2/1/4/121496570/higson_-_2004_-_the_local_index_formula_in_noncommutative_geometry.pdf). Relevant: smooth domains of the commutator derivation and the local-index pseudodifferential calculus.
