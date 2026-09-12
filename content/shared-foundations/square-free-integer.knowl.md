+++
id = "shared-foundations/square-free-integer"
title = "Square-free integer"
kind = "definition"
summary = "An integer not divisible by the square of any prime."
aliases = ["squarefree integer", "square-free number"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/divisibility"]
+++

A nonzero integer \(d\) is **square-free** if the only positive integer \(m\) for which \(m^2\) [[shared-foundations/divisibility|divides]] \(d\) is \(m=1\). Equivalently, no prime square divides \(d\).

## Examples

The integers \(1,2,3,5,6\) are square-free; \(12\) is not, since \(4\mid12\). The sign makes no difference. Zero is excluded.

## Quadratic-field parameters

Removing square factors gives \(\mathbb Q(\sqrt{-12})=\mathbb Q(\sqrt{-3})\). Using a positive square-free parameter avoids describing the same imaginary quadratic field repeatedly.
