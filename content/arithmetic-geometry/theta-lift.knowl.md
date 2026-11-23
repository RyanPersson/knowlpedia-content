+++
id = "arithmetic-geometry/theta-lift"
title = "Global theta lift"
kind = "construction"
summary = "An integral against a theta kernel that transfers automorphic forms between the two members of a reductive dual pair."
aliases = ["theta lift", "theta lifts"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["langlands/automorphic-form", "algebra-fields-galois/adeles-restricted-product"]
+++

A **global theta lift** turns an [[langlands/automorphic-form|automorphic form]] on one group \(G\) into one on a partner \(H\) by pairing it with a theta kernel \(\Theta(g,h)\). The groups form a reductive dual pair, with the appropriate lifts or splittings for the Weil representation. For a cusp form \(f\), one convention writes the convergent pairing as
\[
\theta(f)(h)=\int_{G(F)\backslash G(\mathbb A_F)}
               \Theta(g,h)\,\overline{f(g)}\,dg .
\]
Here \(F\) is the base number field and \(\mathbb A_F\) its [[algebra-fields-galois/adeles-restricted-product|adeles]]. Integrating out \(g\) leaves a function of \(h\).

## Unitary partners

A Hermitian space and a skew-Hermitian space over a quadratic extension give a unitary dual pair. The lift can vanish. Using a series of nonzero lifts with controlled norms and integral structures is additional work in an [[arithmetic-geometry/iterated-theta-lifts|iterated construction]].

## References

- Wee Teck Gan, [Automorphic forms and the theta correspondence, Lecture 3, §§3.1–3.9](https://swc-math.github.io/aws/2022/2022GanNotes.pdf).
