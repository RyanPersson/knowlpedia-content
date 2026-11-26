+++
id = "linear-algebra/conjugates-of-a-rational-gram-determinant"
title = "Conjugates of a Gram determinant with rational metric"
kind = "theorem"
summary = "Bounds on Gram determinants after conjugating coordinates bound every conjugate of the original determinant."
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/symmetric-positive-definite-matrix", "linear-algebra/conjugate-transpose", "linear-algebra/gram-matrix", "algebra-fields-galois/field-automorphism", "shared-foundations/complex-conjugate", "linear-algebra/determinant", "linear-algebra/mixed-gram-determinant-inequality"]
+++

Let \(G\) be a rational [[linear-algebra/symmetric-positive-definite-matrix|symmetric positive definite matrix]], \(X\) a complex matrix with the same number of rows, \(X^*\) its [[linear-algebra/conjugate-transpose|conjugate transpose]], and \(\Delta(X)=\det(X^*GX)\), its [[linear-algebra/gram-matrix|Gram determinant]]. Suppose \(\Delta(\tau X)\le e^c\) for every [[algebra-fields-galois/field-automorphism|field automorphism]] \(\tau\) of \(\mathbb C\), applied entrywise. Then \(|\sigma(\Delta(X))|\le e^c\) for every such \(\sigma\).

## Proof

Let \(j\) denote [[shared-foundations/complex-conjugate|complex conjugation]] and put \(\sigma'=j\sigma j\). For every scalar \(x\) one has \(\sigma(\bar x)=\overline{\sigma'(x)}\). Since \(\sigma\) fixes the entries of \(G\) and commutes with taking [[linear-algebra/determinant|determinants]], this gives
\[
\sigma(\Delta(X))=\det\big((\sigma'X)^*G(\sigma X)\big).
\]
Apply the [[linear-algebra/mixed-gram-determinant-inequality|mixed Gram determinant inequality]] in the inner product defined by \(G\). Its two families are the columns of \(\sigma'X\) and \(\sigma X\). The hypotheses apply to both automorphisms, so \(|\sigma(\Delta(X))|^2\le\Delta(\sigma'X)\Delta(\sigma X)\le e^{2c}\). Taking the nonnegative square root gives the claim.

## References

- [Conjugates of the untwisted Gram determinant](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L294)
