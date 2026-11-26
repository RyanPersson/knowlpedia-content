+++
id = "proofs/grh/upper-elementary-divisors/few-further-generators"
title = "Few further generators for the image of the pairing"
kind = "proposition"
summary = "For a split injection Q and a near inverse B of A whose images satisfy conditions C, a multiple a of everything lies in the image of AQ plus the span of few vectors, their number bounded by the dimension of the reductions S; applied to the pairing map this gives at most theta times the rank further generators."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_finset_card_le_smul_top_le_sup_span", "New.exists_elementary_divisors_mod_summand", "New.card_add_card_le_mul_finrank", "New.smul_top_le_of_le_sup_smul_top", "New.FrobeniusCycle.IsEdgeCondition.exists_finset_smul_top_le_range_sup_span"]
lean_files = ["src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean"]
proof_status = "full"
+++

**Proposition (linear algebra).** Let \(O\) be a valuation ring and a domain with maximal ideal \(\mathfrak{m}\) and residue field \(\bar O\); let \(X,I,E\) be finite sets, \(Q,B\colon O^{E}\to O^{X\times I}\) and \(R,A\colon O^{X\times I}\to O^{E}\) matrices, \(a,u,w\in O\), \(C\subseteq O^{I}\) a submodule and \(S\subseteq\bar O^{I}\) a subspace. Assume: \(RQ=1\); \(w\in\mathfrak{m}\) and \(aw\mid u\); every entry of \(AB-a\cdot1\) is divisible by \(u\); every vector \(\varphi\) in the image of \(Q\) or of \(B\) is \(C\)-valued (\(\varphi(x,\cdot)\in C\) for all \(x\)); and for every \(h\in O^{I}\) with \(uh\in C\) the reduction of \(h\) lies in \(S\). Then there is a finite set \(s\subseteq O^{E}\) with
\[
\#E+\#s\le\#X\cdot\dim_{\bar O}S\qquad\text{and}\qquad a\,O^{E}\subseteq\operatorname{im}(AQ)+\operatorname{span}(s).
\]

