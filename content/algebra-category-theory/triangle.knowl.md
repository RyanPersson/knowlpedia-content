+++
id = "algebra-category-theory/triangle"
title = "Triangle in a shifted category"
kind = "knowl"
summary = "A cyclic diagram of three objects whose last morphism lands in the shift of the first."
aliases = ["triangle in a category", "triangle"]
domains = ["algebra-category-theory", "algebra-homological"]
+++

In a category with a [[algebra-category-theory/shift-functor|shift functor]] \([1]\), a **triangle** is a diagram
\[
X\xrightarrow{f}Y\xrightarrow{g}Z\xrightarrow{h}X[1].
\]
A morphism of triangles is a triple of morphisms between corresponding objects that makes all three resulting squares commute, including the square involving the shifted first object.

Rotating the triangle moves \(Y\) to the first position and produces \(Y\to Z\to X[1]\to Y[1]\), with a convention-dependent minus sign on the final map. A chosen subclass may be declared [[algebra-category-theory/distinguished-triangle|distinguished]].
