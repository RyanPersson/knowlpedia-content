+++
id = "fiber-bundles/universal-principal-bundle-egbg"
title = "Universal principal bundle EG→BG"
kind = "knowl"
summary = "A canonical principal G-bundle whose pullbacks classify principal G-bundles over paracompact bases."
aliases = ["universal-principal-bundle-egbg", "Universal principal bundle EG→BG"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/universal-principal-bundle-egbg.md"
prerequisites = ["topology/topological-group", "fiber-bundles/numerable-principal-bundle", "topology/contractible-space", "topology/homotopy", "topology/quotient-topology"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/topological-group|topological group]]. A **universal principal \(G\)-bundle** is a [[fiber-bundles/numerable-principal-bundle|numerable topological principal bundle]] \(\pi:EG\to BG\) with [[topology/contractible-space|contractible]] total space and the following universal property: for every space \(X\), pullback induces a bijection
\[
[X,BG]\longrightarrow
\{\text{numerable principal }G\text{-bundles over }X\}/\cong,
\qquad [f]\longmapsto[f^*EG].
\]
Here \([X,BG]\) means continuous maps modulo unbased [[topology/homotopy|homotopy]], and \(f^*EG=\{(x,e):f(x)=\pi(e)\}\) has the pullback topology and right action. Thus every numerable bundle is such a pullback, and two maps give isomorphic pullbacks exactly when they are homotopic. The base \(BG\) is the orbit space \(EG/G\) with its quotient topology.

## Existence and scope

Universal bundles exist for topological groups, using the Milnor construction and the numerable classification theorem. Equivalently, a numerable principal bundle with contractible total space has the stated classification property. Models are unique up to equivariant homotopy equivalence, with bases unique up to homotopy equivalence.

On a paracompact Hausdorff base every locally trivial principal bundle is numerable, so the theorem classifies all such bundles. For a Lie group and a smooth manifold, continuous principal bundles admit compatible smooth structures unique up to smooth bundle isomorphism. The spaces \(EG\) and \(BG\) themselves need not be finite-dimensional manifolds.

## Examples
1. **Circle group.** For \(G=U(1)\) one model is \(EU(1)=S^\infty\) with the free \(U(1)\)-action by scalar multiplication, and \(BU(1)=\mathbb{C}P^\infty\).
2. **A two-point group.** For \(G=\mathbb{Z}/2\), take \(EG=S^\infty\) with the antipodal action; then \(BG=\mathbb{R}P^\infty\).
3. **Classifying bundles over manifolds.** For any principal \(G\)-bundle \(P\to M\) over a smooth manifold \(M\), choosing \(EG\to BG\) produces a classifying map \(M\to BG\) whose pullback recovers \(P\) (up to isomorphism).
