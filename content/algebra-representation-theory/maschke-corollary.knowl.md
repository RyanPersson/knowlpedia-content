+++
id = "algebra-representation-theory/maschke-corollary"
title = "Maschke corollary (regular representation decomposition)"
kind = "knowl"
summary = "When char(k) does not divide |G|, the group algebra is semisimple and the regular representation splits into irreducibles with multiplicity equal to dimension."
aliases = ["maschke-corollary", "Maschke corollary (regular representation decomposition)"]
domains = ["algebra-representation-theory"]
legacy_source_path = "algebra-representation-theory/maschke-corollary.md"
+++

Let \(G\) be a finite group and \(k\) an algebraically closed field such that \(\operatorname{char}(k)\nmid |G|\). Let \(\{V_1,\dots,V_r\}\) be representatives of the isomorphism classes of finite-dimensional [[algebra-representation-theory/irreducible-representation|irreducible representations]] of \(G\), and set \(d_i=\dim_k V_i\). Then the [[algebra-representation-theory/regular-representation|regular representation]] decomposes as a left \(k[G]\)-module:
\[
k[G]\;\cong\;\bigoplus_{i=1}^r d_i\,V_i.
\]
Thus each \(V_i\) occurs with multiplicity \(d_i\).

## Explanation

By [[algebra-representation-theory/maschkes-theorem|Maschke's theorem]], the regular representation is completely reducible. Algebraic closedness identifies the multiplicity of \(V_i\) with \(\dim_k V_i\).

## Remarks

A closely related semisimple-algebra statement is that the [[algebra-representation-theory/group-algebra|group algebra]] admits a Wedderburn decomposition
\[
k[G]\;\cong\;\bigoplus_{i=1}^r \operatorname{End}_k(V_i)\;\cong\;\bigoplus_{i=1}^r \mathrm{Mat}_{d_i}(k),
\]
where the second isomorphism uses \(\dim(V_i)=d_i\) and algebraic closedness of \(k\).

Taking dimensions in the module decomposition gives the formula [[algebra-representation-theory/sum-squares-degrees|sum of squares of degrees]]:
\[
|G|=\dim_k(k[G])=\sum_i d_i^2.
\]

## Examples

1. **\(S_3\) (order \(6\)).**
   Over \(\mathbb C\), the irreducibles are \(\mathbf{1}\) (trivial), \(\mathrm{sgn}\) (sign), and the \(2\)-dimensional standard representation \(V\).
   The corollary gives
   \[
   \mathbb C[S_3]\;\cong\; 1\cdot \mathbf{1}\;\oplus\;1\cdot \mathrm{sgn}\;\oplus\;2\cdot V.
   \]
   The dimensions sum to \(1+1+2\cdot 2=6\).

2. **\(C_n\) (order \(n\)).**
   All irreducibles are \(1\)-dimensional characters \(\chi_0,\dots,\chi_{n-1}\), hence
   \[
   \mathbb C[C_n]\;\cong\;\chi_0\oplus\chi_1\oplus\cdots\oplus\chi_{n-1}.
   \]

3. **\(D_8\) (order \(8\)).**
   The group \(D_8\) has four \(1\)-dimensional irreducibles \(\chi_1,\dots,\chi_4\) and one \(2\)-dimensional irreducible \(V\), so
   \[
   \mathbb C[D_8]\;\cong\;\chi_1\oplus\chi_2\oplus\chi_3\oplus\chi_4\oplus 2\cdot V,
   \]
   and \(4\cdot 1 + 2\cdot 2 = 8\).
