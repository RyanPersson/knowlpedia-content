+++
id = "algebraic-geometry-foundations/constant-finite-group-scheme"
title = "Constant finite group scheme"
kind = "definition"
summary = "The group scheme obtained by placing one copy of the base scheme at each element of a finite group."
aliases = ["constant finite group scheme", "constant group scheme"]
domains = ["algebraic-geometry-foundations"]
+++

To let the abstract Galois group \(G=\operatorname{Gal}(K/F)\) act on \(\operatorname{Spec}K\) over \(\operatorname{Spec}F\), regard \(G\) as a [[algebraic-geometry-foundations/scheme|scheme]]: put one copy of the base at every group element, with multiplication dictated by the multiplication table of \(G\).

Let \(G\) be a finite [[algebra-groups/group|group]] and \(S\) a [[algebraic-geometry-foundations/scheme|scheme]]. The **constant finite [[algebraic-geometry-foundations/group-scheme|group scheme]]** \(G_S\) is

\[
G_S:=\coprod_{g\in G}S,
\]

with multiplication, identity, and inverse induced by those of \(G\). If \(S=\operatorname{Spec}R\), then

\[
G_S\cong\operatorname{Spec}\!\left(\prod_{g\in G}R\right).
\]

It is finite étale over \(S\), and its \(T\)-points are the locally constant maps from \(T\) to the finite set \(G\). It supplies the group scheme in the [[algebraic-geometry-foundations/galois-extension-as-etale-torsor|Galois extension as étale torsor]] construction.

**Warning.** A constant group scheme is not the same as every finite group scheme with the same number of geometric points. For example, in characteristic \(p\), the group scheme \(\mu_p\) can be nonreduced and non-étale, whereas the constant scheme attached to \(\mathbb Z/p\mathbb Z\) remains a disjoint union of \(p\) copies of the base.
