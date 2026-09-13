+++
id = "shared-foundations/recursion-on-natural-numbers"
title = "Recursion on the natural numbers"
kind = "theorem"
summary = "An initial value and a specified next-step rule determine a unique sequence."
aliases = ["recursive sequence construction"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/natural-numbers", "shared-foundations/sequence", "shared-foundations/function", "shared-foundations/mathematical-induction"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a set, \(x_0\in X\), and \(F:\mathbb N\times X\to X\) a function. There exists a unique [[shared-foundations/sequence|sequence]] \((x_n)_{n\ge0}\) such that
\[
x_{n+1}=F(n,x_n)\qquad(n\ge0)
\]
with the given initial value. This is **recursion on the natural numbers**.

## Construction and uniqueness

Construct each finite list by appending the value specified by \(F\). Induction shows that these finite lists agree on overlaps; their union defines the infinite sequence. If two sequences obey the same initial value and step rule, induction gives equality at every index.

The rule must supply a value for every input it is asked to process. A procedure saying only to choose a parameter requires a proof that an admissible value exists; choosing the least admissible integer, when available, turns it into a specified rule.
