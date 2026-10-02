+++
id = "algebra-groups/classification-finite-simple-groups"
title = "Classification of finite simple groups"
kind = "theorem"
summary = "Finite simple groups are cyclic of prime order, alternating, of Lie type with the Tits boundary case, or one of 26 sporadic groups."
aliases = ["CFSG", "classification of finite simple groups"]
domains = ["algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/finite-group", "algebra-groups/simple-group", "algebra-groups/group-isomorphism"]
dependency_heuristic = "finite-groups-semantic-review-v1"
dependency_review_count = 1
+++

**Classification of finite simple groups.** Every [[algebra-groups/finite-group|finite]] [[algebra-groups/simple-group|simple group]] is isomorphic to a cyclic group \(C_p\) of prime order; an [[algebra-groups/alternating-group|alternating group]] \(A_n\) with \(n\geq5\); a simple group in the Lie-type classification, including the Tits group \({}^2F_4(2)'\); or one of the 26 sporadic simple groups.

## Reading the families

The [finite-group table](/catalog/finite-groups/table/) separates the two elementary families, six classical Lie-type families, ten exceptional Lie-type families, the Tits boundary case, and the 26 sporadics. Field sizes, ranks, central quotients, and small nonsimple exceptions are part of each family's constraints. The [[catalog/finite-groups/lie-type/finite-chevalley-central-quotient|split construction]] and [[catalog/finite-groups/lie-type/steinberg-fixed-point-group|twisted construction]] explain the Lie-type entries.

Some small groups have more than one family presentation. A table tile therefore names a family or a specified construction, rather than asserting that all tiles are pairwise nonisomorphic.

## What the theorem does not classify

The [[algebra-groups/jordan-holder-theorem-groups|Jordan–Hölder theorem]] makes the multiset of simple composition factors of a finite group well-defined. Those factors do not determine the original group: \(C_4\) and \(C_2\times C_2\) each have two factors isomorphic to \(C_2\), but only \(C_4\) has an element of order four.

## References

- P. J. Cameron, [Group Theory revision notes](https://maths.qmul.ac.uk/~pjc/MTHM024/gtrev.pdf), §5.4, p. 26: the classification statement; §§5.1–5.2, pp. 22–24: composition factors.
- R. Solomon, [The Classification of the Finite Simple Groups: A Progress Report](https://www.ams.org/journals/notices/201806/rnoti-p646.pdf), *Notices of the AMS* **65** (2018), pp. 646–651, especially the classification theorem on p. 648.
