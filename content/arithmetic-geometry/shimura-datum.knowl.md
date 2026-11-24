+++
id = "arithmetic-geometry/shimura-datum"
title = "Shimura datum"
kind = "definition"
summary = "A rational reductive group together with a conjugacy class of homomorphisms from the Deligne torus satisfying three conditions."
aliases = ["Shimura data"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/reductive-algebraic-group", "differential-geometry/pure-hodge-structure"]
+++

A **Shimura datum** \((G,X)\) consists of a connected [[algebraic-geometry-foundations/reductive-algebraic-group|reductive group]] over \(\mathbb Q\) and a \(G(\mathbb R)\)-conjugacy class \(X\) of homomorphisms \(h:\mathbb S\to G_{\mathbb R}\). The Deligne torus \(\mathbb S=\operatorname{Res}_{\mathbb C/\mathbb R}\mathbb G_m\) has real points \(\mathbb C^\times\). Each \(h\in X\) satisfies three conditions.

- The [[differential-geometry/pure-hodge-structure|Hodge structure]] induced on the Lie algebra of \(G\) by the adjoint action has only types \((-1,1),(0,0),(1,-1)\).
- Conjugation by \(h(i)\) induces a [[lie-groups/cartan-involution-real-lie-algebra|Cartan involution]] on the real adjoint group.
- The projection of \(h\) to each nontrivial \(\mathbb Q\)-simple factor of the adjoint group is nontrivial.

## The modular example

Multiplication by \(a+bi\) on \(\mathbb C\), viewed as a two-dimensional real vector space, gives a real matrix in \(\mathrm{GL}_2(\mathbb R)\) for \(a+bi\ne0\). The conjugacy class of this homomorphism gives the datum for modular curves. The two components of \(X\) identify with the upper and lower half-planes.

## References

- J. S. Milne, [Introduction to Shimura Varieties, §5, Shimura data and the modular example](https://jmilne.org/math/xnotes/svi.pdf).
