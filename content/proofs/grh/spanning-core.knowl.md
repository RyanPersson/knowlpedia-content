+++
id = "proofs/grh/spanning-core"
title = "Spanning: the second moment, equal multiplicities, and Bessel systems"
kind = "page"
summary = "The abstract second-moment argument that few translates of the Poincaré map span the target forms, the equality of Hecke multiplicities on spaces that differ in their signs, and the analysis at a real place behind the Bessel systems."
aliases = []
domains = ["proofs"]
section_mode = "continuous"
prerequisites = []
lean_files = ["src/New/Spanning/SecondMoment/PositiveType.lean", "src/New/Spanning/SecondMoment/FewTranslates.lean", "src/New/Spanning/SecondMoment/SpanningTheorem.lean", "src/New/Spanning/Multiplicities/HeckeEigensystems.lean", "src/New/Spanning/Multiplicities/EqualMultiplicities.lean", "src/New/Spanning/Bessel/Basic.lean", "src/New/Spanning/Bessel/GramSection.lean", "src/New/Spanning/Bessel/Orthonormality.lean", "src/New/Spanning/Bessel/MeanValue.lean", "src/New/Spanning/Bessel/SobolevBound.lean"]
+++

This chapter covers three folders of the part "Spanning: a second moment" of the argument: `SecondMoment`, `Multiplicities` and (in part, see the end) `Bessel`. Its output for the rest of the proof is the statement that the translates of the Poincaré map are [[proofs/grh/spanning-core/translates-of-the-good-poincare-map-spread|spread]], from which [[?lean:New.Data.enough_forms|Theorem B (enough forms)]] is deduced in another chapter, and the [[proofs/grh/spanning-core/equal-multiplicities-of-eigensystems|equality of multiplicities]] between the spaces \(Y_0,W_1,\dots,W_m\).

Notation follows the reading guide of the Lean source: \(D\) is admissible data, \(E=K(\zeta)\) the CM field, \(r\) the rank of \(Y_0\) and of the \(W_j\), \(\bar G=\prod_w\mathrm{GL}_r(\mathbb{F}_w)\) the finite group at the chosen places above \(p_0,p_1\), \(e_0\in\mathbb{C}[\bar G]\) the good idempotent, \(b\) the scale. Inner products are conjugate-linear in the first variable.

## 1. Few translates fill: the abstract argument

Let a finite group \(\Gamma\) act unitarily on a finite-dimensional space \(T\), let \(\mathrm{pr}_0\) be the orthogonal projection onto an invariant subspace \(T_0\), and let \(B\colon S\to T\) be linear. Norms of maps are [[proofs/grh/spanning-core/hilbert-schmidt-norm-of-a-linear-map|Hilbert–Schmidt norms]].

* \(B\) is a [[proofs/grh/spanning-core/near-isometry-in-mean-square|near isometry]] if \(\lVert B\,\mathrm{pr}_U\rVert^2\ge\dim U-\varepsilon\dim S\) for all subspaces \(U\). This follows from a [[proofs/grh/spanning-core/near-isometry-from-small-defect|small defect \(B^*B-1\)]] and survives [[proofs/grh/spanning-core/near-isometry-after-projection|projections that miss little]].
* The function \(s\mapsto\lVert B^*sB\rVert^2\) is of [[proofs/grh/spanning-core/function-of-positive-type|positive type]], and [[proofs/grh/spanning-core/cauchy-schwarz-for-translates|Cauchy–Schwarz]] bounds the mean of \(\lVert\mathrm{pr}_WsB\rVert^2\) by the second moment \(\sum_s\lVert B^*sB\rVert^2\).
* **[[proofs/grh/spanning-core/one-translate-from-second-moment|One translate]].** If \(\mathrm{pr}_0B\) is a near isometry and the second moment is at most \((1+\varepsilon)\lvert\Gamma\rvert(\dim S)^2/\dim T_0\), the maps \(\mathrm{pr}_0sB\) are a [[proofs/grh/spanning-core/spread-family-of-linear-maps|spread family]]: every subspace \(W\subseteq T_0\) of share \(\alpha\) has a preimage of dimension at most \((\tfrac{1+\alpha}2+\tfrac32\varepsilon)\dim S\) under some translate.
* **[[proofs/grh/spanning-core/few-spread-maps-span-almost-everything|Few maps span]].** A greedy choice of \(O(\log(1/\varepsilon)\dim W/\dim V)\) members of a spread family spans all but a share \(16\varepsilon\) of \(W\); and [[proofs/grh/spanning-core/restricting-maps-to-a-subspace|restricting to a subspace]] of the source costs its codimension per map.

