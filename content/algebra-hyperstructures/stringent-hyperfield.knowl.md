+++
id = "algebra-hyperstructures/stringent-hyperfield"
title = "Stringent hyperfield"
kind = "definition"
summary = "A hyperfield whose sum is single-valued unless the summands are additive inverses."
aliases = ["stringent commutative hyperfield"]
domains = ["algebra-hyperstructures", "matroid-theory"]
prerequisites = ["algebra-hyperstructures/hyperfield"]
dependency_review_count = 1
section_mode = "progressive"
+++

A [[algebra-hyperstructures/hyperfield|hyperfield]] \(F\) is **stringent** if
\[
a\ne-b\quad\Longrightarrow\quad a\boxplus b
\text{ is a singleton}
\]
for every \(a,b\in F\). Thus genuine ambiguity can occur only when adding an
element to its hyper-additive inverse.

## Examples

Every ordinary [[algebra-rings/field|field]] is stringent because all of its
sums are singletons.
The [[algebra-hyperstructures/krasner-hyperfield|Krasner]] and
[[algebra-hyperstructures/sign-hyperfield|sign]] hyperfields are stringent.
Every
[[algebra-hyperstructures/valuative-hyperfield|valuative hyperfield]] is
stringent as well: each nonzero element is its own additive inverse, unequal
inputs have the unique maximum as their sum, and only a tied sum can be
multivalued.

## Related theorems

- [[algebra-hyperstructures/doubly-distributive-hyperfields-are-stringent|Every
  doubly distributive hyperfield is stringent]], but the converse fails.
- The [[algebra-hyperstructures/classification-of-stringent-hyperfields|classification
  of stringent hyperfields]] describes them as tropical extensions with
  residue layer an ordinary field, the Krasner hyperfield, or the sign
  hyperfield.

## References

Nathan Bowler and Ting Su,
[*Classification of doubly distributive skew hyperfields and stringent hypergroups*](https://arxiv.org/abs/2003.03751).
