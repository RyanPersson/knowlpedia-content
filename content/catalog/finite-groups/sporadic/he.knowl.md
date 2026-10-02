+++
id = "catalog/finite-groups/sporadic/he"
title = "Held group"
kind = "definition"
summary = "The Held group, specified by a complete two-generator finite presentation."
aliases = ["He"]
domains = ["catalog", "algebra-groups", "finite-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/group-presentation", "algebra-groups/commutator"]
dependency_heuristic = "finite-catalog-semantic-core-v1"
dependency_review_count = 1
+++

The **Held group** \(\mathrm{He}\) is the group with generators \(a,b\) and the following complete [[algebra-groups/group-presentation|defining relations]]:
\[
\begin{gathered}
a^2=b^7=(ab)^{17}=1,\\
 [a,b]^6=[a,b^3]^5=1,\\
 [a,babab^{-1}abab]=1,\\
 (ab)^4ab^2ab^{-3}ababab^{-1}ab^3ab^{-2}ab^2=1.
\end{gathered}
\]
Here \([x,y]=x^{-1}y^{-1}xy\) is the [[algebra-groups/commutator|commutator]]. The presented group consists of words in \(a,b\) and their inverses, identified by these relations; multiplication is concatenation followed by this identification.

## Order and structure

This is a nonabelian finite [[algebra-groups/simple-group|simple group]], with
\[
|\mathrm{He}|=4030387200=2^{10}\cdot3^{3}\cdot5^{2}\cdot7^{3}\cdot17.
\]
It belongs to the Monster display block of the sporadic groups. This grouping records the ATLAS organization, without asserting a direct embedding into another displayed group.

## Reading the presentation

Every displayed equality is imposed on the [[algebra-groups/free-group|free group]] on the two generators. This is a full presentation; the shorter generator-order tests on the group’s main ATLAS page are only a semi-presentation. The identification with the named sporadic simple group is the cited presentation result.

## References

1. [ATLAS, Held group](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/He/), order heading.
2. [ATLAS, full presentation HeG1-P1](https://brauer.maths.qmul.ac.uk/Atlas/v3/pres/HeG1-P1), displayed relation list and [Magma source](https://brauer.maths.qmul.ac.uk/Atlas/spor/He/mag/HeG1-P1.M).
