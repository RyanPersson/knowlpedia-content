+++
id = "proofs/grh/onelift-comparison/false-lifts"
title = "False lifts and forms orthogonal to them"
kind = "definition"
summary = "Forms in the image of an idempotent, killed by a Hecke polynomial at a split place off the level, and lying in a given subspace."
aliases = ["false lift", "orthogonal to the false lifts"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.groupAlgAction", "New.DescentPair.falseLiftsAt", "New.DescentPair.IsOrthogonalToFalseLifts"]
lean_files = ["src/New/OneLift/TestedForms.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with a fixed [[?c:CM type|CM type]], let \(r,n\) be finite index sets with \(\lvert r\rvert<\lvert n\rvert\), and let \(O\) be a [[?lean:New.DescentPair|descent pair]]: a [[?c:Hermitian space|hermitian space]] \(W\) of rank \(\lvert r\rvert\) over \(E\), the standard definite space \(V=I_n\) of rank \(\lvert n\rvert\), an injection \(\operatorname{incl}\colon r\hookrightarrow n\), two finite sets of split finite places \(M\) (the chosen places) and \(Q\) (the places of the twist), and a character \(\mu\) of \(U(1)(\mathbb{A})\) with tame parts \(\psi_w\), characters of the [[algebra-commutative/residue-field|residue fields]] \(k_w\), trivial for \(w\notin M\cup Q\). Let \(\bar G_M=\prod_{w\in M}\mathrm{GL}_r(k_w)\); it acts on the forms on \(V\) by the [[?lean:New.DescentPair.formAction|form action]] (\(g\) acts as \(\prod_{w\in M}\psi_w(\det g_w)\) times right translation by an integral element reducing at \(w\in M\) to \(g_w\) on the indices \(\operatorname{incl}\) and \(1\) on the others, and to \(1\) at \(Q\)), hence so does the [[algebra-representation-theory/group-algebra|group algebra]] \(\mathbb{C}[\bar G_M]\).

Let \(e_0\in\mathbb{C}[\bar G_M]\) and let \(Z\) be a subspace of the forms on \(V\). For a finite place \(w\ne\bar w\) off the level (\(w\notin M\cup Q\cup\overline{M\cup Q}\)) the space of **false lifts at \(w\)** for \((e_0,Z)\) is
\[
\mathrm{FL}_w(e_0,Z)=\operatorname{im}(e_0)\ \cap\ \ker H_w(X_*(w))\ \cap\ Z,
\]
where \(H_w\) is the [[?lean:New.DescentPair.heckePolyOnForms|Hecke polynomial operator]] and \(X_*(w)=\bigl(\nu_W(w)\,q_w^{\,t-1}\bigr)^{-1}\) is the [[?lean:New.DescentPair.liftHeckeRoot|lift Hecke root]] (\(t=\lvert n\rvert-\lvert r\rvert\), \(\nu_W(w)\) the Frobenius value in rank \(r\) of the character \(\chi_W\) of the pair).

A form \(y\) on \(V\) is **orthogonal to the false lifts** for \((e_0,Z)\) if \(y\perp\mathrm{FL}_w(e_0,Z)\), for the inner product \(\langle\ ,\ \rangle=\langle\ ,\ \rangle_{1}\), for every such place \(w\).

## Remarks

In use \(Z\) is the orthogonal complement of a space of lifts, or the kernel of the normalized descent. Genuine theta lifts from \(W\) are killed by \(H_w(X_*(w))\); a false lift shares this property and the \(e_0\)-type but is orthogonal to the lifts.

## References

1. Lean: `New.DescentPair.groupAlgAction`, `New.DescentPair.falseLiftsAt`, `New.DescentPair.IsOrthogonalToFalseLifts` in `src/New/OneLift/TestedForms.lean`.
