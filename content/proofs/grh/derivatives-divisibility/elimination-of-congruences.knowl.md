+++
id = "proofs/grh/derivatives-divisibility/elimination-of-congruences"
title = "Imposing congruences on the rows of a matrix by elimination"
kind = "lemma"
summary = "Finitely many linear congruences on the rows of a square matrix over the integers of C_p can be met by a matrix whose determinant divides the product of the moduli."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_det_dvd_and_dvd_mulVec", "New.exists_det_dvd_prod_and_dvd_mulVec"]
lean_files = ["src/New/Derivatives/Divisibility/NullFrames.lean"]
proof_status = "full"
+++

**Lemma.** Let \(\mathcal{O}\) be the valuation ring of \(\mathbb{C}_p\) (see the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]]), \(m\ge0\), and let \(A_i\in\mathcal{O}^m\) and \(\alpha_i\in\mathcal{O}\) be given for \(i\) in a finite set \(t\). Then there is a matrix \(g\in M_m(\mathcal{O})\) such that

1. \(\det g\) divides \(\prod_{i\in t}\alpha_i\) in \(\mathcal{O}\), and
2. for every \(i\in t\) and every row \(g_k\) of \(g\), \(\alpha_i\) divides \(\sum_{l}g_{k,l}A_{i,l}\).

## Proof

*One congruence.* Let \(a\in\mathcal{O}^m\) and \(\alpha\in\mathcal{O}\); we find \(u\in M_m(\mathcal{O})\) with \(\det u\mid\alpha\) and \(\alpha\mid(ua)_k\) for all \(k\). If \(m=0\) take the empty matrix. Otherwise choose \(k_0\) with \(\lvert a_{k_0}\rvert\) maximal. Then \(a_{k_0}\) divides every \(a_k\) in \(\mathcal{O}\); write \(a_k=a_{k_0}c_k\). Let \(u\) be the identity matrix with its column \(k_0\) replaced by the vector \(b\) with \(b_{k_0}=\alpha\) and \(b_k=-c_k\) for \(k\ne k_0\). Then \(\det u=\alpha\), \((ua)_{k_0}=\alpha a_{k_0}\), and \((ua)_k=a_k-c_ka_{k_0}=0\) for \(k\neq k_0\).

*Several congruences.* Induct on \(t\), starting from \(g=1\) for \(t=\emptyset\). Given \(g\) for \(t\) and a new index \(i\), apply the first step to \(a=gA_i\) and \(\alpha_i\) to get \(u\), and replace \(g\) by \(ug\). Its determinant \(\det u\det g\) divides \(\alpha_i\prod_{j\in t}\alpha_j\); the new congruence holds since \((ug)A_i=u(gA_i)\); and the old ones persist, because each row of \(ug\) is a combination, with coefficients in \(\mathcal{O}\), of the rows of \(g\). \(\blacksquare\)

## References

1. Lean: `New.exists_det_dvd_and_dvd_mulVec`, `New.exists_det_dvd_prod_and_dvd_mulVec` in `src/New/Derivatives/Divisibility/NullFrames.lean`.
