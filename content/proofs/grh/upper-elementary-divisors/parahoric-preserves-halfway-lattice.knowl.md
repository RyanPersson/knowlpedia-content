+++
id = "proofs/grh/upper-elementary-divisors/parahoric-preserves-halfway-lattice"
title = "The stabiliser of an edge preserves its halfway lattice"
kind = "lemma"
summary = "For u in the parahoric subgroup, the depth scaling times rho(u) is an integral matrix times the depth scaling; for block diagonal g the two commute."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.exists_depthScaling_mul_letterRep_eq", "New.FrobeniusCycle.commute_depthScaling_letterRep", "New.FrobeniusCycle.letterMatrix_eq_zero_of_mem_levi"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Edges.lean"]
proof_status = "full"
+++

**Lemma.** Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\), \(N\ge1\), and \(\Delta=\Delta_r\) the [[proofs/grh/upper-elementary-divisors/edges-and-halfway-lattices|depth scaling]].

1. If \(u\in\mathrm{Par}_r(W)\), there is a matrix \(A\) with entries in \(O\) such that \(\Delta\,\rho_n(u)=A\,\Delta\).
2. If \(g\in\mathrm{GL}_k(W)\) is block diagonal for the blocks \(\{b<r\}\), \(\{b\ge r\}\), then \(\Delta\,\rho_n(g)=\rho_n(g)\,\Delta\).

## Proof

Let \(D_s=\operatorname{diag}(w^{\delta_r(b,s)})_b\), so \(\Delta=\bigotimes_s\operatorname{Sym}^n(D_s)\); by multiplicativity of \(\operatorname{Sym}^n\) and of the Kronecker product it suffices to treat each letter: (1) \(D_su_s=A_sD_s\) with \(A_s\in M_k(O)\); (2) \(D_sg_s=g_sD_s\).

(1) We need \(w^{\delta(j,s)}\mid w^{\delta(i,s)}(u_s)_{ij}\). If \(\delta(j,s)\le\delta(i,s)\) this is clear. Otherwise \(x_{j,s}\) is deep and \(x_{i,s}\) is not: for even \(s\), \(i<r\le j\); for odd \(s\), \(j<r\le i\). In both cases \(p=w^{2}\) divides \((u_s)_{ij}\) by [[proofs/grh/upper-elementary-divisors/maps-of-cycle-kill-maximal-ideal|the lemma on parahoric elements]], and \(w\mid w^{2}\).

(2) \((g_s)_{ij}=0\) unless \(i,j\) are in the same block (for odd \(s\) because \(g^{-1}\) is block diagonal too), and indices in the same block have the same \(\delta(\cdot,s)\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.exists_depthScaling_mul_letterRep_eq`, `New.FrobeniusCycle.commute_depthScaling_letterRep`, `New.FrobeniusCycle.letterMatrix_eq_zero_of_mem_levi` in `src/New/UpperBound/ElementaryDivisors/Edges.lean`.
