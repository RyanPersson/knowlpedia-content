+++
id = "fiber-bundles/kernel-and-image-bundles-of-a-constant-rank-morphism"
title = "Kernel and image bundles of a constant-rank morphism"
kind = "definition"
summary = "The smooth subbundles formed by the pointwise kernels and images of a constant-rank vector bundle morphism."
aliases = ["kernel bundle", "image bundle", "constant-rank bundle map theorem"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/vector-bundle-morphism", "fiber-bundles/vector-subbundle", "topology/connected-component"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\Phi:E\to F\) be a smooth [[fiber-bundles/vector-bundle-morphism|vector bundle morphism]] over the identity of a manifold \(M\), and suppose the fiber maps \(\Phi_x:E_x\to F_x\) have locally constant rank. Its **kernel bundle** and **image bundle** are
\[
\ker\Phi=\coprod_{x\in M}\ker\Phi_x\subseteq E,
\qquad
\operatorname{im}\Phi=\coprod_{x\in M}\operatorname{im}\Phi_x\subseteq F.
\]
The constant-rank bundle-map theorem gives these sets unique smooth [[fiber-bundles/vector-subbundle|vector subbundle]] structures. If \(E\) and \(F\) have ranks \(e\) and \(f\), and \(\Phi\) has rank \(r\) on a [[topology/connected-component|connected component]], then their ranks are \(e-r\) and \(r\), respectively.

## Why constant rank is sufficient

In local frames, \(\Phi\) is represented by a smooth matrix-valued function. A nonvanishing \(r\times r\) minor can be used, after smooth changes of local frame, to put that matrix into block form
\[
\begin{pmatrix}I_r&0\\0&0\end{pmatrix}.
\]
The coordinate spans of the zero block and the \(I_r\) block then give smooth local frames for the kernel and image. This is the vector-bundle analogue of the constant-rank normal form.

## Exact sequences and induced isomorphism

The inclusion and projection associated with \(\Phi\) yield exact sequences
\[
0\longrightarrow\ker\Phi\longrightarrow E\longrightarrow\operatorname{im}\Phi\longrightarrow0
\]
\[
0\longrightarrow\operatorname{im}\Phi\longrightarrow F\longrightarrow F/\operatorname{im}\Phi\longrightarrow0.
\]
Fiberwise, the first isomorphism theorem induces \(E/\ker\Phi\cong\operatorname{im}\Phi\); the local block form shows that this is an isomorphism of smooth [[fiber-bundles/vector-bundle|vector bundles]], not merely a collection of vector-space isomorphisms.

## Failure when rank jumps

The constant-rank hypothesis cannot be omitted. Multiplication by \(x\) defines a morphism of trivial [[fiber-bundles/line-bundle|line bundles]] over \(\mathbb R\),
\[
(x,v)\longmapsto(x,xv).
\]
Its kernel is zero away from \(0\) and one-dimensional over \(0\), while its image has the opposite rank jump. Neither family is a vector bundle over \(\mathbb R\).

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 10, bundle homomorphisms and the vector-bundle rank theorem.
2. D. Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: Chapter 3, vector-bundle exact sequences and subbundles.
