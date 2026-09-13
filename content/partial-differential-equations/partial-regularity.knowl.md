+++
id = "partial-differential-equations/partial-regularity"
title = "Partial regularity"
kind = "definition"
summary = "Regularity away from an exceptional set whose size is quantitatively controlled."
aliases = []
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["topology/open-set", "measure-theory/hausdorff-measure", "measure-theory/parabolic-hausdorff-measure"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

A **partial regularity theorem** specifies a class of solutions, a notion of regular point, and a bound on the size of the exceptional set of nonregular points. A typical conclusion is \(\mathcal H^s(S)=0\), using [[measure-theory/hausdorff-measure|Hausdorff measure]] or, for parabolic equations, [[measure-theory/parabolic-hausdorff-measure|parabolic Hausdorff measure]]. The regular points usually form an [[topology/open-set|open set]].

## Meaning of the conclusion

Small measure or dimension of the exceptional set does not imply that it is empty. [[fluid-dynamics/caffarelli-kohn-nirenberg-theorem|The Caffarelli–Kohn–Nirenberg theorem]] is a standard example.
