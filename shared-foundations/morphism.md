---
title: "Morphism"
description: "A structure-preserving map between objects of the same type"
---

A **morphism** is a map between two mathematical structures of the same kind that preserves the defining operations or relations of that structure.

The precise definition depends on context:
- Between {{< knowl id="group" section="algebra-groups" text="groups" >}}: a {{< knowl id="group-homomorphism" section="algebra-groups" text="group homomorphism" >}} preserves the group operation.
- Between {{< knowl id="ring" section="algebra-rings" text="rings" >}}: a {{< knowl id="ring-homomorphism" section="algebra-rings" text="ring homomorphism" >}} preserves addition and multiplication.
- Between {{< knowl id="vector-space" section="linear-algebra" text="vector spaces" >}}: a {{< knowl id="linear-map" section="linear-algebra" text="linear map" >}} preserves addition and scalar multiplication.
- Between topological spaces: a {{< knowl id="continuity-on-a-set" section="analysis" text="continuous map" >}} preserves the property of being open (via preimages).
- Between smooth manifolds: a {{< knowl id="smooth-map" section="fiber-bundles" text="smooth map" >}} preserves differentiable structure.

This pattern—objects plus structure-preserving maps—is formalized in {{< knowl id="category" section="algebra-category-theory" text="category theory" >}}, where morphisms are the arrows between objects satisfying composition and identity axioms.

An **isomorphism** is a morphism with a two-sided inverse that is also a morphism; isomorphic structures are "the same" from the perspective of their defining properties.
