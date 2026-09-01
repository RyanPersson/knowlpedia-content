+++
id = "nonassociative-algebra/spin-factor-jordan-algebra"
title = "Spin-factor Jordan algebra"
kind = "definition"
summary = "The rank-two Euclidean Jordan algebra built from a real inner-product space."
aliases = ["spin factor", "spin-factor Jordan algebra", "Jordan spin factor"]
domains = ["nonassociative-algebra"]
prerequisites = ["linear-algebra/vector-space", "linear-algebra/inner-product", "nonassociative-algebra/euclidean-jordan-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(V\) be a finite-dimensional real inner-product space. The **spin
factor** \(J(V)\) is the real [[linear-algebra/vector-space|vector space]] \(\mathbb R\oplus V\) with product
\[
(\lambda,u)\circ(\mu,v)
=\bigl(\lambda\mu+\langle u,v\rangle,\lambda v+\mu u\bigr).
\]
Its unit is \(e=(1,0)\). With [[linear-algebra/inner-product|inner product]]
\(\langle(\lambda,u),(\mu,v)\rangle_J
=\lambda\mu+\langle u,v\rangle\), it is a
[[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]].

## Spectral data

For \(u\neq0\), the element \(x=(\lambda,u)\) has decomposition
\[
x=(\lambda+\|u\|)c_+ +(\lambda-\|u\|)c_-,
\qquad
c_\pm=\frac12\left(1,\pm\frac{u}{\|u\|}\right).
\]
Thus every nontrivial spin factor has rank \(2\), Jordan trace \(2\lambda\),
and determinant \(\lambda^2-\|u\|^2\). Its cone of squares is the Lorentz
cone \(\{(\lambda,u):\lambda\geq\|u\|\}\).

## Simplicity and symmetries

The spin factor is simple when \(\dim V\geq2\). For \(\dim V=1\), it is
isomorphic to \(\mathbb R\oplus\mathbb R\) with coordinatewise product and is
not simple. Every orthogonal transformation of \(V\) extends to an
automorphism, and all automorphisms arise this way. Hence
\(\operatorname{Aut}(J(V))\cong O(V)\).

## Hermitian degree-two models

\[
\mathfrak h_2(\mathbb R)\cong J(\mathbb R^2),\quad
\mathfrak h_2(\mathbb C)\cong J(\mathbb R^3),\quad
\mathfrak h_2(\mathbb H)\cong J(\mathbb R^5),\quad
\mathfrak h_2(\mathbb O)\cong J(\mathbb R^9).
\]
These algebras have dimensions \(3,4,6,10\), respectively.

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. [Publisher record](https://global.oup.com/academic/product/analysis-on-symmetric-cones-9780198534778).
2. Pascual Jordan, John von Neumann, and Eugene Wigner, “On an Algebraic Generalization of the Quantum Mechanical Formalism,” *Annals of Mathematics* 35 (1934), 29–64. [JSTOR record](https://www.jstor.org/stable/1968117).
