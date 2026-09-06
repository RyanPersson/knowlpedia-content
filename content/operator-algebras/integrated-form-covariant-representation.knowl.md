+++
id = "operator-algebras/integrated-form-covariant-representation"
title = "Integrated form of a covariant representation"
kind = "definition"
summary = "The representation of a crossed-product convolution algebra obtained by integrating a covariant pair."
aliases = ["integrated covariant representation", "pi cross U"]
domains = ["operator-algebras", "representation-theory"]
prerequisites = ["operator-algebras/covariant-representation-cstar-dynamical-system", "harmonic-analysis/haar-measure", "operator-algebras/crossed-product-convolution-star-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \((\pi,U)\) be a [[operator-algebras/covariant-representation-cstar-dynamical-system|covariant representation]] of \((A,G,\alpha)\) on \(H\), and fix a left [[harmonic-analysis/haar-measure|Haar measure]] on \(G\). Its **integrated form**, written \(\pi\rtimes U\), is the operator-valued map on the [[operator-algebras/crossed-product-convolution-star-algebra|convolution \(*\)-algebra \(C_c(G,A)\)]] defined by
\[
(\pi\rtimes U)(f)
=\int_G\pi(f(s))U_s\,ds.
\]
The integral is understood weakly, equivalently as a strong operator integral on compact support. Covariance implies that \(\pi\rtimes U\) preserves convolution and involution, so it is a nondegenerate \(*\)-representation and is bounded for the full crossed-product norm.

## Representation correspondence

The integrated form therefore extends uniquely to a [[operator-algebras/nondegenerate-star-homomorphism|nondegenerate representation]] of the [[operator-algebras/full-crossed-product|full crossed product]] \(A\rtimes_\alpha G\). Conversely, every nondegenerate representation of \(A\rtimes_\alpha G\) determines a unique covariant pair, and reintegration recovers the original representation. This gives a bijection, compatible with unitary equivalence, between covariant representations of \((A,G,\alpha)\) and nondegenerate representations of the full crossed product.

## How the formula encodes covariance

Formally, the crossed product contains compatible copies of \(A\) and \(G\) in its [[operator-algebras/multiplier-algebra|multiplier algebra]]. The integrated form sends these copies to \(\pi(a)\) and \(U_s\). For \(f\in C_c(G,A)\), the factor \(\pi(f(s))\) represents the coefficient at \(s\), while \(U_s\) represents the group element; integration combines them into one bounded operator.

For a discrete group the integral becomes the finite sum
\[
(\pi\rtimes U)(f)=\sum_{s\in G}\pi(f(s))U_s.
\]
Omitting the unitary factors would generally lose the [[algebra-groups/group-action|group action]] and would not represent the crossed-product convolution.

## Conventions and scope

The order \(\pi(f(s))U_s\) matches the covariance and convolution conventions used here. Sources using the opposite covariance identity or a right Haar measure may display a different-looking formula. The notation \(\pi\rtimes U\) denotes the integrated representation, not the crossed-product algebra itself.

## References

1. Dana P. Williams, Crossed Products of \(C^*\)-Algebras, Mathematical Surveys and Monographs 134, American Mathematical Society, 2007. [DOI record](https://doi.org/10.1090/surv/134). Relevant: §2.3, Proposition 2.23 on integrated forms, and §2.4, Proposition 2.40 on the representation correspondence.
