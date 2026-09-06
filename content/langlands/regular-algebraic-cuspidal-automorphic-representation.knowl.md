+++
id = "langlands/regular-algebraic-cuspidal-automorphic-representation"
title = "Regular algebraic cuspidal automorphic representation"
kind = "knowl"
summary = "A cuspidal automorphic representation of a general linear group with regular integral archimedean infinitesimal character."
aliases = ["RACAR", "regular algebraic cuspidal representation", "regular algebraic cuspidal automorphic representation of GLn"]
domains = ["langlands", "number-theory", "representation-theory"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/number-field", "langlands/cuspidal-automorphic-representation", "lie-groups/infinitesimal-character", "langlands/c-algebraic-automorphic-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(F\) be a
[[algebra-fields-galois/number-field|number field]]. A
**regular algebraic cuspidal automorphic
representation** of \(\operatorname{GL}_n(\mathbb A_F)\), often abbreviated
RACAR, is a
[[langlands/cuspidal-automorphic-representation|cuspidal automorphic
representation]] whose archimedean
[[lie-groups/infinitesimal-character|infinitesimal character]] is
integral and regular: it agrees with that of an irreducible algebraic
representation having pairwise distinct shifted weights at every
archimedean embedding.

Unless another normalization is stated, “algebraic” here is Clozel's
condition, equivalently the
[[langlands/c-algebraic-automorphic-representation|\(C\)-algebraic]]
normalization.

## Regularity

For each embedding \(\tau:F\hookrightarrow\mathbb C\), the archimedean
parameter determines \(n\) weight exponents. Regularity means that these
exponents, after the chosen standard shift, are pairwise distinct. It is
stronger than algebraicity and rules out singular infinitesimal character.

Authors package the same data as a dominant [[lie-groups/highest-weight|highest weight]]
\(\lambda_{\tau,1}\geq\cdots\geq\lambda_{\tau,n}\), often with strictness
appearing only after adding the \(\rho\)-shift. Formulas should therefore
state whether they use motivic, cohomological, \(C\)-algebraic, or
\(L\)-algebraic normalization.

## Importance

RACAR representations are a principal theorem-level setting for the
[[langlands/automorphic-galois-correspondence|automorphic–Galois
correspondence]]. Under hypotheses that vary with the base field and
polarization, they have associated [[langlands/compatible-system-of-galois-representations|compatible systems]] of
\(n\)-dimensional \(\ell\)-adic Galois representations, whose local
representations above \(\ell\) have prescribed
[[langlands/hodge-tate-representation|Hodge–Tate weights]], with extensive
[[langlands/local-global-compatibility|local–global compatibility]].

## Variants

“Regular algebraic essentially self-dual cuspidal” and “regular algebraic
polarizable cuspidal” add self-duality conditions needed by many
construction and automorphy-lifting theorems. These adjectives are genuine
extra hypotheses, not part of RACAR itself.

## References

1. Laurent Clozel, “Motifs et formes automorphes: applications du principe
   de fonctorialité,” 1990.
2. Thomas Barnet-Lamb, Toby Gee, David Geraghty, and Richard Taylor,
   “Potential automorphy and change of weight,” *Annals of Mathematics* 179
   (2014), 501–609. [arXiv](https://arxiv.org/abs/1010.2561).
