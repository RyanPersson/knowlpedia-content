+++
id = "catalog/lie-groups-table-guide"
title = "Reading the Lie-group table"
kind = "index"
summary = "Compare compact, split-real and complex Lie groups while keeping their dimensions, parameters and global forms distinct."
aliases = ["Lie group periodic table", "table of Lie groups"]
domains = ["catalog", "lie-groups"]
section_mode = "continuous"
prerequisites = []
dependency_heuristic = "lie-table-semantic-review-v1"
dependency_review_count = 1
+++

[Open the interactive Lie-group table](/catalog/lie-groups/table/).

The table compares [[fiber-bundles/lie-group|Lie groups]] through their [[lie-groups/lie-algebra-of-a-lie-group|Lie algebras]], dimensions and global constructions. Select a cell for its precise parameter range, defining group, and recorded relationships. The family view also includes additive groups, tori, Heisenberg groups, affine groups, Euclidean groups and small examples.

## Types and forms

The comparison uses the nine series in the [[lie-groups/classification-simple-lie-algebras|classification of complex simple Lie algebras]]: \(A,B,C,D,G_2,F_4,E_6,E_7,E_8\). For each type it shows a compact real group, a split real group, and a complex group. The real Lie algebras in the first two columns have the complex Lie algebra of the third as their [[lie-groups/complexification-of-a-real-lie-algebra|complexification]]. Other real forms exist; these three columns are a selection.

The rank parameter \(r\) is not generally the matrix size. For example, type \(A_r\) uses \(\mathrm{SU}(r+1)\), \(\mathrm{SL}(r+1,\mathbb R)\), and \(\mathrm{SL}(r+1,\mathbb C)\). A cell can restrict and reparameterize an existing family: its details explain the substitution before linking to the full family definition.

Dimensions in the two real columns are real dimensions. Dimensions in the complex column are complex dimensions; the underlying real group has twice that dimension. Thus \(\mathrm{SL}(2,\mathbb C)\) has complex dimension 3 and real dimension 6. A real Lie group may be defined using complex or quaternionic matrices: \(\mathrm{SU}(2)\) and \(\mathrm{Sp}(1)\) both have real dimension 3.

## Global forms and maps

A Lie algebra does not specify a unique [[lie-groups/connected-lie-group|connected Lie group]]. A connected group is a quotient of its [[lie-groups/universal-covering-group|simply connected covering group]] by a discrete central subgroup. These [[lie-groups/central-quotient-of-a-lie-group|central quotients]] preserve the Lie algebra while changing global topology.

The compact and complex columns choose simply connected groups. In the split column, the classical entries use the indicated matrix groups, taking the [[lie-groups/identity-component-of-a-lie-group|identity component]] \(\mathrm{SO}_0(p,q)\) in the orthogonal cases; the exceptional entries use connected adjoint groups. These split representatives are not all topologically simply connected. A type label therefore never substitutes for the displayed global-form convention.

For example, \(\mathrm{SU}(2)\) and \(\mathrm{SO}(3)\) share a Lie algebra, but the map \(\mathrm{SU}(2)\to\mathrm{SO}(3)\) is a two-sheeted covering with kernel \(\{\pm I\}\). It is not an isomorphism. The table preserves the catalogue's distinction between isomorphisms, embeddings, coverings and quotient maps.

## Small ranks and the wider catalogue

The classical rows start at \(A_1,B_2,C_3,D_4\) to avoid repeating complex simple types. The familiar coincidences are \(B_1=C_1=A_1\), \(B_2=C_2\), and \(D_3=A_3\); \(D_2=A_1\oplus A_1\) is semisimple rather than simple. These are Lie-algebra type identifications. Group isomorphisms require matching global forms, as illustrated by \(\mathrm{Spin}(3)\cong\mathrm{SU}(2)\) and \(\mathrm{Spin}(4)\cong\mathrm{SU}(2)\times\mathrm{SU}(2)\).

The broader family view retains parameter-dependent compactness and connectedness. “Not recorded” means the catalogue has no value for a property; it does not mean the property is false. The comparison of simple types is not a classification of all Lie groups.

- [[catalog/lie-groups-index|Full Lie-group catalogue]].
- [[catalog/lie-algebras-index|Lie algebras, real forms and dimensions]].
- [[catalog/relationships/compact-freudenthal-magic-square|The compact Freudenthal magic square]].
- [Explore maps and category views](/catalog/explorer/).
- [Compare the finite-group table](/catalog/finite-groups/table/).

## References

- Pavel Etingof, [Lie Groups and Lie Algebras](https://ocw.mit.edu/courses/18-755-lie-groups-and-lie-algebras-ii-spring-2024/mit18_755_s24_lec_full.pdf), §3.2, Proposition 3.5 and Exercise 3.9; §23.8, Remark 23.18; §§40–43 on real forms and global groups. Individual cells link to their construction knowls and more specific references.
