+++
id = "arithmetic-geometry/diophantine-inequality"
title = "Diophantine inequality"
kind = "definition"
summary = "An inequality in which the unknowns are restricted to integers, rationals or other specified arithmetic data."
aliases = []
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["shared-foundations/integers", "shared-foundations/rational-numbers"]
+++

A **Diophantine inequality** asks which values in a specified arithmetic domain, often the [[shared-foundations/integers|integers]] or the [[shared-foundations/rational-numbers|rational numbers]], satisfy an inequality. For example, with integers \(a,b\) and \(b>0\), the condition
\[
\left|\sqrt{2}-\frac{a}{b}\right|<\frac{1}{b^2}
\]
asks how closely a fraction can approximate \(\sqrt{2}\) for a given denominator.

## Approximating a square root

The fraction \(7/5\) satisfies the inequality. Since \(2\cdot5^2-7^2=1\), factoring a difference of squares gives
\[
\left|\sqrt{2}-\frac75\right|
=\frac{1}{25(\sqrt{2}+7/5)}<\frac{1}{25}.
\]
The [[real-analysis/absolute-value|absolute value]] measures the distance between the two numbers. Doubling the denominator divides the permitted error by four.
