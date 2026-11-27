+++
id = "proofs/grh/spanning-unfolding-a/eichler-element-with-prescribed-row"
title = "A unipotent element of level M with one prescribed row"
kind = "lemma"
summary = "For an integral linear form l vanishing at e_b, e_b* for b <= a, some element of the unipotent congruence subgroup has row M l at e_a and trivial rows at the other e_b, outside the column e_a*."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.exists_eichler_classUnipotent"]
lean_files = ["src/New/Spanning/Unfolding/ReducedPoints.lean"]
proof_status = "full"
+++

**Lemma.** Keep the notation of [[proofs/grh/spanning-unfolding-a/eichler-elements-of-unipotent-congruence-subgroup|Eichler elements of the unipotent congruence subgroups]]: \(E\) is a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) is [[?lean:New.Filling|filling data]] with level \(M\), \(c\) is a class and \(\mathsf U_c(M)\) the [[?lean:New.Filling.classUnipotent|unipotent congruence subgroup at \(c\)]]. Fix \(a\in\{1,\dots,\varrho\}\). Let \(l\) be a row vector over \(E\) indexed by the basis of \(V\) such that

1. \(l_j=0\) for \(j=e_b\) and for \(j=e_b^{*}\) with \(b\le a\) (the positions \((a,j)\) that are not [[?lean:New.RealPlace.IsFreeEntry|free entries]]);
2. \(l\) is integral on the lattice \(\Lambda_c\) of the class: its values on the [[?lean:New.Filling.classBasis|class basis]] lie in \(\widehat{\mathcal O}\).

Let \(s\in\mathcal O_E\) with \(\bar s=-s\). Then there is \(\gamma\in\mathsf U_c(M)\) such that for every \(b\in\{1,\dots,\varrho\}\) and every basis index \(j\) with \(j\ne e_a^{*}\), or for every \(j\) if \(l=0\),
\[
\gamma_{e_b,\,j}=\delta_{e_b,j}+M\cdot\begin{cases} l_j+ s\,[\,j=e_a^{*}\,] & b=a,\\ 0 & b\ne a.\end{cases}
\]

## Proof

The [[?c:Gram matrix|Gram matrix]] \(J\) is invertible, so \(l=u^{*}J\) for a unique column vector \(u\). Apply the [[proofs/grh/spanning-unfolding-a/eichler-elements-of-unipotent-congruence-subgroup|Eichler elements lemma]] with a one-element index set, \(p=a\), \(x=e_a\), this \(u\), and the \(1\times1\) matrix \(s\). Its hypotheses hold: the coordinate of \(u\) at \(e^{*}_{a'}\) is the conjugate of \(l_{e_{a'}}\), which is \(0\) for \(a'\le a\) by 1; \(s\) is skew and integral; and \(u\in\Lambda_c\), because the Gram matrix \(J'\) in the lattice basis is unimodular ([[?lean:New.Filling.isUnimodular_latticeMiddle|unimodularity of the lattice form]]), so a vector whose linear form \(h(u,\cdot)\) is integral on \(\Lambda_c\) lies in \(\Lambda_c\) (its coordinate vector is the [[?c:Conjugate transpose|conjugate transpose]] of the integral row \(l\cdot(\text{class basis})\cdot J'^{-1}\)).

We get \(\gamma\in\mathsf U_c(M)\) with \(\gamma-1=M\bigl(e_a\,l-(u+e_a(\tau\,l u-s))\,e_a^{*}{}^{\!\top}\bigr)\), where \(e_a^{*}{}^{\!\top}=x^{*}J\) is the row vector with the single entry \(1\) in column \(e_a^{*}\). The row \(e_b\) of \(e_a\,l\) is \(\delta_{ab}\,l\). The second matrix is supported in the column \(e_a^{*}\). Hence for \(j\ne e_a^{*}\) the entry \((e_b,j)\) of \(\gamma-1\) is \(M\delta_{ab}l_j\). If \(l=0\) then \(u=0\) and \(\gamma-1=M s\,e_a e_a^{*}{}^{\!\top}\), whose only possibly nonzero entry is \(Ms\) at \((e_a,e_a^{*})\).

## References

1. Lean: `New.Filling.exists_eichler_classUnipotent` in `src/New/Spanning/Unfolding/ReducedPoints.lean`.
