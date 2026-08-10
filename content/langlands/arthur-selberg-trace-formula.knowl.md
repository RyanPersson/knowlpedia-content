+++
id = "langlands/arthur-selberg-trace-formula"
title = "Arthur-Selberg trace formula"
kind = "knowl"
summary = "An equality between geometric orbital distributions and spectral automorphic distributions."
aliases = ["Arthur trace formula", "Selberg trace formula for reductive groups", "invariant trace formula"]
domains = ["langlands", "harmonic-analysis", "number-theory"]
section_mode = "progressive"
+++

For a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] \(G\) over a global field and a suitable
adelic [[functional-analysis/test-function-space|test function]] \(f\), the **Arthur–Selberg trace formula** is an
identity

\[
J_{\mathrm{geom}}(f)=J_{\mathrm{spec}}(f)
\]

between a geometric expansion indexed by conjugacy data in \(G(F)\) and a
spectral expansion indexed by [[langlands/automorphic-representation|automorphic representations]] and Levi data.

## Kernel heuristic

Right convolution by \(f\) has the formal automorphic kernel

\[
K_f(x,y)=\sum_{\gamma\in G(F)}f(x^{-1}\gamma y).
\]

If the automorphic quotient were compact, integrating \(K_f(x,x)\) would
give both a sum of [[langlands/orbital-integral|orbital integrals]] and a
sum of traces of automorphic representations. For a general reductive group,
the quotient and the continuous spectrum make this naive integral diverge.

Arthur's truncation operator removes the divergent constant-term
contributions and produces the actual formula.

## Geometric side

The fine geometric expansion is a sum over Levi subgroups and conjugacy
classes of coefficients times weighted orbital integrals. Elliptic regular
terms resemble centralizer volumes multiplied by products of ordinary local
orbital integrals. Unipotent and singular terms require separate
distributions.

## Spectral side

The spectral expansion contains the
[[langlands/discrete-automorphic-spectrum|discrete automorphic spectrum]]
of Levi subgroups together with normalized intertwining operators and
integrals representing the continuous spectrum. Under simplifying support
hypotheses it can reduce to a trace on the discrete spectrum, but that is
not the general formula.

## Invariant and stable forms

Arthur first reorganizes the truncated identity into an invariant trace
formula. [[langlands/stable-trace-formula|Stabilization]] then expresses its
unstable terms through stable trace formulas of endoscopic groups. These are
successive refinements, not synonyms for the initial coarse formula.

## Uses

Comparing trace formulas proves instances of functoriality, constructs or
classifies automorphic representations, computes cohomological traces, and
links orbital geometry to [[harmonic-analysis/multiplicity-function-direct-integral-representation|spectral multiplicities]].

## References

1. James Arthur, “An introduction to the trace formula,” 2005.
   [Clay Mathematics Proceedings](https://www.claymath.org/library/cw/arthur/pdf/61.pdf).
2. James Arthur, “A trace formula for reductive groups I,” *Duke
   Mathematical Journal* 45 (1978), 911–952.
   [DOI](https://doi.org/10.1215/S0012-7094-78-04542-5).
