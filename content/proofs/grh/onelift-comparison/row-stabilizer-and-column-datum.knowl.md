+++
id = "proofs/grh/onelift-comparison/row-stabilizer-and-column-datum"
title = "Row stabilizer and column datum"
kind = "lemma"
summary = "For a function invariant under a row stabilizer H, the function chi(det z) F(z^-1 y) cut down to z in H is a product of a datum of the columns e of z and F(y)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Rows.FixesColsOff", "New.Rows.rowStabilizer", "New.Rows.columnDatum", "New.Rows.columnDatum_mul_ite_eq_ite_mem_rowStabilizer"]
lean_files = ["src/New/OneLift/ComparisonOperator/OneExchange.lean"]
proof_status = "outline"
+++

Let \(R,S\) be commutative rings, \(\varphi\colon R\to S\) a ring homomorphism, \(N,r,c,a\) finite index sets, \(e\colon r\hookrightarrow N\) an injection with inclusion matrix \(\iota_e\in R^{N\times r}\) (column \(j\) is the unit vector at \(e(j)\)), \(w\in S^{c\times N}\), and \(\chi\) a multiplicative character of \(R\) with values in \(\mathbb{C}\) (extended by \(0\) to non-units).

* A square matrix \(z\in R^{N\times N}\) **has the columns of \(1\) off \(e\)** if \(z(1-\iota_e\iota_e^{\mathsf T})=1-\iota_e\iota_e^{\mathsf T}\).
* The **row stabilizer** \(H=H(\varphi,w,e)\subseteq\mathrm{GL}_N(R)\) is the subgroup of the \(A\) that have the columns of \(1\) off \(e\) and satisfy \(w\,\varphi(A)=w\).
* The **column datum** is the function on \(R^{N\times r}\)
\[
\kappa(\sigma)=\begin{cases}\chi(\det\sigma_e)&\text{if }w\,\varphi(\sigma)=w\,\iota_e,\\0&\text{otherwise,}\end{cases}
\]
with \(\sigma_e\) the \(r\times r\) matrix of the rows \(e\) of \(\sigma\).

**Lemma.** Let \(F\colon R^{N\times a}\to\mathbb{C}\) satisfy \(F(Ay)=F(y)\) for all \(A\in H\). For every \(y\in R^{N\times a}\) and every \(z\in R^{N\times N}\), writing \(z^{(e)}\in R^{N\times r}\) for the columns \(e\) of \(z\),
\[
\kappa\bigl(z^{(e)}\bigr)\cdot\bigl[z\text{ has the columns of }1\text{ off }e\bigr]\,F(y)=\bigl[z\in H\bigr]\;\chi(\det z)\,F(z^{-1}y).
\]

## Proof

Outline (the 35-line Lean proof was read through its comments, not line by line). If \(z\) does not have the columns of \(1\) off \(e\), both sides vanish (membership in \(H\) requires it). Otherwise write \(z=1+u\,\iota_e^{\mathsf T}\) with \(u=z^{(e)}-\iota_e\). Then the columns \(e\) of \(z\) are \(z^{(e)}=\iota_e+u\), and expanding the determinant along the identity columns gives \(\det z=\det\bigl(z^{(e)}\bigr)_e\). Moreover \(w\varphi(z)=w\) and \(w\varphi(z^{(e)})=w\iota_e\) both say \(w\varphi(u)=0\), since \(\iota_e^{\mathsf T}\) has a right inverse \(\iota_e\). So on such \(z\): if \(w\varphi(u)\neq0\) both sides are \(0\); if \(w\varphi(u)=0\) and \(\det z\) is not a unit, \(\chi(\det z)=0\) on the left and \(z\notin H\) on the right; and if \(\det z\) is a unit then \(z\in H\), the left side is \(\chi(\det z)F(y)\) and the right side is \(\chi(\det z)F(z^{-1}y)=\chi(\det z)F(y)\) by the invariance of \(F\) under \(z^{-1}\in H\).

## References

1. Lean: `New.Rows.FixesColsOff`, `New.Rows.rowStabilizer`, `New.Rows.columnDatum`, `New.Rows.columnDatum_mul_ite_eq_ite_mem_rowStabilizer` in `src/New/OneLift/ComparisonOperator/OneExchange.lean`.
