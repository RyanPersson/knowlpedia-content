+++
id = "algebra-category-theory/fusion-category"
title = "Fusion category"
kind = "definition"
summary = "A finite semisimple linear rigid monoidal category with simple tensor unit."
aliases = []
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/k-linear-category", "algebra-category-theory/semisimple-category", "algebra-category-theory/rigid-category", "algebra-category-theory/simple-object"]
+++

Fix an algebraically closed field \(k\). A **fusion category over \(k\)** is an essentially small [[algebra-category-theory/k-linear-category|\(k\)-linear]] [[algebra-category-theory/semisimple-category|semisimple abelian category]] with a [[algebra-category-theory/rigid-category|rigid monoidal structure]], such that:

1. each vector space \(\operatorname{Hom}(X,Y)\) is finite-dimensional;
2. there are finitely many isomorphism classes of [[algebra-category-theory/simple-object|simple objects]];
3. the tensor product is \(k\)-bilinear on morphisms;
4. the tensor unit \(\mathbb1\) is simple.

Here semisimplicity means every object is a **finite** direct sum of simples. Essentially small means that the isomorphism classes of objects form a set. Many treatments additionally assume \(\operatorname{char}k=0\); that assumption will be stated whenever needed here.

## Unpacking the bundle

| Ingredient | What it lets you do |
| --- | --- |
| [[algebra-category-theory/abelian-category|Abelian]] | Form kernels, cokernels, and exact sequences. |
| [[algebra-category-theory/k-linear-category|\(k\)-linear]] | Add and scale parallel arrows. |
| [[algebra-category-theory/semisimple-category|Semisimple]] | Decompose objects into finite sums of simple pieces. |
| [[algebra-category-theory/monoidal-category|Monoidal]] | Tensor objects and arrows, with coherent associativity and unit maps. |
| [[algebra-category-theory/rigid-category|Rigid]] | Evaluate and coevaluate left and right duals. |
| Finiteness and simple unit | Use a finite list of simple building blocks and an indecomposable tensor identity. |

Neither [[algebra-category-theory/braided-monoidal-category|braiding]] nor symmetry is required. Forgetting the simple-unit condition gives a [[algebra-category-theory/multifusion-category|multifusion category]]. Equivalently, a fusion category is a semisimple [[algebra-category-theory/finite-tensor-category|finite tensor category]].

## Fusion of simple objects

Choose simple representatives \(S_0=\mathbb1,S_1,\ldots,S_r\). Their tensor products decompose as
\[
S_i\otimes S_j\cong\bigoplus_{\ell=0}^{r}S_\ell^{\oplus N_{ij}^{\ell}},
\qquad N_{ij}^{\ell}=\dim_k\operatorname{Hom}(S_\ell,S_i\otimes S_j).
\]
The nonnegative integers \(N_{ij}^{\ell}\) are the fusion multiplicities. These integers do not specify the associator; the monoidal coherence data remain part of the category.

## Examples

Finite-dimensional \(k\)-vector spaces form a fusion category with one simple class. For a finite group \(G\) and \(\operatorname{char}k=0\), finite-dimensional representations of \(G\) give another example.

Finite-dimensional \(G\)-graded vector spaces, with \((V\otimes W)_g=\bigoplus_{ab=g}V_a\otimes W_b\), give an example for any finite group \(G\). Simples are one-dimensional spaces concentrated in a single degree. If \(G\) is nonabelian, this category cannot be braided: the simple tensor products in degrees \(gh\) and \(hg\) would otherwise have to be isomorphic.

## The unit and the ground field

Under the hypotheses above, simplicity of \(\mathbb1\) is equivalent to \(\operatorname{End}(\mathbb1)\cong k\). In a semisimple category, a decomposition into two nonzero summands gives a nontrivial idempotent endomorphism, so an endomorphism algebra equal to \(k\) forces simplicity. Conversely, simplicity, finite-dimensional Hom spaces, and algebraic closure force its endomorphisms to be scalars. The finite-dimensionality and ground-field assumptions should not be dropped from that converse.

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), §4.1 and §4.9; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
