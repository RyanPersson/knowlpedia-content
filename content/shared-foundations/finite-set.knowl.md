+++
id = "shared-foundations/finite-set"
title = "Finite set"
kind = "definition"
summary = "A set admitting a bijection with an initial segment of the natural numbers."
aliases = ["finiteness", "finite index set"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/natural-numbers", "shared-foundations/bijective-function"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A [[shared-foundations/set|set]] \(A\) is **finite** if there is a [[shared-foundations/natural-numbers|natural number]] \(n\) and a [[shared-foundations/bijective-function|bijection]]
\[
\{0,1,\ldots,n-1\}\longrightarrow A.
\]
For \(n=0\), the domain is empty. The unique such number \(n\) is the **cardinality** of \(A\), written \(|A|\). A set is **infinite** if it is not finite.

## Counting and enumeration

A finite set can be listed without repetition as \(a_1,\ldots,a_n\); the enumeration is a choice of order, not additional data intrinsic to the set. An indexed list can contain repetitions, so the number of its indices need not equal the number of distinct values.

## Examples

The empty set has cardinality zero. The set \(\{1,3,5\}\) has cardinality three. A finite family of sets can have an infinite union if even one member is infinite; a finite union of finite sets is finite.

## References

- [Jonathan Pila, Set Theory, Sections 2–9 and 15](https://www.maths.ox.ac.uk/system/files/attachments/SetTheoryHT18.pdf).
