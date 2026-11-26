+++
id = "proofs/grh/determinant-exchange/block-datum-is-sharp"
title = "The block datum is sharp for the principal level at the chosen places"
kind = "proposition"
summary = "The finite datum of a descent pair is sharp for the level J_M, with an explicit mass, so that the Rallis inner product formula applies to it."
aliases = ["block mass"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.isSharp_blockDatum", "New.DescentPair.isSharpFn_blockFn", "New.DescentPair.exists_reductionGL_eq_submatrix_of_blockFn_ne_zero", "New.DescentPair.blockMass"]
lean_files = ["src/New/Determinant/Norms/AdjointThetaLift.lean"]
proof_status = "outline"
+++

Let \(O\) be a [[?lean:New.DescentPair|descent pair]] with spaces \(W\) (rank \(r\)) and \(V=I_n\), chosen places \(M\), places of the twist \(Q\), \(t=n-r\), and let \(R=\mathcal{O}_E/\pi_MQ\). Let \(J_M\) be the subgroup of the stabiliser \(K_0\subset U(W)(\mathbb{A}_f)\) of the standard lattice consisting of the elements that reduce to \(1\) at every chosen place. The **block mass** is
\[
c_\Psi=\frac{\prod_{w\in Q}\#GL_r(k_w)\cdot\bigl(\prod_{w\in Q}q_w\bigr)^{tr}}{\#M_{n\times r}(R)\cdot\prod_{w\in M}\#GL_r(k_w)} .
\]

**Proposition.** Suppose that all signs of \(W\) agree or that \(M\cup Q\neq\varnothing\). Then the finite datum \(\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\) of the pair is [[?lean:New.SiegelWeil.IsSharp|sharp]] for the level \(J_M\) off the set \(S_0\) of the places of \(M\cup Q\) and their conjugates, for the character \(\nu_V\), with mass \(c_\Psi\). That is: its norm is nonzero; at the finite points \(g\) of \(U(W)\) that are integral off \(S_0\), the matrix coefficient \(\langle F,\omega(g)F\rangle\) of \(F=\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\) equals \(\langle F,F\rangle\) for \(g\in J_M\) and \(0\) otherwise; \(\langle F,F\rangle/[K_0:J_M]=c_\Psi\); and for every Fock vector \(v\) the datum \(v\otimes F\) is a vacuum off \(S_0\) and clean.

## Proof

Outline. By the general criterion [[?lean:New.SiegelWeil.IsSharpFn.isSharp|sharp functions give sharp data]], it suffices that the [[proofs/grh/determinant-exchange/block-datum-function-and-norm|block function]] \(\Psi_{\mathrm{bl}}\) on \(M_{n\times r}(R)\) is a [[?lean:New.SiegelWeil.IsSharpFn|sharp function]] for \(J_M\); the criterion then gives the mass as the mean of \(\lvert\Psi_{\mathrm{bl}}\rvert^2\) over all matrices divided by the index \([K_0:J_M]=\prod_{w\in M}\#GL_r(k_w)\), and the mean is computed by the [[proofs/grh/determinant-exchange/block-datum-function-and-norm|norm formula]]. The criterion itself is not reproved here. The five conditions for a sharp function are verified as follows.

* *The principal congruence subgroup modulo \(\pi_MQ\) lies in \(J_M\)*, and \(J_M\subset K_0\): an integral point that reduces to \(1\) modulo \(\pi_MQ\) reduces to \(1\) at each place of \(M\).
* *\(\Psi_{\mathrm{bl}}\neq0\)*: its squared norm is a product of positive integers by the norm formula.
* *\(J_M\) fixes the datum*: for \(k\in J_M\) the transformation law of the block datum for the pair \((k,1)\) gives the factor \(\prod_{w\in M}\psi_w(\det 1)^{-1}=1\).
* *Support*: there is a matrix \(B\) (the transpose \(\iota^{\mathsf T}\) of the inclusion matrix, an \(r\times n\) matrix) such that whenever \(\Psi_{\mathrm{bl}}(x)\neq0\), the \(r\times r\) matrix \(Bx\) is the reduction modulo \(\pi_MQ\) of an element of \(J_M\). Indeed \(\iota^{\mathsf T}x\) is the block \(x'\) of \(x\) on the rows \(\iota\). If \(\Psi_{\mathrm{bl}}(x)\ne0\) then \(x'_w=\iota^{\mathsf T}\iota=1\) for \(w\in M\) and \(\psi_w(\det x'_w)\neq0\), so \(x_w'\in GL_r(k_w)\), for \(w\in Q\). Every family in \(\prod_{w\in M\cup Q}GL_r(k_w)\) is the reduction of an integral point \(k\in K_0\) ([[?lean:New.stdLevel.exists_reduceFamily_eq|surjectivity of reduction]]); this \(k\) reduces to \(1\) on \(M\), so \(k\in J_M\), and its reduction modulo \(\pi_MQ\) is \(x'\) by the Chinese remainder theorem.

## References

1. Lean: `New.DescentPair.isSharpFn_blockFn`, `New.DescentPair.isSharp_blockDatum`, `New.DescentPair.blockMass` in `src/New/Determinant/Norms/AdjointThetaLift.lean`.
