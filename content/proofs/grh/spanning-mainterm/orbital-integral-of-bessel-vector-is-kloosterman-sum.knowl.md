+++
id = "proofs/grh/spanning-mainterm/orbital-integral-of-bessel-vector-is-kloosterman-sum"
title = "The orbital integral of the finite Bessel vector is a Kloosterman sum"
kind = "theorem"
summary = "The (a,b) entry of the orbital integral of the finite Bessel vector at x is the volume of K(M) times the Kloosterman sum of x at s, where a b^{-1} lies in sK(M)."
aliases = ["besselOrbitalIntegral_besselVector_apply"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.IntegralPlace.IsLargeLatticeData.besselOrbitalIntegral_besselVector_apply", "New.Floors.PlaceData.mem_unitaryLevel_one_of_inv_mul_mul_inv_mem"]
lean_files = ["src/New/Spanning/MainTerm/KloostermanSum.lean"]
proof_status = "full"
+++

**Theorem.** Let \(F\) be place data at a finite place (or product of finite places) for the
unitary group \(G\), as in the definition of the
[[proofs/grh/spanning-mainterm/kloosterman-sum-at-finite-places|Kloosterman sum]], and assume
that \(F\) is
[[?lean:New.Floors.IntegralPlace.IsLargeLatticeData|large lattice data]] (the form is unimodular
over the ring of integers, the data of \(F\) are those of the lattice of integral vectors, the
rank is large, the character of the place is trivial on traces and \(G\) is unimodular). Let
\(\mu\) be the [[?lean:New.Floors.PlaceData.groupMeasure|measure on \(G\) built from \(F\)]], which
under this hypothesis is a [[harmonic-analysis/haar-measure|Haar measure]]. Let \(Z\) be a
subgroup with \(K(M)\subseteq Z\subseteq G(\mathcal O)\) (the integral points), and let
\(W=(W_a)_{a\in Z/K(M)}\) be the
[[?lean:New.Floors.PlaceData.IntermediateGroup.besselVector|Bessel vector of \(Z\)]],
\(W_a(y)=\chi(y\dot a^{-1})\), where \(\chi\) is the finite Bessel function and \(\dot a\in Z\)
the chosen representative of the coset \(a\). Let \(x,s\in G\) and let \(a,b\in Z/K(M)\) satisfy
\(\dot a\,\dot b^{-1}\in sK(M)\). Then the entry \((a,b)\) of the
[[?lean:New.besselOrbitalIntegral|orbital integral]] of \(W\) at \(x\) is

\[
  \int_GW_a(y)\,\overline{W_b(x^{-1}y)}\,d\mu(y)\;=\;\mu\bigl(K(M)\bigr)\cdot\operatorname{Kl}_F(x,s).
\]

## Proof

Write \(K=K(M)\). Since \(\dot a,\dot b\) are integral and \(s^{-1}\dot a\dot b^{-1}\in K\subseteq G(\mathcal O)\),
the point \(s=\dot a\dot b^{-1}(s^{-1}\dot a\dot b^{-1})^{-1}\) is integral.

By definition the left-hand side is \(\int_G\chi(y\dot a^{-1})\overline{\chi(x^{-1}y\dot b^{-1})}\,d\mu(y)\).
The Haar measure \(\mu\) is right invariant (\(G\) is unimodular), so substituting
\(y\mapsto y\dot b\) gives

\[
  \int_G\chi(y\,\dot b\,\dot a^{-1})\,\overline{\chi(x^{-1}y)}\,d\mu(y).
\]

The integrand depends only on the coset \(yK\) and equals
\(\Phi(yK)=\chi(\dot q s^{-1})\overline{\chi(x^{-1}\dot q)}\) with \(q=yK\). Indeed, let
\(z=\dot q\), so \(y^{-1}z\in K\). Then \((x^{-1}y)^{-1}(x^{-1}z)=y^{-1}z\in K\), and
\((y\dot b\dot a^{-1})^{-1}(zs^{-1})=\dot a\dot b^{-1}\,(y^{-1}z)\,s^{-1}
= s\cdot\bigl[(s^{-1}\dot a\dot b^{-1})(y^{-1}z)\bigr]\cdot s^{-1}\in K\), because the integral
point \(s\) normalises \(K\). By right \(K\)-invariance of \(\chi\) the two values of \(\chi\)
are unchanged.

\(K\) is open and compact, hence of finite measure, so by the
[[proofs/grh/spanning-mainterm/integral-over-cosets-of-open-subgroup|integral over the cosets of an open subgroup]]
the integral is \(\mu(K)\sum_{q\in G/K}\Phi(q)\), and this sum is \(\operatorname{Kl}_F(x,s)\) by
the [[proofs/grh/spanning-mainterm/bessel-coset-sum-is-kloosterman-sum|coset sum lemma]].
\(\blacksquare\)

## References

1. Lean: `New.Floors.IntegralPlace.IsLargeLatticeData.besselOrbitalIntegral_besselVector_apply`
   in `src/New/Spanning/MainTerm/KloostermanSum.lean`.
2. For the shape of the statement compare: H. Jacquet and Y. Ye, *Germs of Kloosterman integrals
   for GL(3)*, Trans. Amer. Math. Soc., 1999 (cited in the head of
   `src/New/Spanning/MainTerm/EnergyEstimate.lean` as related work).
