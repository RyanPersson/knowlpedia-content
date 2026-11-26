+++
id = "proofs/grh/upper-objects/primitive-polynomial"
title = "Primitive polynomial (primitive label)"
kind = "definition"
summary = "An irreducible label of degree r over a finite field one of whose roots generates the multiplicative group of the extension of degree r."
aliases = ["primitive label", "primitive polynomial over a finite field"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.IsPrimitivePolynomial", "New.IsPrimitivePolynomial.two_le_card_pow"]
lean_files = ["src/New/UpperBound/Objects/LabelsAndIndexTypes.lean"]
+++

Let \(k\) be a [[algebra-fields-galois/finite-field|finite field]] with \(q\) elements, \(\bar k\) an [[?c:algebraic closure|algebraic closure]], and \(r\ge0\) an integer. Recall that a [[?lean:New.IsLabel|label]] of degree \(r\) over \(k\) is a monic squarefree polynomial \(c\in k[X]\) of degree \(r\) with \(c(0)\ne0\).

**Definition.** A polynomial \(c\in k[X]\) is a **primitive polynomial of degree \(r\)** if

1. \(c\) is a label of degree \(r\),
2. \(c\) is [[?c:irreducible polynomial|irreducible]], and
3. \(c\) has a root \(\xi\in\bar k\) that is a [[?c:primitive root of unity|primitive root of unity]] of order \(q^r-1\); equivalently, \(\xi\) generates the cyclic group \(\mathbb F_{q^r}^\times\).

## Remarks

This is the usual notion of a primitive polynomial over a finite field. If a primitive polynomial of degree \(r\) exists then \(q^r\ge2\), i.e. \(r\ge1\).

## References

1. Lean: `New.IsPrimitivePolynomial` in `src/New/UpperBound/Objects/LabelsAndIndexTypes.lean`.
