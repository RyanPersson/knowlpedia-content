+++
id = "arithmetic-geometry/constant-family-height-inequality"
title = "A product formula for simultaneous height bounds"
kind = "theorem"
summary = "A constant nonzero family cannot be small at all complex and finite comparisons."
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/simultaneous-height-bound","algebra-fields-galois/field-automorphism","arithmetic-geometry/algebraicity-from-bounded-padic-conjugates","algebra-fields-galois/norm-field","algebra-fields-galois/field-embedding","algebra-fields-galois/extend-embedding-of-countable-subfield","arithmetic-geometry/product-formula"]
+++

Suppose the constant family \(y_\iota=z\ne0\) has [[arithmetic-geometry/simultaneous-height-bound|simultaneous height at most]] \(c\). If \(|\sigma(z)|\le e^b\) for every [[algebra-fields-galois/field-automorphism|automorphism]] of \(\mathbb C\), then \(b+c\ge0\).

## Proof

The constant family \(z^{-1}\) has height at most \(b\). Take \(z\) as its multiplier, take \(b\) as the archimedean bound and take every finite exponent to be zero. Multiply its witnesses by those for \(z\). This gives height at most \(b+c\) for the constant family \(1\). It remains to show that every height bound \(C\) for \(1\) is nonnegative.

Let \(H\ne0,\alpha,(h_p)\) be the witnesses for \(1\). At \(p=2\) every comparison satisfies \(|\iota H|_2\le2^{h_2}\), so \(H\) is [[arithmetic-geometry/algebraicity-from-bounded-padic-conjugates|algebraic]]. Set \(K=\mathbb Q(H)\), \(d=[K:\mathbb Q]\) and \(r=N_{K/\mathbb Q}(H)\ne0\). At the real absolute value and at each \(p\)-adic absolute value, the [[algebra-fields-galois/norm-field|field norm]] \(r\) is the product of the images of \(H\) under the \(d\) [[algebra-fields-galois/field-embedding|embeddings]] of \(K\) into the corresponding algebraically closed field. Each embedding [[algebra-fields-galois/extend-embedding-of-countable-subfield|extends to a comparison or complex automorphism]]. Hence
\[
\log |r|\le d\alpha,\qquad \log |r|_p\le d h_p\log p .
\]

Take \(S\) to be the primes dividing the numerator or denominator of \(r\) in lowest terms. The [[arithmetic-geometry/product-formula|rational product formula]] gives \(\log|r|+\sum_{p\in S}\log|r|_p=0\), since a prime power in \(r\) contributes opposite logarithms at \(p\) and at infinity. Adding the estimates gives \(0\le d(\alpha+\sum_{p\in S}h_p\log p)\le dC\). Since \(d>0\), this proves \(C\ge0\).

## References

- [Heights of a constant family and its inverse](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean#L191)
- [The implication for a nonzero scalar](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean#L225)
