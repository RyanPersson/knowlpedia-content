+++
id = "algebra-groups/quaternion-order-norm-one-group"
title = "Norm-one group of a quaternion order"
kind = "definition"
summary = "The units in a quaternion order whose reduced norm is one."
aliases = []
domains = ["algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-order", "algebra-rings/quaternion-reduced-norm", "algebra-rings/unit"]
+++

For an [[algebra-rings/quaternion-order|order]] \(\mathcal O\) in a quaternion algebra, its **norm-one group** is
\[
\mathcal O^1=\{x\in\mathcal O^\times:\operatorname{nrd}(x)=1\},
\]
where \(\mathcal O^\times\) denotes its [[algebra-rings/unit|units]] and \(\operatorname{nrd}\) is the [[algebra-rings/quaternion-reduced-norm|reduced norm]]. Multiplicativity of the reduced norm makes this a subgroup of the unit group.

## The matrix case

For \(\mathcal O=M_2(\mathcal O_K)\), the reduced norm is the determinant, hence
\[
\mathcal O^1=\operatorname{SL}_2(\mathcal O_K).
\]
This is the bridge from quaternionic constructions to Bianchi groups.

## Complex realization

Under a complex splitting, the norm-one elements map into \(\operatorname{SL}_2(\mathbb C)\). Their image in \(\operatorname{PSL}_2(\mathbb C)\) identifies the central elements \(1\) and \(-1\).

## References

1. F. W. Gehring, C. Maclachlan, G. J. Martin, and A. W. Reid, *Arithmeticity, discreteness and volume*, Transactions of the AMS 349 (1997). [Author-hosted paper](https://math.rice.edu/~ar99/ADV.pdf), §4, definition using O¹.
