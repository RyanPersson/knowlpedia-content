+++
id = "lie-groups/ck-vector-unitary-representation"
title = "Differentiable vector of order k"
kind = "definition"
summary = "A vector whose orbit map has k continuous Hilbert-norm derivatives."
aliases = ["C^k vector", "differentiable vector", "C1 vector"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/strongly-continuous-unitary-representation", "fiber-bundles/lie-group", "fiber-bundles/orbit-map", "real-analysis/frechet-derivative"]
+++

Let \(\pi\) be a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of a finite-dimensional [[fiber-bundles/lie-group|Lie group]] \(G\) on \(H\), and let \(k\geq0\) be an integer. A vector \(v\in H\) is a **\(C^k\) vector** if its [[fiber-bundles/orbit-map|orbit map]]
\[
g\longmapsto\pi(g)v
\]
is \(C^k\): in local coordinates its [[real-analysis/frechet-derivative|norm derivatives]] through order \(k\) exist and are continuous. Write \(H^k\) for this subspace. A \(C^1\) vector is also called a **differentiable vector**.

## All orders versus one order

Strong continuity gives \(H^0=H\), and
\[
H\supseteq H^1\supseteq H^2\supseteq\cdots,
\qquad H^\infty=\bigcap_{k\geq0}H^k.
\]
The last space consists of [[lie-groups/smooth-vector-unitary-representation|smooth vectors]]. Differentiability once must not be used as a synonym for smoothness at all orders.

## Generator interpretation

For a finite-dimensional Lie group, membership in \(H^k\) is equivalent to existence of every ordered composition of at most \(k\) infinitesimal generators on the vector. The [[lie-groups/smooth-vectors-iterated-generator-domains|iterated-domain theorem]] makes these domain requirements precise. For the [[lie-groups/modulation-unitary-group|modulation group]], \(H^k=\{f\in L^2(\mathbb R):x^k f\in L^2(\mathbb R)\}\).

## References

1. Karl-Hermann Neeb, [*On Differentiable Vectors for Representations of Infinite Dimensional Lie Groups*](https://arxiv.org/abs/1002.1602). Definition 3.1(b) and Theorem 9.4.
