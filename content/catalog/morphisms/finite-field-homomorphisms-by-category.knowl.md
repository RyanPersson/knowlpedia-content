+++
id = "catalog/morphisms/finite-field-homomorphisms-by-category"
title = "Finite-field Hom-sets under field and ring conventions"
kind = "example"
summary = "Some finite-field pairs have no field embedding but still have a zero homomorphism in the arbitrary-ring category."
aliases = []
domains = ["catalog", "algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["catalog/categories/fields", "catalog/categories/rings", "algebra-fields-galois/finite-field"]
dependency_heuristic = "catalog-semantic-review-v1"
dependency_review_count = 1
+++

In the [[catalog/categories/fields|category of fields]], all maps preserve \(1\). The following are exact Hom-set calculations:

| Source and target | Field homomorphisms | Arbitrary [[algebra-rings/ring-homomorphism|ring homomorphisms]] |
| --- | --- | --- |
| \(\mathbb F_2\to\mathbb F_4\) | the unique prime-field inclusion | inclusion and zero |
| \(\mathbb F_2\to\mathbb F_3\) | none | zero only |
| \(\mathbb F_4\to\mathbb F_8\) | none | zero only |
| \(\mathbb F_4\to\mathbb F_4\) | identity and \(x\mapsto x^2\) | those two and zero |

In the last row both field endomorphisms are automorphisms. “Zero only” is a singleton set, whereas “none” means the [[shared-foundations/empty-set|empty set]].

## Verification

A field homomorphism is injective and preserves characteristic, excluding \(\mathbb F_2\to\mathbb F_3\). A map \(\mathbb F_4\to\mathbb F_8\) would inject a multiplicative group of order \(3\) into one of order \(7\), contrary to [[algebra-groups/lagranges-theorem|Lagrange's theorem]]. Maps out of the prime field are determined by \(1\).

Write \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\). Its nontrivial element \(u\) must map to one of the two roots \(u,u^2\), giving identity and Frobenius. Finally, every nonzero ring map between fields is unital: its value on \(1\) is a nonzero idempotent. Thus allowing arbitrary ring maps adds precisely the zero map in each row.

## Catalogue meaning

These are affirmative calculations of emptiness or nonemptiness. An unrecorded pair in the catalogue has status “not catalogued,” which is distinct from both outcomes above.
