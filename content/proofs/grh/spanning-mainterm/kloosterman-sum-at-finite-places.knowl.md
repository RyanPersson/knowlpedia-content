+++
id = "proofs/grh/spanning-mainterm/kloosterman-sum-at-finite-places"
title = "Kloosterman sum of a unitary group at the finite places"
kind = "definition"
summary = "The sum of psi(u) conj psi(u') over pairs u, u' of the Bessel unipotent group modulo its intersection with K(M) such that u^{-1} x u' lies in s K(M)."
aliases = ["kloostermanSum", "PlaceData.kloostermanSum", "UnipotentCosets"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Floors.PlaceData.kloostermanSum", "New.Floors.PlaceData.UnipotentCosets"]
lean_files = ["src/New/Spanning/MainTerm/KloostermanSum.lean"]
+++

Let \(A\) be a finite place of the CM field, or a finite product of such places, with its
involution and its ring of integers ([[?lean:New.Floors.IntegralPlace|an integral place]]). Let
\(G\) be the [[?c:Unitary group of a hermitian form|unitary group]] of the hermitian form
[[?lean:New.Shape.Form.splitGram|\(\varrho\) hyperbolic planes plus a middle space with Gram matrix \(T\)]]
over \(A\), and let \(F\) be [[?lean:New.Floors.PlaceData|place data]] for it, with level
\(M\) (a unit of \(A\)). Write

- \(\mathsf U\subseteq G\) for the [[?lean:New.Shape.Form.besselU|Bessel unipotent subgroup]];
- \(K(M)\subseteq G\) for the
  [[?lean:New.Floors.PlaceData.congruenceSubgroup|principal congruence subgroup of level \(M\)]]:
  the integral points congruent to \(1\) modulo \(M\);
- \(\chi\colon G\to\mathbb C\) for the
  [[?lean:New.Floors.IntegralPlace.extendedBesselChar|finite Bessel function]] of level \(M\):
  it vanishes off \(\mathsf UK(M)\), is right invariant under \(K(M)\), and on \(\mathsf U\) it is
  the character \(\psi_{\mathsf U}\) of \(\mathsf U\).

The set of **unipotent cosets** is \(\mathsf U/(\mathsf U\cap K(M))\). Fix a representative
\(\dot w\in\mathsf U\) of each coset \(w\). For \(x,s\in G\) the **Kloosterman sum of \(x\) at
\(s\)** is

\[
  \operatorname{Kl}_F(x,s)\;=\;\sum_{\substack{(w,w')\in(\mathsf U/(\mathsf U\cap K(M)))^2\\ \dot w^{-1}x\,\dot w'\in sK(M)}}\chi(\dot w)\,\overline{\chi(\dot w')} .
\]

The sum is taken as an unconditional sum, with value \(0\) if the family is not summable.

## Remarks

Since \(\chi\) is right \(K(M)\)-invariant, \(\chi(\dot w)\) does not depend on the choice of the
representative. When \(s\) is an integral point, \(s\) normalises \(K(M)\) and the condition
\(\dot w^{-1}x\dot w'\in sK(M)\) is independent of the representatives too, so the sum is then
intrinsic. It is the classical shape of a
[[?c:Kloosterman sum|Kloosterman sum]]: pairs of unipotent elements linked through a fixed double
coset, weighted by a character. It arises as an
[[proofs/grh/spanning-mainterm/orbital-integral-of-bessel-vector-is-kloosterman-sum|orbital integral of the finite Bessel vector]].

## References

1. Lean: `New.Floors.PlaceData.UnipotentCosets`, `New.Floors.PlaceData.kloostermanSum` in
   `src/New/Spanning/MainTerm/KloostermanSum.lean`.
