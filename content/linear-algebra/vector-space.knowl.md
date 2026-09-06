+++
id = "linear-algebra/vector-space"
title = "Vector space"
kind = "knowl"
summary = "A set with addition and scalar multiplication satisfying the vector space axioms."
aliases = ["vector-space", "Vector space"]
domains = ["linear-algebra"]
prerequisites = ["algebra-rings/field", "shared-foundations/set", "shared-foundations/function"]
dependency_review_count = 1
legacy_source_path = "linear-algebra/vector-space.md"
+++

A **vector space** over a [[algebra-rings/field|field]] \(\mathbb{F}\) is a [[shared-foundations/set|set]] \(V\) equipped with two operations ([[shared-foundations/function|functions]]) \(+:V\times V\to V\) and \(\cdot:\mathbb{F}\times V\to V\). The following identities hold for all \(u,v,w\in V\) and \(a,b\in\mathbb{F}\), with one common additive identity \(0\in V\):
\[
\begin{aligned}
&u+v=v+u,\qquad (u+v)+w=u+(v+w),\\
&v+0=v,\qquad \forall v\in V\ \exists\,(-v)\in V:\ v+(-v)=0,\\
&a\cdot(u+v)=a\cdot u+a\cdot v,\qquad (a+b)\cdot v=a\cdot v+b\cdot v,\\
&(ab)\cdot v=a\cdot(b\cdot v),\qquad 1\cdot v=v.
\end{aligned}
\]

The first two rows give the abelian-group laws for addition: commutativity and
associativity, then one common additive identity and an additive inverse for
each vector. The last two rows give distributivity, compatibility with field
multiplication, and the identity scalar.

## Context

Vector spaces are the basic objects studied via [[linear-algebra/linear-map|linear maps]] and invariants including the [[linear-algebra/determinant|determinant]] and [[linear-algebra/eigenvalue|eigenvalues]] of operators.

## Examples

The zero vector space, consisting only of \(0\), is allowed. The field is part
of the structure: the same additive group can be a vector space over more
than one field, but the scalar multiplication must be specified.

- \(\mathbb{R}^n\) with componentwise addition and scalar multiplication is a vector space over \(\mathbb{R}\).
- The set of polynomials \(\mathbb{F}[x]\) with the usual addition and scalar multiplication is a vector space over \(\mathbb{F}\).
- The set of \(m\times n\) matrices over \(\mathbb{F}\) is a vector space over \(\mathbb{F}\).
