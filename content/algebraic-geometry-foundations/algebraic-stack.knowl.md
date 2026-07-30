+++
id = "algebraic-geometry-foundations/algebraic-stack"
title = "Algebraic stack"
kind = "definition"
summary = "A stack in groupoids with a representable diagonal and a smooth surjective atlas by a scheme."
aliases = ["Artin stack"]
domains = ["algebraic-geometry-foundations"]
section_mode = "progressive"
+++

An **algebraic stack** (or **Artin stack**) is a stack in groupoids on a
Grothendieck site whose diagonal is representable by algebraic spaces and
which admits a smooth surjective atlas \(U\to\mathcal X\) from a scheme \(U\).
The precise finiteness and topology conventions vary, so they should be stated
in applications.

Unlike a coarse moduli space, a stack retains the automorphism group of every
object. This is essential for
[[algebraic-geometry-foundations/moduli-stack-of-g-bundles-on-a-curve|\(\operatorname{Bun}_G\)]],
because a principal bundle can have nontrivial automorphisms.

## Quotient example

If an algebraic group \(G\) acts on a scheme \(U\), the quotient stack
\([U/G]\) remembers stabilizers as isotropy groups. Even when an ordinary
geometric quotient exists, it generally forgets this information.

## Derived warning

Modern geometric Langlands uses derived algebraic stacks. Their structure
sheaves carry homotopical information beyond an ordinary Artin stack. The
ordinary definition here is an entry point, not a replacement for that
derived enhancement.

## References

1. Michael Artin, “Versal deformations and algebraic stacks,” *Inventiones
   Mathematicae* 27 (1974), 165–189.
   [DOI](https://doi.org/10.1007/BF01390174).
2. Gérard Laumon and Laurent Moret-Bailly, *Champs algébriques*, Springer,
   2000. [DOI](https://doi.org/10.1007/978-3-540-24899-6).
