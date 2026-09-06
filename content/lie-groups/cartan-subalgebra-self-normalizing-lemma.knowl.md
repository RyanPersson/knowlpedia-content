+++
id = "lie-groups/cartan-subalgebra-self-normalizing-lemma"
title = "Cartan subalgebras are self-normalizing"
kind = "theorem"
summary = "A maximal toral subalgebra of a complex semisimple Lie algebra equals its Lie-algebra normalizer."
aliases = ["cartan-subalgebra-self-normalizing-lemma", "Cartan subalgebras are self-normalizing"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/semisimple-lie-algebra", "lie-groups/cartan-subalgebra"]
dependency_review_count = 1
legacy_source_path = "lie-groups/cartan-subalgebra-self-normalizing-lemma.md"
+++

Let \(\mathfrak g\) be a finite-dimensional complex
[[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]], and let
\(\mathfrak h\subseteq\mathfrak g\) be a [[lie-groups/cartan-subalgebra|Cartan
subalgebra]], understood here as a maximal toral subalgebra. Then
\[
N_{\mathfrak{g}}(\mathfrak{h})=\{X\in\mathfrak{g}:[X,\mathfrak{h}]\subset \mathfrak{h}\}=\mathfrak{h}.
\]

## Proof from the root-space decomposition

Use the [[lie-groups/root-space-decomposition|root-space decomposition]]
\[
\mathfrak g=\mathfrak h\oplus\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha.
\]
Write \(X=X_0+\sum_{\alpha\in\Phi}X_\alpha\), where \(X_0\in\mathfrak h\) and
\(X_\alpha\in\mathfrak g_\alpha\). If \(X\) normalizes \(\mathfrak h\), then
for every \(H\in\mathfrak h\),
\[
[H,X]=\sum_{\alpha\in\Phi}\alpha(H)X_\alpha\in\mathfrak h.
\]
The sum is direct, so \(\alpha(H)X_\alpha=0\) for every \(H\). For each root
\(\alpha\), some \(H\) has \(\alpha(H)\ne0\); hence \(X_\alpha=0\). Therefore
\(X=X_0\in\mathfrak h\).

## Convention outside the semisimple case

For a general finite-dimensional Lie algebra over an algebraically closed
field of characteristic \(0\), a common definition says that a Cartan
subalgebra is a nilpotent, self-normalizing subalgebra. Under that convention,
the displayed equality is part of the definition rather than a separate
lemma. The substantive semisimple statement above is that the alternative
“maximal toral” characterization implies self-normalization.

## References

1. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, §8. [Publisher record](https://doi.org/10.1007/978-1-4612-6398-2).
2. Anthony W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Birkhäuser, 2002, Chapter II. [Publisher record](https://doi.org/10.1007/978-1-4757-2453-0).
