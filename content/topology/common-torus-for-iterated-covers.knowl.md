+++
id = "topology/common-torus-for-iterated-covers"
title = "Common torus for iterated integer coverings"
kind = "definition"
summary = "Several levels of an iterated torus map can be represented on the least active level."
aliases = ["common covering torus"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/integer-matrix-torus-cover", "shared-foundations/composition-of-functions", "shared-foundations/descent-through-surjection", "real-analysis/chain-rule-multivariable"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Let \(J\) be a nonsingular integer matrix and suppose finitely many nonnegative integer levels \(i\) occur. Put \(i_0=\min i\) and \(H=p_{J^{i_0}}(Y)\). Then every level variable has the representation
\[
p_{J^i}(Y)=p_{J^{i-i_0}}(H).
\]
Thus the torus with coordinate \(H\) is a **common torus** on which all these level functions can be compared, added, and multiplied by [[shared-foundations/composition-of-functions|pullback]].

## Bounded levels and compatibility

If \(0\le i-i_0\le D\), only finitely many matrices \(J^{i-i_0}\) occur. The chain rule therefore gives uniform constants at each fixed derivative order for these pullbacks. A function defined on the common torus need not descend to an individual higher level: that would require additional invariance under the relevant deck translations.

When the active levels vary between slow-coordinate neighborhoods, local formulas must have equal pullbacks to the original \(Y\)-torus on overlaps. This is the compatibility condition defining one global function; merely giving a smooth formula on each local common torus does not ensure it.
