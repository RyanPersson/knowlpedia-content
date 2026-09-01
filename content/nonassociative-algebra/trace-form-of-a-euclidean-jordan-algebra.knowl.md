+++
id = "nonassociative-algebra/trace-form-of-a-euclidean-jordan-algebra"
title = "Trace form of a Euclidean Jordan algebra"
kind = "definition"
summary = "The canonical positive-definite associative bilinear form obtained from the Jordan trace."
aliases = ["Jordan trace form", "trace form of a Euclidean Jordan algebra", "canonical trace inner product"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/euclidean-jordan-algebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(J\) be a [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean
Jordan algebra]]. Its **Jordan trace form** is
\[
\tau(x,y)=\operatorname{tr}_J(x\circ y),
\]
where \(\operatorname{tr}_J(x)\) is the sum of the Jordan eigenvalues of \(x\).

## Fundamental properties

The form \(\tau\) is symmetric, positive definite, and associative:
\[
\tau(x\circ y,z)=\tau(x,y\circ z).
\]
Thus it is a canonical compatible Euclidean [[linear-algebra/inner-product|inner product]]. A Euclidean Jordan
algebra may be presented with another compatible inner product; on each simple
ideal, every such form is a positive scalar multiple of the canonical trace
form. Different simple summands may carry different positive scalings.

## Matrix and spin-factor cases

On \(\mathfrak h_n(\mathbb R)\), \(\mathfrak h_n(\mathbb C)\), and
\(\mathfrak h_n(\mathbb H)\), the Jordan trace is the ordinary real matrix
trace, and
\[
\tau(X,Y)=\operatorname{Re}\operatorname{Tr}(XY).
\]
For \(J(V)=\mathbb R\oplus V\),
\[
\operatorname{tr}_J(\lambda,u)=2\lambda,\qquad
\tau((\lambda,u),(\mu,v))
=2(\lambda\mu+\langle u,v\rangle).
\]

## Operator-trace convention

Another [[linear-algebra/bilinear-form|bilinear form]], also sometimes called “the trace form,” is
\[
\beta(x,y)=\operatorname{Tr}(L_{x\circ y}),
\qquad L_x(z)=x\circ z.
\]
Here \(\operatorname{Tr}\) is the trace of a vector-space endomorphism. On a
[[nonassociative-algebra/simple-euclidean-jordan-algebra|simple Euclidean Jordan algebra]] of dimension \(N\) and rank \(r\),
\[
\beta(x,y)=\frac Nr\,\tau(x,y).
\]
The conventions differ only by a positive factor on each simple ideal, but a
formula should identify its normalization.

Every Jordan automorphism preserves spectral eigenvalues and hence
\(\operatorname{tr}_J\) and \(\tau\). This realizes
\(\operatorname{Aut}(J)\) as a closed subgroup of the [[lie-groups/orthogonal-group|orthogonal group]] of the
trace form.

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. [Publisher record](https://global.oup.com/academic/product/analysis-on-symmetric-cones-9780198534778).
2. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-12622-6).
