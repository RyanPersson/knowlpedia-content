+++
id = "proofs/grh/reduction-main/colength-bounds-length"
title = "Over a discrete valuation ring, a colength bound bounds a length"
kind = "lemma"
summary = "If the colength of N in a finitely generated M divides z over a DVR, then M/(M ∩ N) has length at most the valuation of z."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.ColengthDvd.relLength_le", "New.IsOntoUpToColength.exists_relLength_le"]
lean_files = ["src/New/Reduction/Lattices/Colength.lean"]
proof_status = "full"
+++

**Lemma.** Let \(O\) be a [[algebra-commutative/dvr|discrete valuation ring]] with normalized valuation \(v\) (so \(v(0)=\infty\)), let \(V\) be an \(O\)-[[algebra-modules/module|module]] and \(M,N\subseteq V\) submodules with \(M\) [[?c:finitely generated module|finitely generated]]; \(N\subseteq M\) is not assumed. Write \(\ell_O\) for the [[algebra-modules/length-module|length]] of an \(O\)-module, a value in \(\{0,1,2,\dots\}\cup\{\infty\}\).

1. If [[proofs/grh/reduction-main/colength-divides|\(\operatorname{colen}(M,N)\mid z\)]], then
\[
\ell_O\bigl(M/(M\cap N)\bigr)\ \le\ \ell_O(O/zO)=v(z).
\]
2. If an endomorphism \(y\) of \(V\) is [[proofs/grh/reduction-main/onto-up-to-colength|onto on \(M\) modulo \(p^n\) up to colength \(c\)]], then there is an integer \(l\ge0\), \(l\le c\), with
\[
\ell_O\bigl(M/(y(M)+p^nM)\bigr)\ \le\ l\cdot\ell_O(O/pO).
\]

(In (2), \(y(M)+p^nM\subseteq M\), so the quotient is \(M\) modulo its intersection with that module.)

## Proof

(1) Choose generators \(\Phi_1,\dots,\Phi_n\) of \(M\) and a matrix \(m\) with \(\det m\mid z\) and \((m\Phi)_i:=\sum_k m_{ik}\Phi_k\in N\). By the [[algebra-modules/smith-normal-form-theorem|Smith normal form]] over the principal ideal domain \(O\), \(m=Q\operatorname{diag}(a)P\) with \(Q,P\) invertible. Put \(\Psi=P\Phi\). Then \(\operatorname{diag}(a)\Psi=Q^{-1}(m\Phi)\), so \(a_j\Psi_j\in N\) for every \(j\). Therefore
\[
\pi:\ \prod_{j=1}^n O/a_jO\ \longrightarrow\ V/N,\qquad (x_j)_j\mapsto\sum_j x_j\Psi_j \bmod N
\]
is well defined and \(O\)-linear. Its image contains the image of \(M\) in \(V/N\), because \(\Phi=P^{-1}\Psi\) expresses each generator of \(M\) through the \(\Psi_j\). The image of \(M\) in \(V/N\) is isomorphic to \(M/(M\cap N)\). Since length does not increase under passing to submodules and quotients, and \(\ell_O(O/a_jO)=v(a_j)\),
\[
\ell_O\bigl(M/(M\cap N)\bigr)\le\sum_j v(a_j)=v\Bigl(\prod_j a_j\Bigr)\le v(z),
\]
the last step because \(\prod_ja_j\) is \(\det m\) up to the units \(\det Q,\det P\), hence divides \(z\).

(2) By definition there is \(l\le c\) with \(\operatorname{colen}(M,y(M)+p^nM)\mid p^l\). Apply (1): the length is at most \(v(p^l)=l\,v(p)=l\,\ell_O(O/pO)\).

## References

1. Lean: `New.ColengthDvd.relLength_le`, `New.IsOntoUpToColength.exists_relLength_le` in `src/New/Reduction/Lattices/Colength.lean`. The module `M/(M\cap N)` is `relLength M N` of `Lib/General/Algebra/FittingIdealsAndLengths.lean`.
