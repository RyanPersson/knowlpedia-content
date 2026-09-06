+++
id = "linear-algebra/vector-space"
title = "Vector space"
kind = "knowl"
summary = "A set with addition and scalar multiplication satisfying the vector space axioms."
aliases = ["vector-space", "Vector space"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/vector-space.md"
prerequisites = ["algebra-rings/field", "shared-foundations/set", "shared-foundations/function"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

A **vector space** over a [[algebra-rings/field|field]] \(\mathbb F\) is a [[shared-foundations/set|set]] \(V\) with operations ([[shared-foundations/function|functions]]) \(+:V\times V\to V\) and \(\cdot:\mathbb F\times V\to V\), and an element \(0\in V\), satisfying the following for all \(u,v,w\in V\) and \(a,b\in\mathbb F\):

- **Commutativity:** \(u+v=v+u\).
- **Associativity:** \((u+v)+w=u+(v+w)\).
- **Additive identity:** \(v+0=v\).
- **Additive inverse:** for each \(v\), there is \(-v\in V\) with \(v+(-v)=0\).
- **Distributivity over vector addition:** \(a\cdot(u+v)=a\cdot u+a\cdot v\).
- **Distributivity over scalar addition:** \((a+b)\cdot v=a\cdot v+b\cdot v\).
- **Scalar associativity:** \((ab)\cdot v=a\cdot(b\cdot v)\).
- **Scalar identity:** \(1\cdot v=v\).

## Context

Vector spaces are the basic objects studied via [[linear-algebra/linear-map|linear maps]] and invariants including the [[linear-algebra/determinant|determinant]] and [[linear-algebra/eigenvalue|eigenvalues]] of operators.

## Examples

The zero vector space, consisting only of \(0\), is allowed. The field is part
of the structure: the same additive group can be a vector space over more
than one field, but the scalar multiplication must be specified.

- \(\mathbb{R}^n\) with componentwise addition and scalar multiplication is a vector space over \(\mathbb{R}\).
- The set of polynomials \(\mathbb{F}[x]\) with the usual addition and scalar multiplication is a vector space over \(\mathbb{F}\).
- The set of \(m\times n\) matrices over \(\mathbb{F}\) is a vector space over \(\mathbb{F}\).
