+++
id = "proofs/grh/derivatives-divisibility/legendre-bound-for-jets"
title = "Legendre's bound for the jet of an integral series"
kind = "lemma"
summary = "The jet of a series with integral coefficients in degree l along an integral homogeneous polynomial of degree l has valuation at least l/(p-1) minus the number of variables times 1 + floor(log_p l)."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.norm_jet_le_of_isHomogeneous", "New.norm_prod_factorial_le"]
lean_files = ["src/New/Derivatives/Divisibility/Count.lean"]
proof_status = "full"
+++

**Lemma.** In the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]], let \(G\) be a power series over \(\mathbb{C}_p\) in variables indexed by a finite set \(\sigma\), let \(l\ge0\), and suppose every coefficient of \(G\) of degree \(l\) is integral. Let \(Q\) be a homogeneous polynomial of degree \(l\) in the same variables with coefficients in \(\mathcal{O}\). Then the jet satisfies
\[
\lvert Q(\partial)G(0)\rvert\le p^{\,\lvert\sigma\rvert\,(\lfloor\log_pl\rfloor+1)-l/(p-1)} ,
\]
with the convention \(\lfloor\log_p0\rfloor=0\).

## Proof

By definition \(Q(\partial)G(0)=\sum_{\lvert d\rvert=l}d!\,Q_dG_d\), and \(\lvert Q_d\rvert,\lvert G_d\rvert\le1\); by the ultrametric inequality it suffices to bound \(\lvert d!\rvert=p^{-\sum_xv_p(d_x!)}\) for a multi-index \(d\) of degree \(l\). Put \(K=\lfloor\log_pl\rfloor+1\), so that \(d_x\le l<p^K\). By [[?c:Legendre's formula|Legendre's formula]], \((p-1)v_p(k!)=k-s_p(k)\) with \(s_p(k)\) the sum of the base-\(p\) digits of \(k\); for \(k<p^K\) there are at most \(K\) digits, each at most \(p-1\), so \(v_p(k!)\ge k/(p-1)-K\). Summing over \(x\in\sigma\) gives \(\sum_xv_p(d_x!)\ge l/(p-1)-\lvert\sigma\rvert K\). \(\blacksquare\)

## References

1. Lean: `New.norm_jet_le_of_isHomogeneous`, `New.norm_prod_factorial_le` in `src/New/Derivatives/Divisibility/Count.lean`; `New.padicValNat_factorial_mem_Icc` in `src/Lib/General/Algebra/IntegralPowerSeries.lean`.
