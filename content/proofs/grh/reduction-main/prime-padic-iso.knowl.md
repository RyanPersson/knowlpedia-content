+++
id = "proofs/grh/reduction-main/prime-padic-iso"
title = "Finite place of the complex numbers: a prime with an isomorphism to the algebraic closure of the l-adic numbers"
kind = "definition"
summary = "A pair of a prime l and a field isomorphism from C to an algebraic closure of Q_l, with its absolute value, valuation ring and conjugate."
aliases = ["PrimePadicIso", "l-adic place of the complex numbers"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.PrimePadicIso", "New.PrimePadicIso.conj", "New.PrimePadicIso.place", "New.PrimePadicIso.integers", "New.PrimePadicIso.norm_place", "New.PrimePadicIso.inv_pow_le_norm_of_dvd", "New.conjAut"]
lean_files = ["src/New/Reduction/Lattices/Heights.lean", "src/New/Reduction/Lattices/TwistedLattice.lean"]
+++

A **finite place of \(\mathbb C\)** (in this proof) is a pair \(\iota=(\ell,\iota)\) consisting of a prime number \(\ell\) and a [[?c:field isomorphism|field isomorphism]]
\[
\iota:\ \mathbb C\ \xrightarrow{\ \sim\ }\ \overline{\mathbb Q}_\ell
\]
onto an [[algebra-fields-galois/algebraic-closure|algebraic closure]] of the field \(\mathbb Q_\ell\) of [[?c:p-adic number|\(\ell\)-adic numbers]]. We write \(\iota\mid\ell\). Such isomorphisms exist because both fields are algebraically closed of characteristic \(0\) and of the cardinality of the continuum; they are not continuous.

Attached to \(\iota\mid\ell\):

- the **absolute value** \(\lvert x\rvert_\iota:=\lvert\iota(x)\rvert_\ell\) on \(\mathbb C\), where \(\lvert\cdot\rvert_\ell\) is the unique extension to \(\overline{\mathbb Q}_\ell\) of the [[?c:p-adic absolute value|\(\ell\)-adic absolute value]] with \(\lvert\ell\rvert_\ell=\ell^{-1}\);
- the **valuation ring** \(\mathcal O_\iota:=\{x\in\mathbb C:\lvert x\rvert_\iota\le 1\}\), a [[?c:valuation ring (domain)|valuation domain]] with fraction field \(\mathbb C\); a number in \(\mathcal O_\iota\) is called *integral at \(\iota\)*;
- the **conjugate place** \(\bar\iota\mid\ell\), defined by \(\bar\iota(z)=\iota(\bar z)\), where \(\bar z\) is complex conjugation.

For a field automorphism \(\sigma\) of \(\mathbb C\) we also write \(\sigma'\) for the automorphism \(\sigma'(z)=\overline{\sigma(\bar z)}\).

## Properties

1. Composing \(\iota\) with the isometric embedding \(\overline{\mathbb Q}_\ell\hookrightarrow\mathbb C_\ell\) into the completion gives an embedding \(\mathbb C\to\mathbb C_\ell\) inducing the same absolute value \(\lvert\cdot\rvert_\iota\).
2. If \(x\in\mathcal O_\iota\) divides \(\ell^j\) in \(\mathcal O_\iota\), then \(\lvert x\rvert_\iota\ge\ell^{-j}\). (If \(\ell^j=xy\) with \(\lvert y\rvert_\iota\le1\), then \(\ell^{-j}=\lvert x\rvert_\iota\lvert y\rvert_\iota\le\lvert x\rvert_\iota\).)

## References

1. Lean: `New.PrimePadicIso` in `src/New/Reduction/Lattices/Heights.lean`; `New.PrimePadicIso.conj`, `.place`, `.integers`, `.norm_place`, `.inv_pow_le_norm_of_dvd`, `New.conjAut` in `src/New/Reduction/Lattices/TwistedLattice.lean`.
