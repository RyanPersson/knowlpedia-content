+++
id = "ergodic-theory/product-system"
title = "Product of probability-preserving systems"
kind = "definition"
summary = "Coordinatewise dynamics on the product probability space."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system", "measure-theory/product-measure", "measure-theory/product-sigma-algebra"]
+++

The **product system** of two [[ergodic-theory/measure-preserving-system|probability-preserving systems]] \((X,\Sigma,\mu,T)\) and \((Y,\mathcal T,\nu,S)\) is
\[
(X\times Y,\Sigma\otimes\mathcal T,\mu\otimes\nu,T\times S),
\qquad(T\times S)(x,y)=(Tx,Sy).
\]
One may complete the product measure. For group actions, the diagonal action uses the same \(g\) on both coordinates.

## Ergodicity of products

Two ergodic systems can have a nonergodic product: equal irrational rotations fix the difference of the two circle coordinates. The condition that \(T\times T\) be ergodic is exactly [[ergodic-theory/weak-mixing|weak mixing]].
