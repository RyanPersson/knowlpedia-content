+++
id = "linear-algebra/quaternionic-vector-space"
title = "Quaternionic vector space"
kind = "definition"
summary = "A quaternionic vector space is a left or right module over the quaternion division algebra, with the scalar side fixed as part of the convention."
aliases = ["right quaternionic vector space", "ℍ-vector space"]
domains = ["linear-algebra"]
section_mode = "progressive"
+++

A **quaternionic vector space** is a vector space over the
[[linear-algebra/quaternion-division-algebra|quaternion division algebra]]
\(\mathbb H\), meaning a unital left or right \(\mathbb H\)-module. In this
knowl the default is a **right** quaternionic vector space: an abelian group
\(V\) with products \(vq\) satisfying
\[
(v+w)q=vq+wq,\qquad v(q+r)=vq+vr,\qquad (vq)r=v(qr),\qquad v1=v.
\]
Because \(\mathbb H\) is noncommutative, the side of scalar multiplication is
part of the structure. A map of right quaternionic vector spaces must satisfy
\(T(vq)=T(v)q\). No finite-dimensionality is assumed.

## Bases and dimension

As for vector spaces over any [[algebra-rings/division-ring|division ring]], a
quaternionic basis is a family in which every vector has a unique finite
right-linear expansion. A
finite-dimensional space of quaternionic dimension \(n\) is isomorphic to
\(\mathbb H^n\) and has underlying real dimension \(4n\). Right-linear
endomorphisms of column vectors in \(\mathbb H^n\) are represented by
quaternionic matrices acting on the left
[Givental, Supplement E, pp. 191–193](https://math.berkeley.edu/~giventh/la/la_15_sE.pdf).

## Passing between right and left conventions

Quaternionic conjugation converts a right space \(V\) into a left space by
defining \(q\cdot v=v\overline q\). This is a convention-changing construction,
not permission to move scalars through vectors: generally \(vq\) and \(qv\)
are not two notations for the same product. Many geometric texts choose right
modules so that matrix groups act from the left; the convention and its use in
quaternionic geometry are described in
[Salamon, §1.5](https://search.worldcat.org/title/18522302).

## Examples and near-misses

The basic example is \(\mathbb H^n\) with componentwise right scalar
multiplication. Restricting scalars along \(\mathbb C\subset\mathbb H\) gives a
complex vector space, and then along \(\mathbb R\subset\mathbb C\) a real vector
space. A real vector space equipped with one complex structure is not thereby
quaternionic: it needs compatible actions of quaternionic units \(i,j,k\) with
\(i^2=j^2=k^2=ijk=-1\).

## References

1. Simon Salamon, *Riemannian Geometry and Holonomy Groups*, Pitman Research Notes in Mathematics 201, Longman Scientific & Technical, 1989. [Library catalog record](https://search.worldcat.org/title/18522302). Relevant: §1.5 on quaternionic linear algebra and conventions used in quaternionic geometry.
2. Alexander Givental, *Linear Algebra*, Supplement E, “Quaternionic Linear Algebra.” [Author course PDF](https://math.berkeley.edu/~giventh/la/la_15_sE.pdf). Relevant: printed pp. 191–193 on handedness, conjugation, bases, and quaternionic matrices.
