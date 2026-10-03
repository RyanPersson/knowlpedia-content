+++
id = "lie-groups/distribution-vectors-of-a-representation"
title = "Distribution vectors of a Lie-group representation"
kind = "definition"
summary = "Continuous antilinear functionals on the Fréchet space of smooth vectors of a Lie-group representation."
aliases = ["generalized vectors", "distribution globalization", "H-infinity dual"]
domains = ["lie-groups", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group", "lie-groups/smooth-vector-unitary-representation", "lie-groups/smooth-vector-frechet-topology", "functional-analysis/continuous-antidual"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] and let \((\pi,\mathcal H)\) be a strongly continuous
unitary representation. Write \(\mathcal H^\infty\) for its
[[lie-groups/smooth-vector-unitary-representation|space of smooth vectors]],
with its [[lie-groups/smooth-vector-frechet-topology|smooth-vector Fréchet topology]]. The space of **distribution vectors** is
\[
\mathcal H^{-\infty}=(\mathcal H^\infty)'_{\mathrm{anti}},
\]
the [[functional-analysis/continuous-antidual|continuous anti-dual]] of \(\mathcal H^\infty\), equipped usually
with its [[functional-analysis/strong-dual|strong dual topology]]. The Hilbert-space pairing gives continuous
dense inclusions
\[
\mathcal H^\infty\subseteq\mathcal H\subseteq\mathcal H^{-\infty}.
\]
Thus a distribution vector is a generalized vector acting continuously on
smooth test vectors, not necessarily an element of \(\mathcal H\).

## The Hilbert-space inclusion and topology

Use the inner product linear in its first argument. The inclusion is
\[
j(v)(w)=\langle v,w\rangle_H,\qquad v\in H,\quad w\in H^\infty.
\]
It is linear in \(v\), conjugate-linear in \(w\), and injective by density of smooth vectors. A bounded subset of the smooth-vector space is bounded in Hilbert norm, so Cauchy–Schwarz proves continuity into the strong anti-dual.

The [[lie-groups/smooth-vector-frechet-topology|defining seminorms]] control every ordered derivative, including the order-zero norm. A continuous functional is bounded by finitely many of these seminorms. This continuity requirement distinguishes distribution vectors from arbitrary algebraic functionals.

## Extended group and Lie-algebra actions

The contragredient action is defined by
\[
(\pi^{-\infty}(g)\lambda)(v)=\lambda(\pi(g^{-1})v).
\]
Differentiating on the test-vector side extends the
[[lie-groups/derived-representation-on-smooth-vectors|derived
representation]] to distribution vectors:
\[
(d\pi^{-\infty}(X)\lambda)(v)=-\lambda(d\pi(X)v).
\]
These formulas are well-defined because the original action preserves
\(\mathcal H^\infty\) continuously.

## Use in representation theory

Distribution vectors allow [[fiber-bundles/equivariant-map|equivariant maps]] to be encoded by generalized
matrix coefficients and invariant functionals. Delta distributions in
geometric realizations and automorphic distribution vectors are typical
examples. In the representation theory of real reductive groups, the passage
between smooth globalizations and their distribution duals is a basic tool;
it is broader than the Hilbert-space representation and must retain the
chosen locally convex topology.

## Point evaluation and nuclearity

In the Schrödinger model, the test space is [[lie-groups/schrodinger-smooth-vectors|Schwartz space]]. The functional \(w\mapsto\overline{w(x_0)}\) is a distribution vector, the anti-linear version of a [[functional-analysis/dirac-delta-distribution|point mass]], and is not represented by an \(L^2\) vector. The group and infinitesimal formulas above extend ordinary transport and distributional differentiation.

The triple \(H^\infty\hookrightarrow H\hookrightarrow H^{-\infty}\) exists without nuclearity. Under the nuclear convention for [[functional-analysis/rigged-hilbert-space|rigged Hilbert spaces]], it is a nuclear rigging exactly when the representation is [[lie-groups/nuclear-smooth-vectors-trace-class|trace class]]. Type I alone does not supply that extra property.

## References

1. Nolan R. Wallach, *Real Reductive Groups I*, Pure and Applied Mathematics 132, Academic Press, 1988. [WorldCat record](https://search.worldcat.org/title/15055114). Relevant: §4.4 on smooth and distribution vectors.
2. W. Casselman, “Canonical Extensions of Harish-Chandra Modules to Representations of \(G\),” *Canadian Journal of Mathematics* 41 (1989), 385–438. [DOI record](https://doi.org/10.4153/CJM-1989-019-5). Relevant: smooth globalizations and distributional duality.
3. Gerrit van Dijk, Karl-Hermann Neeb, Hadi Salmasian, and Christoph Zellner, [*On the characterization of trace class representations and Schwartz operators*](https://arxiv.org/abs/1512.02451), Lemma 1.9 and Proposition 1.11.
