+++
id = "proofs/grh/determinant-exchange/theta-lift-of-descent-pair"
title = "Theta lift of a descent pair"
kind = "definition"
summary = "The lift from automorphic forms on U(W) of a fitting parameter to algebraic forms on the definite group U(V), by the datum of the highest weight vector."
aliases = ["Theta_W", "lift of a descent pair"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.thetaLift", "New.DescentPair.ofAlgForm_thetaLift", "New.DescentPair.coe_thetaLift", "New.DescentPair.FitsParams.isArrow_fockDatum", "New.DescentPair.FitsParams.isArrow_swap_fockDatum"]
lean_files = ["src/New/Determinant/Norms/AdjointThetaLift.lean"]
+++

Let \(E\) be a [[?c:CM field|CM field]] with a CM type and Weil data, and let \(O\) be a [[?lean:New.DescentPair|descent pair]] with hermitian space \(W\) of rank \(r\ge 1\) and signs \(s\), and definite space \(V=I_n\), \(n>r\). Let \(l\) be a (doubled) Harish-Chandra parameter on \(W\) that [[?lean:New.DescentPair.FitsParams|fits the pair]], and let \(l'\) be the [[?lean:New.DescentPair.paramV|parameter of the pair on \(V\)]], whose highest weight is \((k,e)\). Let \(\xi_0\) be the [[?lean:New.highestVector|highest weight vector]] of the representation of weight \((k,e)\), and \(\varphi_0=\varphi_{\xi_0}\) the corresponding [[?lean:New.DescentPair.fockDatum|datum]] \(v_{P_{\xi_0}}\otimes\Psi_{\mathrm{bl}}\otimes\mathrm{vac}\).

The **theta lift of the pair** is the linear map
\[
\Theta_W:\ \{\text{forms on }W\text{ of parameter }l\}\longrightarrow\{\text{algebraic forms on }V\text{ of the pair}\}
\]
that sends a [[?lean:New.Space.Form|form]] \(y\) on \(U(W)(\mathbb{A})\), of the [[?lean:New.typeKernel|type]] of parameter \(l\) and of any level, to the [[?c:Algebraic modular form|algebraic form]] that corresponds to the function
\[
h\longmapsto\int_{[U(W)]}y(g)\,\theta_{\varphi_0}(g,h)\,dg \qquad(h\in U(V)(\mathbb{A}))
\]
on the adelic group of \(V\), the [[?c:Theta lift|theta lift]] of \(y\) by the datum \(\varphi_0\) ([[?lean:New.formLift|lift of forms]]). Here \(\theta_{\varphi_0}\) is the [[?lean:New.pairTheta|theta kernel]] with the characters \(\nu_W,\nu_V\) of the pair, and the passage between functions on \(U(V)(\mathbb{A})\) of the type of parameter \(l'\) and algebraic forms of weight \((k,e)\) is the [[?lean:New.Space.toAlgForm|standard isomorphism]] for the definite space \(V\).

## Why this is well defined

Because \(l\) fits the pair, the polynomial of the highest vector is an [[?lean:New.IsEdge|edge]] between the types of parameters \(l\) and \(l'\) ([[?lean:New.DescentPair.FitsParams.isEdge|fitting parameters give an edge]]). Hence the datum \(\varphi_0\) is an [[?lean:New.IsArrow|arrow]] from \(W\) to \(V\): the lift by it takes forms of parameter \(l\) to forms of parameter \(l'\); and it is an arrow from \(V\) to \(W\) between the conjugate types for the transposed kernel. The level \(K\) of the pair acts on \(\varphi_0\) through the level character ([[?lean:New.DescentPair.omega_fockDatum_star|action of the level on the datum]], using that the highest vector is real), so the lift has level \(K\) with that character, that is, it is one of the [[?lean:New.DescentPair.FormV|forms on \(V\)]] of the pair.

## References

1. Lean: `New.DescentPair.thetaLift`, `New.DescentPair.ofAlgForm_thetaLift` in `src/New/Determinant/Norms/AdjointThetaLift.lean`.
