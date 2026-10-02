+++
id = "catalog/arithmetic/f5-rational-functions"
title = "Rational-function field F_5(t)"
kind = "definition"
summary = "Rational-function field F_5(t) with its specified scalar field, operations, and categorical structure."
aliases = []
domains = ["catalog", "algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-rings/fraction-field", "catalog/arithmetic/f5-polynomials"]
dependency_heuristic = "catalog-definition-core-reviewed-v1"
dependency_review_count = 0
+++

The **rational-function field \(\mathbb F_5(t)\)** is the [[algebra-rings/fraction-field|fraction field]] of the [[catalog/arithmetic/f5-polynomials|polynomial ring \(\mathbb F_5[t]\)]]. An element is a quotient \(a(t)/b(t)\), with \(a,b\in\mathbb F_5[t]\) and \(b\ne0\); two fractions agree when cross multiplication gives the same polynomial.

## Global and local roles

This is a [[algebra-fields-galois/global-function-field|global function field]]. Its places include those attached to monic [[algebra-rings/irreducible-polynomial|irreducible polynomials]] and the place at infinity. Completing at \((t)\) gives [[catalog/arithmetic/f5-laurent|\(\mathbb F_5((t))\)]], which is a different field.

## Scalar conventions

The constants embed as \(\mathbb F_5\). A homomorphism over the constant field fixes these constants, while an abstract field map need not fix each of them when \(q\) is not prime. No topology is part of this bare global-field record.
