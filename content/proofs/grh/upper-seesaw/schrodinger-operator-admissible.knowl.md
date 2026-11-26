+++
id = "proofs/grh/upper-seesaw/schrodinger-operator-admissible"
title = "Values of the Schrödinger operators are admissible combinations of translates"
kind = "lemma"
summary = "The operator attached to a function modulo a modulus sends a vector to an admissible combination of Heisenberg translates of its projection, by finite Fourier inversion."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.isAdmissibleCombination_schrodingerOp_of_reduction", "New.Seesaw.isAdmissibleCombination_schrodingerOp", "New.Seesaw.card_residueRing_pi_dvd", "New.Seesaw.star_idem_smul_mem_translations"]
lean_files = ["src/New/UpperBound/Seesaw/AdmissibleCombinations.lean"]
proof_status = "full"
+++

**Lemma.** Let \(E\) be a [[?c:CM field|CM field]] with [[?lean:New.WeilData|Weil data]] and
\(V\) a [[?lean:New.Space|hermitian space with a point]] with coordinates indexed by a finite set
\(n\). Let \(\mathfrak{m}\) be a [[?lean:New.Modulus|modulus]] of \(E\) (a nonzero ideal of
\(\mathcal{O}_E\) such that no prime divides it together with its conjugate), let
\(g\in\mathcal{O}_E\), \(d\in\widehat{\mathcal{O}}_E\) and \(q\in\mathbb{N}\) with
\(gq\in\mathfrak{m}\) and \(dq\equiv0\bmod\mathfrak{m}\). Let
\(\Psi\colon(\mathcal{O}_E/\mathfrak{m})^{n}\to\mathbb{C}\) take values
[[proofs/grh/upper-seesaw/integral-away|integral away from \(q\)]], let \(u\in\mathcal{S}(V)\) and
let \(v=P^{\mathfrak{m}}u\) be its image under the
[[?lean:New.Space.projOn|projection at the places dividing \(\mathfrak{m}\)]]. Let \(B\) be real
and \(p\) a proposition such that, under \(p\),
\(\sum_{x}\lvert\sigma\Psi(x)\rvert\le B\) for all automorphisms \(\sigma\) of \(\mathbb{C}\).

Then the value at \(u\) of the [[?lean:New.Space.schrodingerOp|Schrödinger operator]] attached to
\(\Psi\) (read on integral [[?c:Finite adele ring of a number field|finite adelic]] vectors by reduction modulo \(\mathfrak{m}\)) is an
[[proofs/grh/upper-seesaw/admissible-combination|admissible combination]] of the translates
\(\varrho_f(y)v\), over \(y\) in the
[[proofs/grh/upper-seesaw/translation-groups|translation group]] \(T^{n}_q(\bar d)\), with
denominator \(\mathrm{N}(g)^{\lvert n\rvert}\) away from \(q\) and size \(B\) under \(p\). Here
\(\mathrm{N}(g)\) is the [[?c:Absolute norm of an ideal|absolute norm]] of the ideal \((g)\).

The case \(d=g\) is the form used later.

## Proof

*Counting.* Since \(\mathfrak{m}\mid(gq)\), the cardinality
\(\lvert(\mathcal{O}_E/\mathfrak{m})^{n}\rvert=\mathrm{N}(\mathfrak{m})^{\lvert n\rvert}\) divides
\(\mathrm{N}(gq)^{\lvert n\rvert}=\mathrm{N}(g)^{\lvert n\rvert}q^{[E:\mathbb{Q}]\lvert n\rvert}\).
Hence \(\mathrm{N}(g)^{\lvert n\rvert}/\lvert(\mathcal{O}_E/\mathfrak{m})^{n}\rvert\) is integral
away from \(q\).

*Indices.* Choose integral lifts \(z_b\in\widehat{\mathcal{O}}_E^{\,n}\) of the residue vectors
\(b\), and let \(y_b\) be the conjugate of \(\varpi_{\mathfrak{m}}^{-1}z_b\) restricted to the
places dividing \(\mathfrak{m}\) (zero elsewhere), where \(\varpi_{\mathfrak{m}}\) is the chosen
idele generating \(\mathfrak{m}\widehat{\mathcal{O}}\). Then \(y_b\in T^{n}_q(\bar d)\): if \(t\) is
\(\bar d\) times an entry of \(y_b\), then \(qt\) is the conjugate of the integral adele
\(\varpi_{\mathfrak{m}}^{-1}(dq)\,z_{b,i}\) (integral since \(dq\in\mathfrak{m}\widehat{\mathcal{O}}\)),
and \(q\) is a unit at every place \(w\nmid q\).

*Fourier inversion.* By linearity in \(\Psi\), the operator applied to \(u\) is
\(\sum_a\Psi(a)\,\delta_a\), with \(\delta_a\) the value for the indicator of the point \(a\). By
[[?lean:New.Modulus.schrodingerOp_single_eq_mean_translate_projOn|the formula for the operator of a point mass]],
\[
\delta_a=\frac{1}{\lvert(\mathcal{O}_E/\mathfrak{m})^{n}\rvert}\sum_{b}\psi_{\mathfrak{m}}(-a\cdot b)\,\varrho_f(y_b)\,v,
\]
with \(\psi_{\mathfrak{m}}\) the primitive [[?c:Additive character|additive character]] modulo \(\mathfrak{m}\), whose values
are [[?c:Root of unity|roots of unity]]. So each \(\delta_a\) is an admissible combination of the \(\varrho_f(y)v\),
\(y\in T^{n}_q(\bar d)\), with denominator \(\mathrm{N}(g)^{\lvert n\rvert}\) and size \(1\) (there
are \(\lvert(\mathcal{O}_E/\mathfrak{m})^{n}\rvert\) terms, each of absolute value the reciprocal of
that number at every conjugate). The sum \(\sum_a\Psi(a)\delta_a\) is an admissible combination of
the \(\delta_a\) with denominator \(1\) and size \(B\).
[[proofs/grh/upper-seesaw/admissible-combination-substitution|Substitution]] gives the result.
\(\blacksquare\)

## References

1. Lean: `New.Seesaw.isAdmissibleCombination_schrodingerOp_of_reduction`, `New.Seesaw.isAdmissibleCombination_schrodingerOp`, `New.Seesaw.card_residueRing_pi_dvd`, `New.Seesaw.star_idem_smul_mem_translations` in `src/New/UpperBound/Seesaw/AdmissibleCombinations.lean`.