A separate tool, used in the proof of the second moment bound in the chapter on unfolding, is the estimate for [[proofs/grh/spanning-core/singular-minors-have-small-mass|singular minors]]: for a function \(\Theta\ge0\) of positive type on a finite group acting on \(k^n\), \(k\) a finite field, the \(\Theta\)-mass of the \(s\) with \(\det(A_1^{\mathsf T}\pi(s)A_0)=0\) is small if stabilisers of nonzero vectors have small mass; it rests on a [[proofs/grh/spanning-core/character-sum-bound-by-stabilisers|character sum bound]].

## 2. The Poincaré map

The abstract argument is applied to \(\Gamma=\bar G\), \(T\) the forms of principal level on \(Y_0\), \(\mathrm{pr}_0=\rho(e_0)\) (whose image is the space of target forms) and \(B=P\) the [[proofs/grh/spanning-core/scaled-poincare-map|scaled Poincaré map]] in coordinates. Its hypotheses are supplied as follows.

1. [[proofs/grh/spanning-core/unfolding-of-the-scaled-poincare-map|Unfolding]]: the blocks of \(P^*sP\) are the amplitude sums of the filling data, divided by the unipotent covolume.
2. [[proofs/grh/spanning-core/bad-types-are-rare|Bad types are rare]]: \(e_0=e_{p_0}\otimes e_{p_1}\) with central idempotents whose complements have coefficient at \(1\) at most \(\tfrac12b^{-8}\).
3. Hence \(\rho(e_0)P\) is a [[proofs/grh/spanning-core/good-poincare-map-is-a-near-isometry|near isometry]] with error \(5b^{-4}\), and the [[proofs/grh/spanning-core/second-moment-of-the-poincare-map|second moment]] is at most \((1+9b^{-4})D_X^2/(\deg\cdot\mathrm{mass}_r)\); both rest on theorems of the unfolding chapter.
4. The [[proofs/grh/spanning-core/dimension-of-the-target|dimension of the target]] is at most \(\lvert\bar G\rvert\deg\,\mathrm{mass}_r\); it is counted on the definite space \(W_m\), using the equality of multiplicities of Section 3.

The conclusion is that the maps \(\lvert\bar G\rvert e_0s\Pi\) from source forms to target forms are [[proofs/grh/spanning-core/translates-of-the-good-poincare-map-spread|spread with error \(\tfrac32\cdot\tfrac1{8b^2}\)]].

## 3. Equality of multiplicities

The [[proofs/grh/spanning-core/spherical-hecke-algebra-away-from-the-level|spherical Hecke algebra away from the level]] \(\mathcal H\) consists of families of operators on the forms of principal level of all hermitian spaces of rank \(r\), given by one element of the group algebra of the adelic points trivial at the chosen places. It contains the [[proofs/grh/spanning-core/hecke-operators-at-split-places|operators \(T_{w,i}\)]] at split places off the level, commutes with \(\bar G\) and so [[proofs/grh/spanning-core/hecke-action-on-good-forms|acts on good forms]]. The forms decompose into [[proofs/grh/spanning-core/hecke-eigensystem-part|eigensystem parts]] ([[proofs/grh/spanning-core/eigensystem-parts-decompose-the-forms|decomposition]]), and \(\mathcal H\) contains [[proofs/grh/spanning-core/hecke-projector-onto-an-eigensystem|projectors onto single eigensystems]].

