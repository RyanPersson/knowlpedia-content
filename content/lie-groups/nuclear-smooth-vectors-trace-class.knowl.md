+++
id = "lie-groups/nuclear-smooth-vectors-trace-class"
title = "Nuclear smooth vectors and trace-class representations"
kind = "theorem"
summary = "For a finite-dimensional Lie group, the smooth-vector space is nuclear exactly when the representation is trace class."
aliases = []
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/trace-class-representation", "lie-groups/smooth-vector-frechet-topology", "functional-analysis/nuclear-space"]
+++

Let \(\pi\) be a strongly continuous unitary representation of a finite-dimensional Lie group \(G\). With the [[lie-groups/smooth-vector-frechet-topology|smooth-vector Fréchet topology]],
\[
H^\infty\text{ is nuclear}
\quad\Longleftrightarrow\quad
\pi(f)\text{ is trace class for every }f\in C_c^\infty(G).
\]
In other words, [[functional-analysis/nuclear-space|nuclearity]] of \(H^\infty\) is equivalent to \(\pi\) being a [[lie-groups/trace-class-representation|trace-class representation]].

## Consequence for Hilbert-space riggings

The continuous dense inclusions
\[
H^\infty\hookrightarrow H\hookrightarrow H^{-\infty}
\]
exist for every such representation, with [[lie-groups/distribution-vectors-of-a-representation|distribution vectors]] on the right. Under the nuclear convention for a [[functional-analysis/rigged-hilbert-space|rigged Hilbert space]], this becomes a nuclear Gelfand triple precisely in the trace-class case.

## Type I is a different condition

Being a [[lie-groups/type-i-locally-compact-group|type I group]] controls decomposition into irreducible representations. It does not guarantee nuclear smooth vectors, even for every irreducible representation. For \(n\geq2\),
\[
G=\operatorname{SL}_n(\mathbb R)\ltimes\mathbb R^n
\]
is type I but has an irreducible unitary representation that is not trace class. Its smooth-vector space is therefore not nuclear. Here the [[algebra-groups/semidirect-product|semidirect product]] uses the usual linear action on \(\mathbb R^n\).

## Regularity versus summability

The [[lie-groups/nelson-laplacian|Nelson Laplacian]] controls smooth-vector regularity. The trace-class condition additionally requires a sufficiently high negative power of one plus its nonnegative self-adjoint closure to be trace class. Smoothness alone is not this summability requirement.

## References

1. Gerrit van Dijk, Karl-Hermann Neeb, Hadi Salmasian, and Christoph Zellner, [*On the characterization of trace class representations and Schwartz operators*](https://arxiv.org/abs/1512.02451). Proposition 1.11; Theorem 1.3 for the equivalent Laplacian criterion.
2. Anton Deitmar and Gerrit van Dijk, [*Trace class groups*](https://arxiv.org/abs/1501.02375). Proposition 1.9(b) for the type I counterexample.
