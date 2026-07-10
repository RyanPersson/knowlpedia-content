+++
id = "algebra-category-theory/terminal-object"
title = "Terminal object"
kind = "definition"
summary = "An object receiving a unique morphism from every object of a category."
aliases = ["terminal object", "final object"]
domains = ["algebra-category-theory"]
+++

Let \(\mathcal C\) be a [[algebra-category-theory/category|category]]. A **terminal object** is an [[algebra-category-theory/object|object]] \(1\) such that for every object \(X\) there is exactly one [[algebra-category-theory/morphism|morphism]]

\[
X\longrightarrow 1.
\]

Any two terminal objects are uniquely isomorphic, so notation such as \(1\) refers to a choice that is immaterial up to unique isomorphism.

For example, a one-point set is terminal among sets, and a one-point space is terminal among topological spaces. In a category of objects over a fixed base \(S\), the identity \(S\to S\) is terminal. Consequently, on a site with terminal object \(1\), a covering family \(\{U_i\to 1\}\) expresses a global object as being covered by local pieces.

**Warning.** Terminal does not mean that there is a unique morphism *from* \(1\) to every object. Reversing the arrows gives the distinct notion of an initial object.
