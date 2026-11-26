+++
id = "algebra-fields-galois/extend-embedding-of-countable-subfield"
title = "Extending an isomorphism of countable subfields"
kind = "theorem"
summary = "In two uncountable algebraically closed fields of the same cardinality, an isomorphism of countable subfields extends to the whole fields."
domains = ["algebra-fields-galois"]
section_mode = "progressive"
prerequisites = ["algebraic-geometry-foundations/algebraically-closed-field","shared-foundations/cardinality","algebra-fields-galois/field-isomorphism","shared-foundations/countable-set","algebra-fields-galois/transcendence-basis","algebra-fields-galois/algebraic-independence","algebra-fields-galois/algebraic-closure-uniqueness"]
+++

Let \(F,F'\) be [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed fields]] of the same uncountable [[shared-foundations/cardinality|cardinality]]. Every [[algebra-fields-galois/field-isomorphism|field isomorphism]] \(u:K\to K'\) between [[shared-foundations/countable-set|countable]] subfields \(K\subseteq F\), \(K'\subseteq F'\) extends to an isomorphism \(F\to F'\).

## Proof

Take [[algebra-fields-galois/transcendence-basis|transcendence bases]] \(B\) of \(F/K\) and \(B'\) of \(F'/K'\). A rational expression uses finitely many coefficients and finitely many elements of \(B\). Hence \(K(B)\) has at most \(\max(\aleph_0,|B|)\) elements. An algebraic extension of this field still has at most that many elements, since each nonzero polynomial has finitely many roots. As \(F\) is uncountable and contains \(B\), it follows that \(|B|=|F|\). The same argument gives \(|B'|=|F'|\).

Choose a bijection \(B\to B'\). Coefficient transport by \(u\) and substitution by this bijection give an isomorphism \(K(B)\to K'(B')\) by [[algebra-fields-galois/algebraic-independence|algebraic independence]]. The ambient fields are algebraic and algebraically closed over these two fields. [[algebra-fields-galois/algebraic-closure-uniqueness|Uniqueness of algebraic closures]] extends the isomorphism as required.

## References

- [Relative Steinitz theorem](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Geometry/GaloisCovers.lean#L65)
