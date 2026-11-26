+++
id = "proofs/grh/spanning-unfolding-b/filling-admissible"
title = "Admissible filling datum (standing hypotheses)"
kind = "definition"
summary = "The standing hypotheses of the filling theorem: the source level is the preimage of K(M), reduction is onto, and size inequalities between b, M, N, the constants and the second moments."
aliases = ["standing hypotheses of the filling theorem", "IsAdmissible"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.IsAdmissible"]
lean_files = ["src/New/Spanning/Unfolding/Setup.lean"]
+++

A [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] \(S\) is **admissible** if, with the [[proofs/grh/spanning-unfolding-b/filling-unitary-groups|maps]] \(\iota_H\), the [[proofs/grh/spanning-unfolding-b/filling-level-and-reduction|groups \(K\), \(K(M)\)]] and the [[proofs/grh/spanning-unfolding-b/filling-constants|constants]] of \(S\), the following hold.

1. The source level is \(L=\iota_H^{-1}(K(M))\).
2. The reduction \(K\to\bar G\) is surjective.
3. \(\lvert\Phi_v(\varpi)\rvert\le b\) for every infinite place \(v\).
4. \(1\le\lvert\kappa_v\rvert\le b^{23}\) for every infinite place \(v\).
5. \(N\le b^{60n}\).
6. \(b^{11kf}\,\mathcal{M}_{\mathrm{id}}\le\mathcal{M}_{\mathrm{main}}\le\bigl(M/b^{6}\bigr)^{kf}\,\mathcal{M}_{\mathrm{id}}\).
7. The number of Bessel coordinates satisfies \(\lvert I\rvert\le b^{2kf}\).
8. Let \(K_{X_0}\subset U(X_0)(\mathbb{A}_f)\) be the [[?lean:New.stdLevel|stabiliser of the standard lattice]] of \(X_0\). Then
\[
\bigl(N^k/b\bigr)^{f}\le\bigl[K_{X_0}:K_{X_0}\cap\iota_H^{-1}(K)\bigr],
\]
where the [[algebra-groups/index-of-subgroup|index]] is read as \(0\) if it is infinite.
9. With \(c_G\) the [[?lean:New.Shape.openCellConst|open cell constant]] of the shape,
\[
a_*\le\bigl(1+b^{-9}\bigr)\,\mathcal{M}_{\mathrm{main}}\cdot\deg\cdot c_G^{\,f}\cdot\operatorname{vol}(\widehat{\mathcal{O}})^{-n}\cdot\Bigl(\frac{\operatorname{cov}_{\mathsf U}\cdot\Lambda}{\lvert I\rvert}\Bigr)^{2}.
\]

## Remarks

Condition 9 is the only place where the mass of the genus of rank \(r\) is compared with the local constants; for the data of the main argument it is verified through the Siegel mass formula in [[proofs/grh/spanning-unfolding-b/filling-of-admissible-data-is-admissible|the admissibility of the filling datum of admissible data]].

## References

1. Lean: `New.Filling.IsAdmissible` in `src/New/Spanning/Unfolding/Setup.lean`.
