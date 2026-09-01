+++
id = "algebra-modules/matrix-representation"
title = "Matrix representation"
kind = "knowl"
summary = "A matrix encoding a linear map relative to chosen bases."
aliases = ["matrix-representation", "Matrix representation"]
domains = ["algebra-modules"]
prerequisites = ["linear-algebra/linear-map", "linear-algebra/matrix"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-modules/matrix-representation.md"
+++

The **matrix representation** of a [[linear-algebra/linear-map|linear map]] \(T: V \to W\) with respect to bases \(\mathcal{B} = \{v_1, \ldots, v_n\}\) of \(V\) and \(\mathcal{C} = \{w_1, \ldots, w_m\}\) of \(W\) is the \(m \times n\) [[linear-algebra/matrix|matrix]] \([T]_{\mathcal{B}}^{\mathcal{C}}\) whose columns are the coordinate vectors of \(T(v_j)\) in the basis \(\mathcal{C}\).

That is, if \(T(v_j) = \sum_{i=1}^m a_{ij} w_i\), then the \((i,j)\) entry of the matrix is \(a_{ij}\).

## Properties

- **Composition**: \([ST]_{\mathcal{B}}^{\mathcal{D}} = [S]_{\mathcal{C}}^{\mathcal{D}} [T]_{\mathcal{B}}^{\mathcal{C}}\).
- **Change of basis**: If \(P\) and \(Q\) satisfy \([v]_{\mathcal B}=P[v]_{\mathcal B'}\) and \([w]_{\mathcal C}=Q[w]_{\mathcal C'}\), then \([T]_{\mathcal{B}'}^{\mathcal{C}'} = Q^{-1} [T]_{\mathcal{B}}^{\mathcal{C}} P\).
- **Similarity**: Two matrices represent the same operator (different bases) iff they are similar.

## Standard representation
For \(T: \mathbb{R}^n \to \mathbb{R}^m\), the standard matrix is \([T(e_1) \mid \cdots \mid T(e_n)]\).

## Invariants

The [[linear-algebra/rank|rank]] is independent of both basis choices. For an endomorphism \(T:V\to V\), the [[linear-algebra/determinant|determinant]] and [[linear-algebra/eigenvalue|eigenvalues]] are also independent of the basis used for both domain and codomain.
