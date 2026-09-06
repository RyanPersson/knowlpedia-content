+++
id = "operator-algebras/transformation-group-cstar-algebra"
title = "Transformation-group C*-algebra"
kind = "definition"
summary = "The crossed-product C*-algebra obtained from a continuous action of a locally compact group on a locally compact space."
aliases = ["transformation group algebra", "crossed product of a transformation group"]
domains = ["operator-algebras"]
prerequisites = ["topology/locally-compact-space", "topology/locally-compact-group", "operator-algebras/full-crossed-product"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a [[topology/locally-compact-space|locally compact Hausdorff
space]] and let a [[topology/locally-compact-group|locally compact group]]
\(G\) act continuously on \(X\). The induced action
\(\alpha:G\to\operatorname{Aut}(C_0(X))\) is
\[
\alpha_s(f)(x)=f(s^{-1}x).
\]
The **full transformation-group \(C^*\)-algebra** of \((G,X)\) is the
[[operator-algebras/full-crossed-product|full crossed product]]
\(C_0(X)\rtimes_\alpha G\). Its reduced version is
\(C_0(X)\rtimes_{\alpha,r}G\). Thus the object records both the topology of
\(X\) and the dynamics of the action; the acting group and the action are
part of the defining data.

## Covariant description

A [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate
representation]] of \(C_0(X)\rtimes_\alpha G\) is determined by a
[[operator-algebras/covariant-representation-cstar-dynamical-system|covariant
pair]] \((\pi,U)\): a [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]] \(\pi\) of \(C_0(X)\), a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous
unitary representation]] \(U\) of \(G\), and the covariance equations
\[
U_s\pi(f)U_s^*=\pi(\alpha_s(f)).
\]
The full algebra is universal for these pairs. The reduced algebra instead
uses [[operator-algebras/regular-covariant-representation|regular covariant
representations]]. This distinction is essential when the action is not
amenable; there is always a canonical quotient from the full algebra to the
reduced one.

## Standard examples

If \(X\) is a one-point space with the trivial action, the full and reduced
transformation-group algebras are respectively the full and reduced group
\(C^*\)-algebras of \(G\). If \(G\) acts on itself by [[lie-groups/left-translation|left translation]], then
\(C_0(G)\rtimes_r G\) is naturally isomorphic to the
[[operator-algebras/compact-operator-cstar-algebra|compact operators]] on
\(L^2(G)\). More generally, transformation-group algebras are the operator
algebras attached to dynamical quotients even when the [[lie-groups/orbit-space|orbit space]] \(X/G\)
has poor separation properties.

## Conventions and scope

**Warning.** Some authors use “transformation-group \(C^*\)-algebra” only for
the full crossed product and write “reduced transformation-group
\(C^*\)-algebra” explicitly for the reduced completion. Others let the phrase
refer to either completion once a convention has been fixed. The subscript
\(r\) should therefore never be suppressed when full and reduced norms may
differ.

This construction concerns an action on a space. A general
[[operator-algebras/cstar-dynamical-system|\(C^*\)-dynamical system]] need not
arise from a commutative coefficient algebra.

## References

1. Dana P. Williams, *Crossed Products of C*-Algebras*, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: Chapters 2–3 on crossed products, covariant representations, and transformation groups.
