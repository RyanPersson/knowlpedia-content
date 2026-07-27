+++
id = "noncommutative-geometry/pre-cstar-algebra"
title = "Pre-C*-algebra"
kind = "definition"
summary = "A possibly incomplete normed involutive algebra satisfying the C*-identity."
aliases = ["pre-C*-algebra", "pre-C-star algebra"]
domains = ["noncommutative-geometry", "operator-algebras", "functional-analysis"]
section_mode = "progressive"
+++

A **pre-\(C^*\)-algebra** is a complex normed [[operator-algebras/involutive-algebra|\(*\)-algebra]] \(A\), not assumed complete, whose norm is submultiplicative and satisfies the \(C^*\)-identity
\[
\lVert a^*a\rVert=\lVert a\rVert^2
\qquad (a\in A).
\]
The involution and multiplication are therefore compatible with the norm, but incompleteness distinguishes \(A\) from a [[operator-algebras/cstar-algebra|\(C^*\)-algebra]]. Unitality is not part of the definition; when \(A\neq0\) has an identity, the \(C^*\)-identity forces that identity to have norm \(1\). Some authors say “pre-\(C^*\)-normed algebra” to emphasize that the displayed identity, rather than completeness, is the decisive condition.

## Completion

The involution is isometric and therefore extends continuously to the Banach-space completion \(\overline A\). Multiplication extends as well, and the \(C^*\)-identity passes to limits, so \(\overline A\) is a \(C^*\)-algebra in which \(A\) is a dense \(*\)-subalgebra. Conversely, every \(*\)-subalgebra of a \(C^*\)-algebra, equipped with the inherited norm, is a pre-\(C^*\)-algebra. These standard completion facts follow from the basic \(C^*\)-norm identities in [Murphy, §2.1](https://doi.org/10.1016/C2009-0-22289-6).

## Examples and non-examples

For a compact [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\), \(C^\infty(M)\) with pointwise operations, complex conjugation, and the [[real-analysis/supremum-norm|supremum norm]] is a pre-\(C^*\)-algebra; its completion is \(C(M)\). It is not a \(C^*\)-algebra unless it is already complete in that norm. By contrast, an arbitrary dense \(*\)-subalgebra carrying a stronger norm need not be pre-\(C^*\): the stronger norm may fail \(\lVert a^*a\rVert=\lVert a\rVert^2\).

## Conventions and scope

**Warning.** “Pre-\(C^*\)-algebra” records only the inherited \(C^*\)-norm structure. It does not imply closure under the [[functional-analysis/holomorphic-functional-calculus-banach-algebra|holomorphic functional calculus]]. Blackadar calls a pre-\(C^*\)-normed algebra satisfying an additional matrix-level spectral-invariance condition a local \(C^*\)-algebra [Blackadar, Chapter II, §3.1](https://doi.org/10.1017/9781009701907.004); that is a strictly richer notion.

## References

1. Gerard J. Murphy, *C*-Algebras and Operator Theory*, Academic Press, 1990. [DOI record](https://doi.org/10.1016/C2009-0-22289-6). Relevant: §2.1 on \(C^*\)-norms and completion.
2. Bruce Blackadar, *K-Theory for Operator Algebras*, 2nd ed., Cambridge University Press, 1998. [Chapter record](https://doi.org/10.1017/9781009701907.004). Relevant: Chapter II, §3.1 on local Banach \(*\)-algebras and pre-\(C^*\)-norms.
