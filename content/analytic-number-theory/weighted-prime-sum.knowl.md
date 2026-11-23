+++
id = "analytic-number-theory/weighted-prime-sum"
title = "Weighted prime sum"
kind = "definition"
summary = "A finite sum of weights over primes or prime powers up to a chosen cutoff."
aliases = ["prime sum", "truncated prime sum"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/von-mangoldt-function"]
+++

A **weighted prime sum** adds a specified quantity for each eligible prime \(p\). A common variant also counts powers \(p^k\), using the [[analytic-number-theory/von-mangoldt-function|von Mangoldt weight]]. For a weight \(w_x\) and cutoff \(x\), this variant is
\[
\sum_{n\le x}\Lambda(n)w_x(n)
=\sum_{p^k\le x}(\log p)\,w_x(p^k).
\]
The cutoff is the truncation. The weights specify how much of each term survives.

## The ramp in the post

Taking \(w_x(n)=x/n-1\) for \(n\le x\) makes terms at the cutoff vanish and gives more weight to smaller \(n\). Multiplying by a [[analytic-number-theory/dirichlet-character|Dirichlet character]] measures a different combination of residue classes. The [[analytic-number-theory/centered-prime-sum|centered sum]] also removes an explicit main term.

## References

- Levent Alpöge, [announcement, p. 3, item 5](https://alpo.ge/remark.pdf).
