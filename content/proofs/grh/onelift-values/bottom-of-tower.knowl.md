+++
id = "proofs/grh/onelift-values/bottom-of-tower"
title = "The bottom of the tower: from the block datum to all data"
kind = "theorem"
summary = "If the descents of a form on V by the block datum vanish for all polynomials, the twist characters are nontrivial and the hyperplane sums annihilate the form, then its descents to W vanish for all data that are vacuum off the places of the descent pair."
aliases = ["bottom of the tower"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.descentsVanish_of_hyperplaneSumsAnnihilate"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
proof_status = "full"
+++

**Theorem (bottom of the tower).** Let \(E\) be a [[?c:CM field|CM field]] with
[[?lean:New.WeilData|Weil data]] and \(O\) a [[?lean:New.DescentPair|descent pair]] over \(E\), with spaces
\(W\) (rank \(r\)) and \(V=I_n\) (definite, rank \(n>r\)), chosen places and twist places \(Q\) (together
\(S_O\)), residue characters \(\chi_w\) and character \(\nu_W\) of \(U(1)\). Let \(y\in\mathcal{F}_V\) be a
form on \(V\) and \(u\) a linear functional on its space of values. Assume:

1. \(\chi_w\neq 1\) for every \(w\in Q\);
2. the [[proofs/grh/onelift-values/hyperplane-sums-annihilate|hyperplane sums annihilate]] \(y\);
3. for every polynomial \(P\), the [[proofs/grh/onelift-values/descent-pairing|block descent]] of \(y\)
   vanishes: the theta lift to \(U(W)\) of \(\overline{c_u(y)}\) with datum
   \(v_P\otimes\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\) is zero.

Then [[?lean:New.SiegelWeil.DescentsVanish|all descents]] of \(\overline{c_u(y)}\) from \(U(V)\) to \(U(W)\),
twisted by \(\nu_W\), vanish for the data that are the vacuum at every finite place outside \(S_O\) and its
conjugate: for each such datum \(f\) on \(\operatorname{Hom}(W,V)\),
\[
\int_{[U(V)]}\theta\bigl(\omega(g,h)f\bigr)\,\overline{c_u(y)(h)}\,dh=0\qquad\text{for all } g\in U(W)(\mathbb{A}).
\]

## Proof

The set \(S_O\) is disjoint from its conjugate and \(\overline{c_u(y)}\) is automorphic on the definite group
\(U(V)\). By the reduction to special data
([[?lean:New.SiegelWeil.DescentsVanish.of_schrodingerOp|test on Schrödinger data]]) it suffices to prove
that the lift vanishes for the data \(v_P\otimes\Psi\otimes\mathrm{vac}\), with \(P\) a polynomial and
\(\Psi\) Schwartz–Bruhat above \(S_O\); that is, \(B_{u,P,g}(\Psi,y)=0\) for all \(g\), in the notation of
the [[proofs/grh/onelift-values/descent-pairing|descent pairing]].

Fix \(P\) and \(g\). The functions \(\Psi\) with \(B(\Psi,y)=0\) form a subspace (the kernel of a linear
form). By [[proofs/grh/onelift-values/factorial-classes-span-schwartz-bruhat|the spanning lemma]] it is
enough to show that for every point \(z\) the indicator of the class of \(z\) modulo \(i!\) at \(S_O\) pairs
to zero with \(y\) for all large \(i\). There are two cases.

* If \(z_w\) has an [[proofs/grh/onelift-values/integral-block-ratio|integral block ratio]] at every
  \(w\in S_O\), this is part (a) of
  [[proofs/grh/onelift-values/descent-pairing-vanishes-on-small-classes|the vanishing on small classes]],
  which uses hypothesis 3.
* Otherwise it is part (b), valid for every \(i\), which uses hypotheses 1 and 2. \(\blacksquare\)

## Remarks

The idea: around a point with integral block ratios, the average of a small class under the level group is
a multiple of a \(U(W)\)-translate of the block datum; around any other point, the stabiliser of the class
in the maximal level contains shears through which a hyperplane sum acts, and this sum kills \(y\).

## References

1. Lean: `New.DescentPair.descentsVanish_of_hyperplaneSumsAnnihilate` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`.
