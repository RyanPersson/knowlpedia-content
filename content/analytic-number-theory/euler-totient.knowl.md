+++
id = "analytic-number-theory/euler-totient"
title = "Euler’s totient function"
kind = "definition"
summary = "The number of invertible residue classes modulo a positive integer."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["algebra-rings/group-of-units", "algebra-rings/quotient-ring"]
+++

For a positive integer \(q\), **Euler’s totient** \(\varphi(q)\) is the order of the [[algebra-rings/group-of-units|group of units]] of the [[algebra-rings/quotient-ring|residue ring]] \(\mathbb Z/q\mathbb Z\). Equivalently it counts the integers \(1\le a\le q\) relatively prime to \(q\).

## A modulus with two prime factors

The units modulo \(12\) are \(1,5,7,11\), so \(\varphi(12)=4\). For a [[analytic-number-theory/prime-number|prime]] \(p\), all \(p-1\) nonzero classes are units.
