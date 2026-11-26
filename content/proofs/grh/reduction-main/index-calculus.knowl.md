+++
id = "proofs/grh/reduction-main/index-calculus"
title = "Calculus of indices in a twisted lattice"
kind = "lemma"
summary = "Index bounds are monotone, independent of numbering, follow from colength bounds, and add over unions of families."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.TwistedLattice.IndexLe.mono", "New.TwistedLattice.IndexLe.of_comp_equiv", "New.TwistedLattice.indexLe_of_colengthDvd", "New.TwistedLattice.IndexLe.sumElim", "New.TwistedLattice.indexLe_card_mul"]
lean_files = ["src/New/Reduction/Lattices/TwistedLattice.lean"]
proof_status = "full"
+++

**Lemma.** Let \(L\) be a [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]] on \(V\) with integral vectors \(L_\iota\). We use [[proofs/grh/reduction-main/index-bound|index bounds]] for finite families in \(V\).

1. If \(y\) has index at most \(\delta\) and \(\delta\le\delta'\), then \(y\) has index at most \(\delta'\).
2. If \(f:S'\to S\) is a bijection and \((y_{f(k)})_{k\in S'}\) has index at most \(\delta\), then \((y_k)_{k\in S}\) has index at most \(\delta\).
3. **(From colengths.)** Let \(y_1,\dots,y_n\in V\), and let \(e_\ell\ge0\) satisfy \(\sum_{\ell\in U}e_\ell\log\ell\le\delta\) for every finite set \(U\) of primes. Suppose that for every finite place \(\iota\mid\ell\) there are an integer \(j\ge0\), \(j\le e_\ell\), and an \(\mathcal O_\iota\)-submodule \(M\subseteq V\) containing all \(y_i\) with [[proofs/grh/reduction-main/colength-divides|\(\operatorname{colen}(M,L_\iota)\mid\ell^{\,j}\)]] over \(\mathcal O_\iota\). Then \(y\) has index at most \(\delta\).
4. **(Unions.)** If \(y\) has index at most \(\delta\) and \(y'\) has index at most \(\delta'\), the concatenated family \((y,y')\) has index at most \(\delta+\delta'\).
5. **(Several sets.)** Let \(t\) be a finite index set and \(A_s\subseteq V\), \(s\in t\), subsets such that every finite family with all members in one \(A_s\) has index at most \(\delta\). Then every finite family \(y\) each of whose members lies in some \(A_s\), \(s\in t\), has index at most \(\# t\cdot\delta\).

## Proof

(1) The same \(\delta_\ell\) and matrices serve. (2) Re-index the matrices: \(u'_{ik}=u_{f^{-1}(i)f^{-1}(k)}\) has the same determinant.

(3) Take \(\delta_\ell=e_\ell\). At \(\iota\mid\ell\) the colength relation applied to the family \(y\subseteq M\) gives \(u\in\mathcal O_\iota^{n\times n}\) with \(\det u\mid\ell^{\,j}\) in \(\mathcal O_\iota\) and \(\sum_ku_{ik}y_k\in L_\iota\). By property (2) of [[proofs/grh/reduction-main/prime-padic-iso|finite places]], \(\lvert\det u\rvert_\iota\ge\ell^{-j}\ge\ell^{-e_\ell}\).

(4) Add the numbers \(\delta_\ell,\delta'_\ell\) and use block diagonal matrices (see "carrying a family with loss" in [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]]).

(5) Induction on \(\# t\). If \(t=\emptyset\) the family is empty and has index at most \(0\) (empty matrices, \(\delta_\ell=0\)). Otherwise pick \(s\in t\) and split \(y\) into the members lying in \(A_s\), of index at most \(\delta\) by hypothesis and (2), and the rest, each of which lies in some \(A_{s'}\) with \(s'\in t\setminus\{s\}\), of index at most \((\# t-1)\delta\) by induction. Conclude by (4) and (2).

## References

1. Lean: `New.TwistedLattice.IndexLe.mono`, `.of_comp_equiv`, `New.TwistedLattice.indexLe_of_colengthDvd`, `New.TwistedLattice.IndexLe.sumElim`, `New.TwistedLattice.indexLe_card_mul` in `src/New/Reduction/Lattices/TwistedLattice.lean`.
