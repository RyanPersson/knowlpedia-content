+++
id = "algebra-fields-galois/discriminant-field"
title = "Discriminant (of a field basis)"
kind = "knowl"
summary = "The determinant of the trace-pairing matrix associated with a basis of a finite field extension."
aliases = ["discriminant-field", "Discriminant (of a field basis)"]
domains = ["algebra-fields-galois"]
prerequisites = ["algebra-fields-galois/field-extension", "algebra-fields-galois/trace-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-fields-galois/discriminant-field.md"
+++

Let \(L/K\) be a finite [[algebra-fields-galois/field-extension|field extension]] of degree \(n\), and let \(\mathrm{Tr}_{L/K}\) be the [[algebra-fields-galois/trace-field|field trace]]. For an \(n\)-tuple \(\mathbf{b}=(b_1,\dots,b_n)\) in \(L\) that is a \(K\)-basis of \(L\), the **discriminant** of \(\mathbf{b}\) (relative to \(L/K\)) is
\[
\mathrm{disc}_{L/K}(\mathbf{b}) \;:=\; \det\!\big(\mathrm{Tr}_{L/K}(b_i b_j)\big)_{1\le i,j\le n}\in K.
\]

## Remarks

If \(L/K\) is separable (see [[algebra-fields-galois/separable-extension|separable extension]]), then \(\mathrm{disc}_{L/K}(\mathbf{b})\neq 0\), and one can also express it using \(K\)-[[algebra-fields-galois/field-embedding|embeddings]] \(\sigma_1,\dots,\sigma_n:L\hookrightarrow \Omega\) into a common overfield \(\Omega\):
\[
\mathrm{disc}_{L/K}(\mathbf{b}) \;=\; \det(\sigma_i(b_j))_{i,j}^2.
\]
Thus separability is equivalent to nondegeneracy of the trace pairing, and hence to the nonvanishing of the discriminant of every basis.

### Examples
1. **Quadratic basis.** Let \(L=K(\sqrt{d})\) with \(\mathrm{char}(K)\neq 2\) and basis \((1,\sqrt{d})\). Using \(\mathrm{Tr}_{L/K}(1)=2\), \(\mathrm{Tr}_{L/K}(\sqrt{d})=0\), \(\mathrm{Tr}_{L/K}(d)=2d\),
\[
\mathrm{disc}_{L/K}(1,\sqrt{d})=\det\begin{pmatrix}2&0\\0&2d\end{pmatrix}=4d.
\]

2. **Power basis in a simple extension.** If \(L=K(\alpha)\) with \([L:K]=n\), the “power basis” \((1,\alpha,\dots,\alpha^{n-1})\) has discriminant
\(\mathrm{disc}_{L/K}(1,\alpha,\dots,\alpha^{n-1})=\det(\mathrm{Tr}_{L/K}(\alpha^{i+j}))_{0\le i,j\le n-1}\),
which can be computed from the minimal polynomial of \(\alpha\) in concrete cases.

3. **Finite fields.** For \(L=\mathbb{F}_{q^n}\) over \(K=\mathbb{F}_q\), every \(K\)-basis has nonzero discriminant because finite fields are [[algebra-fields-galois/finite-fields-perfect|perfect]].
