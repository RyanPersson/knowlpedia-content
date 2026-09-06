+++
id = "algebra-rings/lcm"
title = "Least common multiple"
kind = "knowl"
summary = "A common multiple m of a and b that divides every other common multiple (defined up to associates)."
aliases = ["lcm", "Least common multiple"]
domains = ["algebra-rings"]
legacy_source_path = "algebra-rings/lcm.md"
prerequisites = ["algebra-rings/integral-domain"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(R\) be an [[algebra-rings/integral-domain|integral domain]] and let \(a,b\in R\). A **least common multiple** of \(a\) and \(b\) is an element \(m\in R\) such that:

1. \(a\mid m\) and \(b\mid m\);
2. if \(a\mid n\) and \(b\mid n\), then \(m\mid n\).

## Remarks

An lcm is unique up to [[algebra-rings/associated-elements|associates]]. In a principal ideal domain or a unique factorization domain, if \(d\) is a [[algebra-rings/gcd|gcd]] of \(a,b\) and \(m\) is an lcm, then \(dm\) is associate to \(ab\).

## Examples

- In \(\mathbb Z\), \(\operatorname{lcm}(12,18)=36\).
- In \(k[x]\), an lcm of \(x\) and \(x^2\) is \(x^2\), up to multiplication by a nonzero scalar.
- For any \(a\in R\), an lcm of \(a\) and \(0\) is \(0\).
