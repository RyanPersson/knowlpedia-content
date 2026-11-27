+++
id = "proofs/grh/spanning-unfolding-a/reduction-of-unitriangular-matrices"
title = "Reduction of unitriangular matrices modulo a triangular discrete group"
kind = "lemma"
summary = "If a group of unitriangular matrices has entries in L above the diagonal and contains the elementary matrices with entries in L, each unitriangular matrix has exactly one translate with entries in a set of representatives modulo L."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.existsUnique_mul_unitriangular_mem"]
lean_files = ["src/New/Spanning/Unfolding/ReducedPoints.lean"]
proof_status = "full"
+++

**Lemma.** Let \(R\) be a commutative ring, \(L\subseteq R\) an additive submonoid and \(D\subseteq R\) a set such that for every \(w\in R\) there is exactly one \(l\in L\) with \(l+w\in D\). Let \(\Gamma\) be a subgroup of the group of [[?c:Unitriangular matrix|upper unitriangular]] \(n\times n\) matrices over \(R\) such that

1. for all \(a<b\) and \(l\in L\) the elementary matrix \(1+l\,E_{ab}\) belongs to \(\Gamma\);
2. for all \(\gamma\in\Gamma\) and \(a<b\), \(\gamma_{ab}\in L\).

Then for every upper unitriangular matrix \(x\) there is exactly one \(\gamma\in\Gamma\) such that \((x\gamma)_{ab}\in D\) for all \(a<b\).

## Proof

Use as coordinates of a unitriangular matrix \(g\) its entries \(g_{ab}\), \(a<b\), and grade the position \((a,b)\) by \(\deg(a,b)=b-a\ge1\). The coordinates determine \(g\).

*Triangular action.* Let \(\gamma\in\Gamma\) and a position \((a,b)\) be such that \(\gamma_{a'b'}=0\) for all positions of degree \(<b-a\). Then for every unitriangular \(g\),
\[
(g\gamma)_{ab}=\sum_{l}g_{al}\gamma_{lb}=\gamma_{ab}+g_{ab},
\]
because \(g_{al}=0\) for \(l<a\), \(\gamma_{lb}=0\) for \(l>b\), and for \(a<l<b\) the position \((l,b)\) has degree \(b-l<b-a\), so \(\gamma_{lb}=0\); the terms \(l=a\) and \(l=b\) give \(\gamma_{ab}\) and \(g_{ab}\). Also the elementary matrix \(1+lE_{ab}\) has coordinate \(l\) at \((a,b)\) and \(0\) at every other position.

*Existence.* Treat the positions in order of increasing degree. Suppose \(\gamma\in\Gamma\) puts the coordinates of \(x\gamma\) at a set \(s\) of positions into \(D\), where \(s\) is closed downward in degree relative to the next position \(p=(a,b)\) (all positions of \(s\) have degree \(\le\deg p\)). Choose \(l\in L\) with \(l+(x\gamma)_{ab}\in D\) and \(\delta=1+lE_{ab}\in\Gamma\). By the triangular action applied to \(\delta\), \((x\gamma\delta)_{ab}=l+(x\gamma)_{ab}\in D\), and for \(q\in s\), \((x\gamma\delta)_q=\delta_q+(x\gamma)_q=(x\gamma)_q\). After all positions are treated, \(x\gamma\) has all coordinates in \(D\).

*Uniqueness.* Let \(x\gamma\) and \(x\gamma\delta\) both have all coordinates in \(D\), \(\delta\in\Gamma\). By induction on the degree, all coordinates of \(\delta\) vanish: if those of degree \(<\deg p\) vanish, then \(\delta_p\in L\) by 2 and \(\delta_p+(x\gamma)_p=(x\gamma\delta)_p\in D\); as also \(0+(x\gamma)_p\in D\), uniqueness of the translate gives \(\delta_p=0\). Hence \(\delta=1\).

## Remarks

The source deduces this from a general statement about injective graded coordinates on a group with a triangular right action, [[?lean:New.Filling.existsUnique_mul_mem_box|unique translate into a box]]; the argument above is that proof specialised to matrix entries.

## References

1. Lean: `New.Filling.existsUnique_mul_unitriangular_mem` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
