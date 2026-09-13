+++
id = "linear-algebra/kronecker-delta"
title = "Kronecker delta"
kind = "definition"
summary = "A two-index symbol equal to one for matching indices and zero otherwise."
aliases = []
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["shared-foundations/first-order-logic", "shared-foundations/natural-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The **Kronecker delta** is the symbol
\[
\delta_{ij}=\begin{cases}1,&i=j,\\0,&i\ne j.\end{cases}
\]
It tests [[shared-foundations/first-order-logic|equality]] of the indices. The indices are often natural numbers, but the same definition works on any specified index set.

## Finite sums

For indices \(i,j\in\{1,\ldots,n\}\), the matrix \((\delta_{ij})\) is the identity matrix, and \(\sum_j\delta_{ij}v_j=v_i\). This discrete symbol is different from the Dirac delta distribution.
