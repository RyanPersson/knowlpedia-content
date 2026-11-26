+++
id = "proofs/grh/reduction-main/index-bound"
title = "Index bound for a family in a twisted lattice"
kind = "definition"
summary = "A finite family has index at most delta if at each finite place one integral matrix, independent of the twist, carries it into the integral vectors, with losses summing to at most delta."
aliases = ["index at most delta", "IndexLe"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.TwistedLattice.IndexLe"]
lean_files = ["src/New/Reduction/Lattices/TwistedLattice.lean"]
+++

Let \(L\) be a [[proofs/grh/reduction-main/twisted-lattice|twisted lattice]] on \(V\), with integral vectors \(L_\iota\) at the [[proofs/grh/reduction-main/prime-padic-iso|finite places \(\iota\mid\ell\) of \(\mathbb C\)]]. Let \(y=(y_k)_{k\in S}\) be a family in \(V\) indexed by a finite set \(S\), and \(\delta\in\mathbb R\). The family \(y\) **has index at most \(\delta\)** if there are real numbers \(\delta_\ell\ge0\), one for each natural number \(\ell\), such that

1. \(\sum_{\ell\in U}\delta_\ell\log\ell\le\delta\) for every finite set \(U\) of primes, and
2. for every finite place \(\iota\mid\ell\) there is a matrix \(u\in\mathcal O_\iota^{S\times S}\) that carries \(y\) into \(L_\iota\) with loss \(\delta_\ell\): \(\lvert\det u\rvert_\iota\ge\ell^{-\delta_\ell}\) and \(\sum_ku_{ik}y_k\in L_\iota\) for all \(i\).

Because \(L_\iota\) is defined through all twists allowed at \(\ell\), the matrix \(u\) does not depend on the twist. Rules for index bounds are in [[proofs/grh/reduction-main/index-calculus|the calculus of indices]].

## References

1. Lean: `New.TwistedLattice.IndexLe` in `src/New/Reduction/Lattices/TwistedLattice.lean`.
