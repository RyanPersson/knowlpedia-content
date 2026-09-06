+++
id = "algebra-hyperstructures/classification-of-stringent-hyperfields"
title = "Classification of stringent hyperfields"
kind = "theorem"
summary = "Stringent hyperfields are tropical extensions whose residue layer is a field, the Krasner hyperfield, or the sign hyperfield."
aliases = ["Bowler-Su classification of stringent hyperfields"]
domains = ["algebra-hyperstructures", "matroid-theory"]
prerequisites = ["algebra-hyperstructures/stringent-hyperfield", "algebra-hyperstructures/krasner-hyperfield", "algebra-hyperstructures/sign-hyperfield", "algebra-rings/field", "algebra-groups/ordered-abelian-group"]
dependency_review_count = 1
section_mode = "progressive"
+++

Every [[algebra-hyperstructures/stringent-hyperfield|stringent hyperfield]]
\(R\) is a tropical extension of one of the following kinds of residue
hyperfield:

1. the [[algebra-hyperstructures/krasner-hyperfield|Krasner hyperfield]];
2. the [[algebra-hyperstructures/sign-hyperfield|sign hyperfield]];
3. an ordinary [[algebra-rings/field|field]].

More invariantly, there is a totally
[[algebra-groups/ordered-abelian-group|ordered abelian group]] \(\Gamma\) and
an exact sequence
\[
1\longrightarrow F^\times\longrightarrow R^\times
\xrightarrow{\,v\,}\Gamma\longrightarrow1,
\]
where \(F\) is one of the three kinds above. The order on \(\Gamma\), the
hyperaddition of \(F\), and the extension data determine the hyperaddition on
\(R\): between unequal layers the larger layer is the unique sum, while
cancellation in one layer exposes lower layers.

Conversely, the compatible tropical-extension construction from such data
produces a stringent hyperfield. The extension need not split, so the theorem
does not assert that \(R^\times\) is a direct product.

## Consequence

This explains the three basic sources of stringent behavior: valuative
extensions of Krasner type, signed valuative extensions, and valued-field
extensions. The additional
[[algebra-hyperstructures/doubly-distributive-hyperfield|double-distributivity]]
condition selects a proper subclass.

## References
Nathan Bowler and Ting Su,
[*Classification of doubly distributive skew hyperfields and stringent hypergroups*, Theorem 4.10](https://arxiv.org/abs/2003.03751).
