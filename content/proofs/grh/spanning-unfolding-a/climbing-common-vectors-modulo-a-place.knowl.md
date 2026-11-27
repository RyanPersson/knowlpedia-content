+++
id = "proofs/grh/spanning-unfolding-a/climbing-common-vectors-modulo-a-place"
title = "Climbing modulo a place above M"
kind = "theorem"
summary = "If the reduction of an integral element k agrees and the spans of the frame and of its image meet modulo a place above M, some common vector has coefficients not both zero at the last index."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.exists_pairOccursInColumnsAt_top_of_meetsAt", "New.Filling.pairOccursInColumnsAt_succ_of_agree", "New.Filling.vecMul_frameImage_dotProduct_cons_init_eq_of_agrees", "New.Filling.exists_eichler_mem_latticeStabilizer"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
proof_status = "full"
+++

**Theorem.** Let \(E\) be a [[?c:CM field|CM field]] containing a primitive 5040-th root of unity, \(S\) [[?lean:New.Filling|filling data]] over \(E\), and \(k\) an element of the integral subgroup \(K\) ([[?lean:New.Filling.latticeStabilizer|lattice stabiliser]]) whose reduction \(\bar k\) [[?lean:New.Filling.Agrees|agrees]]: integral \(u,u'\in K\cap\mathsf U\) with \(\bar u\bar k=\bar k\bar u'\) have \(\psi(u)=\psi(u')\) ([[?lean:New.Filling.unipotentChar|unipotent character]]). Let \(p=(w,\varepsilon)\) be a place above \(M\), \(k_w\) its [[algebra-commutative/residue-field|residue field]], and \(g=\bar k[p]\) the [[proofs/grh/spanning-unfolding-a/meeting-places-and-meet-norm|action of \(\bar k\) at \(p\)]], i.e. the matrix of \(k\) reduced at \(p\). All vectors below are over \(k_w\).

1. *(One step.)* If \((\mu,\mu')\) [[proofs/grh/spanning-unfolding-a/common-vectors-of-two-flags|occurs]] at an index \(j<\varrho\) for the frame \(f\) and its image \(gf\), it occurs at \(j+1\).
2. If \(\bar k\) meets at \(p\), there are \(\mu,\mu'\in k_w\), not both zero, such that \((\mu,\mu')\) occurs at the last index \(\varrho\): \(f\cdot x=gf\cdot y\) with \(x_\varrho=\mu\), \(y_\varrho=\mu'\).

## Proof

**1.** As over \(E\) (see [[proofs/grh/spanning-unfolding-a/climbing-common-vectors-over-the-field|climbing over the field]]), by the criterion by linear forms and the shift identity it suffices to prove: if \(f\cdot x=gf\cdot y\) with \(x,y\) vanishing above \(j\), and a linear form \(m\) kills \(f_b\) and \(gf_b\) for \(b\le j\), then
\[
m(f\cdot x^{+})=m(gf\cdot y^{+}).\tag{1}
\]
*Lifts.* By the lemma on [[proofs/grh/spanning-unfolding-a/prescribing-residues-above-the-level|prescribing residues]], choose \(\ell:k_w\to\widehat{\mathcal O}\) with \(\ell(0)=0\), \(\operatorname{red}_p\ell(t)=t\) and \(\operatorname{red}_{p'}\ell(t)=0\) for the other places \(p'\) above \(M\). In particular the conjugates \(\overline{\ell(t)}\) reduce to \(0\) at all places \((q,\varepsilon)\) with the same sign \(\varepsilon\), because \(\operatorname{red}_{(q,\varepsilon)}(\bar a)=\operatorname{red}_{(q,\neg\varepsilon)}(a)\) and \((q,\neg\varepsilon)\ne p\). For \(g'\in\{1,g\}\) and coordinates \(z\in\{x,y\}\) put
\[
\Pi(g',z)=\sum_b\ell\bigl(m(g'f_{b+1})\bigr)\,\ell(z_b)\in\widehat{\mathcal O},
\]
whose reduction at \(p\) is \(m(g'f\cdot z^{+})\). By the description of divisibility by \(M\) ([[?lean:New.Filling.inv_ideleM_smul_mem_iff|divisibility by the level]]: \(M^{-1}a\in\widehat{\mathcal O}\) iff \(a\) reduces to \(0\) at all places above \(M\)), (1) follows once \(M^{-1}\bigl(\Pi(1,x)-\Pi(g,y)\bigr)\in\widehat{\mathcal O}\). The ring \(\widehat{\mathcal O}\) is self-dual for the character \(\chi(a)=\psi_f(-a/\varpi)\) ([[?lean:New.Filling.forall_selfDualChar_mul_eq_one_iff|self-duality of the integral adeles]]), so it suffices that for all \(r\in\widehat{\mathcal O}\)
\[
\chi\bigl(M^{-1}r\,\Pi(1,x)\bigr)=\chi\bigl(M^{-1}r\,\Pi(g,y)\bigr).\tag{2}
\]

*Integral Eichler maps.* Let \(a=j+1\), \(r\in\widehat{\mathcal O}\), \(\tilde z\in\widehat{\mathcal O}^{\varrho+1}\) vanishing from \(a\) on, and \(\tilde m\) an integral linear form killing the frame vectors of index \(<a\). Choosing \(v\) with \(h(v,\cdot)=\tilde m\) over \(\widehat{\mathcal O}\) (the lattice form is unimodular) and an integral \(\tau\) with \(\tau+\bar\tau=1\) (which exists as \(E\) contains a primitive 5040-th root of unity), the [[?lean:New.exists_mem_besselU_eq_eichlerMap|Eichler map]] \(y\mapsto y+h(v,y)X-h(X,y)(v+\varsigma X)\) along \(X=r\,f\cdot\tilde z\) is an element \(u\in K\cap\mathsf U\) with [[?lean:New.simpleRootSum|simple root sum]] \(\sigma(u)=r\sum_b\tilde m(f_{b+1})\tilde z_b\). Modulo a place \(p'\) above \(M\) at which all \(\overline{\tilde z_b}\) reduce to \(0\), the term \(h(X,y)(\dots)\), which is conjugate-linear in \(X\), vanishes, and
\[
u\equiv1+\operatorname{red}_{p'}(r)\,(f\cdot\bar z)\,\bar m\qquad(\text{rank one}),
\]
with \(\bar z,\bar m\) the reductions at \(p'\).

Apply this to \(\tilde z=\ell\circ x\), \(\tilde m=\ell\circ m\), giving \(u\) with \(\sigma(u)=r\,\Pi(1,x)\); and to \(\tilde z=\ell\circ y\), \(\tilde m=\ell\circ(m\circ g)\), giving \(u'\) with \(\sigma(u')=r\,\Pi(g,y)\). By the vanishing properties of \(\ell\), at the places \((q,\varepsilon)\):
\[
\bar u[(w,\varepsilon)]=1+\bar r\,(f\cdot x)\,m,\qquad\bar u'[(w,\varepsilon)]=1+\bar r\,(f\cdot y)\,(m\circ g),\qquad\bar u[(q,\varepsilon)]=\bar u'[(q,\varepsilon)]=1\ (q\ne w).
\]
*Commutation.* At \(p\): \(\bar u[p]\,g=g+\bar r(f\cdot x)(m\circ g)\) and \(g\,\bar u'[p]=g+\bar r\,(gf\cdot y)(m\circ g)\); these agree since \(gf\cdot y=f\cdot x\). At the other places \((q,\varepsilon)\) both are \(\bar k[(q,\varepsilon)]\). An element of the residue group is determined by its actions at the places of one sign, so \(\bar u\,\bar k=\bar k\,\bar u'\). As \(\bar k\) agrees, \(\psi(u)=\psi(u')\), i.e. \(\chi(M^{-1}\sigma(u))=\chi(M^{-1}\sigma(u'))\), which is (2).

**2.** Let \(x\ne0,y\) with \(f\cdot x=gf\cdot y\), and let \(j\) be the top index of \((x,y)\). Then \((x_j,y_j)\) occurs at \(j\) and is not \((0,0)\). By 1 and induction it occurs at the last index.

## References

1. Lean: `New.Filling.exists_pairOccursInColumnsAt_top_of_meetsAt` in `src/New/Spanning/Unfolding/Climbing.lean`.
2. Lean: `New.Filling.pairOccursInColumnsAt_succ_of_agree` in `src/New/Spanning/Unfolding/Climbing.lean`.
3. Lean: `New.Filling.vecMul_frameImage_dotProduct_cons_init_eq_of_agrees` in `src/New/Spanning/Unfolding/Climbing.lean`.
4. Lean: `New.Filling.exists_eichler_mem_latticeStabilizer` in `src/New/Spanning/Unfolding/Climbing.lean`.
