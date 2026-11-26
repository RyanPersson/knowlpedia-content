+++
id = "proofs/grh/upper-seesaw/admissible-combination-substitution"
title = "Substitution in admissible combinations"
kind = "lemma"
summary = "Substituting admissible combinations into an admissible combination multiplies denominators and sizes."
aliases = ["bind for admissible combinations"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.IsAdmissibleCombination.bind", "New.Seesaw.IsAdmissibleCombination.bind_one"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
proof_status = "full"
+++

**Lemma (substitution).** Fix a natural number \(n\) and a proposition \(p\). Let \(z\) be an
[[proofs/grh/upper-seesaw/admissible-combination|admissible combination]] of vectors \(v_x\),
\(x\in A\), with denominator \(d\) away from \(n\) and size \(B\) under \(p\). Suppose that every
\(v_x\) with \(x\in A\) is an admissible combination of vectors \(v'_y\), \(y\in A'\), with
denominator \(d'\) away from \(n\) and size \(B'\) under \(p\). Let \(e\) be a natural number with
\(d\,d'\mid e\) and \(C\) a real number such that \(B\,\lvert B'\rvert\le C\) if \(p\) holds. Then
\(z\) is an admissible combination of the \(v'_y\), \(y\in A'\), with denominator \(e\) away from
\(n\) and size \(C\) under \(p\).

In particular (\(d'=1\), \(B'=1\)): if each \(v_x\) is an admissible combination of the \(v'_y\)
with denominator \(1\) and size \(1\), then \(z\) is one with the same denominator \(d\) and size
\(B\).

## Proof

Write \(z=\sum_x c(x)v_x\) with admissible coefficients \(c\), and for each \(x\) in the support of
\(c\) (so \(x\in A\)) choose admissible coefficients \(r_x\) with \(v_x=\sum_y r_x(y)v'_y\). Put
\[
t(y)=\sum_{x\in\operatorname{supp}c} c(x)\,r_x(y).
\]
Then \(t\) is finitely supported and \(z=\sum_y t(y)v'_y\) by linearity.

*Support.* If \(t(y)\ne0\) then \(r_x(y)\ne0\) for some \(x\), hence \(y\in A'\).

*Denominator.* Write \(e=d\,d'\,k\). Then
\(e\,t(y)=\sum_x k\cdot\bigl(d\,c(x)\bigr)\bigl(d'\,r_x(y)\bigr)\), a sum of products of numbers
[[proofs/grh/upper-seesaw/integral-away|integral away from \(n\)]]; these form a ring.

*Size.* Assume \(p\) and let \(\sigma\) be an automorphism of \(\mathbb{C}\). For each \(x\) in the
support of \(c\), \(\sum_y\lvert\sigma r_x(y)\rvert\le B'\le\lvert B'\rvert\). By the triangle
inequality and an exchange of the finite sums,
\[
\sum_y\lvert\sigma t(y)\rvert\le\sum_x\lvert\sigma c(x)\rvert\sum_y\lvert\sigma r_x(y)\rvert
\le\lvert B'\rvert\sum_x\lvert\sigma c(x)\rvert\le B\,\lvert B'\rvert\le C. \qquad\blacksquare
\]

## References

1. Lean: `New.Seesaw.IsAdmissibleCombination.bind`, `New.Seesaw.IsAdmissibleCombination.bind_one` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
