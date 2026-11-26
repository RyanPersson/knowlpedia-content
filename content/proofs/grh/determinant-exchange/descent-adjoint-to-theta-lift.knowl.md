+++
id = "proofs/grh/determinant-exchange/descent-adjoint-to-theta-lift"
title = "The normalized descent is adjoint to the theta lift"
kind = "theorem"
summary = "For a descent pair, the inner product of a lift with a form on V equals the Petersson product on W of the lifted form with the normalized descent; the descent of a form is a form."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.DescentPair.inner_thetaLift", "New.DescentPair.isForm_normalizedDescent"]
lean_files = ["src/New/Determinant/Norms/AdjointThetaLift.lean"]
proof_status = "full"
+++

**Theorem.** Let \(O\) be a [[?lean:New.DescentPair|descent pair]] over a CM field \(E\) with Weil data, with spaces \(W\) (rank \(r\ge 1\), signs \(s\)) and \(V=I_n\), and let \(l\) be a parameter on \(W\) that [[?lean:New.DescentPair.FitsParams|fits the pair]]. Let \(\Theta_W\) be the [[proofs/grh/determinant-exchange/theta-lift-of-descent-pair|theta lift]] and \(\theta\) the [[?lean:New.DescentPair.normalizedDescent|normalized descent]]. Then for every form \(\Xi\) on \(V\) of the pair:

1. \(\theta\Xi\) is a form on \(W\) of the type of parameter \(l\);
2. for every form \(y\) on \(W\) of parameter \(l\),
\[
\langle\Theta_Wy,\Xi\rangle=\langle y,\theta\Xi\rangle_{\mathrm{Pet}},
\]
where the left side is the class sum inner product of algebraic forms on \(V\) and the right side is the [[?c:Petersson inner product|Petersson product]] on \([U(W)]\). Both products are conjugate linear in the first argument.

## Proof

Let \(\varphi_0\) be the datum of the highest weight vector, let \(x\) be the function on \(U(V)(\mathbb{A})\) attached to \(\Xi\), and put \(c=[K_0:K_0\cap K]\cdot\dim\rho\), the index of the level \(K\) of the pair times the dimension of the weight representation \(\rho\). Three facts are used.

(a) The class sum inner product of two algebraic forms on \(V\) is \(c\) times the Petersson product of the attached functions ([[?lean:New.LevelPlaces.LevelForm.inner_eq_petersson|class sum product and Petersson product]]).

(b) Since \(\varphi_0\) is an arrow from \(W\) to \(V\) and an arrow from \(V\) to \(W\) for the transposed kernel between the conjugate types, the lift \(L\) by \(\varphi_0\) has an adjoint for the Petersson products: \(\langle Ly,x\rangle=\langle y,L^{\ast}x\rangle\), where \(L^{\ast}x=\overline{L^{t}(\bar x)}\) is the complex conjugate of the transposed lift of the conjugate form ([[?lean:New.IsArrow.inner_formLift_adjoint|adjoint of a lift]]). This is an exchange of the order of integration in \(\iint \overline{y(g)}\,\overline{\theta_{\varphi_0}(g,h)}\,x(h)\).

(c) The normalized descent, defined as a class sum, equals \(c\cdot L^{\ast}x\) ([[?lean:New.DescentPair.normalizedDescent_eq_smul_star_lift_swap|descent as conjugate transposed lift]]).

Statement 1 follows from (c): the conjugate of the transposed lift of the conjugate of a form is a form of parameter \(l\), because the polynomial of the highest vector is an edge ([[?lean:New.IsEdge.isForm_star_lift_swap|descent by an edge is a form]]), and forms are stable under scalar multiples. For statement 2,
\[
\langle\Theta_Wy,\Xi\rangle\overset{(a)}{=}c\,\langle Ly,x\rangle_{\mathrm{Pet}}\overset{(b)}{=}c\,\langle y,L^{\ast}x\rangle_{\mathrm{Pet}}=\langle y,c\,L^{\ast}x\rangle_{\mathrm{Pet}}\overset{(c)}{=}\langle y,\theta\Xi\rangle_{\mathrm{Pet}} .
\]

## References

1. Lean: `New.DescentPair.inner_thetaLift`, `New.DescentPair.isForm_normalizedDescent` in `src/New/Determinant/Norms/AdjointThetaLift.lean`.
