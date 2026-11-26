+++
id = "algebra-fields-galois/algebraic-independence"
title = "Algebraic independence"
kind = "definition"
summary = "A family satisfies no nonzero polynomial relation over its base field."
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebra-fields-galois/field-extension","algebra-rings/polynomial-ring","algebra-fields-galois/transcendental-element"]
+++

A family \((t_i)_{i\in I}\) in a [[algebra-fields-galois/field-extension|field extension]] \(L/K\) is **algebraically independent over \(K\)** if, for all distinct \(i_1,\ldots,i_n\) and every [[algebra-rings/polynomial-ring|polynomial]] \(P\in K[X_1,\ldots,X_n]\), the equality \(P(t_{i_1},\ldots,t_{i_n})=0\) implies \(P=0\).

## One element

A singleton is algebraically independent exactly when its element is [[algebra-fields-galois/transcendental-element|transcendental]] over \(K\).
