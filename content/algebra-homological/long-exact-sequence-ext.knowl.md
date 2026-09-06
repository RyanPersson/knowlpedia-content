+++
id = "algebra-homological/long-exact-sequence-ext"
title = "Long exact sequence for Ext"
kind = "knowl"
summary = "The natural long exact sequence in Ext induced by a short exact sequence of modules."
aliases = ["long-exact-sequence-ext", "Long exact sequence for Ext"]
domains = ["algebra-homological"]
prerequisites = ["algebra-modules/short-exact-sequence", "algebra-homological/ext", "algebra-homological/hom-left-exact"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "algebra-homological/long-exact-sequence-ext.md"
+++

Let \(R\) be a ring. A [[algebra-modules/short-exact-sequence|short exact sequence]] of left \(R\)-modules
\[
0 \longrightarrow A' \xrightarrow{u} A \xrightarrow{v} A'' \longrightarrow 0
\]
and a left \(R\)-module \(B\) induce natural connecting maps
\[
\delta^n:\operatorname{Ext}_R^{n}(A',B)\longrightarrow \operatorname{Ext}_R^{n+1}(A'',B)
\quad (n\ge 0),
\]
and a natural long exact sequence
\[
0\to \operatorname{Hom}_R(A'',B)\to \operatorname{Hom}_R(A,B)\to \operatorname{Hom}_R(A',B)
\to \operatorname{Ext}_R^{1}(A'',B)\to \operatorname{Ext}_R^{1}(A,B)\to \operatorname{Ext}_R^{1}(A',B)
\to \operatorname{Ext}_R^{2}(A'',B)\to \cdots .
\]

## Sequence in the second variable

A short exact sequence
\[
0 \longrightarrow B' \xrightarrow{u} B \xrightarrow{v} B'' \longrightarrow 0
\]
be a short exact sequence of left \(R\)-modules, and let \(A\) be a left \(R\)-module. Then there is a natural long exact sequence
\[
0\to \operatorname{Hom}_R(A,B')\to \operatorname{Hom}_R(A,B)\to \operatorname{Hom}_R(A,B'')
\to \operatorname{Ext}_R^{1}(A,B')\to \operatorname{Ext}_R^{1}(A,B)\to \operatorname{Ext}_R^{1}(A,B'')
\to \operatorname{Ext}_R^{2}(A,B')\to \cdots .
\]

## Examples

1. **Computing \(\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n, A)\cong A/nA\).**
   Start from
   \[
   0\to \mathbb Z \xrightarrow{\cdot n}\mathbb Z \to \mathbb Z/n \to 0.
   \]
   Apply \(\operatorname{Hom}_{\mathbb Z}(-,A)\). Since \(\operatorname{Hom}_{\mathbb Z}(\mathbb Z,A)\cong A\), the relevant piece of the long exact sequence is
   \[
   A \xrightarrow{\cdot n} A \to \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\to 0,
   \]
   so
   \[
   \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,A)\cong \operatorname{coker}(\cdot n:A\to A)\cong A/nA.
   \]
   (Also \(\operatorname{Ext}^i_{\mathbb Z}(\mathbb Z/n,-)=0\) for \(i\ge 2\) because \(\mathbb Z/n\) has a length-1 projective resolution.)

2. **Computing \(\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n, \mathbb Z/m)\cong \mathbb Z/\gcd(n,m)\).**
   Take \(A=\mathbb Z/m\) in the previous example:
   \[
   \operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z/m)\cong (\mathbb Z/m)/n(\mathbb Z/m)
   \cong \mathbb Z/\gcd(n,m).
   \]

## Remarks

These sequences are instances of the [[algebra-homological/long-exact-sequence-derived|long exact sequence for derived functors]], with connecting maps supplied by the [[algebra-homological/connecting-homomorphism-lemma|connecting homomorphism]].
