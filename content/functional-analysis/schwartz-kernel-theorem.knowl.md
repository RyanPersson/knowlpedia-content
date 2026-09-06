+++
id = "functional-analysis/schwartz-kernel-theorem"
title = "Schwartz kernel theorem"
kind = "theorem"
summary = "Every continuous operator from test functions to distributions is represented uniquely by a distributional kernel."
aliases = ["kernel theorem", "distribution kernel", "kernel theorem for distributions", "distribution kernel theorem"]
domains = ["functional-analysis", "distribution-theory"]
prerequisites = ["functional-analysis/continuous-linear-map", "functional-analysis/test-function-space", "functional-analysis/distribution", "topology/continuous-map"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\subseteq\mathbb R^m\) and \(Y\subseteq\mathbb R^n\) be open. The
**Schwartz kernel theorem** states that every
[[functional-analysis/continuous-linear-map|continuous linear map]]
\[
A:\mathcal D(Y)\longrightarrow\mathcal D'(X)
\]
from the [[functional-analysis/test-function-space|test-function space]] on
\(Y\) to the distributions on \(X\) has a unique
[[functional-analysis/distribution|distribution]]
\(K_A\in\mathcal D'(X\times Y)\) such that
\[
\langle A\varphi,\psi\rangle
=\langle K_A,\psi\otimes\varphi\rangle
\]
for all \(\varphi\in\mathcal D(Y)\) and \(\psi\in\mathcal D(X)\).
Conversely, every such \(K_A\) determines a [[topology/continuous-map|continuous map]] \(A\). The
distribution \(K_A\) is called the **Schwartz kernel** of \(A\).

## Bilinear formulation

Equivalently, every separately continuous bilinear functional on
\(\mathcal D(X)\times\mathcal D(Y)\) is evaluation against a unique
distribution on \(X\times Y\). The operator formulation follows by applying
this statement to
\((\psi,\varphi)\mapsto\langle A\varphi,\psi\rangle\). Separate continuity is
the natural hypothesis here; on test-function spaces it supplies the
hypocontinuity needed in the tensor-product formulation.

## Role of nuclearity

The theorem reflects the [[functional-analysis/nuclear-space|nuclearity]] of
the test-function space. Nuclearity identifies the completed tensor-product
topology needed to pass from bilinear functionals on
\(\mathcal D(X)\times\mathcal D(Y)\) to continuous linear functionals on
\(\mathcal D(X\times Y)\). This mechanism extends the theorem to several
other nuclear function spaces.

## Examples and scope

An integral operator with kernel \(k(x,y)\) has Schwartz kernel given by the
regular distribution induced by \(k\). Differential operators have kernels
supported on the diagonal, typically derivatives of the delta distribution.
The theorem does not assert that every kernel is a function: singular
distributional kernels are essential. On manifolds or for [[fiber-bundles/vector-bundle|vector bundles]],
one uses the corresponding test sections and density conventions.

## References

1. Laurent Schwartz, *Théorie des distributions*, Hermann, 1966. [Bibliographic record](https://catalogue.bnf.fr/ark:/12148/cb33167919f). Relevant: the kernel theorem for distributions.
2. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967. [Publisher record](https://shop.elsevier.com/books/topological-vector-spaces-distributions-and-kernels/treves/978-1-4831-9859-0). Relevant: Chapter 51 on the kernel theorem.
