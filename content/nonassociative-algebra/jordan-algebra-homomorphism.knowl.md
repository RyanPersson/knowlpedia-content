+++
id = "nonassociative-algebra/jordan-algebra-homomorphism"
title = "Jordan algebra homomorphism"
kind = "definition"
summary = "A linear map preserving the Jordan product; preservation of units is an additional condition."
aliases = ["Jordan algebra homomorphism", "Jordan homomorphism"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
+++

Let \(J\) and \(K\) be [[nonassociative-algebra/jordan-algebra|Jordan
algebras]] over the same field. A **Jordan algebra homomorphism** is a linear
map \(\varphi:J\to K\) such that
\[
\varphi(x\circ y)=\varphi(x)\circ\varphi(y)
\qquad(x,y\in J).
\]
If both algebras are unital, \(\varphi\) is **unital** when
\(\varphi(e_J)=e_K\).

## Units are not automatic

Product preservation does not make an arbitrary homomorphism unital. For
example, inclusion of a matrix corner sends the corner unit to a proper
idempotent in the larger algebra. By contrast, a bijective homomorphism between
unital Jordan algebras necessarily sends unit to unit, since the image of the
source unit acts as a unit on every element of the target.

## Kernels and images

The kernel is a Jordan ideal: if \(x\in\ker\varphi\) and \(y\in J\), then
\(\varphi(x\circ y)=0\). The image is a
[[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]] of \(K\). An
injective homomorphism is a Jordan embedding, while a bijective one is a Jordan
isomorphism.

## Relation to associative maps

Every homomorphism of associative algebras induces a Jordan homomorphism
between their symmetrized Jordan algebras. The converse fails: a Jordan map
preserves \(xy+yx\), not necessarily the ordered product \(xy\). On matrix
algebras, transpose-type operations furnish standard Jordan symmetries that
are not associative-algebra homomorphisms.

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. [Publisher record](https://global.oup.com/academic/product/analysis-on-symmetric-cones-9780198534778).
2. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-12622-6).
