+++
id = "algebra-groups/eulers-theorem"
title = "Euler's Theorem"
kind = "knowl"
summary = "If gcd(a,n)=1 then a^{φ(n)} ≡ 1 (mod n)."
aliases = ["eulers-theorem", "Euler's Theorem"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/eulers-theorem.md"
prerequisites = ["algebra-rings/gcd", "shared-foundations/integers", "algebra-rings/group-of-units", "algebra-groups/lagranges-theorem"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Euler's theorem.** Let \(n\ge 1\) and \(a\in\mathbb Z\). If the [[algebra-rings/gcd|greatest common divisor]] of \(a\) and \(n\) is \(1\), then
\[
a^{\varphi(n)}\equiv 1\pmod n,
\]

where Euler's totient function is
\[
\varphi(n)=\bigl|\{k\in\{1,\dots,n\}:\gcd(k,n)=1\}\bigr|.
\]

Here \(x\equiv y\pmod n\) means that \(n\) divides \(x-y\).

## Remarks

This follows from [[algebra-groups/lagranges-theorem|Lagrange's theorem]] applied to the [[algebra-rings/group-of-units|group of units]] \((\mathbb Z/n\mathbb Z)^\times\), whose order is \(\varphi(n)\). The case in which \(n=p\) is prime is [[algebra-groups/fermats-little-theorem|Fermat's little theorem]].

## Examples

- For \(n=10\) and \(a=3\), \(\varphi(10)=4\) and \(3^4=81\equiv1\pmod {10}\).
- The coprimality hypothesis is essential: \(2^{\varphi(8)}=2^4\equiv0\pmod 8\).
