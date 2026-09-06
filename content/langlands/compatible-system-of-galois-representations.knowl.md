+++
id = "langlands/compatible-system-of-galois-representations"
title = "Compatible system of Galois representations"
kind = "knowl"
summary = "A family of l-adic Galois representations with coefficient-independent Frobenius polynomials at almost all places."
aliases = ["compatible system", "weakly compatible system", "compatible family of l-adic representations"]
domains = ["langlands", "number-theory", "algebraic-geometry"]
prerequisites = ["algebra-fields-galois/number-field", "langlands-letter/knowls/galois-extension-and-group", "algebra-fields-galois/inertia-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F\) and \(E\) be
[[algebra-fields-galois/number-field|number fields]]. A
**weakly compatible system of
\(n\)-dimensional Galois representations over \(E\)** consists of continuous
semisimple representations

\[
\rho_\lambda:
\operatorname{Gal}(\overline F/F)
\longrightarrow
\operatorname{GL}_n(\overline E_\lambda)
\]

of the [[langlands-letter/knowls/galois-extension-and-group|absolute Galois
group]], for finite places \(\lambda\) of \(E\), together with a finite set
\(S\) of
places of \(F\), such that for every \(v\notin S\) and every
\(\lambda\nmid v\), the restriction of \(\rho_\lambda\) to the
[[algebra-fields-galois/inertia-subgroup|inertia subgroup]] at \(v\) is
trivial, and

\[
P_v(X)=
\det\!\left(1-X\,\rho_\lambda(\operatorname{Frob}_v)\right)
\in E[X]
\]

is independent of \(\lambda\), after the fixed embeddings of \(E\) into the
local coefficient fields.

## Frobenius convention

The polynomial changes by inverting eigenvalues when arithmetic Frobenius
is replaced by geometric
[[langlands-letter/knowls/frobenius-unramified|Frobenius]]. A compatible
system must use one
convention consistently. Many arithmetic sources use geometric Frobenius in
[[langlands/local-class-field-theory|local class field theory]] but arithmetic
Frobenius in étale-cohomological
[[linear-algebra/characteristic-polynomial|characteristic polynomials]]; the formula, not the word alone, is decisive.

## Stronger compatibility

The adjective “compatible system” is used with several strengths. A stronger
system can additionally prescribe:

- a \(\lambda\)-independent multiset of
  [[langlands/hodge-tate-representation|Hodge–Tate numbers]] at each embedding;
- [[langlands/de-rham-galois-representation|de Rham]] or
  [[langlands/crystalline-galois-representation|crystalline]] behavior at
  places above \(\ell\);
- compatible [[langlands/weil-deligne-representation|Weil–Deligne representations]] at all finite places;
- purity of a fixed weight;
- a common coefficient field and polarization.

These conditions should be listed rather than inferred from the name.

## Semisimplicity and ramification

Almost-all Frobenius polynomials determine only the semisimplification, by the
[[algebra-fields-galois/chebotarev-density-theorem|Chebotarev density
theorem]]. They do not by themselves recover monodromy operators at
ramified places. Full [[langlands/local-global-compatibility|local–global
compatibility]] contains strictly more information.

## Automorphic origin

[[langlands/regular-algebraic-cuspidal-automorphic-representation|Regular algebraic cuspidal automorphic representations]] of general linear
groups produce compatible systems in many theorem-level settings. The
general expectation for [[algebraic-geometry-foundations/reductive-algebraic-group|reductive groups]] is naturally
\(\widehat G\)- or \(L\)-group-valued and requires a representation of the
dual group to recover the displayed \(\operatorname{GL}_n\)-valued system.

## References

1. Jean-Pierre Serre, *Abelian \(\ell\)-Adic Representations and Elliptic
   Curves*, second edition, 1998.
2. Thomas Barnet-Lamb, Toby Gee, David Geraghty, and Richard Taylor,
   “Potential automorphy and change of weight,” §5.
   [arXiv](https://arxiv.org/abs/1010.2561).
