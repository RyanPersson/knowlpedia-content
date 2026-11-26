+++
id = "proofs/grh/upper-objects/free-levels-at-the-chosen-places"
title = "Levels that are principal at the chosen places are free"
kind = "theorem"
summary = "In rank at most 2 n_m, a level whose elements reduce to 1 at the chosen places has trivial stabilisers of all classes; for an arbitrary integral level the stabilisers have order dividing the chosen group order."
aliases = ["free levels"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.classAut_eq_bot_of_le_levelOf_chosenPlace", "New.Data.classAut_eq_bot_of_le_chosenLevel", "New.Data.card_classAut_dvd_chosenGroupOrder"]
lean_files = ["src/New/UpperBound/Objects/LiftChains.lean"]
proof_status = "full"
+++

Let \(D\) be admissible data, \(n\) a finite index set, \(G=U(I_n)(\mathbb A_f)\) over \(E\), \(\Gamma\subset G\) the rational points of the standard definite unitary group, \(K_0\) the stabiliser of the standard lattice, and \(n_m=k+m(t+1)\). See [[proofs/grh/upper-objects/chosen-places-and-chosen-group-order|chosen level and chosen group order]].

**Theorem.**

1. Let \(i\in\{0,1\}\), let \(K\subseteq K_0\) consist of elements reducing to \(1\) at the chosen places above \(p_i\), and let \(\lvert n\rvert\le4n_m\). Then \(\Gamma\cap gKg^{-1}=1\) for all \(g\in G\).
2. If \(K\) is contained in the chosen level and \(\lvert n\rvert\le2n_m\), then \(\Gamma\cap gKg^{-1}=1\) for all \(g\in G\).
3. If \(K\subseteq K_0\) and \(\lvert n\rvert\le2n_m\), then \(\lvert\Gamma\cap gKg^{-1}\rvert\) divides the chosen group order, for all \(g\in G\).

## Proof

*1.* The Lean theorem `New.Variety.classAut_eq_bot` (a unitary variant of [[?c:Minkowski's lemma on integral matrices of finite order|Minkowski's lemma]], in another area; cited) states, for a CM field with at least two infinite places: if \(K\) consists of integral elements reducing to \(1\) at a family of distinct places the product of whose norms exceeds \((2\lvert n\rvert)^{[E:\mathbb Q]}\), then all stabilisers \(\Gamma\cap gKg^{-1}\) are trivial. Here the \(f\) chosen places above \(p_i\) have norm \(p_i\), \([E:\mathbb Q]=2f\), and \((2\cdot4n_m)^2<p_i\) by the sizes of the data, so \((2\lvert n\rvert)^{2f}\le((8n_m)^2)^f<p_i^f\).

*2.* The chosen level is contained in the level of 1 for \(i=0\).

*3.* Conjugation by \(g^{-1}\) maps \(\Gamma\cap gKg^{-1}\) into \(K\subseteq K_0\); compose with the reduction at the chosen places to get a homomorphism to \(\prod_{w\in C}\mathrm{GL}_n(\mathbb F_w)\). An element \(\gamma\) of its kernel lies in \(\Gamma\cap gK'g^{-1}\) with \(K'\) the chosen level, hence is trivial by 2. So the homomorphism is injective and the order divides \(\lvert\prod_w\mathrm{GL}_n(\mathbb F_w)\rvert\), which divides the chosen group order since \(\lvert n\rvert\le2n_m\le rt\). \(\square\)

## References

1. Lean: `New.Data.classAut_eq_bot_of_le_chosenLevel`, `New.Data.card_classAut_dvd_chosenGroupOrder` in `src/New/UpperBound/Objects/LiftChains.lean`; `New.Variety.classAut_eq_bot`.