The main input is a comparison of traces from the library (a simple trace formula for test functions cuspidal at one place): a member of \(\mathcal H\) has [[proofs/grh/spanning-core/equal-traces-on-good-forms|the same trace on the good forms]] of two spaces that differ only in their signs at the real places, because each good family of labels has a primitive member, which makes the test function cuspidal there. Consequences: [[proofs/grh/spanning-core/equal-multiplicities-of-eigensystems|each eigensystem has the same multiplicity]], the good forms on \(Y_0\) and \(W_j\) have the same dimension, and — since [[proofs/grh/spanning-core/translation-as-a-hecke-operator|translations off the level]] and hence [[proofs/grh/spanning-core/rallis-series-is-a-hecke-operator|the series of Rallis' formula]] are given by members of \(\mathcal H\) — the Rallis operator has the same determinant on the good forms of both spaces.

## 4. Bessel systems at a real place

The real group is the unitary group \(G_1\) of \(\varrho\) hyperbolic planes, a positive space \(X_0\) of rank \(k\) and a vector \(z\) with \(h(z,z)=-1\); the frame is \((e_1,\dots,e_\varrho,z)\).

*Sizes.* The [[proofs/grh/spanning-core/bessel-length|Bessel length]] \(\ell(y)=\inf_{s\in S}(\lVert sy\rVert+1)\) is [[proofs/grh/spanning-core/bessel-length-versus-orthogonal-frame|comparable]] to the lengths of the [[proofs/grh/spanning-core/orthogonal-frame-of-a-point|Gram–Schmidt vectors of the moved frame]], via a [[proofs/grh/spanning-core/norm-bound-from-frame-and-dual-columns|norm bound from the frame and dual columns]].

*Frames and discriminants.* The [[proofs/grh/spanning-core/frame-gram-matrix-of-an-isometry|frame Gram matrix]] \(Z(\gamma)\), the [[proofs/grh/spanning-core/frame-discriminant|frame discriminant]] \(\mathsf g=\lvert\det Z\rvert^2-N^2\lvert D_\varrho\rvert^2\) (a Gram determinant of two frames), the [[proofs/grh/spanning-core/bessel-lattice-basis|lattice basis]] and the [[proofs/grh/spanning-core/link-of-an-isometry|link]] of an isometry are set up for use in the chapters on unfolding and on the remaining terms.

*The data.* A [[proofs/grh/spanning-core/bessel-system|Bessel system]] packages a Bessel function \(W\) and its cut \(W^\flat\): a [[proofs/grh/spanning-core/cut-pair-of-bessel-functions|cut pair]], the [[proofs/grh/spanning-core/schur-bound-for-a-bessel-function|Schur bound]] for \(W\) and its derivatives, and [[proofs/grh/spanning-core/local-bounds-of-a-bessel-function|local bounds]] for \(W^\flat\). By Schur's lemma the coordinates of \(W\) are [[proofs/grh/spanning-core/normalisation-of-a-bessel-function|orthonormal]] in \(L^2(\mathsf U\backslash G_1)\).

*The open cell.* On the [[proofs/grh/spanning-core/open-cell-of-frame-matrices|open cell]] \(\Omega=\{\mathsf g>0\}\) there is an explicit [[proofs/grh/spanning-core/gram-section|Gram section]] \(Z\mapsto\gamma_Z\) with \(Z(\gamma_Z)=Z\) ([[proofs/grh/spanning-core/gram-section-is-a-section|section property]]), with [[proofs/grh/spanning-core/bounds-for-the-gram-section|polynomial bounds]]; the [[proofs/grh/spanning-core/fibres-of-the-frame-gram-map|fibres of \(Z\)]] are orbits of the fixer of the frame on both sides (Witt). In the coordinates \((s',Z,s)\mapsto s'\gamma_Zs\) Haar measure has density at least \(c_G\mathsf g(Z)^{k-1}\): this is the [[proofs/grh/spanning-core/mean-value-inequality-over-the-gram-section|mean value inequality]], obtained from [[proofs/grh/spanning-core/coordinates-on-frames-over-a-gram-matrix|coordinates on frames over a Gram matrix]]. Together with an [[proofs/grh/spanning-core/unfolding-bound-on-the-real-group|unfolding bound]] it controls [[proofs/grh/spanning-core/integral-over-the-section-orbit|integrals over the orbit of the section]], and Sobolev's inequality on a small cube turns the Schur bound into an [[proofs/grh/spanning-core/sobolev-bound-at-the-gram-section|\(L^2\) bound at \(\gamma_Z\)]].

## 5. Not covered

The files `Bessel/Average`, `Bessel/OpenCellBound`, `Bessel/OpenCellPairing`, `Bessel/LargeFunction`, `Bessel/CutTailBound`, `Bessel/SchurBound` and `Bessel/FillingData` (the open cell bound for a Bessel system, the construction of Bessel systems of discrete series type, and the filling data `New.Data.filling` of admissible data) are not translated in this chapter; items of them are referred to by their Lean names, e.g. [[?lean:New.Data.filling|the filling data of \(D\)]].

## References

1. Lean: the files listed in the front matter, under `documents/grh-lean/grh/`.
