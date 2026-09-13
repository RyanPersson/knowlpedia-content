+++
id = "asymptotics/comparable-functions"
title = "Comparable positive functions"
kind = "definition"
summary = "Two positive quantities bounded above and below by fixed multiples of one another."
aliases = []
domains = ["asymptotics"]
section_mode = "progressive"
prerequisites = ["asymptotics/big-o"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Positive functions \(f\) and \(g\) are **comparable**, written \(f\asymp g\), on a specified domain if constants \(0<c\le C<\infty\) satisfy
\[
cg\le f\le Cg.
\]
For an asymptotic domain these inequalities need only hold eventually. Equivalently, both \(f=O(g)\) and \(g=O(f)\), with the [[asymptotics/big-o|implicit constants]] independent of the variables declared uniform.

## Consequences

For fixed real \(a\), comparability implies \(f^a\asymp g^a\); negative powers reverse the individual inequalities. Comparability does not say that \(f/g\) has a limit.
