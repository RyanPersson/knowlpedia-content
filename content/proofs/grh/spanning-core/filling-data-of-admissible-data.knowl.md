+++
id = "proofs/grh/spanning-core/filling-data-of-admissible-data"
title = "Filling data of admissible data"
kind = "construction"
summary = "The abstract data of the filling theorem attached to admissible data: the level N, the two level primes with their chosen places, the source level, and a Bessel system at each real place."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.filling", "New.Data.isDiscreteSeriesBessel_filling_besselSystem", "New.Data.levelX_zero_eq_comap", "New.Data.natCast_levelPrime_dvd_iff"]
lean_files = ["src/New/Spanning/Bessel/FillingData.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]] with CM field \(E\) and [[?lean:New.Data.shape|shape]] \(\mathfrak s\) of \(Y_0\). The **filling data of \(D\)** is the instance of the abstract structure [[?lean:New.Filling|`Filling`]] (the data of the filling theorem, defined in the unfolding chapter) with

* the prime \(N\) and the finite idele of \(\pi_N\) (with \(\pi_N\bar\pi_N=N\), integral, \(N\) split as required);
* the level primes \(p_0,p_1\), with the chosen places above \(p_i\): the finite places \(w\) containing both [[?lean:New.Data.piM|\(\pi_M\)]] and \(p_i\); they have residue cardinality \(p_i\), no two are conjugate, and \(M=p_0p_1\) divides an integral finite adele exactly when it vanishes modulo all chosen places and their conjugates;
* the generator \(\delta_E\) of the different;
* the size parameter \(b\);
* the source level [[?lean:New.Data.levelX|\(D.\mathrm{levelX}\,0\)]] on \(U(X_0)\), for which all stabilisers of classes are trivial;
* at each infinite place \(v\), a Bessel system chosen by [[proofs/grh/spanning-core/bessel-systems-exist-at-the-real-places|existence of Bessel systems]];
* the size inequalities required by `Filling` (between \(\varrho,k,f,b,M,N\) and the root discriminant), all instances of the size inequalities of the data.

## Properties

1. The Bessel system at \(v\) is [[proofs/grh/spanning-core/bessel-system-of-discrete-series-type|of discrete series type]] \((2\varsigma_v,\mathrm{cc}_v)\).
2. The source level is the preimage, under the embedding of the finite adelic points of \(U(X_0)\) into those of \(U(Y_0)\), of the [[?lean:New.Filling.principalLevel|principal level \(K(M)\)]] of the filling data (congruence modulo \(\pi_N\) and reduction to \(1\) at the chosen places).

## Proof

(1) is the choice. (2) Both sides say that \(k\) satisfies the congruence modulo \(\pi_N\) and reduces to \(1\) at the chosen places; integrality, also asked on the left, is contained in the congruence (unfolding of the definitions, with the library lemmas `reduction_inclHFin_eq_one_iff` and `inclHFin_mem_latticeStabilizer_iff`). The divisibility criterion for \(M\): each \(p_i\) is unramified in \(E\), so it divides \(r\) iff \(r\) vanishes modulo every place above it, and every such place is chosen or conjugate to a chosen one; \(p_0\ne p_1\) are coprime. \(\blacksquare\)

## Remarks

The Bessel systems are obtained by choice from an existence theorem, so they are not canonical; only the listed properties are used.

## References

1. Lean: `New.Data.filling`, `New.Data.isDiscreteSeriesBessel_filling_besselSystem`, `New.Data.levelX_zero_eq_comap` in `src/New/Spanning/Bessel/FillingData.lean`.
