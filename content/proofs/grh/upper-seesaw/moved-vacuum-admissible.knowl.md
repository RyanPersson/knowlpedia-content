+++
id = "proofs/grh/upper-seesaw/moved-vacuum-admissible"
title = "A moved translate of the vacuum is an admissible combination of translates"
kind = "lemma"
summary = "Applying a finite unitary element to a translate of the vacuum gives a mean over lattice classes of translates times roots of unity."
aliases = ["moved vacua"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.isAdmissibleCombination_weil_vacElem"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a [[?c:CM field|CM field]] with [[?lean:New.WeilData|Weil data]], \(V\) a
[[?lean:New.Space|hermitian space with a point]] over \(E\) with coordinates indexed by \(n\),
\(\omega\) its [[?lean:New.Space.ω|Weil representation]] on \(\mathcal{S}(V)\), \(v_0\) the
[[?lean:New.Space.vacElem|vacuum vector]] and \(\varrho_f(y)\) the
[[?lean:New.Space.finHeisenbergOp|finite Heisenberg operators]]
(\(y\in\mathbb{A}_{E,f}^{n}\)). Let \(g\in G_f\), \(x\in\mathbb{A}_{E,f}^{n}\), and let
\(A\subseteq\mathbb{A}_{E,f}^{n}\) contain \(g(x+z)\) for all \(z\) in the standard lattice
\(L=\widehat{\mathcal{O}}_E^{\,n}\). Factor the [[?lean:New.finMultiplier|finite multiplier]] as
\(\Delta_f(g)=c\,C\) with \(c,C\in\mathbb{C}\). Let \(q,d\) be natural numbers and \(p\) a
proposition such that

* \(d\cdot c/\lvert\Delta_f(g)\rvert^{2}\) is
  [[proofs/grh/upper-seesaw/integral-away|integral away from \(q\)]];
* if \(p\) holds, \(\lvert\sigma c\rvert\le1\) for all automorphisms \(\sigma\) of \(\mathbb{C}\).

Then \(\omega(1,g)\,\varrho_f(x)v_0\) is an
[[proofs/grh/upper-seesaw/admissible-combination|admissible combination]] of the vectors
\(C\,\varrho_f(y)v_0\), \(y\in A\), with denominator \(d\) away from \(q\) and size \(1\) under
\(p\).

## Proof

Let \(H=\{z\in L: gz\in L\}\). It has finite index in \(L\), and
\([L:H]=\lvert\Delta_f(g)\rvert^{2}\)
([[?lean:New.norm_finMultiplier_sq|the squared norm of the multiplier is an index]]); the index is
nonzero because \(\Delta_f(g)\ne0\). Two facts about the Weil representation are used:

* \(\omega(1,g)\,\varrho_f(x)=\varrho_f(gx)\,\omega(1,g)\)
  ([[?lean:New.Space.omega_finHeisenbergOp|the Weil representation intertwines the finite
  Heisenberg operators]]);
* \(\omega(1,g)v_0=\dfrac{\Delta_f(g)}{\lvert\Delta_f(g)\rvert^{2}}\displaystyle\sum_{z\in L/H}\varrho_f(g\tilde z)v_0\),
  with \(\tilde z\) a representative of \(z\)
  ([[?lean:New.Space.omega_vacElem_sum|the moved vacuum]]).

By the [[?lean:New.Space.finHeisenbergOp_finHeisenbergOp|composition law]],
\(\varrho_f(gx)\varrho_f(g\tilde z)=\zeta_z\,\varrho_f(g(x+\tilde z))\) with
\(\zeta_z=\psi\bigl(\bar c_0\,(g\tilde z)^{*}(gx)\bigr)\) a root of unity. Put
\(a=c/\lvert\Delta_f(g)\rvert^{2}\), so \(aC=\Delta_f(g)/\lvert\Delta_f(g)\rvert^{2}\). Then
\[
\omega(1,g)\,\varrho_f(x)v_0=\sum_{z\in L/H}a\cdot\zeta_z\,C\,\varrho_f\bigl(g(x+\tilde z)\bigr)v_0 .
\]
Each index \(g(x+\tilde z)\) lies in \(A\). The coefficients \(a\) satisfy: \(d\,a\) is integral
away from \(q\) by hypothesis; and under \(p\), for every automorphism \(\sigma\),
\(\sum_{z}\lvert\sigma a\rvert=[L:H]\cdot\lvert\sigma c\rvert/[L:H]=\lvert\sigma c\rvert\le1\)
(the number \(\lvert\Delta_f(g)\rvert^{2}=[L:H]\) is a rational integer, fixed by \(\sigma\)). By
rules 1 and 5 of the [[proofs/grh/upper-seesaw/admissible-combination-calculus|calculus]] (finite
sums; change of family up to the roots of unity \(\zeta_z\)) the claim follows. \(\blacksquare\)

## References

1. Lean: `New.Seesaw.isAdmissibleCombination_weil_vacElem` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
