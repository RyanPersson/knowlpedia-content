+++
id = "shared-foundations/floor-function"
title = "Floor function"
kind = "definition"
summary = "The greatest integer not exceeding a real number."
aliases = ["floor", "flooring"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/integers", "shared-foundations/real-numbers", "real-analysis/archimedean-property", "shared-foundations/well-ordering-principle"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a real number \(x\), its **floor** \(\lfloor x\rfloor\) is the unique integer satisfying
\[
\lfloor x\rfloor\le x<\lfloor x\rfloor+1.
\]
Existence follows from the [[real-analysis/archimedean-property|Archimedean property]] and the [[shared-foundations/well-ordering-principle|well-ordering of nonnegative integers]]; uniqueness follows because distinct integers differ by at least one.

## Examples and properties

\(\lfloor2.3\rfloor=2\), whereas \(\lfloor-2.3\rfloor=-3\). For every integer \(k\), \(\lfloor x+k\rfloor=\lfloor x\rfloor+k\). The function is constant on each interval \([k,k+1)\) and jumps at the integers. Holding a selected floor index fixed while differentiating another variable is different from differentiating the floor as a function of that variable.
