+++
id = "proofs/grh/reduction-main/colength-of-matrix-image"
title = "Colength of the image of a square matrix over a valuation domain"
kind = "lemma"
summary = "Over a valuation domain, a submodule of O^I containing the image of a square matrix A has colength dividing every multiple of det A."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.colengthDvd_inf_comap_span", "New.ColengthDvd.of_det_dvd", "New.colengthDvd_top_smul_top", "New.colengthDvd_sup_span"]
lean_files = ["src/New/Reduction/Lattices/Colength.lean"]
proof_status = "full"
+++

**Lemma.** Let \(O\) be a [[?c:valuation ring (domain)|valuation domain]] (an integral domain in which, of any two elements, one divides the other), and let \(V\) be an \(O\)-[[algebra-modules/module|module]]. We use the relation [[proofs/grh/reduction-main/colength-divides|\(\operatorname{colen}(M,N)\mid z\)]].

1. **(One linear condition.)** For a submodule \(M\subseteq V\), an \(O\)-linear form \(f:V\to O\) and \(a\in O\),
\[
\operatorname{colen}\bigl(M,\ \{x\in M: f(x)\in aO\}\bigr)\mid a .
\]
2. **(Image of a matrix.)** Let \(I\) be a finite set, \(A\) an \(I\times I\) matrix over \(O\) with \(\det A\mid z\), and \(L\subseteq O^I\) a submodule containing \(\{Av: v\in O^I\}\). Then \(\operatorname{colen}(O^I,L)\mid z\).
3. For \(a\in O\): \(\operatorname{colen}(O^I,\ aO^I)\mid a^{\# I}\).
4. For a submodule \(N\subseteq V\), a finite set \(s\subseteq V\) and \(z\in O\):
\[
\operatorname{colen}\bigl(N+\operatorname{span}_O(s),\ N+zV\bigr)\mid z^{\# s}.
\]

## Proof

(1) Let \(\Phi_1,\dots,\Phi_n\in M\). If \(n=0\) the empty matrix serves. Otherwise the principal ideals \(f(\Phi_k)O\) are totally ordered by inclusion, because \(O\) is a valuation domain; choose \(p\) with \(f(\Phi_p)O\) largest. Then \(f(\Phi_p)\mid f(\Phi_k)\) for all \(k\); write \(f(\Phi_k)=c_k f(\Phi_p)\). Let \(m\) be the identity matrix with its \(p\)-th column replaced by the column with entry \(a\) in row \(p\) and \(-c_i\) in row \(i\ne p\). Expanding along row \(p\), whose only nonzero entry is \(a\) on the diagonal, gives \(\det m=a\). The combinations are
\[
\sum_k m_{pk}\Phi_k=a\Phi_p,\qquad \sum_k m_{ik}\Phi_k=\Phi_i-c_i\Phi_p\quad(i\ne p).
\]
They lie in \(M\), and \(f(a\Phi_p)=af(\Phi_p)\in aO\), \(f(\Phi_i-c_i\Phi_p)=0\in aO\).

(2) By the [[?c:Smith normal form over a valuation domain|Smith normal form over a valuation domain]], \(A=g\,\operatorname{diag}(d)\,g'\) with \(g,g'\) invertible over \(O\) and \(d\in O^I\). For \(j\in I\) let \(f_j(x)\) be the \(j\)-th coordinate of \(g^{-1}x\), and for \(s\subseteq I\) let
\[
S(s)=\{x\in O^I: d_j\mid f_j(x)\ \text{for all } j\in s\}.
\]
By induction on \(s\), \(\operatorname{colen}(O^I,S(s))\mid\prod_{j\in s}d_j\): for \(s=\emptyset\), \(S(\emptyset)=O^I\); and \(S(s\cup\{j\})=\{x\in S(s): f_j(x)\in d_jO\}\), so part (1) and the chain rule of [[proofs/grh/reduction-main/colength-calculus|the calculus of colengths]] give the step. Next, \(S(I)\) lies in the image of \(A\): if \(g^{-1}x=\operatorname{diag}(d)w\), then \(x=g\operatorname{diag}(d)w=A(g'^{-1}w)\). Finally \(\det A=\det g\cdot\prod_j d_j\cdot\det g'\) with \(\det g,\det g'\) units, so \(\prod_j d_j\mid\det A\mid z\). Hence \(\operatorname{colen}(O^I,S(I))\mid z\), and since \(S(I)\subseteq L\) the chain rule with \(\operatorname{colen}(S(I),L)\mid 1\) gives \(\operatorname{colen}(O^I,L)\mid z\).

(3) Apply (2) to \(A=a\cdot 1\), with \(\det A=a^{\# I}\) and image \(aO^I\).

(4) Let \(\operatorname{comb}:O^s\to V\) be the map \((x_v)_{v\in s}\mapsto\sum_{v\in s}x_vv\); its image is \(\operatorname{span}_O(s)\). By (3), \(\operatorname{colen}(O^s,zO^s)\mid z^{\# s}\). Apply the image rule of the calculus of colengths with \(M'=N+\operatorname{span}(s)\) and \(N'=N+zV\): indeed \(M'\subseteq\operatorname{comb}(O^s)+N'\), and \(\operatorname{comb}(zO^s)=z\operatorname{span}(s)\subseteq zV\subseteq N'\).

## References

1. Lean: `New.colengthDvd_inf_comap_span`, `New.ColengthDvd.of_det_dvd`, `New.colengthDvd_top_smul_top`, `New.colengthDvd_sup_span` in `src/New/Reduction/Lattices/Colength.lean`. The Smith normal form used is `isValuationPair_top.smith_normal_form` (file `Lib/General/Algebra/FittingIdealsAndLengths.lean` and its imports).
