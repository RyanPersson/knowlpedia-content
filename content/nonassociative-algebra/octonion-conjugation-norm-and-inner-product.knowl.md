+++
id = "nonassociative-algebra/octonion-conjugation-norm-and-inner-product"
title = "Octonion conjugation, norm, and inner product"
kind = "definition"
summary = "The canonical involution and Euclidean geometry carried by the octonions."
aliases = ["octonion conjugation", "octonion norm", "octonion inner product"]
domains = ["nonassociative-algebra"]
prerequisites = ["linear-algebra/inner-product", "linear-algebra/vector-space", "linear-algebra/bilinear-form", "linear-algebra/orthogonal-complement"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Every octonion \(x\in\mathbb O\) splits uniquely as \(x=\operatorname{Re}(x)+\operatorname{Im}(x)\), with real and imaginary parts. Its **conjugate**, **norm**, and **inner product** are
\[
 x^*=\operatorname{Re}(x)-\operatorname{Im}(x),
 \qquad
 N(x)=xx^*=x^*x=\lVert x\rVert^2,
 \qquad
 \langle x,y\rangle=\operatorname{Re}(xy^*).
\]
The last formula is the standard Euclidean [[linear-algebra/inner-product|inner product]] on the eight-dimensional real [[linear-algebra/vector-space|vector space]] \(\mathbb O\).

## Identities

Conjugation is a real-linear involutive antiautomorphism:
\[
 (x^*)^*=x,
 \qquad
 (xy)^*=y^*x^*.
\]
The quadratic norm composes,
\[
 N(xy)=N(x)N(y),
\]
and hence \(\lVert xy\rVert=\lVert x\rVert\lVert y\rVert\). Every nonzero octonion has the two-sided inverse
\[
 x^{-1}=\frac{x^*}{N(x)}.
\]

## Polarization and conventions

One also encounters
\[
 \langle x,y\rangle
 =\frac12\bigl(N(x+y)-N(x)-N(y)\bigr)
 =\frac12(xy^*+yx^*).
\]
The final expression is real, so it is identified with a scalar multiple of the unit. Some composition-algebra texts define the polar form without the factor \(1/2\); their trace [[linear-algebra/bilinear-form|bilinear form]] is therefore twice the Euclidean inner product.

## Orthogonal splittings

The imaginary octonions are the [[linear-algebra/orthogonal-complement|orthogonal complement]] of \(1\), giving
\[
 \mathbb O=\mathbb R1\oplus\operatorname{Im}(\mathbb O).
\]
After choosing a unit imaginary octonion \(i\), the copy \(\mathbb C=\operatorname{span}_{\mathbb R}\{1,i\}\) has a six-dimensional orthogonal complement, yielding the [[nonassociative-algebra/octonions-as-complex-vectors|model \(\mathbb O\cong\mathbb C\oplus\mathbb C^3\)]].

## References

1. John C. Baez, “The Octonions,” *Bulletin of the American Mathematical Society* **39** (2002), 145–205. [DOI record](https://doi.org/10.1090/S0273-0979-01-00934-X). Relevant: §§2.1–2.2.
2. John H. Conway and Derek A. Smith, *On Quaternions and Octonions*, A K Peters, 2003. [DOI record](https://doi.org/10.1201/9781439864180). Relevant: Chapters 3–4.
