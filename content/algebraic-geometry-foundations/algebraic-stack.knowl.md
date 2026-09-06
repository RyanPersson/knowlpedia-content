+++
id = "algebraic-geometry-foundations/algebraic-stack"
title = "Algebraic stack"
kind = "definition"
summary = "A stack in groupoids with a representable diagonal and a smooth surjective atlas by a scheme."
aliases = ["Artin stack"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/algebraic-space", "algebra-groups/automorphism-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(S\) be a scheme. An **algebraic stack** (or **Artin stack**) over \(S\)
is a stack in groupoids on the big fppf site of \(S\) such that:

1. its diagonal is representable by
   [[algebraic-geometry-foundations/algebraic-space|algebraic spaces]]; and
2. there is a scheme \(U\) and a representable, smooth, surjective morphism
   \(U\to\mathcal X\).

The morphism \(U\to\mathcal X\) is a **smooth atlas**. Some conventions impose
additional separation or finiteness conditions, which must be stated
separately.

Unlike a coarse moduli space, a stack retains the [[algebra-groups/automorphism-group|automorphism group]] of every
object. This is essential for
[[algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve|\(\operatorname{Bun}_G\)]],
because a principal bundle can have nontrivial automorphisms.

## Quotient example

If an algebraic group \(G\) acts on a scheme \(U\), the quotient stack
\([U/G]\) remembers stabilizers as isotropy groups. Even when an ordinary
geometric quotient exists, it generally forgets this information.

## Derived warning

Modern geometric Langlands often replaces ordinary algebraic stacks by
[[algebraic-geometry-foundations/derived-algebraic-stack|derived algebraic
stacks]], whose structure sheaves retain homotopical information. That is an
additional structure, not part of the definition above.

## References

1. Michael Artin, “Versal deformations and algebraic stacks,” *Inventiones
   Mathematicae* 27 (1974), 165–189.
   [DOI](https://doi.org/10.1007/BF01390174).
2. Gérard Laumon and Laurent Moret-Bailly, *Champs algébriques*, Springer,
   2000. [DOI](https://doi.org/10.1007/978-3-540-24899-6).
