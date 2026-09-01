+++
id = "algebra-groups/fermats-little-theorem"
title = "Fermat's Little Theorem"
kind = "knowl"
summary = "For a prime p, every integer a satisfies a^p congruent to a modulo p."
aliases = ["fermats-little-theorem", "Fermat's Little Theorem"]
domains = ["algebra-groups"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebra-groups/fermats-little-theorem.md"
+++

**Fermat's little theorem.** Let \(p\) be a prime and \(a\in\mathbb Z\). Then
\[
a^p\equiv a\pmod p.
\]

If \(p\nmid a\), this is equivalent to
\[
a^{p-1}\equiv 1\pmod p.
\]

Here \(x\equiv y\pmod p\) means that \(p\mid(x-y)\).

## Remarks

The second form follows from [[algebra-groups/lagranges-theorem|Lagrange's theorem]] applied to the [[algebra-rings/group-of-units|unit group]] \((\mathbb Z/p\mathbb Z)^\times\), which has order \(p-1\). The first form also covers the case \(p\mid a\).

## Examples

- For \(p=7\) and \(a=3\), \(3^6=729\equiv1\pmod 7\).
- If \(p\nmid a\), then \(a^{p-2}\) is a multiplicative inverse of \(a\) modulo \(p\).
