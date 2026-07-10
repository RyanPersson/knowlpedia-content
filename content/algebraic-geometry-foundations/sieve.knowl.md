+++
id = "algebraic-geometry-foundations/sieve"
title = "Sieve on an object"
kind = "knowl"
summary = "A collection of morphisms into one object that is closed under precomposition."
aliases = ["sieve", "sieves", "sieve on an object"]
domains = ["algebraic-geometry-foundations"]
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]] and let \(U\) be an object of \(\mathcal C\). A **sieve on \(U\)** is a collection \(S\) of [[algebra-category-theory/morphism|morphisms]] with codomain \(U\) that is closed under precomposition: if \(f:V\to U\) belongs to \(S\) and \(g:W\to V\) is any morphism, then

\[
f\circ g:W\longrightarrow U
\]

also belongs to \(S\).

The **maximal sieve** on \(U\) contains every morphism into \(U\). A family \(\{f_i:U_i\to U\}\) generates the smallest sieve containing all the \(f_i\); it consists of the morphisms into \(U\) that factor through at least one \(f_i\).

If \(f:V\to U\) is a morphism, the **pullback sieve** \(f^*S\) on \(V\) consists of the morphisms \(g:W\to V\) for which \(f\circ g\) belongs to \(S\):
\[
f^*S=\{g:W\to V\mid f\circ g\in S\}.
\]

A [[algebraic-geometry-foundations/grothendieck-topology|Grothendieck topology]] specifies which sieves count as covering. Equivalently, a [[algebraic-geometry-foundations/covering-family|covering family]] is one whose generated sieve is covering.
