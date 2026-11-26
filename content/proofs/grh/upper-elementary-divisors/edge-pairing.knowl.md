+++
id = "proofs/grh/upper-elementary-divisors/edge-pairing"
title = "Edge pairing"
kind = "definition"
summary = "Weights of a diagonal pairing on coefficient vectors for which translation by g is adjoint to translation by the transpose of g, invertible up to a fixed power of p; existence in degree below q."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.IsEdgePairing", "New.FrobeniusCycle.multinomialExponent", "New.FrobeniusCycle.exists_isEdgePairing", "New.FrobeniusCycle.IsEdgePairing.dotProduct_letterRep_mulVec", "New.FrobeniusCycle.IsEdgePairing.pairing_mul_eq_pow_mul_dotProduct"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/Edges.lean"]
+++

Let \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\) with \(N\ge1\), with \(P=p^{f}\), and put \(c_0=k^{2}fN\) (so \(p^{c_0}=q^{k^{2}}\)). A pair of vectors \(b,b'\in O^{\mathcal{E}(N,k,n)}\) is an **edge pairing** if

1. \(b_\beta\,\rho_n({}^{t}g)_{\beta\alpha}=b_\alpha\,\rho_n(g)_{\alpha\beta}\) for all \(g\in\mathrm{GL}_k(W)\) and all exponents \(\alpha,\beta\), where \(\rho_n\) is the [[proofs/grh/upper-elementary-divisors/twisted-action|twisted representation]];
2. \(b_\beta b'_\beta=p^{Nc_0}\) for all \(\beta\).

With \(\langle h,h'\rangle_b=\sum_\beta h'_\beta b_\beta h_\beta\), condition 1 says \(\langle\rho_n(g)h,h'\rangle_b=\langle h,\rho_n({}^tg)h'\rangle_b\), and condition 2 gives \(\langle b'\eta,h'\rangle_b=p^{Nc_0}\sum_\beta h'_\beta\eta_\beta\): the pairing is perfect up to \(p^{Nc_0}\). It is used as the pairing, in normalised coefficients, between the halfway lattices of an edge and of the dual edge.

## Existence

**Lemma.** If \(O\) is a valuation ring and a domain of characteristic \(0\), \(p\) is not a unit of \(O\), and \(n<q\), then an edge pairing exists.

*Proof.* Take [[proofs/grh/upper-elementary-divisors/adjoint-weights|adjoint weights]] \(b_0\) on \(k\) variables with exponent \(fN\): \(p^{kfN}=\binom n\gamma b_0(\gamma)\) for \(\lvert\gamma\rvert=n<p^{fN}=q\). Put \(u=p^{(k-1)kfN}\), \(b_\beta=\prod_s u\,b_0(\beta_s)\) and \(b'_\beta=\prod_s\binom n{\beta_s}\). Then \(u\,b_0(\beta_s)\binom n{\beta_s}=p^{k^{2}fN}=p^{c_0}\), giving 2. For 1, the matrix of \({}^tg\) on the letter \(s\) is \({}^t(g_s)\) for both parities (inverse and transpose commute), and adjointness of \(b_0\) gives \(b_0(\beta_s)\operatorname{Sym}^n({}^tg_s)_{\beta_s\alpha_s}=b_0(\alpha_s)\operatorname{Sym}^n(g_s)_{\alpha_s\beta_s}\); multiply over \(s\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.IsEdgePairing`, `New.FrobeniusCycle.multinomialExponent`, `New.FrobeniusCycle.exists_isEdgePairing`, `New.FrobeniusCycle.IsEdgePairing.dotProduct_letterRep_mulVec`, `New.FrobeniusCycle.IsEdgePairing.pairing_mul_eq_pow_mul_dotProduct` in `src/New/UpperBound/ElementaryDivisors/Edges.lean`.
