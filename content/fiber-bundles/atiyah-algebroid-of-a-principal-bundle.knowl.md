+++
id = "fiber-bundles/atiyah-algebroid-of-a-principal-bundle"
title = "Atiyah algebroid of a principal bundle"
kind = "knowl"
summary = "The quotient TP/G with its natural Lie algebroid structure induced by G-invariant vector fields on the total space."
aliases = ["atiyah-algebroid-of-a-principal-bundle", "Atiyah algebroid of a principal bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/atiyah-algebroid-of-a-principal-bundle.md"
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal G-bundle]]. The right action of \(G\) on \(P\) lifts to an action on the [[fiber-bundles/tangent-bundle|tangent bundle]] \(TP\) by differentials \((R_g)_*:TP\to TP\). Form the [[fiber-bundles/quotient-vector-bundle|quotient vector bundle]]
\[
A(P)\coloneqq TP/G \;\longrightarrow\; M,
\]
whose fiber over \(x\in M\) consists of \(G\)-orbits of tangent vectors \(v_p\in T_pP\) with \(p\in P_x\).

The map \(d\pi:TP\to TM\) is \(G\)-equivariant and descends to a [[fiber-bundles/bundle-map|bundle map]] (the **anchor**)
\[
a:A(P)\to TM.
\]

A section of \(A(P)\) can be identified with a \(G\)-invariant [[fiber-bundles/vector-field|vector field]] on \(P\): explicitly, \( \Gamma(A(P)) \cong \mathfrak{X}(P)^G \). Using this, define a bracket on \(\Gamma(A(P))\) by
\[
[\![\sigma,\tau]\!]\;\coloneqq\;\text{the class of }[X,Y],
\]
where \(X,Y\) are \(G\)-invariant vector fields representing \(\sigma,\tau\) and \([X,Y]\) is their [[fiber-bundles/lie-bracket|Lie bracket]]. This is well-defined and makes \(A(P)\) into a Lie algebroid over \(M\), called the **Atiyah algebroid** of \(P\).

## Examples
1. **Bundle over a point.** If \(M=\{\ast\}\) and \(P=G\), then \(TP/G\) identifies with the Lie algebra \(\mathfrak{g}\) (via left translation), and the induced bracket is the usual Lie bracket on \(\mathfrak{g}\).

2. **Trivial bundle.** For \(P=M\times G\), there is a vector bundle isomorphism
   \[
   TP/G \cong TM \oplus (M\times \mathfrak{g}),
   \]
   and the bracket on sections \((X,\phi)\), \((Y,\psi)\) is
   \[
   [\![(X,\phi),(Y,\psi)]\!] = \bigl([X,Y],\, X(\psi)-Y(\phi)+[\phi,\psi]\bigr).
   \]

3. **Principal \(U(1)\)-bundle.** Since the adjoint action of \(U(1)\) on \(\mathfrak{u}(1)\cong i\mathbb{R}\) is trivial, the adjoint bundle is the trivial [[fiber-bundles/line-bundle|line bundle]] \(M\times\mathfrak{u}(1)\). Thus the Atiyah sequence is an extension of \(TM\) by this bundle; after choosing a connection, its curvature appears in the resulting bracket formula.
