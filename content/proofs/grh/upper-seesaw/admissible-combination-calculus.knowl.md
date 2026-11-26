+++
id = "proofs/grh/upper-seesaw/admissible-combination-calculus"
title = "Calculus of admissible combinations"
kind = "proposition"
summary = "Admissible combinations are stable under linear maps, integral scalars, roots of unity, bilinear maps and pure tensors, with explicit denominators and sizes."
aliases = ["rules for admissible combinations"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.IsAdmissibleCombination.of_sum", "New.Seesaw.IsAdmissibleCombination.smul_single", "New.Seesaw.IsAdmissibleCombination.single", "New.Seesaw.IsAdmissibleCombination.map", "New.Seesaw.IsAdmissibleCombination.smul", "New.Seesaw.IsAdmissibleCombination.smul_of_eq_zero_or_isOfFinOrder", "New.Seesaw.IsAdmissibleCombination.of_eq_isOfFinOrder_smul", "New.Seesaw.IsAdmissibleCombination.map_bilinear", "New.Seesaw.IsAdmissibleCombination.smul_mem", "New.Seesaw.IsAdmissibleCombination.normUnit_smul", "New.Seesaw.IsAdmissibleCombination.pure"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
proof_status = "full"
+++

**Proposition.** Fix a natural number \(n\) and a proposition \(p\). Throughout,
"\(z\in\operatorname{Adm}(v,A;d,B)\)" abbreviates: \(z\) is an
[[proofs/grh/upper-seesaw/admissible-combination|admissible combination]] of the \(v_x\),
\(x\in A\), with denominator \(d\) away from \(n\) and size \(B\) under \(p\).

1. (**Finite sums.**) Let \(S\) be a finite set of indices and \(c\colon S\to\mathbb{C}\) with every
   \(d\,c_i\) [[proofs/grh/upper-seesaw/integral-away|integral away from \(n\)]] and, under \(p\),
   \(\sum_{i\in S}\lvert\sigma c_i\rvert\le B\) for all automorphisms \(\sigma\) of \(\mathbb{C}\).
   Then \(\sum_{i\in S}c_iv_i\in\operatorname{Adm}(v,S;d,B)\).
2. (**Single terms.**) If \(x\in A\), \(d\,c\) is integral away from \(n\) and, under \(p\),
   \(\lvert\sigma c\rvert\le1\) for all \(\sigma\), then \(c\,v_x\in\operatorname{Adm}(v,A;d,1)\). In
   particular \(v_x\in\operatorname{Adm}(v,A;d,1)\) for every \(d\).
3. (**Linear maps.**) If \(z\in\operatorname{Adm}(v,A;d,B)\) and \(L\) is a linear map, then
   \(L z\in\operatorname{Adm}(L\circ v,A;d,B)\).
4. (**Scalars.**) If \(z\in\operatorname{Adm}(v,A;d,B)\), \(c\) is integral away from \(n\) and,
   under \(p\), \(\lvert\sigma c\rvert\le1\) for all \(\sigma\), then
   \(c\,z\in\operatorname{Adm}(v,A;d,B)\). This applies to \(c=0\) and to every [[?c:Root of unity|root of unity]].
5. (**Change of family up to roots of unity.**) If \(z\in\operatorname{Adm}(v,A;d,B)\) and every
   \(v_x\), \(x\in A\), equals \(\zeta\,v'_y\) for a root of unity \(\zeta\) and some \(y\in A'\),
   then \(z\in\operatorname{Adm}(v',A';d,B)\).
6. (**Bilinear maps.**) If \(z\in\operatorname{Adm}(v,A;d,B)\),
   \(z'\in\operatorname{Adm}(v',A';d',B')\) and \(b\) is a
   [[algebra-modules/bilinear-map|bilinear map]], then \(b(z,z')\) is an admissible combination of
   the \(b(v_x,v'_y)\), \((x,y)\in A\times A'\), with denominator \(d\,d'\) and size
   \(B\lvert B'\rvert\).
7. (**Integrality.**) Let \(l\nmid n\) be a prime with a fixed homomorphism
   \(\iota_l\colon\mathbb{C}\to\mathbb{C}_l\), and \(\mathcal{O}_{\iota_l}=\{c:\lVert\iota_l c\rVert\le1\}\).
   If \(z\in\operatorname{Adm}(v,A;d,B)\) and \(M\subseteq Z\) is an \(\mathcal{O}_{\iota_l}\)-submodule
   containing all \(v_x\), \(x\in A\), then \(d\,z\in M\).
8. (**Clearing the denominator.**) Let \(d\ne0\), \(C,a\in\mathbb{C}\), and let \(z\) be an admissible
   combination of the vectors \(C\,v_x\), \(x\in A\), with denominator \(d\) and size \(B\). Put
   \(u=d/(aC)\) if \(aC\ne0\) and \(u=1\) otherwise. Then \(u\,a\,z\in\operatorname{Adm}(v,A;1,dB)\).
9. (**Pure tensors.**) Let \(\alpha_0,\alpha_1,\dots\) be abelian groups with subgroups
   \(A_j\subseteq\alpha_j\), let \(F_0,F_1,\dots\) be complex vector spaces, and
   \(v_i\colon\alpha_{2i}\times\alpha_{2i+1}\to F_i\). If for each \(i<m\) the vector \(f_i\in F_i\)
   is an admissible combination of the \(v_i(s,t)\), \((s,t)\in A_{2i}\times A_{2i+1}\), with
   denominator \(d\) and size \(B\), then \(f_{m-1}\otimes\dots\otimes f_0\) is an admissible
   combination of the [[?c:Tensor product of vector spaces|pure tensors]]
   \(v_{m-1}(y_{2m-2},y_{2m-1})\otimes\dots\otimes v_0(y_0,y_1)\), over the families
   \(y=(y_j)_j\) with all \(y_j\in A_j\), with denominator \(d^{m}\) and size \(\lvert B\rvert^{m}\).

## Proof

(1) Take the coefficients \(c\) extended by \(0\) outside \(S\). (2) is the case \(S=\{x\}\) with
support in \(A\); the "in particular" is \(c=1\).

(3) Apply \(L\) to \(z=\sum r(x)v_x\); the coefficients are unchanged.

(4) By (3), \(cz\) is an admissible combination of the \(c\,v_x\) with the same coefficients; each
\(c\,v_x\) is in \(\operatorname{Adm}(v,A;1,1)\) by (2), and
[[proofs/grh/upper-seesaw/admissible-combination-substitution|substitution]] with \(d'=B'=1\)
gives the claim. A root of unity \(\zeta\) is integral away from \(n\), and \(\sigma\zeta\) is a
root of unity, so \(\lvert\sigma\zeta\rvert=1\).

(5) By (4) each \(v_x=\zeta v'_y\) lies in \(\operatorname{Adm}(v',A';1,1)\); substitute.

(6) By (3) applied to \(b(\cdot,z')\), \(b(z,z')\) is an admissible combination of the
\(b(v_x,z')\), \(x\in A\), with data \((d,B)\). By (3) applied to \(b(v_x,\cdot)\), each
\(b(v_x,z')\) is an admissible combination of the \(b(v_x,v'_y)\), \(y\in A'\), with data
\((d',B')\), hence of the family indexed by \(A\times A'\). Substitution gives denominator \(dd'\)
and size \(B\lvert B'\rvert\).

(7) \(d\,z=\sum_x (d\,r(x))v_x\), and each \(d\,r(x)\) is integral away from \(n\), so
\(\lVert\iota_l(d\,r(x))\rVert\le1\) because \(l\nmid n\).

(8) Let \(z=\sum_x r(x)\,C\,v_x\) and \(z_0=\sum_x r(x)v_x\), so \(a z=aC\,z_0\) and
\(u\,a\,z=(u\,aC)\,z_0\). If \(aC=0\) this is \(0\). Otherwise \(u\,aC=d\) and
\(u\,a\,z=\sum_x d\,r(x)\,v_x\): the coefficients \(d\,r(x)\) are integral away from \(n\) and, under
\(p\), \(\sum_x\lvert\sigma(d\,r(x))\rvert=d\sum_x\lvert\sigma r(x)\rvert\le dB\).

(9) Induction on \(m\). For \(m=0\) the empty tensor is \(1\), which is the member of the family at
\(y=0\) (this is where the \(A_j\) are subgroups). For the step, the pure tensor of length \(m+1\)
is \(f_m\otimes(f_{m-1}\otimes\dots\otimes f_0)\). By (6) it is an admissible combination, with
denominator \(d\cdot d^{m}\) and size \(B\,\lvert B\rvert^{m}\le\lvert B\rvert^{m+1}\), of the
tensors \(v_m(t)\otimes w(s)\) with \(t\in A_{2m}\times A_{2m+1}\) and \(s\) a family in
\(\prod A_j\), where \(w(s)\) is the pure tensor of length \(m\) at \(s\). Since \(w(s)\) depends
only on the coordinates \(s_j\), \(j<2m\), replacing the coordinates \(2m,2m+1\) of \(s\) by \(t\)
gives a family \(y\in\prod A_j\) at which the pure tensor of length \(m+1\) is
\(v_m(t)\otimes w(s)\). Apply (5) with \(\zeta=1\). \(\blacksquare\)

## References

1. Lean: the declarations `New.Seesaw.IsAdmissibleCombination.*` listed in the front matter, in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
