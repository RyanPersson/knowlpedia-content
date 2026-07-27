+++
id = "fiber-bundles/moduli-stack-of-connections"
title = "Moduli stack of connections"
kind = "definition"
summary = "The quotient stack of the space of connections by gauge transformations, retaining the automorphisms of each connection."
aliases = ["connection quotient stack", "stack of connections modulo gauge"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]], let \(\mathcal A(P)\) be its [[fiber-bundles/bundle-of-connections|space of connections]], and let \(\mathcal G(P)\) be its [[fiber-bundles/gauge-group|gauge group]]. The **moduli stack of connections** is the quotient stack
\[
\operatorname{Conn}(P):=[\mathcal A(P)/\mathcal G(P)].
\]
Its presenting action groupoid has connections as objects and, from \(A\) to
\(A'\), [[fiber-bundles/gauge-transformation|gauge transformations]] \(u\) satisfying \(u\!\cdot\!A=A'\) as
morphisms. Thus the isomorphism classes of objects form the
[[fiber-bundles/corollary-conn-gauge-is-a-well-defined-orbit-space|ordinary
gauge-orbit set]] \(\mathcal A(P)/\mathcal G(P)\), while the automorphism
group of \(A\) is its
[[fiber-bundles/stabilizer-of-a-connection|gauge stabilizer]].

## What the stack retains

The coarse [[lie-groups/orbit-space|orbit space]] records only whether two
connections are gauge equivalent. The quotient stack also records all
equivalences and their compositions. In particular,
\[
\operatorname{Aut}_{\operatorname{Conn}(P)}(A)
\cong \operatorname{Stab}_{\mathcal G(P)}(A),
\]
the [[fiber-bundles/stabilizer-of-a-connection|stabilizer of the connection]]. This retained isotropy is essential at [[fiber-bundles/reducible-connection|reducible connections]], where the gauge action is not free and a coarse quotient develops singular behavior.

Passing from an action groupoid to its associated smooth stack also imposes descent: compatible families of connections and gauge identifications over an open cover glue. General quotient-stack and smooth-stack constructions are developed in [Metzler, §§2–3](https://doi.org/10.48550/arXiv.math/0306176).

## Flat and equation-cut substacks

A gauge-invariant equation defines a full substack. For example, restricting the objects to flat connections gives
\[
[\mathcal A_{\mathrm{flat}}(P)/\mathcal G(P)].
\]
Its set of isomorphism classes is the familiar [[fiber-bundles/moduli-space-of-flat-connections|moduli space of flat connections]], but its isotropy groups still remember covariantly constant gauge transformations. Chern–Simons theory naturally works with this quotient geometry and its line bundles rather than merely with a set of orbits [Freed, §§2–3](https://doi.org/10.1006/aima.1995.1039).

## Conventions and scope

**Warning.** The displayed quotient is an infinite-dimensional smooth or differentiable stack, not automatically an algebraic stack. A rigorous analytic model normally replaces the smooth spaces by compatible Sobolev completions.

Some authors let the bundle \(P\) vary and use “the stack of connections” for a larger stack whose objects are principal bundles equipped with connections. Here \(P\) is fixed. The stack quotient is also different from the homotopy quotient, though their associated homotopy types are closely related.

## References

1. David S. Metzler, “Topological and Smooth Stacks,” 2003. [arXiv record](https://doi.org/10.48550/arXiv.math/0306176). Relevant: §§2–3, groupoids, quotient constructions, and smooth stacks.
2. Daniel S. Freed, “Classical Chern–Simons Theory, Part 1,” *Advances in Mathematics* 113 (1995), 237–303. [DOI record](https://doi.org/10.1006/aima.1995.1039). Relevant: §§2–3, connections, gauge transformations, and moduli of flat connections.
