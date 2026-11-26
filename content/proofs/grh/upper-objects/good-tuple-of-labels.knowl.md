+++
id = "proofs/grh/upper-objects/good-tuple-of-labels"
title = "Allowed polynomial and good tuple of labels"
kind = "definition"
summary = "A label is allowed if none of its roots in the base field is an M-th root of unity; a tuple of labels over finite fields is good if all are allowed and at least one is primitive."
aliases = ["allowed polynomial", "good tuple", "good tuples of labels"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsAllowedPolynomial", "New.goodTuples", "New.mem_goodTuples"]
lean_files = ["src/New/UpperBound/Objects/LabelsAndIndexTypes.lean"]
+++

Let \(M,r\ge0\) be integers.

**Definition.** Let \(k\) be a field. A polynomial \(c\in k[X]\) is **allowed** (for \(M\) and \(r\)) if it is a [[?lean:New.IsLabel|label]] of degree \(r\) (monic, squarefree, of degree \(r\), \(c(0)\neq0\)) and \(c(x)\ne0\) for every \(x\in k\) with \(x^M=1\).

Let \((k_w)_{w\in\iota}\) be a finite family of [[algebra-fields-galois/finite-field|finite fields]]. A tuple \((c_w)_{w\in\iota}\), \(c_w\in k_w[X]\), is a **good tuple** (for \(M\) and \(r\)) if every \(c_w\) is allowed for \(M\) and \(r\), and at least one \(c_w\) is a [[proofs/grh/upper-objects/primitive-polynomial|primitive polynomial]] of degree \(r\).

The set of good tuples is finite.

## References

1. Lean: `New.IsAllowedPolynomial`, `New.goodTuples` in `src/New/UpperBound/Objects/LabelsAndIndexTypes.lean`.
