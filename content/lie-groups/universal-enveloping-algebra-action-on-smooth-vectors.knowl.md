+++
id = "lie-groups/universal-enveloping-algebra-action-on-smooth-vectors"
title = "Universal enveloping algebra action on smooth vectors"
kind = "construction"
summary = "The differentiated Lie-algebra action on smooth vectors extended uniquely to the complex universal enveloping algebra."
aliases = ["U(g)-module of smooth vectors", "differentiated enveloping-algebra action"]
domains = ["lie-groups", "functional-analysis"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/lie-algebra", "lie-groups/strongly-continuous-unitary-representation", "lie-groups/derived-representation-on-smooth-vectors", "algebra-modules/algebra-homomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a connected finite-dimensional [[fiber-bundles/lie-group|Lie group]] with
[[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), and let \(\pi\) be a
[[lie-groups/strongly-continuous-unitary-representation|continuous unitary representation]]
on \(\mathcal H\). Its
[[lie-groups/derived-representation-on-smooth-vectors|derived representation]]
on \(\mathcal H^\infty\) extends complex-linearly from
\(\mathfrak g\) to \(\mathfrak g_{\mathbb C}\), then uniquely to a unital
[[algebra-modules/algebra-homomorphism|algebra homomorphism]]
\[
d\pi:U(\mathfrak g_{\mathbb C})\longrightarrow
\operatorname{End}_{\mathbb C}(\mathcal H^\infty).
\]
This natural construction is called the **canonical universal enveloping
algebra action on smooth vectors**. For a
monomial \(X_1\cdots X_r\), it acts as the well-defined composition
\(d\pi(X_1)\cdots d\pi(X_r)\) on the common invariant domain
\(\mathcal H^\infty\).

## Why the extension exists

The differentiated operators satisfy
\[
d\pi([X,Y])=d\pi(X)d\pi(Y)-d\pi(Y)d\pi(X)
\]
on smooth vectors. The universal property of
[[lie-groups/universal-enveloping-algebra|the universal enveloping algebra]]
therefore produces the unique extension. Invariance of
\(\mathcal H^\infty\) under every \(d\pi(X)\) ensures that all words have one
common domain rather than a separately chosen intersection.

## Equivariance and filtration

The [[algebra-groups/group-action|group action]] and enveloping-algebra action obey
\[
\pi(g)d\pi(u)\pi(g)^{-1}=d\pi(\operatorname{Ad}(g)u),
\qquad u\in U(\mathfrak g_{\mathbb C}).
\]
The degree filtration on \(U(\mathfrak g_{\mathbb C})\) records the order of
iterated differentiation. Central elements act by operators commuting with
\(\pi(G)\), a fact that underlies Casimir operators and infinitesimal
characters.

## Example and analytic warning

For \(G=\mathbb R\), one infinitesimal generator \(D\) determines the action:
\(U(\mathfrak g_{\mathbb C})\cong\mathbb C[X]\), and
\(d\pi(p(X))=p(D)\) on the smooth vectors, which lie in the domain of every
power of \(D\).

**Warning.** This is an algebraic action on a dense Fréchet domain, not in
general a homomorphism into bounded operators on \(\mathcal H\). Closures,
adjoints, and self-adjointness are additional analytic questions.

## References

1. Garth Warner, *Harmonic Analysis on Semi-Simple Lie Groups I*, Grundlehren der mathematischen Wissenschaften 188, Springer, 1972. [DOI record](https://doi.org/10.1007/978-3-642-50275-0). Relevant: §4.4 on differentiable and smooth vectors.
2. Jacques Dixmier, *Enveloping Algebras*, Graduate Studies in Mathematics 11, American Mathematical Society, 1996. [DOI record](https://doi.org/10.1090/gsm/011). Relevant: Chapter 2 on the universal property and filtration of enveloping algebras.
