+++
id = "algebra-category-theory/dual-object"
title = "Dual object in a monoidal category"
kind = "definition"
summary = "Evaluation and coevaluation maps obeying the two snake identities."
aliases = ["left dual", "right dual", "snake identities"]
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/monoidal-category"]
+++

In a [[algebra-category-theory/monoidal-category|monoidal category]], a **left dual** of \(X\) consists of an object \(L\) and arrows
\[
e:L\otimes X\to\mathbb1,\qquad c:\mathbb1\to X\otimes L
\]
satisfying the two **snake identities**
\[
\rho_X(1_X\otimes e)\alpha_{X,L,X}(c\otimes1_X)\lambda_X^{-1}=1_X,
\]
\[
\lambda_L(e\otimes1_L)\alpha^{-1}_{L,X,L}(1_L\otimes c)\rho_L^{-1}=1_L.
\]
Here \(\alpha,\lambda,\rho\) are the associator and unitors, and compositions act from right to left. A **right dual** is an object \(R\) with \(e':X\otimes R\to\mathbb1\) and \(c':\mathbb1\to R\otimes X\) satisfying
\[
\lambda_X(e'\otimes1_X)\alpha^{-1}_{X,R,X}(1_X\otimes c')\rho_X^{-1}=1_X,
\]
\[
\rho_R(1_R\otimes e')\alpha_{R,X,R}(c'\otimes1_R)\lambda_R^{-1}=1_R.
\]
The maps are called **evaluation** and **coevaluation**. Left/right naming conventions vary; the displayed arrow directions fix ours.

## Snake identities as commutative diagrams

For the left dual, each detour must equal the identity arrow along the bottom. Associators and unitors are suppressed using monoidal coherence, so \(X\otimes L\otimes X\) means canonically reassociated tensor products.

```tikz-cd
X\otimes L\otimes X \arrow[r, "1_X\otimes e"] & X \\
X \arrow[u, "c\otimes1_X"] \arrow[r, "1_X"'] & X \arrow[u, equal]
```

```tikz-cd
L\otimes X\otimes L \arrow[r, "e\otimes1_L"] & L \\
L \arrow[u, "1_L\otimes c"] \arrow[r, "1_L"'] & L \arrow[u, equal]
```

## Vector-space model

For a finite-dimensional vector space \(V\), take \(L=V^*\), \(e(\varphi\otimes v)=\varphi(v)\), and \(c(1)=\sum_i v_i\otimes v_i^*\) for a basis and its dual basis. The first snake sends \(v\) to \(\sum_i v_i v_i^*(v)=v\); the other gives the corresponding reconstruction of a functional. The coevaluation is independent of the chosen basis.

A dual is not a tensor inverse: these maps need not be isomorphisms. For \(\dim V>1\), \(V^*\otimes V\) is not isomorphic to the one-dimensional unit.

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), Definitions 2.10.1–2.10.2; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
