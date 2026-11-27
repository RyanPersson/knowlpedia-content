+++
id = "proofs/grh/spanning-unfolding-b/positive-type-function-is-largest-at-the-identity"
title = "A function of positive type is largest at the identity"
kind = "lemma"
summary = "A real function on a group given by inner products of a family of vectors indexed by the group is bounded by its value at the identity."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.le_apply_one_of_inner_eq", "New.sum_subgroup_filter"]
lean_files = ["src/New/Spanning/Unfolding/SquareExpansion.lean"]
proof_status = "full"
+++

**Lemma.** Let \(G\) be a group, \(V\) a complex inner product space, \(u\colon G\to V\) and \(\beta\colon G\to\mathbb{R}\) such that \(\langle u_a,u_b\rangle=\beta(a^{-1}b)\) for all \(a,b\in G\) (a [[?c:Positive-definite function on a group|function of positive type]]). Then \(\beta(s)\le\beta(1)\) for all \(s\in G\).

## Proof

\(\lVert u_a\rVert^2=\beta(a^{-1}a)=\beta(1)\) for every \(a\). By the [[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz inequality]], \(\beta(s)=\operatorname{Re}\langle u_1,u_s\rangle\le\lVert u_1\rVert\lVert u_s\rVert=\beta(1)\).

## References

1. Lean: `New.le_apply_one_of_inner_eq` in `src/New/Spanning/Unfolding/SquareExpansion.lean`.
