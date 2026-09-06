+++
id = "langlands/positive-loop-group"
title = "Positive loop group"
kind = "definition"
summary = "The subgroup-valued functor of G-valued loops that extend to the formal disc."
aliases = ["arc group", "L+G"]
domains = ["langlands", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/algebraic-group", "langlands/loop-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be an affine [[algebraic-geometry-foundations/algebraic-group|algebraic group]] over a field \(k\). Its **positive
loop group** is the group-valued functor
\[
L^+G(R)=G(R\lbrack\!\lbrack t\rbrack\!\rbrack)
\]
on \(k\)-algebras \(R\). The inclusion
\(R\lbrack\!\lbrack t\rbrack\!\rbrack\subset R((t))\) identifies \(L^+G\)
as a subgroup of the [[langlands/loop-group|loop group \(LG\)]].

## References

1. Georgios Pappas and Michael Rapoport, “Twisted loop groups and their
   affine flag varieties,” *Advances in Mathematics* 219 (2008), 118–198.
   [arXiv](https://arxiv.org/abs/math/0607130).
