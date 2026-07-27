+++
id = "fiber-bundles/tfae-triviality-of-a-principal-g-bundle-principal-g-bundle-pm"
title = "Equivalent conditions for triviality of a principal bundle"
kind = "knowl"
summary = "A principal bundle is trivial exactly when it admits a global section."
aliases = ["tfae-triviality-of-a-principal-g-bundle-principal-g-bundle-pm", "Equivalent conditions for triviality of a principal bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/tfae-triviality-of-a-principal-g-bundle-principal-g-bundle-pm.md"
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]]. Then \(P\) is trivial if and only if it admits a smooth global section.

## Equivalent conditions

The following are equivalent:

1. (**Bundle isomorphism with the product**)
   \(P\) is trivial: there is a [[fiber-bundles/principal-bundle-isomorphism|principal bundle isomorphism]]
   \[
   \Phi:P \stackrel{\cong}{\longrightarrow} M\times G
   \]
   over \(M\) that intertwines the right \(G\)-actions.

2. (**Existence of a global section**)
   \(P\) admits a smooth global section \(s:M\to P\) with \(\pi\circ s=\operatorname{id}_M\).

3. (**Transition functions can be made trivial**)
   The [[fiber-bundles/principal-bundle-transition-function|transition functions]] can be chosen to be the identity on every overlap; equivalently, the transition cocycle is [[fiber-bundles/equivalence-of-cocycles|equivalent to the trivial cocycle]].

4. (**A global equivariant trivialization map**)
   There is a smooth map \(f:P\to G\) such that
   \[
   f(pg)=g^{-1}f(p)\qquad\text{for all }p\in P,\ g\in G.
   \]
   Thus \(f\) is equivariant for the right action on \(P\) and the left \(G\)-action on itself given by \(g\cdot h=g^{-1}h\).

The equivalence of (1) and (2) is explicit: a section \(s\) defines the trivialization \((x,g)\mapsto s(x)g\).

## Examples
1. **Hopf bundle is not trivial.**
   The Hopf fibration \(S^3\to S^2\) is a nontrivial principal \(U(1)\)-bundle. By the theorem, it admits no global section.

2. **Triviality from a global gauge choice on a trivial bundle.**
   On \(P=M\times G\), the map \(s(x)=(x,e)\) is a global section. Choosing a section is a global gauge choice, and it identifies principal connections with \(\mathfrak g\)-valued \(1\)-forms on \(M\).

3. **Principal bundles over the circle for connected groups.**
   If \(G\) is connected, every principal \(G\)-bundle over \(S^1\) is trivial, hence admits a global section.
