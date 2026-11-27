+++
id = "proofs/grh/upper-divisibility/properties-of-marked-sets"
title = "Properties of marked sets"
kind = "lemma"
summary = "Places inducing a marked prime or its conjugate are not b-places and have weight a/x_1; sums of functions of the lift weights balance between a marked prime and its conjugate; marked primes are split, unramified and away from the level."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsMarked.notMem_bPlaces", "New.Data.IsMarked.cast_weight_eq", "New.Data.IsMarked.sum_inducedPlace_eq_sum_star", "New.Data.IsMarked.sum_placesInducing_eq_sum_placesInducingConj", "New.Data.IsMarked.sum_inducedPlace_sub_star_eq_zero", "New.Data.IsMarked.card_le", "New.Data.IsMarked.valuation_natCast_eq_exp_neg_one", "New.Data.IsMarked.isSplit", "New.Data.IsMarked.maxCompactAt_le_levelX", "New.Data.IsMarked.not_dvd_M_mul_N", "New.Data.IsMarked.natCast_mem_asIdeal"]
lean_files = ["src/New/UpperBound/Divisibility/MarkedPrimes.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\Lambda\) be a [[proofs/grh/upper-divisibility/marked-set-of-primes|marked set]] of primes of \(E\) at \(\iota\colon\mathbb{C}\to\mathbb{C}_p\), and \(\mathfrak l\in\Lambda\).

1. \(\lvert\Lambda\rvert\le f\); \(\mathfrak l\) lies above \(p\); \(\bar{\mathfrak l}\ne\mathfrak l\); \(p\) is a uniformiser at \(\mathfrak l\); \(p\nmid MN\).
2. If \(w_\sigma\in\Lambda\) or \(\bar w_\sigma\in\Lambda\), then \(\sigma\) is not a b-place, and \(w(\sigma)=a/x_1\).
3. (**Balance.**) Let \(\kappa_j(\tau)=w(\tau)+(j+\tfrac12)\Delta\) be the [[?lean:New.Data.liftWeight|weight of the \(j\)-th lift]]. For every function \(G\) of a weight and a prime,
\[
\sum_{\tau:\ w_\tau\in\Lambda}G\bigl(\kappa_j(\tau),w_\tau\bigr)=\sum_{\tau:\ \bar w_\tau\in\Lambda}G\bigl(\kappa_j(\tau),\bar w_\tau\bigr).
\]
4. The group of elements of the standard maximal compact subgroup of the finite adelic unitary group of \(X_0\) that are trivial away from \(\mathfrak l,\bar{\mathfrak l}\) is contained in the [[?lean:New.Data.levelX|level of stage \(0\)]]: source forms are spherical at \(\mathfrak l\).

## Proof

(1) Each prime of \(\Lambda\) is \(w_\tau\) for some place \(\tau\), which gives the first two claims; \(\bar{\mathfrak l}\notin\Lambda\ni\mathfrak l\) gives the third. \(p\) is inert in \(K\); every prime dividing \(q_1\) splits in \(K\) and \(d\) ramifies, so \(p\nmid q_1d\) ([[?lean:New.Parameters.not_dvd_q₁_mul_d_of_inert|`not_dvd_q₁_mul_d_of_inert`]]), and \(p\) is unramified in \(E\) (the discriminant of \(E\) is supported on \(q_1d\); Lean: [[?lean:New.Parameters.intValuation_natCast_eq_exp_neg_one|`intValuation_natCast_eq_exp_neg_one`]]). \(p\nmid MN\) by the [[proofs/grh/upper-divisibility/orbits-at-an-exceptional-prime|theorem on orbits]].

(2) Suppose \(\sigma\) is a b-place. Some a-place \(\tau\) induces \(w_\sigma\) or \(\bar w_\sigma\), so \(\tau=g^{i}\sigma\) with \(g=u(-p)\). Modulo \(q_0\), with \(c\) the class of \(g\): a-places have class \(1\), b-places class \(-1\), so \(-c^{i}=1\). Raising to the odd power \(o_0\) (the order of \(c\)): \(1=(-c^{i})^{o_0}=-(c^{o_0})^{i}=-1\) in \((\mathbb{Z}/q_0)^\times\), which is false as \(q_0>2\). The weight of a place that is not a b-place is \(a/x_1\).

(3) Fix \(\mathfrak l\in\Lambda\). Multiplication by \(g\) is a bijection from \(\{\tau:w_\tau=\mathfrak l\}\) to \(\{\tau:w_\tau=\bar{\mathfrak l}\}\) (it conjugates the induced prime). By (2) both \(\tau\) and \(g\tau\) have weight \(a/x_1\), so \(\kappa_j(g\tau)=\kappa_j(\tau)\). Hence \(\sum_{w_\tau=\mathfrak l}G(\kappa_j(\tau),\mathfrak l)=\sum_{w_\tau=\bar{\mathfrak l}}G(\kappa_j(\tau),\mathfrak l)\); sum over \(\mathfrak l\in\Lambda\).

(4) Neither \(\mathfrak l\) nor \(\bar{\mathfrak l}\) contains \(\pi_M\pi_N\), since its norm \(MN\) is prime to \(p\). An integral element trivial away from \(\mathfrak l,\bar{\mathfrak l}\) is therefore congruent to \(1\) modulo \(\pi_M\pi_N\), and the principal congruence subgroup of level \(\pi_M\pi_N\) lies in the level of stage \(0\). \(\blacksquare\)

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Divisibility/MarkedPrimes.lean`.
