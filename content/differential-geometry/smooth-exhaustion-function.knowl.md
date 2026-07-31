+++
id = "differential-geometry/smooth-exhaustion-function"
title = "Smooth exhaustion function"
kind = "definition"
summary = "A proper smooth nonnegative function whose compact sublevel sets exhaust a smooth manifold."
aliases = ["proper smooth exhaustion", "exhausting function"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be a [[fiber-bundles/smooth-manifold|smooth manifold]]. A **smooth exhaustion function** is a [[fiber-bundles/smooth-map|smooth map]] \(\rho:M\to[0,\infty)\) that is [[differential-geometry/proper-smooth-map|proper]]. Equivalently, every sublevel set
\[
M_c=\{x\in M:\rho(x)\le c\}
\]
is a [[topology/compact-set|compact set]], and the increasing family \((M_c)_{c\ge0}\) covers \(M\). Thus \(\rho(x_j)\to\infty\) along every sequence that eventually leaves each compact subset of \(M\). The codomain and nonnegativity are conventional; a bounded-below proper smooth real-valued function carries the same exhaustion data after translation. This is a global condition.

## Existence and construction

Every standard smooth manifold admits a smooth exhaustion function. One construction chooses a countable locally finite coordinate cover, compactly supported [[differential-geometry/bump-function|cutoff functions]] subordinate to it, and coefficients increasing rapidly enough that the resulting locally finite sum becomes proper. This is a smooth refinement of the fact that a second-countable manifold is \(\sigma\)-compact; see [Lee, chapter on smooth functions and partitions of unity].

Moreover, one can arrange additional properties, such as agreement with a prescribed function on a compact set, by modifying the construction with cutoff functions. Requiring all [[differential-geometry/critical-point-of-a-smooth-map|critical points]] to be nondegenerate is an extra Morse-theoretic refinement, not part of exhaustion.

## Examples and non-examples

On \(\mathbb R^n\), the function \(\rho(x)=\|x\|^2\) is a smooth exhaustion because its sublevel sets are [[topology/closed-ball|closed balls]]. The height function \(x\mapsto x_1\) is smooth and unbounded, but it is not an exhaustion: the inverse image of a compact interval is an unbounded slab and hence not compact.

On a compact manifold, every smooth map to \([0,\infty)\) is proper, so even a constant function is an exhaustion under the definition in the core.

## Uses and scope

Exhaustions reduce arguments on a noncompact manifold to controlled compact stages. They are used to build compactly supported approximations, organize proper embeddings, and localize inductive constructions. A proper Morse function supplies both an exhaustion and handle data, but a general smooth exhaustion may have degenerate critical points or whole critical submanifolds.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer, 2012. [DOI record]. Relevant: smooth partitions of unity, bump functions, and proper exhaustion constructions.
2. Morris W. Hirsch, *Differential Topology*, Graduate Texts in Mathematics 33, Springer, 1976. [DOI record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 6, Morse functions and proper functions on noncompact manifolds.
