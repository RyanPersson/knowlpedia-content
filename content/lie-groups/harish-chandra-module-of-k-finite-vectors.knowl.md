+++
id = "lie-groups/harish-chandra-module-of-k-finite-vectors"
title = "Harish–Chandra module of K-finite vectors"
kind = "construction"
summary = "The algebraic representation obtained by retaining the K-finite vectors of an admissible representation."
aliases = ["underlying (g,K)-module", "K-finite module construction"]
domains = ["lie-groups", "representation-theory"]
section_mode = "progressive"
+++

Let \(G\) be a
[[lie-groups/real-reductive-lie-group|real reductive Lie group]], \(K\) a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]],
and \((\pi,V)\) an
[[lie-groups/admissible-representation-real-reductive-group|admissible]]
finite-length continuous representation in a class for which the
[[lie-groups/k-finite-vector|\(K\)-finite vectors]] are smooth. Its
**Harish–Chandra module of \(K\)-finite vectors** is
\[
V_K=\{v\in V:\dim\operatorname{span}_{\mathbb C}\pi(K)v<\infty\}.
\]
The restricted \(K\)-action and the differentiated action of
\(\mathfrak g_{\mathbb C}\) make \(V_K\) a
[[lie-groups/harish-chandra-module|Harish–Chandra module]]: it is admissible
and finitely generated over \(U(\mathfrak g_{\mathbb C})\). The construction
retains the algebraic [[lie-groups/derived-representation-on-smooth-vectors|infinitesimal representation]] while discarding the
ambient Banach, Hilbert, or Fréchet topology.

## Construction of the actions

The \(K\)-action is simply \(\pi|_K\). Smoothness lets one differentiate:
\[
d\pi(X)v=\left.\frac{d}{dt}\right|_{t=0}
\pi(\exp tX)v,
\qquad X\in\mathfrak g,\ v\in V_K.
\]
The two actions obey the covariance relation required of a
[[lie-groups/g-k-module|\((\mathfrak g_{\mathbb C},K)\)-module]], and the
differentiated action extends to the
[[lie-groups/universal-enveloping-algebra|universal enveloping algebra]].
Admissibility gives finite
\(K\)-multiplicities; finite length supplies the standard finite-generation
hypothesis [Wallach, Chapter 4].

## What the construction preserves

The passage to \(V_K\) preserves \(K\)-types, their multiplicities, invariant
infinitesimal submodules, and the action of the
[[lie-groups/center-of-universal-enveloping-algebra|center of the universal enveloping algebra]].
For irreducible admissible representations, the resulting Harish–Chandra
module is irreducible. Conversely, globalization theorems recover canonical
smooth representations from Harish–Chandra modules, but a choice of Hilbert
globalization is not part of this construction
[Knapp, Chapter VIII].

## Example and scope

For an
[[lie-groups/irreducible-unitary-representation|irreducible unitary representation]]
of \(G\), Harish–Chandra admissibility makes its \(K\)-finite subspace a
Harish–Chandra module. An arbitrary continuous representation is a near-miss:
without admissibility or finite length, its \(K\)-finite part can have
infinite \(K\)-multiplicities or fail finite generation.

**Warning.** Some authors call \(V_K\) the “underlying
\((\mathfrak g,K)\)-module” before verifying the two finiteness properties.
Here “Harish–Chandra module” includes both.

## References

1. Nolan R. Wallach, *Real Reductive Groups I*, Academic Press, 1988. [Publisher record](https://shop.elsevier.com/books/real-reductive-groups-i/wallach/978-0-12-732960-4). Relevant: Chapter 4 on admissible representations and their \(K\)-finite modules.
2. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986. [DOI record](https://doi.org/10.1515/9781400883974). Relevant: Chapter VIII on admissibility and underlying \((\mathfrak g,K)\)-modules.
