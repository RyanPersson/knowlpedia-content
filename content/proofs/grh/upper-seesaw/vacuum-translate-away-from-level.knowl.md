+++
id = "proofs/grh/upper-seesaw/vacuum-translate-away-from-level"
title = "Translates of the vacuum can be moved away from N"
kind = "lemma"
summary = "A translate of the vacuum by a vector with denominators beta away from n, n coprime to N, is a root of unity times a translate by a vector vanishing above N."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Seesaw.exists_finHeisenbergOp_vacElem_eq_of_coprime", "New.Seesaw.v_selfOrConj_eq_one", "New.Seesaw.exists_finHeisenbergOp_add_vacElem"]
lean_files = ["src/New/UpperBound/Seesaw/NeighbourVacuum.lean", "src/New/UpperBound/Seesaw/EdgePairEvaluation.lean"]
proof_status = "full"
+++

Let \(N\) be a prime whose places in the [[?c:CM field|CM field]] \(E\) are exactly those of
\(P\cup\bar P\) ([[?lean:New.IsSplitLevel|split level]]), and let \(\beta\) be an integral adele
that is a unit at all places above \(N\) (as for a
[[proofs/grh/upper-seesaw/neighbour-lattice|scaling at \(M\)]]). Let \(W\) be a
[[?lean:New.Space|hermitian space with a point]] whose coordinates are the entries of a matrix with
two blocks of rows, with vacuum \(v_0\) and finite Heisenberg operators \(\varrho_f\), and let
\(\beta_i=\beta\) on the first block of rows and \(\bar\beta\) on the second.

**Lemma.** Let \(n\) be coprime to \(N\) and \(y\in T_n((\beta_i))\)
([[proofs/grh/upper-seesaw/translation-groups|weighted translations]]). Then there are a
[[?c:Root of unity|root of unity]] \(\zeta\) and \(y'\in T_n((\beta_i))\), vanishing at all places
of \(P\cup\bar P\), with
\[
\varrho_f(y)v_0=\zeta\,\varrho_f(y')v_0 .
\]
One can take \(y'=y-1_{P\cup\bar P}\,y\).

## Proof

Let \(l=1_{P\cup\bar P}\,y\). *\(l\) is integral:* at a place \(w\) above \(N\), \(w\nmid n\) since
\(n\) is coprime to \(N\), so \(\lvert\beta_i\rvert_w\lvert y_i\rvert_w\le1\); and
\(\lvert\beta_i\rvert_w=1\) because \(\beta\) and \(\bar\beta\) are units above \(N\). At the other
places \(l\) vanishes. *\(l\in T_n((\beta_i))\):* the \(\beta_i\) are integral. Hence
\(y'=y-l\in T_n((\beta_i))\), and \(y'\) vanishes above \(N\).

For any \(x\) and any lattice vector \(l'\), by the
[[?lean:New.Space.finHeisenbergOp_finHeisenbergOp|composition law]] and
\(\varrho_f(l')v_0=v_0\):
\(\varrho_f(x)v_0=\varrho_f(x)\varrho_f(l')v_0=\psi(\bar c_0\,l'^{*}x)\,\varrho_f(x+l')v_0\), and the
values of \(\psi\) are roots of unity. Apply this with \(x=y\), \(l'=-l\). \(\blacksquare\)

## References

1. Lean: `New.Seesaw.exists_finHeisenbergOp_vacElem_eq_of_coprime`, `New.Seesaw.exists_finHeisenbergOp_add_vacElem` (the latter in `EdgePairEvaluation.lean`) in `src/New/UpperBound/Seesaw/NeighbourVacuum.lean`.
