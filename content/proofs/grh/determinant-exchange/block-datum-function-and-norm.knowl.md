+++
id = "proofs/grh/determinant-exchange/block-datum-function-and-norm"
title = "The block datum as a function of residue matrices, and its squared norm"
kind = "lemma"
summary = "The finite datum of a descent pair is the vacuum datum of an explicit function of matrices modulo the product of the chosen places and the places of the twist; the sum of its squared absolute values is computed."
aliases = ["block function"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.blockFn", "New.DescentPair.blockDatum_eq_vacuumDatum", "New.DescentPair.bijective_map_levelResidueAt", "New.DescentPair.blockFn_normSq", "New.card_isUnit_submatrix", "New.star_mulChar_det_mul_self"]
lean_files = ["src/New/Determinant/Norms/AdjointThetaLift.lean"]
proof_status = "full"
+++

Let \(O\) be a [[?lean:New.DescentPair|descent pair]] over a CM field \(E\): two finite families \(M\) (chosen places) and \(Q\) (places of the twist) of finite places, with [[algebra-commutative/residue-field|residue fields]] \(k_w\) of cardinality \(q_w\); index sets \(r\subset n\) of the bases of \(W\) and \(V\) (via the embedding \(\iota\) of the pair), of cardinalities \(r<n\), with \(t=n-r\); and [[?c:Multiplicative character of a finite field|multiplicative characters]] \(\psi_w\) of \(k_w\) (extended by \(0\) at \(0\)). Let \(\pi_MQ\) denote the product of the primes of \(M\) and \(Q\) ([[?lean:New.LevelPlaces.levelModulus|level modulus]] with exponent \(1\)) and \(R=\mathcal{O}_E/\pi_MQ\).

**Definition (block function).** For an \(n\times r\) matrix \(x\) over \(R\), with reductions \(x_w\) over \(k_w\),
\[
\Psi_{\mathrm{bl}}(x)=\begin{cases}\displaystyle\prod_{w\in Q}\psi_w\bigl(\det x_w'\bigr)&\text{if }x_w=\iota\text{ for all }w\in M,\\[1ex]0&\text{otherwise,}\end{cases}
\]
where \(x_w'\) is the \(r\times r\) block of \(x_w\) on the rows in the image of \(\iota\), and \(\iota\) also denotes the \(n\times r\) inclusion matrix.

**Lemma.**

1. The [[?lean:New.DescentPair.blockDatum|finite datum]] \(\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\) of the pair, defined with matrices modulo \(\pi_M^2Q\), is the [[?lean:New.vacuumDatum|vacuum datum]] of the block function modulo \(\pi_MQ\).
2. \(\displaystyle\sum_{x\in M_{n\times r}(R)}\lvert\Psi_{\mathrm{bl}}(x)\rvert^2=\prod_{w\in Q}\#GL_r(k_w)\cdot\Bigl(\prod_{w\in Q}q_w\Bigr)^{tr}.\)

## Proof

(1) The two moduli have the same set of places, and both functions factor through the reductions of a matrix at these places; the vacuum datum of a function that factors through the residue fields does not depend on the modulus used to write it.

(2) The places of \(M\) and \(Q\) are pairwise distinct, so by the [[algebra-rings/chinese-remainder-theorem|Chinese remainder theorem]] reduction is a bijection from \(M_{n\times r}(R)\) to \(\prod_{w\in M\cup Q}M_{n\times r}(k_w)\) (it is injective, and both sides have the same cardinality). For a multiplicative character \(\psi\) of a finite field and a square matrix \(X\), \(\lvert\psi(\det X)\rvert^2\) is \(1\) if \(X\) is invertible and \(0\) otherwise. Hence \(\lvert\Psi_{\mathrm{bl}}(x)\rvert^2\) is the product of the indicator of \(x_w=\iota\) over \(w\in M\) and the indicator of "\(x_w'\) invertible" over \(w\in Q\), and the sum is the product of the local sums. The local sum at \(w\in M\) is \(1\). At \(w\in Q\) it is the number of \(n\times r\) matrices over \(k_w\) whose block on the rows \(\iota\) is invertible: the block is an arbitrary element of \(GL_r(k_w)\) and the other \(t\) rows are free, which gives \(\#GL_r(k_w)\cdot q_w^{tr}\).

## References

1. Lean: `New.DescentPair.blockFn`, `New.DescentPair.blockDatum_eq_vacuumDatum`, `New.DescentPair.blockFn_normSq` in `src/New/Determinant/Norms/AdjointThetaLift.lean`.
