+++
id = "arithmetic-geometry/cm-point"
title = "CM point on a Shimura variety"
kind = "definition"
summary = "A special point whose Hodge structure has a torus as its Mumford–Tate group."
aliases = ["special point", "CM points"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/shimura-variety", "algebraic-geometry-foundations/maximal-torus-weight-lattice", "arithmetic-geometry/complex-multiplication"]
+++

A **CM point** (or **special point**) of a [[arithmetic-geometry/shimura-variety|Shimura variety]] is represented by a Hodge homomorphism that factors through an [[algebraic-geometry-foundations/maximal-torus-weight-lattice|algebraic torus]] defined over \(\mathbb Q\). Equivalently, its Mumford–Tate group, the smallest rational algebraic group through which that homomorphism factors, is a torus. On a moduli space of polarized [[arithmetic-geometry/abelian-variety|abelian varieties]] such a point represents an abelian variety with [[arithmetic-geometry/complex-multiplication|complex multiplication]].

## An example on the modular curve

The point represented by \(i\) in the upper half-plane corresponds to \(\mathbb C/(\mathbb Z+i\mathbb Z)\), with [[arithmetic-geometry/complex-multiplication|multiplication by \(i\)]]. Multiplication by \(i\) preserves the lattice because it sends its basis \(1,i\) to \(i,-1\). The resulting endomorphisms contain \(\mathbb Z[i]\), an order in the imaginary quadratic field \(\mathbb Q(i)\).

## References

- J. S. Milne, [Introduction to Shimura Varieties, §§11–12, complex multiplication and special points](https://jmilne.org/math/xnotes/svi.pdf).
- J. S. Milne, [Complex Multiplication, §3, classification up to isogeny](https://www.jmilne.org/math/CourseNotes/CM.pdf).
