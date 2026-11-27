+++
id = "proofs/grh/spanning-unfolding-a/climbing-common-vectors-over-the-field"
title = "Climbing: common vectors of the frame and its image move up the flags"
kind = "theorem"
summary = "If the characters of gamma agree, the leading coefficients of a common vector of the flags of f and gamma f have equal norms and occur at all higher indices."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.mul_star_eq_and_pairOccursAt_of_le", "New.Filling.pairOccursAt_succ", "New.Filling.CharsAgree.pairOccursAt_mono", "New.Filling.CharsAgree.mul_star_eq_of_pairOccursAt", "New.Filling.mul_star_eq_and_ne_zero_and_exists_isTopIndex", "New.Filling.CharsAgree.mul_star_eq_of_isTopIndex", "New.Filling.CharsAgree.mul_star_ne_zero_of_isTopIndex", "New.Filling.CharsAgree.exists_isTopIndex_apply_eq"]
lean_files = ["src/New/Spanning/Unfolding/Climbing.lean"]
proof_status = "full"
+++

**Theorem.** Let \(S\) be [[?lean:New.Filling|filling data]] over a [[?c:CM field|CM field]] \(E\), \(f=(f_0,\dots,f_\varrho)=(e_1,\dots,e_\varrho,z)\) the frame, and \(\gamma\) a rational [[?c:Isometry of a hermitian space|isometry]] of \(V\) whose characters [[?lean:New.Filling.CharsAgree|agree]]: \(\psi(u)=\psi(u')\) for all rational \(u,u'\in\mathsf U\) with \(u\gamma=\gamma u'\). Say that \((\mu,\mu')\in E^2\) [[?lean:New.PairOccursAt|occurs at \(j\)]] if \(\sum_bx_bf_b=\sum_by_b\gamma f_b\) for some \(x,y\in E^{\varrho+1}\) vanishing above \(j\) with \(x_j=\mu\), \(y_j=\mu'\) (the notion of [[proofs/grh/spanning-unfolding-a/common-vectors-of-two-flags|common vectors of two flags]] for \(f\) and \(\gamma f\)).

1. If \((\mu,\mu')\) occurs at \(j\), then it occurs at every \(l\ge j\), and \(\mu\bar\mu=\mu'\bar\mu'\).
2. Let \(x\ne0\) and \(y\) be the coordinates of a common vector, \(\sum x_bf_b=\sum y_b\gamma f_b\), with top index \(j\). Then \(x_j\bar x_j=y_j\bar y_j\ne0\), and for every \(l\ge j\) there is a common vector with coordinates \(x',y'\) of top index \(l\) and \(x'_l=x_j\), \(y'_l=y_j\).

## Proof

**One step.** Let \((\mu,\mu')\) occur at \(j<\varrho\), through \(x,y\). By the criterion by linear forms it suffices to show: for every linear form \(m\) on \(V\) killing \(f_b\) and \(\gamma f_b\) for \(b\le j\), \(\mu\,m(f_{j+1})=\mu'\,m(\gamma f_{j+1})\). By the shift identity, with \(x^{+}\) the coordinates \(x\) shifted up by one index (\(x^{+}_{b+1}=x_b\), \(x^{+}_0=0\)), this says
\[
m(f\cdot x^{+})=m(\gamma f\cdot y^{+}).\tag{1}
\]
Let \(t\in E\) and \(r=-M\varpi t\). Choose \(v\in V\) with \(h(v,\cdot)=m\circ\gamma\); then \(h(\gamma v,\cdot)=m\). By the construction of [[?lean:New.exists_mem_besselU_eq_eichlerMap|Eichler maps in the unipotent group]] (for a vector \(v_0\) orthogonal to the frame vectors of index \(\le j\) and coordinates \(x_0\) vanishing above \(j\), the Eichler map \(y\mapsto y+h(v_0,y)X-h(X,y)(v_0+\varsigma X)\) along \(X=r\,f\cdot x_0\), with \(\varsigma=\tau h(v_0,v_0)\), \(\tau+\bar\tau=1\), lies in \(\mathsf U\) and its [[?lean:New.simpleRootSum|simple root sum]] is \(r\,h(v_0,f\cdot x_0^{+})\)), we get
\[
u\in\mathsf U\ \text{along } r f\cdot x \text{ with } v_0=\gamma v,\quad\sigma(u)=r\,m(f\cdot x^{+});\qquad w\in\mathsf U\ \text{along } rf\cdot y\text{ with }v_0=v,\quad\sigma(w)=r\,m(\gamma f\cdot y^{+}).
\]
Since \(\gamma\) is an isometry, \(\gamma w\gamma^{-1}\) is the Eichler map along \(r\gamma f\cdot y=rf\cdot x\) with the vector \(\gamma v\) and the same \(\varsigma\); so \(u\gamma=\gamma w\). As the characters agree, \(\psi(u)=\psi(w)\). Now \(\psi(g)=\psi_f\bigl(-\sigma(g)/(M\varpi)\bigr)\), so for \(\sigma(g)=rd\) one has \(\psi(g)=\psi_f(t\,d)\). Hence \(\psi_f(t\,d_1)=\psi_f(t\,d_2)\) for all \(t\in E\), with \(d_1,d_2\) the two sides of (1). Since \(E\) is dense in the [[catalog/arithmetic/adeles-number-field-finite|finite adeles]] and \(\psi_f\) is continuous, this holds for all finite adeles \(t\), and the pairing \(\psi_f(t\,a)\) separates finite adeles ([[?lean:New.eq_of_forall_ψf_mul_eq|nondegeneracy of the additive character]]); so \(d_1=d_2\), which is (1).

**1.** Occurrence at all \(l\ge j\) follows from the step by induction. In particular \((\mu,\mu')\) occurs at the last index \(\varrho\): \(f\cdot x=\gamma f\cdot y\) with \(x_\varrho=\mu\), \(y_\varrho=\mu'\). The vectors \(e_a\) are isotropic and orthogonal to each other and to \(z\), so \(h(f\cdot x,f\cdot x)=-N\mu\bar\mu\), and as \(\gamma\) is an isometry \(h(\gamma f\cdot y,\gamma f\cdot y)=-N\mu'\bar\mu'\) ([[?lean:New.Filling.star_mul_last_eq_of_frameImage_eq|equal norms of the last coefficients]]). Hence \(\mu\bar\mu=\mu'\bar\mu'\).

**2.** The pair \((x_j,y_j)\) occurs at \(j\), so by 1 \(x_j\bar x_j=y_j\bar y_j\). Since \(x\ne0\) and \(j\) is the top index, one of \(x_j,y_j\) is nonzero; \(E\) is a field, so the common value of the norms is nonzero. For \(l\ge j\), a common vector with coefficients \((x_j,y_j)\) at \(l\) vanishing above \(l\) has top index \(l\) because these coefficients are not both zero.

## References

1. Lean: `New.Filling.mul_star_eq_and_pairOccursAt_of_le` in `src/New/Spanning/Unfolding/Climbing.lean`.
2. Lean: `New.Filling.pairOccursAt_succ` in `src/New/Spanning/Unfolding/Climbing.lean`.
3. Lean: `New.Filling.CharsAgree.pairOccursAt_mono` in `src/New/Spanning/Unfolding/Climbing.lean`.
4. Lean: `New.Filling.CharsAgree.mul_star_eq_of_pairOccursAt` in `src/New/Spanning/Unfolding/Climbing.lean`.
5. Lean: `New.Filling.mul_star_eq_and_ne_zero_and_exists_isTopIndex` in `src/New/Spanning/Unfolding/Climbing.lean`.
6. Lean: `New.Filling.CharsAgree.mul_star_eq_of_isTopIndex` in `src/New/Spanning/Unfolding/Climbing.lean`.
7. Lean: `New.Filling.CharsAgree.mul_star_ne_zero_of_isTopIndex` in `src/New/Spanning/Unfolding/Climbing.lean`.
8. Lean: `New.Filling.CharsAgree.exists_isTopIndex_apply_eq` in `src/New/Spanning/Unfolding/Climbing.lean`.
