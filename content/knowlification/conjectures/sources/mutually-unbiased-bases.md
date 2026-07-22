In the complex Hilbert space \(\mathbb C^d\), an orthonormal basis is a list \(B=(b_1,\ldots,b_d)\) with \(\langle b_i,b_j\rangle=\delta_{ij}\). Two orthonormal bases \(B=(b_i)\) and \(C=(c_j)\) are mutually unbiased when
\[
|\langle b_i,c_j\rangle|^2=\frac1d
\]
for every \(i,j\). Measuring a state from one basis in the other basis therefore gives the uniform distribution.

Equivalently, write the basis vectors as the columns of unitary matrices \(U\) and \(V\). The bases are mutually unbiased exactly when every entry of the relative unitary matrix \(U^*V\) has squared modulus \(1/d\). A family is mutually unbiased if every distinct pair in the family is mutually unbiased.

Let \(\mu(d)\) be the largest size of a mutually unbiased family in \(\mathbb C^d\).

## Open problem

Determine \(\mu(d)\) for every positive integer \(d\). One always has \(\mu(d)\le d+1\), and a family of size \(d+1\) is called complete. Complete families exist whenever \(d\) is a prime power. It is unknown whether they exist in every other dimension.

Dimension six is the smallest famous unresolved case: at least three mutually unbiased bases are known, while the general upper bound gives \(3\le\mu(6)\le7\). Even deciding whether a fourth basis exists is open.

## Formal source

This page follows `FormalConjectures/OpenQuantumProblems/13.lean`. The formalization represents an orthonormal basis by a unitary matrix and defines unbiasedness entrywise through the relative unitary matrix.
