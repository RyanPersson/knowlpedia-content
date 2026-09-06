+++
id = "algebra-fields-galois/value-group"
title = "Value group of a valuation"
kind = "definition"
summary = "The ordered abelian subgroup consisting of the finite values of a field valuation."
aliases = ["valuation value group"]
domains = ["algebra-fields-galois", "algebra-groups"]
prerequisites = ["algebra-fields-galois/valuation-on-a-field", "shared-foundations/surjective-function"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(v:K\to\Gamma\cup\{\infty\}\) be a
[[algebra-fields-galois/valuation-on-a-field|valuation on a field]]. Its
**value group** is the ordered abelian subgroup
\[
\Gamma_v=v(K^\times)\subseteq\Gamma.
\]
The group operation records multiplication:
\[
v(xy)=v(x)+v(y),
\]
and the order is inherited from \(\Gamma\).

Replacing the original codomain by \(\Gamma_v\cup\{\infty\}\) makes the
valuation surjective without changing its valuation ring or [[algebra-commutative/residue-field|residue field]].
Thus the value group is intrinsic to the valued field, whereas a larger
chosen codomain need not be.

## References
Irving Kaplansky, “Maximal fields with valuations,” *Duke Mathematical
Journal* 9 (1942), 303–321.
[DOI](https://doi.org/10.1215/S0012-7094-42-00922-0).
