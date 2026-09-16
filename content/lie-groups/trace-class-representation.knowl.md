+++
id = "lie-groups/trace-class-representation"
title = "Trace-class unitary representation"
kind = "definition"
summary = "A unitary Lie-group representation whose smooth compactly supported averages are trace-class operators."
aliases = ["trace class representation"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/strongly-continuous-unitary-representation", "fiber-bundles/lie-group", "harmonic-analysis/integrated-form-unitary-representation", "functional-analysis/trace-class-operator"]
+++

A [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] \(\pi\) of a finite-dimensional [[fiber-bundles/lie-group|Lie group]] \(G\) on \(H\) is **trace class** if every [[harmonic-analysis/integrated-form-unitary-representation|integrated operator]]
\[
\pi(f)=\int_G f(g)\pi(g)\,dg,
\qquad f\in C_c^\infty(G),
\]
is a [[functional-analysis/trace-class-operator|trace-class operator]]. The integral uses a fixed left Haar measure.

## What is required to have finite trace

The condition concerns the averages \(\pi(f)\). In an infinite-dimensional representation the individual unitaries \(\pi(g)\) are not trace class: their absolute values equal the identity. Smooth averaging can nevertheless produce summable singular values.

## Examples and a nonexample

Every finite-dimensional unitary representation is trace class. An infinite-dimensional trivial representation is not: choosing \(f\) of integral one gives \(\pi(f)=I\). Thus a condition on the group alone does not force every one of its unitary representations to be trace class.

For finite-dimensional Lie groups, trace class is equivalent to [[lie-groups/nuclear-smooth-vectors-trace-class|nuclearity of the smooth-vector space]].

## References

1. Gerrit van Dijk, Karl-Hermann Neeb, Hadi Salmasian, and Christoph Zellner, [*On the characterization of trace class representations and Schwartz operators*](https://arxiv.org/abs/1512.02451). §1, definition before Lemma 1.1 and Theorem 1.3.
