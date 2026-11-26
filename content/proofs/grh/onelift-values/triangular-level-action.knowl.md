+++
id = "proofs/grh/onelift-values/triangular-level-action"
title = "Integral elements with block triangular reductions act through their first blocks"
kind = "lemma"
summary = "On a vector of the level and character of a descent pair, an element of the maximal level whose reductions are block upper triangular at the chosen places and block lower triangular at the twist places acts as the block action of its first diagonal blocks."
aliases = ["block action"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.smul_chosenGLRep_eq_apply_of_triangular", "New.DescentPair.blockAction", "New.DescentPair.mem_levelGroup_of_reduceAt", "New.rowShear", "New.DescentPair.exists_leftMul_eq_and_blockAction_eq", "New.DescentPair.blockAction_mulSingle_inl", "New.DescentPair.blockAction_mulSingle_inr"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
proof_status = "full"
+++

Let \(O\) be a [[?lean:New.DescentPair|descent pair]] with chosen places, twist places \(Q\), all places
\(S_O\), residue characters \(\chi_w\), level group \(K_O\) with character \(\psi_O\), and \(e=(1,0)^{\mathsf
T}\) the \(n\times r\) inclusion matrix. The group \(\prod_{w\ \mathrm{chosen}}\mathrm{GL}_r(k_w)\) acts on
the vectors of level \((K_O,\psi_O)\) of any representation \(\pi\) of \(U(V)(\mathbb{A}_f)\) by
[[?lean:New.DescentPair.chosenGLRep|\(\bar s\cdot y\)]] \(=\prod_w\chi_w(\det s_w)\,\pi(k_0)y\), where
\(k_0\in K_0\) is any lift of the family equal to \(\operatorname{diag}(s_w,1)\) at the chosen places and
\(1\) at \(Q\); on forms this is the [[?lean:New.DescentPair.formAction|form action]].

For a family \(s=(s_w)_{w\in S_O}\), \(s_w\in\mathrm{GL}_r(k_w)\), the **block action** on a form \(y\) is
\[
s\star y=\Bigl(\prod_{w\in S_O}\chi_w(\det s_w)^{-1}\Bigr)\;\bar s\cdot y ,
\]
where \(\bar s\) is the part of \(s\) at the chosen places. If \(s\) is trivial except at one place \(w\),
then \(s\star y=\chi_w(\det s_w)^{-1}\,\bar s_w\cdot y\) for \(w\) chosen, and
\(s\star y=\chi_w(\det s_w)^{-1}y\) for \(w\in Q\).

**Lemma.** Let \(y\) be a vector of level \((K_O,\psi_O)\) in \(\pi\), and let \(k\in K_0\) have reductions
\(\tau_w\) with
\[
\tau_w e=e\,s_w\ \ (w\text{ chosen}),\qquad \tau_w^{\mathsf T}e=e\,s_w^{\mathsf T}\ \ (w\in Q).
\]
Then \(\pi(k)y=\prod_{w\in S_O}\chi_w(\det s_w)^{-1}\;\bar s\cdot y\); for forms, \(k\cdot y=s\star y\).

**Corollary (shears).** Let \(z\in M_{n\times r}(\mathbb{A}_f)\), let \(l\) be an
[[proofs/grh/onelift-values/integral-block-ratio|annihilating row]] for \(z_w\) at a place \(w\in S_O\), with
reduction \(\bar\lambda\) of its part on \(\iota\), and let \(s=1+v\bar\lambda\) lie in the
[[proofs/grh/onelift-values/hyperplane-group-character-sum|hyperplane group]] \(H_{\bar\lambda}\). Then
there is \(h\in K_0\) such that \(hz\) and \(z\) have the same components at \(S_O\) and \(h\cdot y=s\star y\)
(block \(s\) at \(w\), identity elsewhere) for every form \(y\in\mathcal{F}_V\).

## Proof

*Lemma.* Let \(\sigma\) be the family \(\operatorname{diag}(s_w,1)\) at chosen places and \(1\) at \(Q\), and
\(k_0\in K_0\) a lift of \(\sigma\). We show that \(\sigma^{-1}\tau\) lies in the residual level group. At a
chosen place, \(\tau_we=es_w=\sigma_we\), so \(\sigma_w^{-1}\tau_we=e\). At \(w\in Q\), the relation
\(\tau_w^{\mathsf T}e=es_w^{\mathsf T}\) says that the entries of \(\tau_w\) in rows \(\iota\) and columns
outside \(\iota\) vanish and that its \(\iota\times\iota\) block is \(s_w\); so \(\tau_w\) is block lower
triangular. Hence \(k_0^{-1}k\in K_O\) and
\(\psi_O(k_0^{-1}k)=\prod_{w\in Q}\chi_w(\det s_w)^{-1}=:c\). Therefore
\(\pi(k)y=\pi(k_0)\pi(k_0^{-1}k)y=c\,\pi(k_0)y\). By definition
\(\bar s\cdot y=d\,\pi(k_0)y\) with \(d=\prod_{w\ \mathrm{chosen}}\chi_w(\det s_w)\), and
\(\prod_{w\in S_O}\chi_w(\det s_w)^{-1}\cdot d=c\). This gives the claim.

*Corollary.* Lift \(v\) to an integral column \(\tilde v\) and let \(h_w=1+(\tilde v,0)^{\mathsf T}\,l\) (the
**row shear**: identity plus the column \(\tilde v\) extended by zero along \(\iota\), times the row \(l\)).
By the matrix determinant lemma \(\det h_w=\det(1+\tilde v\lambda)\), which reduces to \(\det s\ne0\), so
\(h_w\in\mathrm{GL}_n(\mathcal{O}_w)\). Let \(h\in K_0\) have component \(h_w\) at \(w\) and \(1\) at the
other places of \(S_O\) ([[proofs/grh/onelift-values/translated-block-datum|existence of such points]]).
Since \(l z_w=0\), \(h_wz_w=z_w\). The reduction of \(h_w\) satisfies \(\bar h_we=e(1+v\bar\lambda)=es\)
always; and if \(w\in Q\), the entries of \(l\) outside \(\iota\) reduce to \(0\), so
\(\bar h_w=1+(v,0)^{\mathsf T}(\bar\lambda,0)\) and \(\bar h_w^{\mathsf T}e=es^{\mathsf T}\). At the other
places the reductions are \(1\). The Lemma applies with the family equal to \(s\) at \(w\) and \(1\)
elsewhere. \(\blacksquare\)

## References

1. Lean: `New.DescentPair.smul_chosenGLRep_eq_apply_of_triangular`, `New.DescentPair.blockAction`, `New.rowShear`, `New.DescentPair.exists_leftMul_eq_and_blockAction_eq` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`.
