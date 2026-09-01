+++
id = "convex-analysis/separation-by-a-hyperplane"
title = "Separation by a Hyperplane"
kind = "knowl"
summary = "Two sets are separable if a nonzero linear functional orders them."
aliases = ["separation-by-a-hyperplane", "Separation by a Hyperplane"]
domains = ["convex-analysis"]
prerequisites = ["linear-algebra/vector-space", "convex-analysis/hyperplane"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "convex-analysis/separation-by-a-hyperplane.md"
+++

Let \(X\) be a real [[linear-algebra/vector-space|vector space]] and let \(\Omega_1,\Omega_2\subseteq X\) be nonempty.

The sets \(\Omega_1\) and \(\Omega_2\) can be **separated by a hyperplane** if there is a nonzero linear functional \(f:X\to\mathbb R\) such that
\[
f(x)\le f(y)\quad\text{whenever }x\in\Omega_1,\ y\in\Omega_2.
\]

Equivalently,
\[
\sup_{x\in\Omega_1}f(x)\le \inf_{y\in\Omega_2}f(y).
\]
Any \(\alpha\) between these two values gives a [[convex-analysis/hyperplane|hyperplane]] \(\{x\in X:f(x)=\alpha\}\) lying between the sets.
