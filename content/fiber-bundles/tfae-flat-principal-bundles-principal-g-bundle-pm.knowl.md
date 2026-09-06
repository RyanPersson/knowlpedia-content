+++
id = "fiber-bundles/tfae-flat-principal-bundles-principal-g-bundle-pm"
title = "TFAE: Flat principal bundles (principal G-bundle with connection)"
kind = "knowl"
summary = "Equivalent conditions for a principal bundle connection to be flat, including vanishing curvature and homotopy-invariant parallel transport."
aliases = ["tfae-flat-principal-bundles-principal-g-bundle-pm", "TFAE: Flat principal bundles (principal G-bundle with connection)"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/tfae-flat-principal-bundles-principal-g-bundle-pm.md"
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/principal-g-bundle", "fiber-bundles/lie-group", "fiber-bundles/principal-connection", "fiber-bundles/curvature", "fiber-bundles/parallel-transport", "fiber-bundles/holonomy-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a connected [[fiber-bundles/smooth-manifold|smooth manifold]] and let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]] for a [[fiber-bundles/lie-group|Lie group]] \(G\). Fix a [[fiber-bundles/principal-connection|principal connection]] \(\omega\) on \(P\), with curvature form \(\Omega\). Then the following are equivalent:

1. **Zero curvature.**
   \(\Omega=0\); equivalently, the [[fiber-bundles/curvature|curvature]] of \(\omega\) vanishes identically.

2. **Local horizontal sections.**
   Every point of \(M\) has a neighborhood \(U\) admitting a smooth local section \(s:U\to P\) such that \(s^*\omega=0\).

3. **Homotopy-invariant parallel transport.**
   [[fiber-bundles/parallel-transport|Parallel transport]] along piecewise smooth curves depends only on the endpoint-fixed homotopy class of the curve. In particular, parallel transport around any contractible loop is the identity.

4. **Trivial restricted holonomy.**
   The identity component of the [[fiber-bundles/holonomy-group|holonomy group]] is trivial: \(\mathrm{Hol}^0_p(\omega)=\{e\}\) for (equivalently, for every) \(p\in P\).

5. **Classification by monodromy representation (when \(M\) is connected).**
   Choosing a basepoint \(x\in M\) and \(p\in P_x\), there is a homomorphism (monodromy)
   \[
   \rho:\pi_1(M,x)\to G
   \]
   such that \((P,\omega)\) is isomorphic (as a bundle with connection) to the quotient of the universal cover \(\widetilde M\times G\) by the diagonal action of \(\pi_1(M,x)\) given by deck transformations on \(\widetilde M\) and left multiplication via \(\rho\) on \(G\). The left multiplication commutes with the residual right principal \(G\)-action.

## Examples

1. **Trivial bundle with the product (zero) connection.**
   For \(P=M\times G\) and the connection with horizontal distribution \(TM\oplus\{0\}\), one has \(\Omega=0\), parallel transport is constant in the \(G\)-factor, and holonomy is trivial.

2. **Flat bundles over the circle classified by a single element of \(G\).**
   Over \(M=S^1\), any choice of \(h\in G\) defines a flat bundle as the quotient \((\mathbb{R}\times G)/\mathbb{Z}\) where \(1\in\mathbb{Z}\) acts by \((t,g)\mapsto(t+1,hg)\). The curvature vanishes, and, with the base fiber represented by \([0,g]\), parallel transport around the positively oriented generator sends \([0,g]\) to \([0,h^{-1}g]\); at \([0,e]\) its holonomy element is \(h^{-1}\). (Calling the quotient parameter \(h^{-1}\) instead gives holonomy \(h\).)

3. **Representations of the torus or surface group.**
   A homomorphism \(\rho:\pi_1(T^2)\to G\) (or \(\pi_1(\Sigma_g)\to G\) for a surface) produces a flat principal bundle via the quotient \(\widetilde M\times_\rho G\). Distinct conjugacy classes of \(\rho\) correspond to distinct flat bundles with connection up to isomorphism.
