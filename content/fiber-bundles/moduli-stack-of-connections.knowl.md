+++
id = "fiber-bundles/moduli-stack-of-connections"
title = "Moduli stack of connections"
kind = "definition"
summary = "The quotient stack of the space of connections by gauge transformations, retaining the automorphisms of each connection."
aliases = ["connection quotient stack", "stack of connections modulo gauge"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection", "fiber-bundles/gauge-group", "fiber-bundles/proposition-gauge-group-acts-on-conn-by-pullback", "topology/open-cover", "fiber-bundles/smooth-map", "algebra-category-theory/groupoid", "fiber-bundles/corollary-conn-gauge-is-a-well-defined-orbit-space", "fiber-bundles/stabilizer-of-a-connection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]], let \(\mathcal A(P)\) be its space of [[fiber-bundles/principal-connection|principal connections]], and let \(\mathcal G(P)\) be its [[fiber-bundles/gauge-group|gauge group]]. Use the left gauge action \(u\cdot A=(u^{-1})^*A\), the inverse-pullback version of the [[fiber-bundles/proposition-gauge-group-acts-on-conn-by-pullback|right pullback action]]. The **moduli stack of connections on \(P\)** is the smooth quotient stack
\[
[\mathcal A(P)/\mathcal G(P)],
\]
defined by the following families and gluing data.

For a smooth test manifold \(S\), choose an [[topology/open-cover|open cover]] \(\{U_i\}\). An object consists of smooth families of connections \(A_i\) parameterized by \(U_i\), and smooth families of gauge transformations \(u_{ij}\) on overlaps, with
\[
A_i=u_{ij}\cdot A_j,\qquad
u_{ii}=e,\qquad u_{ij}u_{jk}=u_{ik}.
\]
A smooth family means that the connection forms (respectively bundle automorphisms) depend smoothly on the parameter in \(U_i\) as well as on the point of \(P\).

A morphism from \((A_i,u_{ij})\) to \((A'_i,u'_{ij})\), after passage to a common refinement, is a family \(v_i\) of gauge transformations such that
\[
A'_i=v_i\cdot A_i,\qquad u'_{ij}=v_i u_{ij}v_j^{-1}.
\]
Morphisms compose by pointwise group multiplication. Data are identified under restriction to common refinements; compatible local objects and morphisms glue. Pullback along a smooth map of test manifolds is restriction of the parameter families. These rules specify a stack of [[algebra-category-theory/groupoid|groupoids]] on smooth manifolds with the open-cover topology.

Over a point, this is the action groupoid: objects are connections and arrows \(A\to A'\) are gauges \(u\) with \(u\cdot A=A'\). Its isomorphism classes form the [[fiber-bundles/corollary-conn-gauge-is-a-well-defined-orbit-space|gauge-orbit set]], while the automorphism group of \(A\) is its [[fiber-bundles/stabilizer-of-a-connection|stabilizer]].

## What the stack retains

The coarse [[lie-groups/orbit-space|orbit space]] records only whether two
connections are gauge equivalent. The quotient stack also records all
equivalences and their compositions. In particular,
\[
\operatorname{Aut}_{\operatorname{Conn}(P)}(A)
\cong \operatorname{Stab}_{\mathcal G(P)}(A),
\]
the [[fiber-bundles/stabilizer-of-a-connection|stabilizer of the connection]]. This retained isotropy is essential at [[fiber-bundles/reducible-connection|reducible connections]], where the gauge action has extra isotropy and a coarse quotient can develop singular behavior.

## Flat and equation-cut substacks

A gauge-invariant equation defines a full substack. For example, restricting the objects to flat connections gives
\[
[\mathcal A_{\mathrm{flat}}(P)/\mathcal G(P)].
\]
Its set of isomorphism classes is the familiar [[fiber-bundles/moduli-space-of-flat-connections|moduli space of flat connections]], but its isotropy groups still remember covariantly constant gauge transformations. Chern–Simons theory naturally works with this quotient geometry and its [[fiber-bundles/line-bundle|line bundles]] rather than merely with a set of orbits.

## Conventions and scope

**Warning.** The definition uses smooth test manifolds and families of smooth connections. It does not assert that the quotient is a finite-dimensional differentiable or algebraic stack. Sobolev completions provide alternative analytic models, whose regularity must be specified.

Some authors let the bundle \(P\) vary and use “the stack of connections” for a larger stack whose objects are principal bundles equipped with connections. Here \(P\) is fixed. The stack quotient is also different from the homotopy quotient, though their associated homotopy types are closely related.

## References

1. David S. Metzler, “Topological and Smooth Stacks,” 2003. [arXiv record](https://doi.org/10.48550/arXiv.math/0306176). Relevant: §§2–3, groupoids, quotient constructions, and smooth stacks.
2. Daniel S. Freed, “Classical Chern–Simons Theory, Part 1,” *Advances in Mathematics* 113 (1995), 237–303. [DOI record](https://doi.org/10.1006/aima.1995.1039). Relevant: §§2–3, connections, gauge transformations, and moduli of flat connections.
