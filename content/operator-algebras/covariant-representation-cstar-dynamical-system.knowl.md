+++
id = "operator-algebras/covariant-representation-cstar-dynamical-system"
title = "Covariant representation of a C*-dynamical system"
kind = "definition"
summary = "A compatible pair consisting of a nondegenerate representation of the coefficient algebra and a strongly continuous unitary representation of the acting group."
aliases = ["covariant pair"]
domains = ["operator-algebras", "representation-theory"]
prerequisites = ["operator-algebras/cstar-dynamical-system", "linear-algebra/hilbert-space", "operator-algebras/nondegenerate-star-homomorphism", "lie-groups/strongly-continuous-unitary-representation", "algebra-groups/group-action"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((A,G,\alpha)\) be a [[operator-algebras/cstar-dynamical-system|\(C^*\)-dynamical system]]. A **covariant representation** of \((A,G,\alpha)\) on a [[linear-algebra/hilbert-space|Hilbert space]] \(H\) is a pair \((\pi,U)\) in which \(\pi:A\to\mathcal B(H)\) is a [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate \(*\)-representation]], \(U:G\to\mathcal U(H)\) is a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]], and
\[
\pi(\alpha_s(a))=U_s\pi(a)U_s^*
\]
for every \(s\in G\) and \(a\in A\). The displayed covariance identity is the compatibility axiom relating the algebra representation to the [[algebra-groups/group-action|group action]].

## Integrated compatibility

The covariance identity is precisely what makes
\[
f\longmapsto\int_G\pi(f(s))U_s\,ds
\]
a \(*\)-representation of the [[operator-algebras/crossed-product-convolution-star-algebra|crossed-product convolution algebra]]. Completion then turns covariant pairs into nondegenerate representations of the [[operator-algebras/full-crossed-product|full crossed product]]. This correspondence is the universal role of covariant representations.

## Examples and non-examples

For the trivial action of \(G\) on \(A\), covariance says that every \(U_s\) commutes with \(\pi(A)\). The one-dimensional pair \((\operatorname{id}_{\mathbb C},U)\) is covariant for the trivial action on \(\mathbb C\) for any [[harmonic-analysis/unitary-character|continuous unitary character]] \(U\).

A representation \(\pi\) and a unitary representation \(U\) on the same Hilbert space do not form a covariant pair merely by coexisting: if conjugation by \(U_s\) fails to implement \(\alpha_s\) through \(\pi\), the covariance axiom fails.

## Conventions and scope

Some treatments permit degenerate \(\pi\), but the standard crossed-product representation correspondence uses nondegenerate representations. The phrase “covariant representation” is setting-dependent: representations of correspondences, operator systems, and dynamical systems have different covariance relations. Here it always refers to the displayed \(C^*\)-dynamical-system identity.

## References

1. Dana P. Williams, Crossed Products of \(C^*\)-Algebras, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: §2.2 on covariant representations and §2.3 on integrated forms.
2. Gert K. Pedersen, \(C^*\)-Algebras and Their Automorphism Groups, 2nd ed., Academic Press, 2018. [DOI record](https://doi.org/10.1016/C2016-0-03431-9). Relevant: §7.6 on covariant representations.
