+++
id = "proofs/grh/upper-elementary-divisors/colength-of-factored-operator"
title = "Colength of the image of the operator factored through edges"
kind = "proposition"
summary = "Under large degree, the image of the pairing with the dual restrictions composed with the restriction to edges, plus p^m times everything, has colength dividing p^l with l at most (3 c_div + theta m) times the rank."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.FrobeniusCycle.exists_colengthDvd_range_pairingMap_mul_edgeRestriction", "New.FrobeniusCycle.IsLargeDegree.exists_basis_det_dvd", "New.colengthDvd_mul_mul_of_smul_top_le", "New.FrobeniusCycle.divisorConstant_nonneg"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean"]
proof_status = "full"
+++

We use the notion "[[?lean:New.ColengthDvd|the colength of \(N'\) in \(M'\) divides \(z\)]]" of the area on lattices: for submodules \(M',N'\) of an \(O\)-module and \(z\in O\), it means that for every finite family \(\Phi_1,\dots,\Phi_\nu\in M'\) there is a \(\nu\times\nu\) matrix \(\mu\) over \(O\) with \(\det\mu\mid z\) and \(\sum_k\mu_{ik}\Phi_k\in N'\) for all \(i\).

**Proposition.** Let \(O\) be a valuation ring and a domain of characteristic \(0\), \(T\) a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] for \((N,W,O)\) with \(p\) not a unit of \(O\), the degree [[proofs/grh/upper-elementary-divisors/large-degree-conditions|large]] for \((k,n,r,\theta)\), and \((b,b')\) an [[proofs/grh/upper-elementary-divisors/edge-pairing|edge pairing]]. Let \(V,H,\mathrm{Ed}\) be finite sets, \(u_e\in\mathrm{GL}_H(O)\) for \(e\in\mathrm{Ed}\), and \(\operatorname{src},\operatorname{src}'\colon H\times\mathrm{Ed}\to V\), \(g,g'\colon H\times\mathrm{Ed}\to\mathrm{GL}_k(W)\) such that both maps \(e\mapsto(\operatorname{src}e,g_e^{-1}\mathrm{Par}_r)\) and \(e\mapsto(\operatorname{src}'e,g_e'^{-1}\mathrm{Par}_r)\) onto \(V\times\mathrm{GL}_k(W)/\mathrm{Par}_r(W)\) are surjective, and \(\#(H\times\mathrm{Ed})=\#V\cdot[\mathrm{GL}_k(W):\mathrm{Par}_r(W)]\). Let \(\mathrm{Res},\mathrm{Res}'\) be the corresponding [[proofs/grh/upper-elementary-divisors/origin-functions|restrictions to edges]] and \(\mathbf{A}=\mathrm{Add}_{\mathrm{Res}'}\cdot\mathrm{Res}\) ([[proofs/grh/upper-elementary-divisors/pairing-map-and-near-inverse|pairing map]]). Then for every \(m\in\mathbb{N}\) there is \(l\in\mathbb{N}\) with
\[
l\le\bigl(3\Delta_T(k,n,r)+\theta m\bigr)\cdot\#V\cdot\#\mathcal{E}
\]
such that the colength of \(\operatorname{im}\mathbf{A}+p^{m}O^{V\times\mathcal{E}}\) in \(O^{V\times\mathcal{E}}\) divides \(p^{l}\).

## Proof

*Both ends.* The residue field of \(O\) has characteristic \(p\). By [[proofs/grh/upper-elementary-divisors/origin-functions-summand-of-small-colength|the theorem on origin functions]] and the bound on [[proofs/grh/upper-elementary-divisors/sum-of-dimensions-of-deep-forms|deep forms]] over \(\bar O\) (valid as \(0<2r\le k\); the divisor constant is unchanged by base change), \(\mathrm{Res}=Qd\) with \(RQ=1\), \(\operatorname{im}Q\) the module of origin functions, and \(\det d\mid w^{\#V\cdot D}\), \(D=\lfloor\Delta_T(k,n,r)\#\mathcal{E}\rfloor\). Likewise \(\mathrm{Res}'=Q'd'\). The images of \(Q,Q'\) are \(\mathcal{A}(k,n,r)\)-valued (part (b) of that theorem). Since \({}^t(Q'd')={}^td'\,{}^tQ'\),
\[
\mathbf{A}={}^{t}d'\cdot(\mathrm{Add}_{Q'}\cdot Q)\cdot d,\qquad\det({}^td')\det(d)\mid w^{2\#VD}=p^{\#VD}.
\]
*The middle.* Let \((C,S,\mathrm{Av})\) be an [[proofs/grh/upper-elementary-divisors/edge-conditions|edge condition]] (it exists under large degree). By [[proofs/grh/upper-elementary-divisors/few-further-generators|the corollary on further generators]] (\(k\ge2\)), with \(c_2=2Nc_0\): \(p^{c_2}O^{V\times\mathcal{E}}\subseteq\operatorname{im}(\mathrm{Add}_{Q'}Q)+\operatorname{span}(s)\), \(\#s\le\theta\#V\#\mathcal{E}\).

*Colengths add.* Write \(A_0=\mathrm{Add}_{Q'}Q\), \(E=V\times\mathcal{E}\), \(z=p^{m}\), \(G=\operatorname{span}(s)\). We use the following facts about colengths from the area on lattices: (i) the image of a square matrix \(M\) has colength dividing \(\det M\) in \(O^{E}\) ([[?lean:New.ColengthDvd.of_det_dvd|by the Smith form]]); (ii) colengths multiply along chains \(M_1\rightsquigarrow M_2\rightsquigarrow M_3\) ([[?lean:New.ColengthDvd.trans|transitivity]]) and push forward along linear maps ([[?lean:New.ColengthDvd.map|images]]); (iii) the colength of \(N'+zO^{E}\) in \(N'+\operatorname{span}(s)\) divides \(z^{\#s}\) ([[?lean:New.colengthDvd_sup_span|span of a finite set]]). Then: the colength of \(\operatorname{im}A_0+G\) in \(O^{E}\) divides \(a^{\#E}\), \(a=p^{c_2}\) (by (i) for \(a\cdot1\), as \(aO^{E}\subseteq\operatorname{im}A_0+G\)); the colength of \(\operatorname{im}(A_0d)+G\) in \(\operatorname{im}A_0+G\) divides \(\det d\) (push (i) for \(d\) forward along \(A_0\)); the colength of \(\operatorname{im}(A_0d)+zO^{E}\) in \(\operatorname{im}(A_0d)+G\) divides \(z^{\#s}\) by (iii); finally push the chain forward along \({}^td'\) and precede it by (i) for \({}^td'\). Altogether the colength of \(\operatorname{im}({}^td'A_0d)+zO^{E}\) in \(O^{E}\) divides \(\det({}^td')\,a^{\#E}\det(d)\,z^{\#s}\), which divides \(p^{l}\) with \(l=\#VD+c_2\#V\#\mathcal{E}+m\#s\).

*The exponent.* \(D\le\Delta\#\mathcal{E}\), \(c_2=2Nc_0\le2\Delta\) ([[proofs/grh/upper-elementary-divisors/consequences-of-large-degree|consequences of large degree]], 5) and \(\#s\le\theta\#V\#\mathcal{E}\) give \(l\le(3\Delta+\theta m)\#V\#\mathcal{E}\). \(\square\)

## References

1. Lean: `New.FrobeniusCycle.exists_colengthDvd_range_pairingMap_mul_edgeRestriction`, `New.FrobeniusCycle.IsLargeDegree.exists_basis_det_dvd`, `New.colengthDvd_mul_mul_of_smul_top_le`, `New.FrobeniusCycle.divisorConstant_nonneg` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.
