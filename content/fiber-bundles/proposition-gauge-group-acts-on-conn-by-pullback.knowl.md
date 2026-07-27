+++
id = "fiber-bundles/proposition-gauge-group-acts-on-conn-by-pullback"
title = "Gauge group action on connections by pullback"
kind = "knowl"
summary = "Pullback gives a right action of the gauge group on principal connections."
aliases = ["proposition-gauge-group-acts-on-conn-by-pullback", "Gauge group action on connections by pullback"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/proposition-gauge-group-acts-on-conn-by-pullback.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] and let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal G-bundle]]. Write \(\mathrm{Conn}(P)\) for the set of [[fiber-bundles/principal-connection|principal connections]] on \(P\), and let \(\mathrm{Gauge}(P)\) denote the gauge group, i.e. the group of \(G\)-equivariant diffeomorphisms \(\Phi:P\to P\) covering the identity on \(M\) (so \(\pi\circ\Phi=\pi\) and \(\Phi(p\cdot g)=\Phi(p)\cdot g\)).

For every \(\Phi\in \mathrm{Gauge}(P)\) and every principal connection \(\omega\in \mathrm{Conn}(P)\), the pullback
\[
\omega\cdot\Phi \;:=\; \Phi^*\omega
\]
is again a principal connection on \(P\). This defines a right group action:
\[
(\omega\cdot\Phi_1)\cdot\Phi_2
=\omega\cdot(\Phi_1\Phi_2),
\qquad \omega\cdot\mathrm{id}=\omega.
\]

Equivalently, if \(\omega\) is viewed as a \(G\)-equivariant horizontal distribution \(H=\ker\omega\subset TP\), then \(\Phi\) sends horizontals to horizontals:
\[
H^{\Phi^*\omega}_p \;=\; (d\Phi_p)^{-1}\bigl(H_{\Phi(p)}^{\omega}\bigr),
\]
so the gauge group acts on the set of horizontal distributions defining connections.

## Examples
1. **Trivial bundle \(P=M\times G\).** With the right principal action \((x,h)\cdot k=(x,hk)\), a gauge transformation determined by \(g:M\to G\) is \(\Phi_g(x,h)=(x,g(x)h)\). In the section \(s(x)=(x,e)\), pullback sends the local connection form \(A\) to
   \[
   A \longmapsto A^g := \mathrm{Ad}_{g^{-1}}A + g^{-1}dg.
   \]
2. **Abelian structure group.** If \(G\) is abelian (e.g. \(U(1)\)), then \(\mathrm{Ad}_{g^{-1}}\) is trivial and the transformation law reduces to
   \[
   A \longmapsto A + g^{-1}dg,
   \]
   i.e. gauge transformations act by translation by an exact 1-form (in a trivialization).
3. **Frame bundle viewpoint.** If \(P\) is a frame bundle of a vector bundle, a gauge transformation is a change of frame covering \(\mathrm{id}_M\). Pulling back the connection corresponds to the usual transformation rule for connection matrices under a change of frame.
