+++
id = "proofs/grh/upper-seesaw/integral-as-sum-over-cut"
title = "An integral over the Bessel quotient as a weighted sum over a cut"
kind = "theorem"
summary = "If the Bessel periods of a function factor over a finite cut T, its integral over the quotient by the rational Bessel points is a constant times the sum over T weighted by inverse cover multiplicities."
aliases = ["integral as coset sum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Grading.exists_integral_eq_sum_over_cut", "New.Seesaw.lintegral_indicator_inv_coverMultiplicity", "New.Seesaw.integral_indicator_smul_quotient", "New.Seesaw.lintegral_besselGroup_cutoff_mul", "New.Seesaw.integral_quotMeasure_eq_integral_withDensity", "New.Seesaw.integral_withDensity_mul_eq_mul", "New.Seesaw.measure_union_cosets"]
lean_files = ["src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean"]
proof_status = "full"
+++

Let \(V\) be a [[?lean:New.Space|hermitian space with a point]] over a [[?c:CM field|CM field]]
\(E\), \(G=G_\infty\times G_f\) its [[?lean:New.G|adelic unitary group]], and \(Y\) a
[[?lean:New.Grading|grading]] with [[?lean:New.Grading.besselGroup|Bessel subgroup]]
\(R\le G\), finite part \(R_f=\{u\in G_f:(1,u)\in R\}\) and rational points \(R(F)=\Gamma\cap R\), where \(\Gamma\) is the group of rational points of the unitary group (matrices over \(E\) preserving the form; \(F=E^{+}\) is the totally real subfield over which the group is defined). Integrals over
\(R(F)\backslash G\) and \(R(F)\backslash R\) are taken with the quotient measures of the
[[harmonic-analysis/haar-measure|Haar measures]].

**Theorem.** Let \(A\le G_f\) be a [[?lean:New.IsLevel|level]] and
\(a\colon G_\infty\to\mathbb{C}\) a function. There is a constant \(\kappa\in\mathbb{C}\),
depending only on \((Y,A,a)\), such that for every level \(J\), every finite
\(T\subseteq G_f/J\), every \(f\colon G\to\mathbb{C}\) and every \(b\colon G_f/J\to\mathbb{C}\)
with

* \(f\) continuous, left invariant under \(R(F)\), and integrable on \(R(F)\backslash G\);
* \(T\) stable under \(R_f\cap A\);
* \(m_T(g_f)\ne0\) whenever \(f(g)\ne0\), where \(m_T\) is the
  [[proofs/grh/upper-seesaw/cover-multiplicity|cover multiplicity]] for \(S=R_f\) and \(A\);
* for every \(t=(t_\infty,t_f)\) with \(t_fJ\in T\):
  \(\displaystyle\int_{R(F)\backslash R}f(rt)\,dr=[K:J]\cdot a(t_\infty)\,b(t_f)\), where \(K\) is the
  group of integral points;

one has
\[
\int_{R(F)\backslash G}f(g)\,dg=\kappa\sum_{t\in T}\frac{b(t)}{m_T(t)} .
\]

## Proof

Let \(\eta\) be the Haar measure on \(R_f\) with \(\eta(R_f\cap A)=1\), and choose a
measurable cutoff \(\beta\ge0\) on \(G\) with \(\int_R\beta(rg)\,dr=1\) for all \(g\) ([[?lean:New.hasCutoff_of_proper|existence of a cutoff for a proper action]]). Put
\[
\alpha(g_\infty)=\int_{R_f}\beta(g_\infty,u)\,d\eta(u),\qquad
\psi=\frac{1}{m_T}\ \text{on } T,\ \ \psi=0\ \text{off } T,\qquad w(g)=\alpha(g_\infty)\psi(g_fJ),
\]
and \(\kappa=\int_{G_\infty}a\,\alpha\) if \(a\) is integrable for the measure with density \(\alpha\), and \(\kappa=0\) otherwise (no measurability or integrability of \(a\) is assumed; all integrals of complex functions here are Bochner integrals with the convention that a non-integrable function has integral \(0\), and the factorisation of the product integral below is used with this convention).

*Orbit integrals of the weight.* By the substitutions \(r\mapsto(1,u^{-1})r\) and \(u\mapsto r_fu\),
\(\int_Rw(rt)\,dr=\int_{R_f}\psi(u^{-1}t_fJ)\,d\eta(u)\). Since \(m_T\) is constant on
\(R_f\)-orbits, the integrand is \(1/m_T(t_f)\) on the set \(\{u:u^{-1}t_fJ\in T\}\), which by
stability of \(T\) is a union of exactly \(m_T(t_f)\) cosets of \(R_f\cap A\), each of mass \(1\).
So the orbit integral is \(1\) if \(m_T(t_f)\ne0\) and \(0\) otherwise.

*Unfolding.* Let \(U=\{g:m_T(g_f)\ne0\}\); \(f\) vanishes off \(U\). Integration in stages along
\(R(F)\le R\le G\), with the weight \(w\) as a partition of unity on \(U\), gives
\[
\int_{R(F)\backslash G}f=\int_G\Bigl(\int_{R(F)\backslash R}f(rt)\,dr\Bigr)w(t)\,dt .
\]
Precisely: by the orbit integrals, the map \((t,r)\mapsto rt\) carries the measure \(w\,dt\otimes dr\) on \(G\times R\) to the Haar measure restricted to \(U\), and [[?lean:New.integral_quotMeasure_stages|integration in stages]] along \(R(E)\le R\) with this fibration gives the formula.

*Evaluation.* The weight vanishes unless \(t_fJ\in T\), where the period hypothesis applies; the
integral factors as
\([K:J]\cdot\bigl(\int_{G_\infty}a\alpha\bigr)\cdot\int_{G_f}\psi(g)b(g)\,dg\). As \(K\) has volume
\(1\), each coset of \(J\) has volume \([K:J]^{-1}\), so
\(\int_{G_f}\psi b=[K:J]^{-1}\sum_{t\in T}b(t)/m_T(t)\). \(\blacksquare\)

## References

1. Lean: `New.Grading.exists_integral_eq_sum_over_cut` and the auxiliary lemmas listed in the front matter, in `src/New/UpperBound/Seesaw/IntegralAsCosetSum.lean`.