**Corollary.** Let \(O\) have characteristic \(0\), \(T\) be a [[proofs/grh/upper-elementary-divisors/frobenius-cycle|Frobenius cycle]] with \(p\) not a unit of \(O\), \(k\ge2\), \((b,b')\) an [[proofs/grh/upper-elementary-divisors/edge-pairing|edge pairing]], and \((C,S,\mathrm{Av})\) an [[proofs/grh/upper-elementary-divisors/edge-conditions|edge condition]] for \((r,c,\theta,b)\) with \(c=5Nc_0\). Let \(V,H,\mathrm{Ed}\) be finite with \(\#(H\times\mathrm{Ed})=\#V\cdot[\mathrm{GL}_k(W):\mathrm{Par}_r(W)]\), \(u_e\in\mathrm{GL}_H(O)\), and let \(Q,Q'\colon O^{V\times\mathcal{E}}\to O^{(H\times\mathrm{Ed})\times\mathcal{E}}\) have left inverses \(R,R'\) and \(\mathcal{A}(k,n,r)\)-valued images. Then there is a finite set \(s\) with \(\#s\le\theta\,\#V\,\#\mathcal{E}\) and
\[
p^{2Nc_0}\,O^{V\times\mathcal{E}}\subseteq\operatorname{im}\bigl(\mathrm{Add}_{Q'}\cdot Q\bigr)+\operatorname{span}(s),
\]
with \(\mathrm{Add}_{Q'}\) the [[proofs/grh/upper-elementary-divisors/pairing-map-and-near-inverse|pairing map]].

## Proof

*Elementary divisors modulo a summand.* Let \(B'=B-QRB\) (the part of \(B\) in \(\ker R\)), and take a Smith form \(B'R=U\operatorname{diag}(t)\Pi\) of the square matrix \(B'R\) ([[?c:Smith normal form|Smith normal form]] over a valuation domain; \(U,\Pi\) invertible). Then \(R\,U\operatorname{diag}(t)=RB'R\Pi^{-1}=0\), so \(RU_j=0\) whenever \(t_j\ne0\) (\(U_j\) the \(j\)-th column); and \(B=Q(RB)+U\operatorname{diag}(t)(\Pi Q)\) (as \(B'RQ=B'\)), \(t_jU_j=B\eta-QRB\eta\) for \(\eta=R\Pi^{-1}e_j\). Hence \(\operatorname{im}Q+\operatorname{im}B=\operatorname{im}Q+\operatorname{span}\{t_jU_j\}\).

*The set \(s\).* Let \(\mathcal{J}=\{j:t_j\mid u,\ t_j\ne0\}\) and \(s=\{AU_j:j\in\mathcal{J}\}\). In a valuation ring, for \(j\notin\mathcal{J}\) we have \(u\mid t_j\).

*Count.* For each column \(Q_e\), \(uQ_e\) is \(C\)-valued; for \(j\in\mathcal{J}\), \(t_jU_j\in\operatorname{im}Q+\operatorname{im}B\) is \(C\)-valued and \(u\) is a multiple of \(t_j\), so \(uU_j\) is \(C\)-valued. Hence the reductions of the columns \(Q_e\) (\(e\in E\)) and \(U_j\) (\(j\in\mathcal{J}\)) lie in \(S^{X}\). They are linearly independent over \(\bar O\), because they have dual rows: the rows of \(R\) and of \(U^{-1}-U^{-1}QR\) satisfy \(R\,Q=1\), \(RU_j=0\), \((U^{-1}-U^{-1}QR)Q=0\), \((U^{-1}-U^{-1}QR)U_j=e_j\) for \(j\in\mathcal{J}\). So \(\#E+\#\mathcal{J}\le\#X\dim S\).

*Span.* Let \(G=\operatorname{im}(AQ)+\operatorname{span}(s)\). Then \(A(\operatorname{im}Q+\operatorname{im}B)\subseteq G+uO^{E}\): \(A(t_jU_j)\in\operatorname{span}(s)\) for \(j\in\mathcal{J}\) and \(\in uO^{E}\) otherwise. For \(\eta\in O^{E}\), \(a\eta=AB\eta-(AB-a)\eta\in G+uO^{E}\). Since \(uO^{E}\subseteq\mathfrak{m}\cdot aO^{E}\), we get \(aO^{E}\subseteq G+\mathfrak{m}\,aO^{E}\), and [[algebra-commutative/nakayama-lemma|Nakayama's lemma]] for the finitely generated module \(aO^{E}\) gives \(aO^{E}\subseteq G\).

*Corollary.* Apply the proposition with \(X:=H\times\mathrm{Ed}\), \(I:=\mathcal{E}\), \(E:=V\times\mathcal{E}\), \(A=\mathrm{Add}_{Q'}\), \(B=\mathrm{Inv}_{\mathrm{Av}}\) (built from \(R'\)), \(a=p^{2Nc_0}\), \(u=w^{c-1}\). Here \(aw=w^{4Nc_0+1}\) divides \(w^{c-1}\) because \(4Nc_0+2\le5Nc_0\) (\(Nc_0\ge2\) as \(k\ge2\)); \(w\in\mathfrak{m}\); \(AB\equiv a\) modulo \(w^{c}\), a fortiori modulo \(u\), by the near-inverse lemma; the image of \(Q\) is \(\mathcal{A}\)-valued, hence \(C\)-valued; the image of \(\mathrm{Inv}_{\mathrm{Av}}\) is \(C\)-valued, since its value at each \(x\) is \(\mathrm{Av}\) applied to a vector; and the last hypothesis is property 5 of an edge condition. Thus \(\#V\#\mathcal{E}+\#s\le\#V\cdot[\mathrm{GL}_k(W):\mathrm{Par}_r]\dim S\le(1+\theta)\#V\#\mathcal{E}\) by property 6. \(\square\)

## References

1. Lean: `New.exists_finset_card_le_smul_top_le_sup_span`, `New.exists_elementary_divisors_mod_summand`, `New.card_add_card_le_mul_finrank`, `New.smul_top_le_of_le_sup_smul_top`, `New.FrobeniusCycle.IsEdgeCondition.exists_finset_smul_top_le_range_sup_span` in `src/New/UpperBound/ElementaryDivisors/ElementaryDivisorTheorem.lean`.
