+++
id = "proofs/grh/reduction-main/onto-up-to-colength-product"
title = "Colength bounds add under products of endomorphisms"
kind = "lemma"
summary = "If each endomorphism in a list is onto on M modulo z^s up to colength t_l, their product is onto up to colength the sum of the t_l."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsOntoUpToColength.prod"]
lean_files = ["src/New/Reduction/Lattices/Colength.lean"]
proof_status = "full"
+++

**Lemma.** Let \(O\) be a [[?c:commutative ring|commutative ring]], \(V\) an \(O\)-[[algebra-modules/module|module]], \(M\subseteq V\) a submodule, \(z\in O\) and \(s\ge 0\). Let \(T_1,\dots,T_N\) be \(O\)-linear endomorphisms of \(V\) and \(t_1,\dots,t_N\) real numbers such that each \(T_l\) is [[proofs/grh/reduction-main/onto-up-to-colength|onto on \(M\) modulo \(z^s\) up to colength \(t_l\)]]. Then the composite \(T_1\circ T_2\circ\cdots\circ T_N\) is onto on \(M\) modulo \(z^s\) up to colength \(t_1+\dots+t_N\).

## Proof

Induction on \(N\). For \(N=0\) the product is the identity, which keeps \(M\), and \(M\subseteq M+z^sM\) gives colength dividing \(z^0=1\), with \(0\le 0\).

For the step write \(T=T_1\) and \(S=T_2\circ\dots\circ T_N\). By hypothesis \(T(M)\subseteq M\) and there is \(i\le t_1\) with \(\operatorname{colen}(M,T(M)+z^sM)\mid z^i\); by induction \(S(M)\subseteq M\) and there is \(j\le t_2+\dots+t_N\) with \(\operatorname{colen}(M,S(M)+z^sM)\mid z^j\). Then \(TS(M)\subseteq T(M)\subseteq M\), and rule (4) of [[proofs/grh/reduction-main/colength-calculus|the calculus of colengths]], applied with \(f=T\), \(N=S(M)\) and \(a=z^s\), gives
\[
\operatorname{colen}\bigl(M,\ T(S(M))+z^sM\bigr)\mid z^iz^j=z^{i+j},
\]
and \(i+j\le t_1+\dots+t_N\).

## References

1. Lean: `New.IsOntoUpToColength.prod` in `src/New/Reduction/Lattices/Colength.lean`.
