+++
id = "algebra-groups/binary-tetrahedral-group"
title = "Binary tetrahedral group"
kind = "definition"
summary = "The group of twenty-four unit quaternions lifting the rotational symmetries of a tetrahedron."
aliases = ["2T", "binary tetrahedral group of order 24", "Hurwitz unit group"]
domains = ["algebra-groups"]
section_mode = "progressive"
prerequisites = ["linear-algebra/quaternion-division-algebra"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
The **binary tetrahedral group** \(2T\) is the following subgroup of the multiplicative group of real [[linear-algebra/quaternion-division-algebra|quaternions]]:
\[
2T=\{\pm1,\pm i,\pm j,\pm k\}
\cup
\left\{\frac{\varepsilon_0+\varepsilon_1i+\varepsilon_2j+\varepsilon_3k}{2}:\varepsilon_r\in\{1,-1\}\right\}.
\]
All sixteen sign choices occur in the second set. These twenty-four elements have norm \(1\), and their multiplication is quaternion multiplication.

## Structure

Its first eight elements form the normal [[algebra-groups/quaternion-group|quaternion subgroup]] \(Q_8\). The element \((-1+i+j+k)/2\) has order \(3\) and conjugates the three quaternion axes cyclically, giving \(2T\cong Q_8\rtimes C_3\).

Conjugation on pure quaternions realizes
\[
2T/\{\pm1\}\cong A_4,
\]
the rotational tetrahedral group. Also \(2T\cong\operatorname{SL}_2(\mathbb F_3)\). Thus the binary group has order \(24\), while its rotation quotient has order \(12\).

## Arithmetic realization

This is the full unit group of the [[catalog/arithmetic/hurwitz-order|Hurwitz quaternion order]]. The half-integral quaternions are essential: the [[catalog/arithmetic/lipschitz-order|Lipschitz order]] has only the eight units in \(Q_8\).

## References

1. John Voight, *Quaternion Algebras*, [§11.2](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_11), Lemma 11.2.1 and §§11.2.2–11.2.4.
