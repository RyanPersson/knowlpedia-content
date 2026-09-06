+++
id = "fiber-bundles/atiyah-algebroid-of-a-principal-bundle"
title = "Atiyah algebroid of a principal bundle"
kind = "knowl"
summary = "The quotient TP/G with its natural Lie algebroid structure induced by G-invariant vector fields on the total space."
aliases = ["atiyah-algebroid-of-a-principal-bundle", "Atiyah algebroid of a principal bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/atiyah-algebroid-of-a-principal-bundle.md"
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/tangent-bundle", "fiber-bundles/quotient-vector-bundle", "fiber-bundles/bundle-map", "fiber-bundles/vector-field", "fiber-bundles/lie-bracket"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
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

A section of \(A(P)\) can be identified with a \(G\)-invariant [[fiber-bundles/vector-field|vector field]] on \(P\): explicitly, \( \Gamma(A(P)) \cong \mathfrak{X}(P)^G \). Define a bracket on \(\Gamma(A(P))\) by
\[
[\![\sigma,\tau]\!]\;\coloneqq\;\text{the class of }[X,Y],
\]
where \(X,Y\) are \(G\)-invariant vector fields representing \(\sigma,\tau\) and \([X,Y]\) is their [[fiber-bundles/lie-bracket|Lie bracket]]. This is well-defined and makes \(A(P)\) into a Lie algebroid over \(M\), called the **Atiyah algebroid** of \(P\).

## Right-action convention

For the right-action convention, invariant vector fields along a group fiber are right-invariant, whose bracket is the opposite of the usual Lie-algebra bracket. With the standard bracket on \(\operatorname{ad}(P)\), the Atiyah sequence is embedded by \([p,\xi]\mapsto[-\xi^\#_p]\); the minus sign compensates for the right-action convention.

## Examples
1. **Bundle over a point.** If \(M=\{\ast\}\) and \(P=G\), then \(TP/G\) identifies with \(\mathfrak{g}\) via right translation; right-invariant vector fields have the opposite of the usual Lie-algebra bracket. Composing this identification with \(\xi\mapsto-\xi\) gives the standard Lie-algebra bracket used for the adjoint-bundle inclusion.

2. **Trivial bundle.** For \(P=M\times G\), there is a vector bundle isomorphism
   \[
   TP/G \cong TM \oplus (M\times \mathfrak{g}),
   \]
   and, using the splitting in which \((X,\phi)\) represents the invariant field with vertical part \(-\phi\), the bracket on sections \((X,\phi)\), \((Y,\psi)\) is
   \[
   [\![(X,\phi),(Y,\psi)]\!] = \bigl([X,Y],\, X(\psi)-Y(\phi)+[\phi,\psi]\bigr).
   \]

3. **Principal \(U(1)\)-bundle.** Since the adjoint action of \(U(1)\) on \(\mathfrak{u}(1)\cong i\mathbb{R}\) is trivial, the adjoint bundle is the trivial [[fiber-bundles/line-bundle|line bundle]] \(M\times\mathfrak{u}(1)\). Thus the Atiyah sequence is an extension of \(TM\) by this bundle; after choosing a connection, its curvature appears in the resulting bracket formula.
