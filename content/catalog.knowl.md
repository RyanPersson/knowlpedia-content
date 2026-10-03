+++
id = "catalog"
title = "Mathematical object catalogue"
kind = "index"
summary = "Objects, category-dependent morphisms, low-dimensional relationships, and the compact magic square."
aliases = []
domains = ["catalog"]
section_mode = "continuous"
prerequisites = []
generated_by = "scripts/generate_catalog_indexes.py"
+++

This catalogue contains **659 separately identified objects and parameterized families**, **42 category conventions**, **689 recorded relationships**, and **175 Hom/End/Aut records**. Real and complex versions, split and compact forms, and the requested small sizes are explicit entries. A family entry states its parameter restrictions; it does not silently treat every parameter value as the same object.

[Open the category explorer](/catalog/explorer/) · [[catalog/created-knowls|List of newly created knowls]] · [Explore the finite-group table](/catalog/finite-groups/table/) · [Explore the Lie-group table](/catalog/lie-groups/table/)

## Long lists of objects

- [[catalog/lie-groups-index|Lie groups catalogue]] — 180 entries.
- [[catalog/lie-algebras-index|Lie algebras catalogue]] — 152 entries.
- [[catalog/algebras-index|Scalar, associative, and Jordan algebras catalogue]] — 109 entries.
- [[catalog/arithmetic-index|Fields, local objects, and orders catalogue]] — 69 entries.
- [[catalog/magic-square-index|Magic-square outputs and triality representations catalogue]] — 5 entries.
- [[catalog/finite-sporadic-index|Sporadic finite simple groups catalogue]] — 26 entries.
- [[catalog/finite-lie-type-index|Finite groups of Lie type catalogue]] — 68 entries.
- [[catalog/finite-elementary-index|Elementary finite groups and families catalogue]] — 50 entries.

## How to compare objects

[[catalog/morphisms/hom-end-aut-by-category|Hom, End, and Aut depend on the chosen category]]. Select two objects in the explorer, choose a shared category, then inspect the recorded maps. End and Aut use a single object with a specified structure. A missing entry means **not catalogued**, not that its Hom-set is empty. Complete and partial descriptions are labeled separately.

A matrix Lie group such as \(SL(2,\mathbb C)\) is not itself a vector space. Use smooth or holomorphic group maps for that object, and real-linear or complex-linear maps for its Lie algebra or a specified ambient vector space. Changing the algebra product is a construction, not merely a change of scalar field.

## Worked comparisons

- [[catalog/morphisms/jordan-unit-conventions|Jord, UJord, and Jord1: units change Hom and End]].
- [[catalog/morphisms/jordan-maps-from-the-scalar-algebra|Jordan maps from the scalar algebra are idempotents]].
- [[catalog/morphisms/complex-numbers-linear-versus-algebra-maps|The complex numbers as a real or complex vector space and algebra]].
- [[catalog/morphisms/linear-endomorphisms-of-sl2-complex|Real and complex linear endomorphisms of sl(2,C)]].
- [[catalog/morphisms/sl2-complex-real-versus-holomorphic-maps|Real versus holomorphic maps on SL(2,C)]].
- [[catalog/morphisms/restriction-of-scalars-endomorphisms|K-linear, F-linear, K-algebra, and F-algebra endomorphisms]].
- [[catalog/morphisms/gaussian-field-endomorphisms|Q(i): linear maps versus algebra maps]].
- [[catalog/morphisms/finite-field-homomorphisms-by-category|Empty field Hom-sets versus the zero ring map]].
- [[catalog/arithmetic/finite-field-linear-and-field-maps|Finite-field linear maps versus Frobenius automorphisms]].

## Low dimensions and the magic square

The [[catalog/relationships/compact-freudenthal-magic-square|compact real Freudenthal magic square]] is backed by all 16 data cells, with both input algebras and each output Lie algebra identified. Changing a composition algebra to a split form requires a new real-form calculation; the compact table is not presented as a table of all real forms.

The low-dimensional entries retain their own identities even when isomorphic. This records, for example, the distinctions between Spin groups and their orthogonal quotients, between one-dimensional Hermitian constructions, and between the three Spin(8) representations related by triality.

## Category conventions

- [[catalog/categories/abelian-groups|Category of abelian groups]] — Abelian groups.
- [[catalog/categories/associative-algebras|Category of associative algebras with arbitrary homomorphisms]] — R-associative algebras; arbitrary maps; C-associative algebras; arbitrary maps; Q-associative algebras; arbitrary maps; F-associative algebras; arbitrary maps; K-associative algebras; arbitrary maps.
- [[catalog/categories/complex-lie-groups|Category of complex Lie groups]] — C Lie groups.
- [[catalog/categories/fields|Category of fields]] — Fields.
- [[catalog/categories/finite-groups|Category of finite groups]] — Finite groups.
- [[catalog/categories/finite-simple-groups|Category of finite simple groups]] — Finite simple groups.
- [[catalog/categories/groups|Category of groups]] — Groups.
- [[catalog/categories/jordan-algebras|Category Jord of Jordan algebras]] — Jord over R; Jord over C.
- [[catalog/categories/lie-algebras|Category of Lie algebras over a field]] — R-Lie algebras; C-Lie algebras.
- [[catalog/categories/nonassociative-algebras|Category of nonassociative algebras]] — R-algebras; no associativity requirement; C-algebras; no associativity requirement.
- [[catalog/categories/real-lie-groups|Category of real Lie groups]] — R Lie groups.
- [[catalog/categories/rings|Category of rings with arbitrary ring homomorphisms]] — Rings; units not required.
- [[catalog/categories/sets|Category of sets]] — Sets.
- [[catalog/categories/spin8-representations|Category of real Spin(8) representations]] — Real Spin(8) representations.
- [[catalog/categories/topological-fields|Category of topological fields]] — Hausdorff topological fields.
- [[catalog/categories/topological-groups|Category of topological groups]] — Hausdorff topological groups.
- [[catalog/categories/topological-rings|Category of unital topological rings]] — Unital Hausdorff topological rings.
- [[catalog/categories/unital-associative-algebras|Category of unital associative algebras]] — R-unital associative algebras; C-unital associative algebras; Q-unital associative algebras; F-unital associative algebras; K-unital associative algebras.
- [[catalog/categories/unital-jordan-algebras-arbitrary-maps|Category UJord of unital Jordan algebras with arbitrary maps]] — UJord over R; UJord over C.
- [[catalog/categories/unital-jordan-algebras-unital-maps|Category Jord1 of unital Jordan algebras and unital maps]] — Jord1 over R; Jord1 over C.
- [[catalog/categories/unital-rings|Category of unital rings]] — Unital rings.
- [[catalog/categories/vector-spaces|Category of vector spaces over a field]] — R-vector spaces; C-vector spaces; Q-vector spaces; F-vector spaces; K-vector spaces; F_2-vector spaces; F_3-vector spaces; F_p-vector spaces.

## Data and proof status

Each recorded relationship names its category or identifies itself as a construction, states its conditions, and carries evidence. The catalogue does not infer arbitrary compositions or inverses. The present evidence is mathematical exposition and checked literature, **not Lean proofs**. Formal-proof references are reserved for future verified declarations.

[Download the indexed JSON](/indexes/catalog.json) · [Download the SQLite catalogue](/indexes/catalog.sqlite)

## Separate algebra-class additions

The [[knowlification/orders-and-fractional-ideals-index|orders and fractional ideals reading list]] covers the separate transcript request, including new definitions and existing prerequisites reused.
