+++
id = "algebra-modules/splitting-lemma"
title = "Splitting lemma"
kind = "knowl"
summary = "A short exact sequence splits iff it has a section or a retraction."
aliases = ["splitting-lemma", "Splitting lemma"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/splitting-lemma.md"
prerequisites = ["algebra-modules/short-exact-sequence", "algebra-modules/module", "algebra-modules/module-homomorphism", "algebra-modules/split-exact-sequence", "algebra-modules/direct-sum-modules"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

**Splitting lemma**: Given a [[algebra-modules/short-exact-sequence|short exact sequence]]
\[
0\to A \xrightarrow{i} B \xrightarrow{p} C \to 0
\]
of \(R\)-[[algebra-modules/module|modules]], the following are equivalent:
1. There exists a [[algebra-modules/module-homomorphism|module homomorphism]] \(s\colon C\to B\) with \(p\circ s=\mathrm{id}_C\) (a section of \(p\)).
2. There exists a homomorphism \(r\colon B\to A\) with \(r\circ i=\mathrm{id}_A\) (a retraction of \(i\)).
3. The sequence is [[algebra-modules/split-exact-sequence|split exact]] in the sense of direct sums: there is an isomorphism \(\varphi\colon B\to A\oplus C\) onto the [[algebra-modules/direct-sum-modules|direct sum]] with \(\varphi\circ i\) the inclusion \(a\mapsto(a,0)\) and \(p\) equal to the projection \((a,c)\mapsto c\) composed with \(\varphi\).

Condition 3 says that the diagram below commutes, where \(\iota_A(a)=(a,0)\) and \(\pi_C(a,c)=c\):

```tikz-cd
0 \arrow[r] & A \arrow[r, "i"] \arrow[d, equal] & B \arrow[r, "p"] \arrow[d, "\varphi", "\cong"'] & C \arrow[r] \arrow[d, equal] & 0 \\
0 \arrow[r] & A \arrow[r, "\iota_A"'] & A\oplus C \arrow[r, "\pi_C"'] & C \arrow[r] & 0
```

This lemma is the basic bridge between homomorphisms that admit one-sided inverses and internal direct sum decompositions.

## Remarks

The compatibility of \(\varphi\) with \(i\) and \(p\) in condition 3 cannot be dropped. Let \(T=\bigoplus_{n\ge1}\mathbb Z/2\mathbb Z\), and consider
\[
0\to\mathbb Z\xrightarrow{\,k\mapsto(2k,0)\,}\mathbb Z\oplus T\xrightarrow{\,(k,t)\mapsto(k \bmod 2,\,t)\,}\mathbb Z/2\mathbb Z\oplus T\to0 .
\]
Since \(\mathbb Z/2\mathbb Z\oplus T\cong T\), the middle term is abstractly isomorphic to the direct sum of the ends. The sequence does not split: a section would send the torsion element \((1,0)\) to a torsion element of \(\mathbb Z\oplus T\), hence into \(0\oplus T\), whose image under the projection has first coordinate \(0\).
