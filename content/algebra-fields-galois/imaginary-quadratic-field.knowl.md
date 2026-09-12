+++
id = "algebra-fields-galois/imaginary-quadratic-field"
title = "Imaginary quadratic field"
kind = "definition"
summary = "A degree-two number field with no real embedding."
aliases = ["quadratic imaginary field"]
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/number-field", "algebra-fields-galois/field-embedding", "shared-foundations/square-free-integer"]
+++

An **imaginary quadratic field** is a [[algebra-fields-galois/number-field|number field]] of degree two over \(\mathbb Q\) with no [[algebra-fields-galois/field-embedding|embedding]] into \(\mathbb R\). It has the form
\[
K=\mathbb Q(\sqrt{-d}),\qquad d>0\text{ square-free}.
\]
Here [[shared-foundations/square-free-integer|square-free]] fixes a unique positive integer parameter for the isomorphism class.

## Elements and embeddings

Each element is uniquely \(a+b\sqrt{-d}\), with \(a,b\in\mathbb Q\). Its two complex embeddings send \(\sqrt{-d}\) to \(i\sqrt d\) and \(-i\sqrt d\); they are exchanged by complex conjugation.

## Example

For \(d=1\), the field is \(\mathbb Q(i)\). Its ring of integers is a smaller subset than the field: denominators are generally not allowed.

## References

1. J. S. Milne, *Algebraic Number Theory*, v3.08. [Author’s text](https://www.jmilne.org/math/CourseNotes/ANTc.pdf), Introduction, quadratic-field examples.
