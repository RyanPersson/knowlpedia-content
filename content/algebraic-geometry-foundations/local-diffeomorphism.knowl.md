+++
id = "algebraic-geometry-foundations/local-diffeomorphism"
title = "Local diffeomorphism"
kind = "knowl"
summary = "A smooth map that restricts near every point to a diffeomorphism onto an open neighborhood."
aliases = ["local diffeomorphism", "locally diffeomorphic map"]
domains = ["algebraic-geometry-foundations"]
+++

A **local diffeomorphism** is a smooth map $f:M\to N$ between smooth manifolds such that every $x\in M$ has an open neighborhood $U$ for which $f(U)$ is open in $N$ and

$$
f|_U:U\longrightarrow f(U)
$$

is a diffeomorphism. Equivalently, $f$ has a smooth local inverse around every point of its source.

## Examples

The map $\mathbb R\to S^1$, $t\mapsto e^{it}$, is a local diffeomorphism even though it is not globally one-to-one.

## Characterization

The inverse function theorem says that a smooth map between manifolds of equal dimension is a local diffeomorphism exactly when its derivative is invertible at every point.

## Analogy with algebraic geometry

An [[algebraic-geometry-foundations/etale-morphism|étale morphism]] is often called the algebraic-geometric analogue of a local diffeomorphism: both notions say that the map has no infinitesimal branching and looks locally like an isomorphism. The analogy is structural, not an identification of schemes with smooth manifolds.
