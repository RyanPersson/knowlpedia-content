+++
id = "catalog/finite-groups"
title = "A table of finite groups"
kind = "index"
summary = "Explore finite simple families, sporadic groups, and familiar finite-group constructions in complementary layouts."
aliases = ["finite group periodic table"]
domains = ["catalog", "algebra-groups"]
section_mode = "continuous"
prerequisites = []
dependency_heuristic = "finite-groups-semantic-review-v1"
dependency_review_count = 1
+++

[Open the interactive finite-group table](/catalog/finite-groups/table/).

This table organizes [[algebra-groups/finite-group|finite groups]] by their constructions and their place in the [[algebra-groups/classification-finite-simple-groups|classification of finite simple groups]]. Select a tile to see its order, defining parameters, simplicity conditions, and a linked definition.

## Two ways to explore

The classification layout gives the finite [[algebra-groups/simple-group|simple groups]] a clear structure: prime-order cyclic and alternating families, classical and exceptional Lie-type families, and the sporadics. The Tits group occupies a separate boundary position beside the exceptional families.

The all-groups layout places familiar families and small examples alongside the classification entries. These include symmetric, dihedral, quaternion, abelian, matrix, and finite Heisenberg groups. A family tile specifies parameters; an individual tile specifies one group. Order sorting compares individual groups using exact integers and keeps symbolic families separate.

## Exceptional families and sporadic groups

An exceptional Lie-type label such as \(E_8(q)\) denotes a family varying with a [[algebra-fields-galois/finite-field|finite field]]. A sporadic label such as \(M_{11}\) denotes one isomorphism type. The distinction explains why ten exceptional-family tiles and 26 sporadic tiles have different meanings.

The sporadic layout follows four display groups: Mathieu, Leech-related, Monster-related, and pariahs. These headings organize the entries; proximity is not an assertion of a direct subgroup inclusion. Verified relationships appear separately in the catalogue explorer.

## Beyond simple groups

The simple-group classification provides possible composition factors. It does not classify all ways of assembling a finite group from those factors. The [[algebra-groups/classification-finite-abelian-groups|finite abelian classification]] is a complete classification within a smaller class.

Broader properties cut across the table: being a [[algebra-groups/p-group|p-group]], [[algebra-groups/nilpotent-group|nilpotent]], or [[algebra-groups/solvable-group|solvable]] does not specify a single group from an order parameter. Follow those definitions to explore the classes.

## Maps and further reading

- [[catalog/finite-groups/relationships/cyclic-group-homomorphisms|Hom, End, and Aut for finite cyclic groups]].
- [[catalog/finite-groups/relationships/endomorphisms-of-finite-simple-groups|Endomorphisms of finite simple groups]].
- [[catalog/finite-sporadic-index|Sporadic groups: definitions and orders]].
- [[catalog/finite-lie-type-index|Lie-type groups: parameters and small cases]].
- [[catalog/finite-elementary-index|Familiar finite groups and examples]].
- [[catalog/categories/finite-groups|The category of finite groups]] and [[catalog/categories/finite-simple-groups|the full subcategory of finite simple groups]].
- [Explore recorded maps and relationships](/catalog/explorer/) · [[catalog|Full mathematical catalogue]].

## References

- R. A. Wilson and collaborators, [ATLAS of Finite Group Representations: sporadic groups](https://brauer.maths.qmul.ac.uk/Atlas/v3/spor/), display sections “Mathieu groups,” “Leech lattice groups,” “Monster sections,” and “Pariahs.”
