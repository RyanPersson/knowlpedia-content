+++
id = "catalog/relationships/compact-freudenthal-magic-square"
title = "Compact Freudenthal magic square"
kind = "index"
summary = "Sixteen catalogue constructions from four real division composition algebras."
aliases = ["Compact Freudenthal magic square"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "continuous"
prerequisites = ["catalog/relationships/vinberg-magic-square-construction", "lie-groups/lie-algebra", "nonassociative-algebra/composition-algebra", "lie-groups/compact-real-form"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

The **compact Freudenthal magic square** assigns a compact real [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak M(A,B)\) to each ordered pair of real division [[nonassociative-algebra/composition-algebra|composition algebras]] \(A,B\in\{\mathbb R,\mathbb C,\mathbb H,\mathbb O\}\), using the [[catalog/relationships/vinberg-magic-square-construction|Vinberg construction]]. All outputs below are real; the exceptional symbols mean [[lie-groups/compact-real-form|compact real forms]].

| Input | \(\mathbb R\) | \(\mathbb C\) | \(\mathbb H\) | \(\mathbb O\) |
|---|---|---|---|---|
| \(\mathbb R\) | [[catalog/lie-algebras/so-3-r|\(\mathfrak{so}(3)\)]] | [[catalog/lie-algebras/su-3|\(\mathfrak{su}(3)\)]] | [[catalog/lie-algebras/sp-3|\(\mathfrak{sp}(3)\)]] | [[catalog/lie-algebras/f4-compact|\(\mathfrak f_4\)]] |
| \(\mathbb C\) | [[catalog/lie-algebras/su-3|\(\mathfrak{su}(3)\)]] | [[catalog/relationships/su3-direct-sum-su3|\(\mathfrak{su}(3)\oplus\mathfrak{su}(3)\)]] | [[catalog/lie-algebras/su-6|\(\mathfrak{su}(6)\)]] | [[catalog/lie-algebras/e6-compact|\(\mathfrak e_6\)]] |
| \(\mathbb H\) | [[catalog/lie-algebras/sp-3|\(\mathfrak{sp}(3)\)]] | [[catalog/lie-algebras/su-6|\(\mathfrak{su}(6)\)]] | [[catalog/lie-algebras/so-12-r|\(\mathfrak{so}(12)\)]] | [[catalog/lie-algebras/e7-compact|\(\mathfrak e_7\)]] |
| \(\mathbb O\) | [[catalog/lie-algebras/f4-compact|\(\mathfrak f_4\)]] | [[catalog/lie-algebras/e6-compact|\(\mathfrak e_6\)]] | [[catalog/lie-algebras/e7-compact|\(\mathfrak e_7\)]] | [[catalog/lie-algebras/e8-compact|\(\mathfrak e_8\)]] |


## Construction and checks

The [[catalog/relationships/tits-magic-square-decomposition|Tits decomposition]] relates the entries to \(H_3(B)\), and the [[catalog/relationships/triality-magic-square-decomposition|triality decomposition]] gives an independent dimension calculation. [[catalog/relationships/magic-square-transposition|Transposing the inputs]] gives isomorphic outputs. The \(\mathbb C,\mathbb C\) entry is a genuine direct sum, with dimension \(16\).

## Octonions and triality

The bottom row contains the exceptional types \(F_4,E_6,E_7,E_8\). The \(F_4\) entry acts on the [[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]], whose [[nonassociative-algebra/spin8-stabilizer-of-an-albert-algebra-frame|frame stabilizer]] exposes all three eight-dimensional \(\operatorname{Spin}(8)\) representations. Compare the [[catalog/relationships/f4-triality-decomposition|decomposition of compact \(\mathfrak f_4\)]] and the [[catalog/relationships/spin8-intertwiner-spaces|different Hom-spaces]] of those modules.

## Real-form convention

\(\mathfrak{sp}(3)\) has quaternionic matrix size three and real dimension \(21\). The scalar \(\mathbb C\) labels a real two-dimensional composition algebra. [[catalog/relationships/magic-square-real-forms|Split inputs and complexification]] require separate choices; their objects must not be merged with the compact real ones.

## Machine-readable construction

The catalogue stores this table as `compact-real-freudenthal`: four row IDs, four column IDs, and sixteen cells, each naming its output and construction relationship. The ordered pair is stored explicitly, so a diagram can show both inputs. A construction edge is not a claim that a scalar algebra maps to its output by a homomorphism.

## References

1. John C. Baez, “The Octonions,” §4.3, Table 5. [Checked section](https://math.ucr.edu/home/baez/octonions/node16.html).
2. C. H. Barton and A. Sudbery, “Magic squares and matrix models of Lie algebras,” §3 and Theorems 4.3–4.4. [Paper](https://arxiv.org/pdf/math/0203010).
