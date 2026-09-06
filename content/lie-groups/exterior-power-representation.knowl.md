+++
id = "lie-groups/exterior-power-representation"
title = "Exterior-power representation"
kind = "construction"
summary = "The representation induced on an exterior power by applying each group element, or infinitesimally by a derivation formula."
aliases = ["exterior power of a representation", "wedge-power representation", "alternating-power representation"]
domains = ["lie-groups", "representation-theory", "linear-algebra"]
prerequisites = ["lie-groups/representation-of-a-lie-group", "algebra-modules/exterior-algebra", "lie-groups/representation-of-a-lie-algebra", "lie-groups/lie-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\rho:G\to\operatorname{GL}(V)\) be a [[lie-groups/representation-of-a-lie-group|representation of a Lie group]] and let \(k\geq0\). Its **\(k\)-th exterior-power representation** is the representation on the degree-\(k\) part of the [[algebra-modules/exterior-algebra|exterior algebra]] given by
\[
(\Lambda^k\rho)(g)(v_1\wedge\cdots\wedge v_k)
=\rho(g)v_1\wedge\cdots\wedge\rho(g)v_k.
\]

If \(d\rho:\mathfrak g\to\mathfrak{gl}(V)\) is a [[lie-groups/representation-of-a-lie-algebra|Lie-algebra representation]], the induced action is
\[
(\Lambda^k d\rho)(X)(v_1\wedge\cdots\wedge v_k)
=\sum_{j=1}^k
v_1\wedge\cdots\wedge d\rho(X)v_j\wedge\cdots\wedge v_k.
\]
Thus the [[lie-groups/lie-algebra|Lie algebra]] acts as a degree-zero derivation, while a group element acts by an algebra automorphism.

## Basic cases

The zeroth exterior power \(\Lambda^0V\) is the one-dimensional trivial representation, and \(\Lambda^1V=V\). If \(V\) has dimension \(n\), then \(\Lambda^nV\) is one-dimensional and carries the determinant character:
\[
\Lambda^n\rho(g)=\det(\rho(g)).
\]
Exterior powers above degree \(n\) vanish.

For the defining representation of \(\mathfrak{sl}_n(\mathbb C)\), the representations \(\Lambda^k\mathbb C^n\), \(1\leq k\leq n-1\), are the [[lie-groups/fundamental-representation|fundamental representations]].

## Weights

Suppose \(V\) has a basis of weight vectors \(v_1,\ldots,v_n\) with weights \(\lambda_1,\ldots,\lambda_n\). Then a nonzero wedge
\[
v_{i_1}\wedge\cdots\wedge v_{i_k}
\]
has weight \(\lambda_{i_1}+\cdots+\lambda_{i_k}\). Antisymmetry forces repeated basis vectors to vanish, which is the representation-theoretic difference between exterior and tensor powers.

## Group versus Lie algebra

Differentiating the group formula gives the displayed derivation formula. Conversely, an exterior power of a Lie-algebra representation integrates whenever the original representation does, but the global representation still belongs naturally to the same covering group as the original. Passing to a [[algebra-groups/quotient-group|quotient group]] requires its kernel to act trivially on \(\Lambda^kV\), which can occur even when it does not act trivially on \(V\).

## References

1. William Fulton and Joe Harris, *Representation Theory: A First Course*, Springer, 1991, §§6 and 15. [Publisher record](https://doi.org/10.1007/978-1-4612-0979-9).
2. Roe Goodman and Nolan R. Wallach, *Symmetry, Representations, and Invariants*, Springer, 2009, §3.1. [Publisher record](https://doi.org/10.1007/978-0-387-79852-3).
