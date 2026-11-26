+++
id = "proofs/grh/onelift-values/annihilating-row-exists"
title = "A matrix without an integral block ratio has an annihilating row"
kind = "lemma"
summary = "If a local n-by-r matrix has no integral block ratio, some integral row, nonzero modulo the place on the distinguished block, annihilates it."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.exists_isAnnihilatingRow_of_not_hasIntegralBlockRatio", "New.exists_isAnnihilatingRow_of_max", "New.exists_isAnnihilatingRow_of_det_eq_zero", "New.exists_isAnnihilatingRow_of_one_le"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
proof_status = "full"
+++

**Lemma.** Let \(w\) be a finite place of a number field \(E\), \(\iota\colon R\hookrightarrow N\) an
injection of finite index sets, and \(x\in M_{N\times R}(E_w)\). If \(x\) does not have an
[[proofs/grh/onelift-values/integral-block-ratio|integral block ratio]] (for a given truth value of
"\(w\) is chosen"), then \(x\) has an
[[proofs/grh/onelift-values/integral-block-ratio|annihilating row]].

## Proof

Write \(\lvert\cdot\rvert\) for the absolute value of \(E_w\), \(x'\) for the rows \(\iota(R)\) of \(x\) and
\(x''\) for the others.

*Normalisation.* Suppose \(\mu\in E_w^{N}\) is a row with \(\mu x=0\), and that some index \(b\in R\) has
\(\mu_{\iota(b)}\neq 0\), \(\lvert\mu_a\rvert\le\lvert\mu_{\iota(b)}\rvert\) for all \(a\in N\), and, if \(w\)
is not chosen, \(\lvert\mu_a\rvert<\lvert\mu_{\iota(b)}\rvert\) for all \(a\notin\iota(R)\). Then
\(l=\mu/\mu_{\iota(b)}\) is integral, \(l x=0\), \(l_{\iota(b)}=1\) is a unit, and for \(w\) not chosen the
entries outside \(\iota(R)\) have absolute value \(<1\). So \(l\) is an annihilating row.

*Case \(\det x'=0\).* There is \(\lambda\in E_w^{R}\), \(\lambda\ne0\), with \(\lambda x'=0\). Choose \(b\)
with \(\lvert\lambda_b\rvert\) maximal, and let \(\mu=(\lambda,0)\). Then \(\mu x=\lambda x'=0\), the entries
outside \(\iota(R)\) vanish, and the normalisation applies.

*Case \(\det x'\ne0\).* Put \(y=x x'^{-1}\), so that \(y x'=x\) and the rows \(\iota(R)\) of \(y\) form the
identity. Since \(x\) has no integral block ratio, there are \(a\notin\iota(R)\) and \(b_0\in R\) with either
\(\lvert y_{a b_0}\rvert>1\), or \(w\) chosen and \(\lvert y_{a b_0}\rvert\ge 1\). (If all entries of
\(x''x'^{-1}\) are integral, failure of the definition forces \(w\) to be chosen and some entry to be a
unit.) Choose \(b\) with \(\lvert y_{ab}\rvert\) maximal in the row \(a\); then \(\lvert y_{ab}\rvert\ge1\),
with strict inequality if \(w\) is not chosen. Let \(\mu\) be the row with entries \(y_{ac}\) at
\(\iota(c)\), \(-1\) at \(a\) and \(0\) elsewhere. Then
\(\mu x=(\text{row }a\text{ of }y)\,x'-(\text{row }a\text{ of }x)=0\). The entries of \(\mu\) outside
\(\iota(R)\) have absolute value \(\le 1\le\lvert\mu_{\iota(b)}\rvert\), strictly smaller when \(w\) is not
chosen, so the normalisation applies. \(\blacksquare\)

## References

1. Lean: `New.exists_isAnnihilatingRow_of_not_hasIntegralBlockRatio` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`.
