+++
id = "proofs/grh/upper-divisibility/collisions"
title = "Collisions of a-places at a prime"
kind = "definition"
summary = "Pairs of an a-place and a partner exponent of p whose partner place is again an a-place, and the sum of a over p to the e over them."
aliases = ["collision", "collision sum"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Data.IsCollision", "New.Data.collisionSum"]
lean_files = ["src/New/UpperBound/Size/ShortColumns.lean"]
+++

Let \(D\) be [[?lean:New.Data|admissible data]], \(\Phi\) the group of infinite places of \(E\), \(\Phi_a\subset\Phi\) the set of [[?lean:New.Data.aPlaces|a-places]], \(p\) a natural number and \(\mathrm{ev}\subset\Phi\) a finite set. A pair \((\tau,e)\in\Phi\times\mathbb{N}\) is a **collision outside \(\mathrm{ev}\)** if

1. \(e\) is a [[?lean:New.positivePartnerExponents|positive partner exponent]] of \(p\) (so \(e\ge1\), and \(p=d\), or \(\chi_K(p)=-1\) and \(e\) is odd);
2. \(\tau\in\Phi_a\setminus\mathrm{ev}\); and
3. \(u(-p^{e})\,\tau\in\Phi_a\setminus\mathrm{ev}\), where \(u(\nu)\) is the [[?lean:New.Data.placeOfInt|place named by the integer \(\nu\)]].

The **collision sum outside \(\mathrm{ev}\)** is
\[
\operatorname{coll}_p(\mathrm{ev})\;=\;\sum_{(\tau,e)\ \text{collision outside}\ \mathrm{ev}}\frac{a}{p^{e}} .
\]

## References

1. Lean: `New.Data.IsCollision`, `New.Data.collisionSum` in `src/New/UpperBound/Size/ShortColumns.lean`.
