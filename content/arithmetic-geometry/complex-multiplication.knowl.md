+++
id = "arithmetic-geometry/complex-multiplication"
title = "Complex multiplication of an elliptic curve"
kind = "definition"
summary = "The geometric endomorphism ring of a characteristic-zero elliptic curve contains an order in an imaginary quadratic field."
aliases = ["CM", "elliptic curve with CM"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/elliptic-curve", "algebra-fields-galois/imaginary-quadratic-field"]
+++

An [[algebraic-geometry-foundations/elliptic-curve|elliptic curve]] \(E\) in characteristic zero has **complex multiplication** (CM) by an [[algebra-fields-galois/imaginary-quadratic-field|imaginary quadratic field]] \(K\) when its geometric endomorphism algebra \(\operatorname{End}_{\bar k}(E)\otimes_{\mathbb Z}\mathbb Q\) is isomorphic to \(K\). The endomorphism ring itself is an order in \(K\), a subring of finite index in its ring of integers.

## An extra symmetry

For \(E=\mathbb C/(\mathbb Z+i\mathbb Z)\), multiplication by \(i\) preserves the lattice. It descends to an endomorphism of \(E\), and \(\operatorname{End}(E)=\mathbb Z[i]\). The generalization to an abelian variety of dimension \(g\) uses a commutative semisimple subalgebra of rational endomorphisms of dimension \(2g\).

## References

- J. S. Milne, [Complex Multiplication, introduction and §§2–3](https://www.jmilne.org/math/CourseNotes/CM.pdf).
