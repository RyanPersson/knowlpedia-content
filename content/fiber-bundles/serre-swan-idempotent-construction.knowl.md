+++
id = "fiber-bundles/serre-swan-idempotent-construction"
title = "Vector bundle from an idempotent matrix"
kind = "definition"
summary = "The vector bundle formed by the pointwise images of a smooth idempotent matrix."
aliases = ["idempotent projector bundle", "image bundle of a smooth projector"]
domains = ["fiber-bundles", "algebra-modules"]
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]], let \(\mathbb F=\mathbb R\) or \(\mathbb C\), and let
\[
p\in M_n\!\left(C^\infty(M,\mathbb F)\right)
\qquad\text{satisfy}\qquad
p^2=p.
\]
Here \(C^\infty(M,\mathbb F)\) is the [[differential-geometry/algebra-of-smooth-functions|algebra of smooth \(\mathbb F\)-valued functions]].
The **[[fiber-bundles/vector-bundle|vector bundle]] defined by \(p\)** is
\[
E_p:=
\{(x,v)\in M\times\mathbb F^n:p(x)v=v\}
=
\coprod_{x\in M}\operatorname{im}p(x).
\]
Because a smooth [[algebra-rings/idempotent-element|idempotent]] has locally constant rank, these images form a smooth [[fiber-bundles/vector-subbundle|vector subbundle]] of the trivial bundle. Its complementary subbundle is \(E_{1-p}\), and \(E_p\oplus E_{1-p}=M\times\mathbb F^n\).

## Sections and projective modules

A [[fiber-bundles/section-of-a-fiber-bundle|smooth section]] of \(E_p\) is precisely a smooth function \(s:M\to\mathbb F^n\) satisfying \(ps=s\). Hence
\[
\Gamma(E_p)\cong p\,C^\infty(M,\mathbb F)^n.
\]
This module is a direct summand of the [[algebra-modules/free-module|free module]] \(C^\infty(M,\mathbb F)^n\), so it is a finitely generated [[algebra-modules/projective-module|projective module]]. Conversely, every finitely generated projective module is the image of an idempotent endomorphism of a finite free module. This is the concrete reconstruction step in the Serre–Swan correspondence.

## Geometry of the construction

The kernel of \(p(x)\) equals the image of \(1-p(x)\), giving a smooth complement even when \(p\) is not self-adjoint. If \(p\) is self-adjoint for the standard [[linear-algebra/inner-product|inner product]], then \(p(x)\) is the [[linear-algebra/orthogonal-projection|orthogonal projection]] onto \(E_{p,x}\).

For \(M=S^m\subset\mathbb R^{m+1}\), the matrix
\[
p(x)=I-xx^{\mathsf T}
\]
is a smooth self-adjoint idempotent whose image is \(T_xS^m\). Thus the [[fiber-bundles/tangent-bundle|tangent bundle]] of a sphere appears directly as an [[fiber-bundles/kernel-and-image-bundles-of-a-constant-rank-morphism|image bundle]].

## Scope and near-misses

The construction itself works on any smooth manifold. For a connected
finite-dimensional Hausdorff second-countable manifold, every finite-rank
smooth bundle is obtained from such a finite idempotent, with no compactness
assumption. For a disconnected base, finitely generated projective modules
correspond to bundles whose ranks across components are globally bounded.
Changing from \(C^\infty(M,\mathbb F)\) to an algebra of functions with a
condition at infinity changes the relevant module category.

A smooth matrix with varying rank does not define a vector bundle by taking images. For example, \(q(x)=[x]\) on \(\mathbb R\) has jumping image dimension at \(0\), and it fails the decisive axiom \(q^2=q\). The term “projector” here means idempotent, not necessarily orthogonal.

## References

1. Richard G. Swan, “Vector Bundles and Projective Modules,” *Transactions of the American Mathematical Society* 105 (1962), 264–277. [DOI record](https://doi.org/10.1090/S0002-9947-1962-0143225-6). Relevant: §§1–3, section modules and the vector-bundle/projective-module correspondence.
2. Max Karoubi, *K-Theory: An Introduction*, Springer, 1978. [DOI record](https://doi.org/10.1007/978-3-540-79890-3). Relevant: Chapter I, vector bundles, projective modules, and idempotents.
