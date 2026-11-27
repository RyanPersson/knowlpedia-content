+++
id = "proofs/grh/spanning-unfolding-a/reductions-are-products-over-places"
title = "Reductions of subgroups defined by fixed entries are products over the chosen places"
kind = "theorem"
summary = "If a subgroup B of the finite adelic group is defined by prescribing entries to be those of 1, its reduction contains s as soon as each component of s is a component of an element of the reduction; this applies to the Bessel subgroup."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.mem_reducedImage_iff_forall_place", "New.Filling.mem_reducedImage_besselS_iff_forall_place"]
lean_files = ["src/New/Spanning/Unfolding/ReducedGroups.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\). Let \(B\) be a subgroup of the finite adelic unitary group (lattice basis) of the form
\[
B=\{k:\ k_{ab}=\delta_{ab}\ \text{ for all positions }(a,b)\text{ in a given set }\mathcal R\},
\]
and \(\bar B\) its [[?lean:New.Filling.reducedImage|reduced image]] in the [[?lean:New.Filling.ResidueGL|residue group]]. Then \(s=(s_w)_w\) lies in \(\bar B\) if and only if for every chosen place \(w\) there is \(t\in\bar B\) with \(t_w=s_w\). In particular this holds for the reduction \(\bar{\mathsf S}\) of the [[?lean:New.Shape.Form.besselS|Bessel subgroup]].

## Proof

One direction is trivial. For the other, since \(\bar B\) is a subgroup of a finite product, it suffices to show that for each chosen \(w\) the element with component \(s_w\) at \(w\) and \(1\) elsewhere lies in \(\bar B\). Let \(t\in\bar B\) with \(t_w=s_w\), the reduction of \(k\in K\cap B\); \(k\) is the image of an [[?c:Isometry of a hermitian space|isometry]] \(g\) over \(\widehat{\mathcal O}\), which is its own inverse adjoint (\(g^{*}Jg=J\)) and has \(g_{ab}=\delta_{ab}\) on \(\mathcal R\). By the lemma on [[proofs/grh/spanning-unfolding-a/gluing-integral-isometries-at-chosen-places|gluing]] with \(u=u'=g\) and \(P=\{w\}\), there is \(l\in K\) that agrees with \(1\) on \(\mathcal R\) — so \(l\in B\) — and whose reduction is \(g\bmod w=s_w\) at \(w\) and \(1\) at the other chosen places.

The Bessel subgroup is of this form by its definition.

## References

1. Lean: `New.Filling.mem_reducedImage_iff_forall_place` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
2. Lean: `New.Filling.mem_reducedImage_besselS_iff_forall_place` in `src/New/Spanning/Unfolding/ReducedGroups.lean`.
