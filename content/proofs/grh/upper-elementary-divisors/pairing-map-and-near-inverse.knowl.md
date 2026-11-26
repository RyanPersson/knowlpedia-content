+++
id = "proofs/grh/upper-elementary-divisors/pairing-map-and-near-inverse"
title = "The pairing map on functions on edges and its near inverse"
kind = "lemma"
summary = "The map Add pairing a function on edges with the columns of a matrix Q', and the map Inv built from a left inverse of Q' and an averaging matrix; Add Inv is p^(2 N c_0) modulo w^c when the columns of Q' have values in the forms of all halfway lattices."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.pairingMap", "New.nearInverse", "New.edgewise", "New.valuedIn", "New.pairingMap_mul_nearInverse_apply", "New.FrobeniusCycle.IsEdgePairing.pairingMap_mul_nearInverse_one", "New.FrobeniusCycle.IsEdgeCondition.pow_dvd_mul_sub_smul_one", "New.edgewise_mul", "New.edgewise_mulVec"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean"]
proof_status = "full"
+++

Let \(O\) be a commutative ring, \(H,\mathrm{Ed},L,\iota\) finite sets. A vector indexed by \((H\times\mathrm{Ed})\times L\) is a function \(\psi\) on \(H\times\mathrm{Ed}\) with values in \(O^{L}\), i.e. a function on the edges \(e\in\mathrm{Ed}\) with values in \(O^{H}\otimes O^{L}\). For a submodule \(C\subseteq O^{L}\), \(\psi\) is **\(C\)-valued** if \(\psi(x,\cdot)\in C\) for all \(x\in H\times\mathrm{Ed}\). For matrices \(u_e\in M_H(O)\) and \(A\in M_L(O)\), the **edgewise** map \(u\boxtimes A\) acts on the value at \(e\) by \(u_e\otimes A\). Given \(u_e\in\mathrm{GL}_H(O)\), \(b,b'\in O^{L}\), a matrix \(Q'\) with columns indexed by \(\iota\) and rows by \((H\times\mathrm{Ed})\times L\), a matrix \(R'\) of the transposed shape, and \(\mathrm{Av}\in M_L(O)\), define
\[
\mathrm{Add}={}^{t}Q'\cdot\bigl(u\boxtimes\operatorname{diag}(b)\bigr),\qquad\mathrm{Inv}_{\mathrm{Av}}=\bigl(u^{-1}\boxtimes(\mathrm{Av}\operatorname{diag}(b'))\bigr)\cdot{}^{t}R'.
\]

**Lemma.** 1. \((\mathrm{Add}\cdot\mathrm{Inv}_{\mathrm{Av}})_{ij}=\sum_{x\in H\times\mathrm{Ed}}\bigl\langle\mathrm{Av}(b'\cdot R'_j(x)),\,Q'_i(x)\bigr\rangle_b\), where \(Q'_i(x)=(Q'_{(x,l),i})_l\), \(R'_j(x)=(R'_{j,(x,l)})_l\) and \(\langle h,h'\rangle_b=\sum_lh'_lb_lh_l\).

Now let \(L=\mathcal{E}(N,k,n)\) for a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] \(T\), \((b,b')\) an [[proofs/grh/upper-elementary-divisors/edge-pairing|edge pairing]], and \(R'Q'=1\).

2. \(\mathrm{Add}\cdot\mathrm{Inv}_{1}=p^{Nc_0}\cdot1\).
3. If \(O\) is a valuation domain, \((C,S,\mathrm{Av})\) is an [[proofs/grh/upper-elementary-divisors/edge-conditions|edge condition]] of precision \(c\), and every column of \(Q'\) is \(\mathcal{A}(k,n,r)\)-valued, then \(\mathrm{Add}\cdot\mathrm{Inv}_{\mathrm{Av}}\equiv p^{2Nc_0}\cdot1\) modulo \(w^{c}\), entry by entry.

## Proof

(1) \((u\boxtimes\operatorname{diag}b)(u^{-1}\boxtimes\mathrm{Av}\operatorname{diag}b')=1\boxtimes B\) with \(B=\operatorname{diag}(b)\mathrm{Av}\operatorname{diag}(b')\), which is block diagonal over \(H\times\mathrm{Ed}\); so \(\mathrm{Add}\cdot\mathrm{Inv}={}^tQ'(1\boxtimes B){}^tR'\) and the entry is \(\sum_xQ'_i(x)\cdot B\,R'_j(x)\).

(2) With \(\mathrm{Av}=1\): \(\langle b'R'_j(x),Q'_i(x)\rangle_b=p^{Nc_0}\sum_lR'_{j,(x,l)}Q'_{(x,l),i}\), and summing over \(x\) gives \(p^{Nc_0}(R'Q')_{ji}\).

(3) By property 4 of an edge condition applied to \(h=b'R'_j(x)\) and \(h'=Q'_i(x)\in\mathcal{A}\), each term of (1) is congruent modulo \(w^{c}\) to \(p^{Nc_0}\langle b'R'_j(x),Q'_i(x)\rangle_b\); sum and use (2). \(\square\)

## References

1. Lean: `New.pairingMap`, `New.nearInverse`, `New.edgewise`, `New.valuedIn`, `New.pairingMap_mul_nearInverse_apply`, `New.FrobeniusCycle.IsEdgePairing.pairingMap_mul_nearInverse_one`, `New.FrobeniusCycle.IsEdgeCondition.pow_dvd_mul_sub_smul_one`, `New.edgewise_mul`, `New.edgewise_mulVec` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.
