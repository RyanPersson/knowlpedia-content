+++
id = "proofs/grh/upper-divisibility/one-lift-evaluated-at-a-neighbor"
title = "One lift, evaluated at a neighbour"
kind = "theorem"
summary = "A standard datum moved by an element of Hecke type of index at most r at the marked primes raises p-adic gauges by at most p to the sum of the Hecke scaling exponents plus the lift loss."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsMarked.ω_ofSplitPlaces_mem_raises", "New.Data.mem_raises_neg_divisibilityBound", "New.Data.sum_card_boxes_le", "New.Data.IsMarked.neighborCharge_ne_zero_or_partner", "New.Data.IsMarked.exists_eq_mul_neighborDiagonal_mul", "New.Data.IsMarked.sum_neighborExponent_mul_lastEntry_eq_zero", "New.Data.IsMarked.sum_neighborExponent_add_neighborCharge_le"]
lean_files = ["src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean"]
proof_status = "outline"
+++

**Theorem.** Let \(D\) be [[?lean:New.Data|admissible data]], \(p\) a prime, \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), \(\Lambda\) a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]], \(\vartheta\) a twist and \(j\ge0\). Let \(\varphi\) be a [[?lean:New.Parameters.standardData|standard datum of level one]] for the lift \(X_j\to X_{j+1}\): a \(p\)-integral combination of translates of the integral vacuum by points integral above \(p\). Let \(g\) be an element of the finite adelic unitary group of \(X_{j+1}\), trivial away from \(\Lambda\cup\bar\Lambda\), whose component at each \(\mathfrak l\in\Lambda\) lies in the double coset of \(\operatorname{diag}(\varpi 1_i,1)\) for some \(i\le\mathfrak r=\mathfrak r(p)\). Then the datum \(\omega(1,g)\varphi\) [[proofs/grh/upper-divisibility/gauge-bound-for-a-chain-of-lifts|raises]] \(p\)-adic gauges, from base point \(1\) to base point \(1\), by at most
\[
p^{\ \sum_{\mathfrak l\in\Lambda}A_{\mathfrak l}+\operatorname{ll}_\Lambda(j)},
\]
with \(A_{\mathfrak l}\) the Hecke scaling exponents and \(\operatorname{ll}_\Lambda(j)\) the [[proofs/grh/upper-divisibility/neighbor-exponents-and-lift-loss|lift loss]].

Also (no marked set): if \(\chi_K(p)\ne1\), a standard datum of level one raises gauges by at most \(p^{-\operatorname{db}_{p,j}(\emptyset)}\).

## Proof

*Reduction to a diagonal.* As \(p\) is a uniformiser at each \(\mathfrak l\in\Lambda\), the component of \(g\) at \(\mathfrak l\) is \(u_{\mathfrak l}\,\operatorname{diag}(p\text{ on }J(\mathfrak l))\,v_{\mathfrak l}\) with integral invertible \(u,v\) and \(\lvert J(\mathfrak l)\rvert=i\le\mathfrak r\). So \(g=u\,\nu_J\,v\) with \(u,v\) integral above \(p\) and \(\nu_J\) the neighbour diagonal.

*Jets.* By [[?lean:New.omega_mem_raises_of_schurJet_le|`omega_mem_raises_of_schurJet_le`]] (quoted from the file on gauges of theta lifts) it suffices to bound, for every vacuum translate \(f\) in the standard datum and all pairs of fillings (a row filling \(T\) of the diagrams by indices of \(X_{j+1}\), and a column filling), the product of the weight of the diagonal \(\nu_J\) on \(T\) and the \(p\)-adic absolute value of the corresponding [[?lean:New.schurJet|Schur jet]] of the theta series of \(f\), by \(p\) to the stated exponent.

(a) *Weight of the diagonal.* It is \(p^{\sum\epsilon_\tau(T\text{-entries})}\) times \(p^{\sum_\tau(\sum_b\epsilon_\tau(b))\cdot e_{j+1}(\tau)}\), where \(e_{j+1}(\tau)=n_j/2-\kappa_{j+1}(\tau)\) is the last entry (determinant power) of the weight. The second exponent vanishes by the [[proofs/grh/upper-divisibility/properties-of-marked-sets|balance]] between a marked prime and its conjugate: \(\sum_{\tau\in\Phi_\Lambda}\lvert J(w_\tau)\rvert e_{j+1}(\tau)=\sum_{\tau\in\Phi_{\bar\Lambda}}\lvert J(\overline{w_\tau})\rvert e_{j+1}(\tau)\).

(b) *Jets with charges.* By the theorem on the divisibility of jets with charges ([[?lean:New.norm_schurJet_jetSeries_le_of_charges|`norm_schurJet_jetSeries_le_of_charges`]], quoted from the chapter on derivatives of theta functions), the jet has absolute value at most \(p^{\,(\text{number of charged boxes of }T)-\operatorname{db}_{p,j}(\Phi_\Lambda)}\), provided the charge function satisfies: for every partner exponent \(e\), place \(\tau\), height \(h\) and index \(b\), if \(\tau\in\Phi_\Lambda\), or \(h=1\) and the partner \(\tau'=u(-p^{e})\tau\in\Phi_\Lambda\), then \(b\) is charged in a column of height one at \(\tau\) or in a column of height \(h\) at \(\tau'\). This holds for the neighbour charge: \(p\) is inert and \(e\) odd, so \(\tau'\) induces the conjugate prime and has the same marked indices; an unmarked index is charged (height one) at the place in \(\Phi_\Lambda\), a marked one at the place in \(\Phi_{\bar\Lambda}\) (any height).

(c) *Count.* For a filling \(T\), the sum over all boxes of exponent plus charge is at most \(\sum_{\mathfrak l\in\Lambda}A_{\mathfrak l}+\mathfrak r\sum_{\tau\in\Phi_\Lambda}c_j(\tau)\). Indeed at \(\tau\notin\Phi_\Lambda\) each box costs \(0\) (at \(\tau\in\Phi_{\bar\Lambda}\) a marked index has exponent \(-1\) and charge \(1\); otherwise both vanish). At \(\tau\in\Phi_\Lambda\) a box costs \([b\in J_\tau]+[h=1,\ b\notin J_\tau]\): each box of the long row (height one) costs exactly \(1\), which gives \(a\) at an a-place and \(0\) otherwise; and in a column of height \(h\ne1\) the entries are distinct, so at most \(\lvert J_\tau\rvert\le\mathfrak r\) of them are marked. Summing, \(\sum_{\tau\in\Phi_\Lambda}[\tau\in\Phi_a]a=\sum_{\mathfrak l}A_{\mathfrak l}\).

Adding (a), (b), (c): the exponent is at most \(\sum A_{\mathfrak l}+\mathfrak r\sum_{\Phi_\Lambda}c_j-\operatorname{db}_{p,j}(\Phi_\Lambda)=\sum A_{\mathfrak l}+\operatorname{ll}_\Lambda(j)\).

The last statement is [[?lean:New.mem_raises_predictedDivisibility|`mem_raises_predictedDivisibility`]] (quoted), since \(\operatorname{db}_{p,j}(\emptyset)\) is the predicted divisibility less the logarithmic term. \(\blacksquare\)

*Status.* The two analytic inputs, the criterion `omega_mem_raises_of_schurJet_le` and the divisibility of jets with charges, are quoted; the combinatorial steps (a) to (c) are proved in this file and were checked.

## References

1. Lean: `New.Data.IsMarked.ω_ofSplitPlaces_mem_raises` and the lemmas listed in the front matter, in `src/New/UpperBound/Divisibility/ValuationAtNonSplitPrimes.lean`.
