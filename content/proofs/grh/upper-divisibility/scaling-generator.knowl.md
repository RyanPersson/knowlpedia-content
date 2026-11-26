+++
id = "proofs/grh/upper-divisibility/scaling-generator"
title = "Scaling generator at a prime dividing pi_N"
kind = "construction"
summary = "For a prime w dividing pi_N, an integral norm-one finite idele supported at w and its conjugate whose component at w generates the units of the residue field."
aliases = ["scaling", "scaling at w", "scaling generator"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsScalingAt", "New.Data.exists_isScalingAt_valuation_pow_iff", "New.Data.scalingGenerator", "New.Data.valuation_scalingGenerator_pow_sub_one_lt_one_iff", "New.Data.scalarFin_scalingGenerator_pow_mem_levelX_iff", "New.Data.mem_levelX", "New.Data.not_isChosen_of_N_mem"]
lean_files = ["src/New/UpperBound/Size/ShortColumns.lean"]
proof_status = "full"
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with CM field \(E\), prime level \(N\) and integer \(\pi=\pi_N\) of \(E\) with \(\pi\bar\pi=N\). Let \(w\) be one of the \(f\) [[?lean:New.Data.piNPlaces|primes of \(E\) dividing \(\pi\)]]; it is split over \(E^{+}\), \(\bar w\ne w\), and its [[algebra-commutative/residue-field|residue field]] has \(N\) elements. A **scaling at \(w\)** is an element \(z\) of the group \(U(1)(\mathbb{A}_f)=\{z\in\mathbb{A}_{E,f}: z\bar z=1\}\) of norm-one [[?c:Finite adele ring of a number field|finite adeles]] that is integral (\(z\in\widehat{\mathcal O}_E\)) and has component \(z_u=1\) at every finite place \(u\notin\{w,\bar w\}\).

**Proposition and construction.** There is a scaling \(z\) at \(w\) such that for every \(i\in\mathbb{N}\)
\[
z_w^{\,i}\equiv1\pmod w\iff (N-1)\mid i .
\]
The **scaling generator** \(z_w\) is a fixed choice of such a scaling.

**Corollary.** For every stage \(j\), the \(i\)-th power of the scalar matrix \(z_w\cdot 1\) in the finite adelic unitary group of \(X_j\) lies in the [[?lean:New.Data.levelX|level of stage \(j\)]] if and only if \((N-1)\mid i\).

## Proof

The units of the residue field at \(w\) form a cyclic group of order \(N-1\), and the units of the completed local ring \(\mathcal O_w\) surject onto it. Choose a unit \(x\in\mathcal O_w^\times\) whose reduction is a generator, let \(\tilde x\) be the finite idele with component \(x\) at \(w\) and \(1\) elsewhere, and put \(z=\tilde x/\bar{\tilde x}\). Then \(z\bar z=1\); \(z\) is a unit at every place, hence integral; its components away from \(w,\bar w\) are \(1\); and since \(\bar w\ne w\) its component at \(w\) is \(x\). Now \(x^{i}\equiv1\) modulo \(w\) if and only if the order \(N-1\) of the reduction of \(x\) divides \(i\).

For the corollary, recall that an element \(k\) of the finite adelic unitary group of \(X_j\) lies in the level of stage \(j\) if and only if it lies in the [[?lean:New.Data.chosenLevel|principal congruence subgroup at the chosen places]] and, at every prime \(u\mid\pi\), the last row of \(k_u-1\) vanishes modulo \(u\) (this is the definition, read place by place). The scalar matrix of \(z_w\) is integral and is \(1\) away from \(w,\bar w\); these two places lie above \(N\), which is larger than the primes \(p_0,p_1\) below the chosen places, so they are not chosen and the scalar matrix lies in the principal congruence subgroup at the chosen places. At a prime \(u\mid\pi\) with \(u\ne w\) we have \(\bar u\ne w\) as well (of two conjugate primes above \(N\) exactly one divides \(\pi\)), so the component is \(1\). At \(u=w\) the matrix \(z_w^{i}-1\) is the scalar \(z_w^{i}-1\), and its last row vanishes modulo \(w\) exactly when \(z_w^{i}\equiv1\). \(\blacksquare\)

## Remarks

The choice is made once and for all; only the two displayed properties are used later.

## References

1. Lean: the declarations listed in the front matter, in `src/New/UpperBound/Size/ShortColumns.lean`.
