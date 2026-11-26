+++
id = "proofs/grh/onelift-values/descent-pairing"
title = "The descent pairing of a finite datum and a form"
kind = "definition"
summary = "The pairing B(Psi, y): the conjugate-linear-in-y value at a point g of the theta descent to U(W) of a matrix coefficient of a form y on V, with datum v_P tensor Psi tensor vacuum."
aliases = ["descent pairing", "block descent vanishes"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.descentPairing", "New.DescentPair.descentPairing_apply", "New.DescentPair.BlockDescentVanishes", "New.DescentPair.leftMul", "New.DescentPair.matrixAt", "New.DescentPair.isAutomorphic_star_algFormCoeff", "New.DescentPair.blockDatum_val"]
lean_files = ["src/New/OneLift/FalseLifts/BottomOfTower.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with [[?lean:New.WeilData|Weil data]], and let \(O\) be a
[[?lean:New.DescentPair|descent pair]] over \(E\): a [[?c:hermitian space|hermitian space]] \(W\) of rank
\(r\), the standard definite space \(V=I_n\) of rank \(n>r\) ([[?lean:New.stdSpace|standard space]]), an
embedding \(\iota\) of the index set of the basis of \(W\) into that of \(V\), two finite families of split
finite places — the chosen places and the twist places \(Q\), whose union is the set \(S_O\) — and
characters \(\chi_w\) of the residue fields \(k_w\). Let \(\mathcal{F}_V\) be its space of
[[?lean:New.DescentPair.FormV|forms on \(V\)]] (algebraic modular forms on \(U(V)\) of the weight and level
of \(O\)). Fix

* a linear functional \(u\) on the weight space in which the forms take their values,
* a polynomial \(P\) in the variables indexed by (infinite place, index of \(V\), index of \(W\)), with
  [[?c:Fock model of the Weil representation|Fock vector]] \(v_P\),
* an adelic point \(g\) of \(U(W)\).

For a function \(\Psi\) on \(M_{n\times r}(\mathbb{A}_f)\) and \(y\in\mathcal{F}_V\), the **descent pairing**
is
\[
B(\Psi,y)=B_{u,P,g}(\Psi,y)=\int_{[U(V)]}\theta\bigl(\omega(g,h)\,(v_P\otimes\Psi\otimes\mathrm{vac})\bigr)\;
\overline{c_u(y)(h)}\;dh ,
\]
where \([U(V)]=U(V)(E)\backslash U(V)(\mathbb{A})\) with its invariant measure, \(\omega\) is the
[[?c:Weil representation of a unitary dual pair|Weil representation]] of \(U(W)\times U(V)\) on the data
on \(\operatorname{Hom}(W,V)\) twisted by the character
[[?lean:New.DescentPair.charW|\(\nu_W\)]] of \(U(1)\) (applied to \(\det h\); no twist in \(g\)), \(\theta\)
is the [[?c:theta functional|theta functional]], \(c_u(y)(h)=u\bigl(\rho(h_\infty^{-1})y(h_f)\bigr)\) is the
[[?lean:New.algFormCoeff|matrix coefficient]] of \(y\) at \(u\), and \(v_P\otimes\Psi\otimes\mathrm{vac}\) is
the datum with \(v_P\) at the infinite places, \(\Psi\) acting on the vacuum through the components at
\(S_O\) ([[?lean:New.Space.schrodingerOp|Schrödinger operator of \(\Psi\)]]), and the vacuum at all other
finite places. Thus \(B(\Psi,y)\) is the value at \(g\) of the theta lift from \(U(V)\) to \(U(W)\)
([[?lean:New.Space.lift|lift]] for the swapped kernel) of \(\overline{c_u(y)}\); it is linear in \(\Psi\)
and conjugate-linear in \(y\).

The function \(\overline{c_u(y)}\) is automorphic on \(U(V)\), and since \(V\) is definite it is rapidly
decreasing, so the integral converges.

The **block descent of \(y\) vanishes** (for \(u\) and \(P\)) if the theta lift of \(\overline{c_u(y)}\)
with datum \(v_P\otimes\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\) is the zero function on \(U(W)(\mathbb{A})\),
where \(\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\) is the
[[?lean:New.DescentPair.blockDatum|block datum]] of \(O\); equivalently
\(B_{u,P,g}(\Psi_{\mathrm{bl}},y)=0\) for all \(g\).

## Notation

For \(x\in M_{n\times r}(\mathbb{A}_f)\) and a finite place \(w\), \(x_w\in M_{n\times r}(E_w)\) is the
component at \(w\). The finite adelic points \(h\) of \(U(V)\) act on such matrices by \(x\mapsto hx\).
The block function \(\Psi_{\mathrm{bl}}\) is
\[
\Psi_{\mathrm{bl}}(x)=\prod_{w\in Q}\chi_w\bigl(\det x'_w \bmod w\bigr)
\]
if \(x\) is integral at all places of \(S_O\) and \(x_w\equiv(1,0)^{\mathsf T}\) modulo \(w\) at the chosen
places (identity in the rows \(\iota\), zero elsewhere), and \(0\) otherwise; here \(x'\) denotes the rows
\(\iota\) of \(x\).

## References

1. Lean: `New.DescentPair.descentPairing`, `New.DescentPair.BlockDescentVanishes` in `src/New/OneLift/FalseLifts/BottomOfTower.lean`.
