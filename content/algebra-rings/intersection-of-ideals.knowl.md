+++
id = "algebra-rings/intersection-of-ideals"
title = "Intersection of ideals"
kind = "knowl"
summary = "The set-theoretic intersection of two ideals, which is again an ideal."
aliases = ["intersection-of-ideals", "Intersection of ideals"]
domains = ["algebra-rings"]
prerequisites = ["algebra-rings/ring", "shared-foundations/intersection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-rings/intersection-of-ideals.md"
+++

Given ideals \(I,J\) in a [[algebra-rings/ring|ring]] \(R\), their **intersection** is the set-theoretic [[shared-foundations/intersection|intersection]] \(I\cap J=\{x\in R:x\in I\text{ and }x\in J\}\).

## Remarks

The intersection \(I\cap J\) is again an [[algebra-rings/ideal|ideal]], and it is the largest ideal contained in both \(I\) and \(J\). Intersections appear naturally in primary decomposition and in comparing congruence conditions.

## Examples

- In \(\mathbb Z\), \((m)\cap (n)=(\operatorname{lcm}(m,n))\), where \(\operatorname{lcm}\) is the [[algebra-rings/lcm|lcm]].
- In \(k[x,y]\), \((x)\cap (y)=(xy)\).
- If \(I\subseteq J\), then \(I\cap J=I\).
