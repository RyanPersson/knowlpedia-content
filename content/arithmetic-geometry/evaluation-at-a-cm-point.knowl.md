+++
id = "arithmetic-geometry/evaluation-at-a-cm-point"
title = "Evaluation of an automorphic form at a CM point"
kind = "construction"
summary = "Evaluating a section produces a vector in the fiber at the special point, with an integral lattice when the data extend integrally."
aliases = ["CM evaluation", "values at CM points"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/cm-point", "arithmetic-geometry/integral-automorphic-form"]
+++

If a geometric automorphic form \(s\) is a section of a bundle \(\mathcal V\), its **evaluation at a CM point** \(P\) is \(s(P)\in\mathcal V_P\), the fiber at that point. To regard a line-valued evaluation as a number one chooses a basis. An [[arithmetic-geometry/integral-automorphic-form|integral form]] and an integral extension of \(P\) supply a lattice in the fiber on which divisibility has a meaning.

## Changing a basis

Suppose \(s(P)=a e\) in a free rank-one lattice over \(\mathbb Z_p\). Replacing \(e\) by another integral basis multiplies \(a\) by a unit, so its [[shared-foundations/p-adic-valuation|valuation]] is unchanged. Belonging to \(p^r\mathcal V_P\) is an extra condition on the evaluation. Integrality by itself gives only \(r\ge0\) for a nonzero value.
