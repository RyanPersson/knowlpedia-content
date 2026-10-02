+++
id = "algebra-rings/quaternion-order"
title = "Order in a quaternion algebra"
kind = "definition"
summary = "A unital integral subring that is a full finitely generated module in a quaternion algebra over a number field."
aliases = ["quaternion order", "order in a quaternion algebra"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-algebra", "algebra-rings/order-in-algebra", "algebra-fields-galois/ring-of-integers", "algebra-modules/finitely-generated-module"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(B\) be a [[algebra-rings/quaternion-algebra|quaternion algebra]] over a number field \(K\). An **order** in \(B\), in the sense of an \(\mathcal O_K\)-[[algebra-rings/order-in-algebra|order in an algebra]], is a subring \(\mathcal O\subseteq B\) containing \(1\) and \(\mathcal O_K\), where \(\mathcal O_K\) is the [[algebra-fields-galois/ring-of-integers|ring of integers]], such that \(\mathcal O\) is a finitely generated \(\mathcal O_K\)-module and spans \(B\) over \(K\).

## Example

In the split algebra \(M_2(K)\), the subring \(M_2(\mathcal O_K)\) is an order: the four matrix units give an integral module basis and span all matrices over \(K\).

## Finiteness is not freeness

Over a general number ring, a full [[algebra-modules/finitely-generated-module|finitely generated module]] need not be free. Thus “has an integral basis of four elements over \(\mathcal O_K\)” would be an unnecessarily restrictive definition.

An order is [[algebra-rings/maximal-order|maximal]] when it is contained in no larger order. Maximality is not required in the definition of an [[lie-groups/arithmetic-kleinian-group|arithmetic Kleinian group]].

## Ideals and examples

The [[catalog/arithmetic/lipschitz-order|Lipschitz]] and [[catalog/arithmetic/hurwitz-order|Hurwitz]] orders give distinct \(\mathbb Z\)-orders in the rational Hamilton algebra. Their [[algebra-rings/quaternion-order-discriminant|reduced discriminants]] distinguish them.

One-sided [[algebra-rings/quaternion-fractional-ideal|fractional ideals]] must specify left or right multiplication. Their [[algebra-rings/quaternion-ideal-class-set|class set]] generally has no ideal-multiplication group law.

## References

1. F. W. Gehring, C. Maclachlan, G. J. Martin, and A. W. Reid, *Arithmeticity, discreteness and volume*, Transactions of the AMS 349 (1997). [Author-hosted paper](https://math.rice.edu/~ar99/ADV.pdf), §4, integral orders used in the arithmetic-group construction.
