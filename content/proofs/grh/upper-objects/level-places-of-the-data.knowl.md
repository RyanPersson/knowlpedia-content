+++
id = "proofs/grh/upper-objects/level-places-of-the-data"
title = "The places dividing pi_N and the levels of the stages X_j"
kind = "definition"
summary = "The set of primes of E dividing pi_N is a split level for N with f elements; the level of stage j consists of the elements principal at the chosen places whose last row is (0,...,0,1) modulo pi_N."
aliases = ["places dividing pi_N", "level of X_j", "level of stage j"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.piNPlaces", "New.Data.star_mem_piNPlaces_iff", "New.Data.isSplitLevel_piNPlaces", "New.Data.card_piNPlaces", "New.Data.levelX", "New.Data.isLevel_levelX", "New.Data.classAut_levelX_zero_eq_bot", "New.Data.FormX"]
lean_files = ["src/New/UpperBound/Objects/Columns.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with CM field \(E\), level prime \(N\), and the integer \(\pi_N\) of \(E\) with \(\pi_N\bar\pi_N=N\). Let \(X_j\) denote the standard definite hermitian space on the [[proofs/grh/upper-objects/index-sets-of-the-hermitian-spaces|index set of \(X_j\)]] (\(n_j\) elements, last index \(\ast\)).

**Definition.**

* \(P_N\) is the finite set of finite places of \(E\) dividing \(\pi_N\).
* The **level of stage \(j\)** is the subgroup \(K_{X_j}\subseteq U(X_j)(\mathbb A_f)\) of the elements that lie in the [[proofs/grh/upper-objects/chosen-places-and-chosen-group-order|chosen level]] (integral, and \(\equiv1\) at every chosen place) and whose last row is congruent to \((0,\dots,0,1)\) modulo \(\pi_N\) (i.e. modulo the ideal \(\pi_N\hat{\mathcal O}_E\) of the integral finite adeles).
* \(\mathcal A(X_j)\) is the space of [[?lean:New.AlgForm|algebraic modular forms]] on \(U(X_j)\) with values in the Weyl module with [[proofs/grh/upper-objects/weights-of-the-definite-spaces|column numbers \(c_\tau(h)\) and determinant exponents \(\ell_j(\tau)\)]], i.e. of highest weight \(\mu(X_j)\).

## Properties

1. \(P_N\) is a [[proofs/grh/upper-objects/split-level|split level]] for \(N\): of a place above \(N\) and its conjugate exactly one divides \(\pi_N\), each has norm \(N\), and \(N\) is a uniformiser there. \(\lvert P_N\rvert=f\).
2. \(K_{X_j}\) is a level: open and contained in the standard maximal compact subgroup.
3. \(K_{X_0}\) is free: \(\Gamma\cap gK_{X_0}g^{-1}=1\) for all \(g\), by [[proofs/grh/upper-objects/free-levels-at-the-chosen-places|freeness of levels principal at the chosen places]] (\(n_0\le2n_m\)).

Statement 1 rests on the same library lemmas on primes \(\equiv1\) modulo \(q_1d\) as the facts on the chosen places; it is not reproved here.

## References

1. Lean: `New.Data.piNPlaces`, `New.Data.isSplitLevel_piNPlaces`, `New.Data.levelX`, `New.Data.FormX` in `src/New/UpperBound/Objects/Columns.lean`.
