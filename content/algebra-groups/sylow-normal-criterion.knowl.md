+++
id = "algebra-groups/sylow-normal-criterion"
title = "Sylow normality criterion"
kind = "knowl"
summary = "If the Sylow p-subgroup is unique then it is normal"
aliases = ["sylow-normal-criterion", "Sylow normality criterion"]
domains = ["algebra-groups"]
prerequisites = ["algebra-groups/group", "algebra-groups/sylow-subgroup", "algebra-groups/normal-subgroup"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-groups/sylow-normal-criterion.md"
+++

**Proposition (If \(n_p=1\) then the Sylow p-subgroup is normal).**
Let \(G\) be a finite [[algebra-groups/group|group]] and let \(p\) be a prime dividing \(|G|\). Let \(P\) be a [[algebra-groups/sylow-subgroup|Sylow p-subgroup]] of \(G\), and let \(n_p\) denote the number of Sylow \(p\)-subgroups of \(G\).
If \(n_p=1\), then \(P\) is a [[algebra-groups/normal-subgroup|normal subgroup]] of \(G\).

## Remarks

**Context.**
Conjugation sends Sylow \(p\)-subgroups to Sylow \(p\)-subgroups (and in fact they are all conjugate by [[algebra-groups/sylows-second-theorem|Sylow's second theorem]]). If there is only one, it must be fixed by conjugation.
