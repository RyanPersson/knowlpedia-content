+++
id = "operator-algebras/minimal-cstar-tensor-product"
title = "Minimal C*-tensor product"
kind = "definition"
summary = "The C*-completion defined by representing two C*-algebras faithfully on separate Hilbert spaces and tensoring those representations."
aliases = ["spatial C*-tensor product", "injective C*-tensor product"]
domains = ["operator-algebras"]
section_mode = "progressive"
+++

Let \(A\) and \(B\) be [[operator-algebras/cstar-algebra|\(C^*\)-algebras]].
Choose faithful [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representations]]
\(\pi:A\to B(H)\) and \(\rho:B\to B(K)\). The **minimal \(C^*\)-tensor norm**
is
\[
\|x\|_{\min}=\|(\pi\otimes\rho)(x)\|_{B(H\otimes K)}
\qquad(x\in A\odot B),
\]
and the completion is the **minimal \(C^*\)-tensor product**
\(A\otimes_{\min}B\). The norm is independent of the chosen faithful
representations. It is the smallest [[operator-algebras/cstar-tensor-norm|
\(C^*\)-tensor norm]] on \(A\odot B\), which explains both “minimal” and the
alternative name “spatial.”

## Spatial construction

On elementary tensors the representation is
\[
(\pi\otimes\rho)(a\otimes b)=\pi(a)\otimes\rho(b).
\]
The images act on separate Hilbert-space factors and therefore commute in the
appropriate tensor-product sense. Faithfulness of \(\pi\) and \(\rho\) makes
the resulting algebraic representation faithful. The nontrivial independence
theorem says that changing either faithful representation leaves the induced
norm unchanged
[Takesaki, Chapter IV, §4].

## Functoriality and injectivity

Given [[operator-algebras/star-homomorphism|\(*\)-homomorphisms]]
\(\varphi:A\to C\) and \(\psi:B\to D\), the algebraic map
\(\varphi\odot\psi\) extends to
\[
\varphi\otimes\psi:A\otimes_{\min}B\longrightarrow
C\otimes_{\min}D.
\]
If both maps are injective, so is their minimal tensor product. This
injectivity property is one reason for the notation \(\otimes_{\min}\) and
the occasional name “injective tensor product.” It does not assert that
minimal tensoring preserves arbitrary [[algebra-modules/short-exact-sequence|short exact sequences]]; that stronger
property is exactness of a \(C^*\)-algebra.

## Standard models

For a [[topology/locally-compact-space|locally compact Hausdorff space]] \(X\),
\[
C_0(X)\otimes_{\min}B\cong C_0(X,B),
\]
where the right side consists of norm-continuous \(B\)-valued functions
vanishing at infinity. Also
\(M_n(\mathbb C)\otimes_{\min}B\cong M_n(B)\), the
[[operator-algebras/matrix-cstar-algebra|matrix \(C^*\)-algebra]] over \(B\).
These examples expose the spatial meaning: scalar functions or matrices
acquire coefficients in \(B\) without introducing an additional tensor norm.

## Conventions and scope

**Warning.** The minimal \(C^*\)-tensor product is a norm completion. For von
Neumann algebras concretely represented on \(H\) and \(K\), the spatial von
Neumann tensor product is instead the weak-operator closure of their
algebraic tensor product in \(B(H\otimes K)\). The two constructions are
related, but they are not identical.

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV, especially §4, on spatial tensor products.
2. Nathanial P. Brown and Narutaka Ozawa, *C*-Algebras and Finite-Dimensional Approximations*, Graduate Studies in Mathematics 88, American Mathematical Society, 2008. [DOI record](https://doi.org/10.1090/gsm/088). Relevant: §2.3 on C*-tensor products.
