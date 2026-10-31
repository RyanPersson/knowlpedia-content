+++
id = "algebra-category-theory/semisimple-category"
title = "Semisimple category"
kind = "definition"
summary = "An abelian category in which every object is a finite direct sum of simple objects."
aliases = []
domains = ["algebra-category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/abelian-category", "algebra-category-theory/simple-object"]
+++

In the finite-length convention used here, a **semisimple category** is an [[algebra-category-theory/abelian-category|abelian category]] in which each object is isomorphic to a **finite** direct sum of [[algebra-category-theory/simple-object|simple objects]]:
\[
X\cong\bigoplus_{i=1}^{r} S_i^{\oplus n_i},\qquad n_i\in\mathbb Z_{\ge0}.
\]
The zero object is the empty sum. The finite list of simples occurring in this expression may depend on \(X\); semisimplicity alone does not require finitely many simple isomorphism classes in the whole category.

## Splitting exact sequences

For a finite-length abelian category, this is equivalent to every short [[algebra-category-theory/exact-sequence-categorical|exact sequence]] splitting. In a sequence \(0\to A\xrightarrow{i}B\xrightarrow{p}C\to0\), a section \(s:C\to B\) with \(ps=\operatorname{id}_C\) gives an isomorphism \(B\cong A\oplus C\) compatible with the sequence:

```tikz-cd
0 \arrow[r] & A \arrow[r, "i"] \arrow[d, equal] & B \arrow[r, "p"] \arrow[d, "\sim"'] & C \arrow[r] \arrow[d, equal] & 0 \\
0 \arrow[r] & A \arrow[r, "\iota_A"'] & A\oplus C \arrow[r, "\pi_C"'] & C \arrow[r] & 0
```

Splitting a composition series successively gives the direct-sum description. The resulting choice of summands need not be canonical.

## Examples and conventions

Finite-dimensional vector spaces are semisimple. Finite-dimensional representations of a finite group over a characteristic-zero field are semisimple by averaging a linear projection onto an invariant subspace. Finite-dimensional \(\mathbb Z\)-graded vector spaces are also semisimple, but have one simple isomorphism class for every integer degree, so they are not a [[algebra-category-theory/fusion-category|fusion category]].

Some authors allow arbitrary direct sums of simples in “semisimple category.” The finite-sum convention here is the one relevant to fusion categories; it excludes infinite-dimensional vector spaces as objects.

## References

P. Etingof, S. Gelaki, D. Nikshych, and V. Ostrik, *Tensor Categories* (2015), §§1.5 and 4.8; [author-hosted text](https://math.mit.edu/~etingof/egnobookfinal.pdf).
