+++
id = "proofs/grh/spanning-unfolding-b/eichler-map-in-bessel-unipotent-group"
title = "Eichler maps in the Bessel unipotent group"
kind = "lemma"
summary = "The Eichler map along a combination of low frame vectors and a vector orthogonal to them is a unipotent isometry, and its simple root sum is computed."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_mem_besselU_eq_eichlerMap"]
lean_files = ["src/New/Spanning/Unfolding/BesselLevelStructure.lean"]
proof_status = "full"
+++

**Lemma.** Let \(A\) be a commutative ring with involution and a fixed element \(\tau\) with \(\tau+\bar\tau=1\). Let \((\varrho,\kappa,k_0)\) be a shape, \(T\) a matrix on \(\kappa\sqcup\{z\}\) such that the [[?lean:New.Shape.Form.splitGram|split Gram matrix]] \(J\) of \(\varrho\) hyperbolic planes and \(T\) is hermitian and invertible, and \(h(y,y')=y^*Jy'\). Let \(f_0,\dots,f_\varrho\) be the frame \((e_0,\dots,e_{\varrho-1},z)\).

Let \(0\le a\le\varrho\), let \(j=(j_0,\dots,j_\varrho)\in A^{\varrho+1}\) with \(j_b=0\) for \(b\ge a\), let \(r\in A\) and \(x=r\sum_bj_bf_b\). Let \(v\) be a vector with \(h(v,f_b)=0\) for all \(b<a\). Put \(\varsigma=\tau\,h(v,v)\). Then the [[?lean:New.eichlerMap|Eichler map]]
\[
\mathcal{E}\colon y\longmapsto y+h(v,y)\,x-h(x,y)\,(v+\varsigma x)
\]
is an element of the [[?lean:New.Shape.Form.besselU|Bessel unipotent group]] \(\mathsf{U}\) of \(J\), and its [[?lean:New.simpleRootSum|simple root sum]] is
\[
\sigma(\mathcal{E})=r\sum_{b=0}^{\varrho-1}j_b\,h(v,f_{b+1}) .
\]

## Proof

Since \(j_\varrho=0\), \(x=\sum_{b<\varrho}rj_b\,e_b\) has only \(e\)-coordinates. As \(h(e_b,\cdot)\) reads the \(e_b^*\)-coordinate, the row vector \(x^*J\) is supported on the \(e^*\)-coordinates, with entry \(\overline{rj_b}\) at \(e_b^*\). The \(e_c^*\)-coordinate of \(v\) is \(\overline{h(v,e_c)}\), which vanishes for \(c<a\); and \(j_b=0\) for \(b\ge a\). Hence for \(c\le b<\varrho\), either \(j_b=0\) or \(v_{e_c^*}=0\). \((\ast)\)

*Isometry.* \(h(x,x)=0\) because \(x\) lies in the isotropic span of the \(e_b\). \(h(v,x)=\sum_b\overline{v_{e_b^*}}\,rj_b=0\) by \((\ast)\) with \(c=b\). Because \(J\) is hermitian, \(\overline{h(v,v)}=h(v,v)\), so \(\varsigma+\bar\varsigma=(\tau+\bar\tau)h(v,v)=h(v,v)\). Under these three conditions the Eichler map is an isometry of \(J\) ([[?lean:New.exists_unitary_eq_eichlerMap|Eichler maps are unitary]]).

*Unipotence.* \(\mathsf{U}\) consists of the isometries whose entries \((p,q)\) with \(\operatorname{level}(q)\le\operatorname{level}(p)\) are those of the identity, where the level is \(b\) on \(e_b\), \(\varrho\) on the middle block and \(2\varrho-b\) on \(e_b^*\). The matrix of \(\mathcal{E}\) is \(1+x\,(v^*J)-(v+\varsigma x)\,(x^*J)\). In the first correction, a nonzero entry \((p,q)\) needs \(p=e_b\) with \(j_b\ne0\); if \(\operatorname{level}(q)\le b\) then \(q=e_c\) with \(c\le b\), and \((v^*J)_{e_c}=\overline{v_{e_c^*}}=0\) by \((\ast)\). In the second, a nonzero entry needs \(q=e_b^*\) with \(j_b\ne0\); if \(\operatorname{level}(p)\ge2\varrho-b\) then \(p=e_c^*\) with \(c\le b\), and \((v+\varsigma x)_{e_c^*}=v_{e_c^*}=0\) by \((\ast)\). So \(\mathcal{E}\in\mathsf{U}\).

*Simple root sum.* For \(b<\varrho\), the column index \(f_{b+1}\) is \(e_{b+1}\) or \(z\), where \(x^*J\) vanishes; so the entry of \(\mathcal{E}\) at \((f_b,f_{b+1})=(e_b,f_{b+1})\) is \(x_{e_b}(v^*J)_{f_{b+1}}=rj_b\,h(v,f_{b+1})\). Summing over \(b\) gives the formula.

## Remarks

In Lean the formula reads \(\sigma=r\sum_{c}m(f_c)\,j'_c\) with \(m=v^*J\) and \(j'=(0,j_0,\dots,j_{\varrho-1})\) the shifted sequence; this is the same sum.

## References

1. Lean: `New.exists_mem_besselU_eq_eichlerMap` in `src/New/Spanning/Unfolding/BesselLevelStructure.lean`.
