+++
id = "lie-groups/regular-lie-subalgebra"
title = "Regular Lie subalgebra"
kind = "definition"
summary = "A Lie subalgebra normalized by a Cartan subalgebra of the ambient semisimple Lie algebra."
aliases = ["regular Lie subalgebra", "regular subalgebra of a Lie algebra"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/semisimple-lie-algebra", "lie-groups/cartan-subalgebra", "lie-groups/lie-subalgebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a finite-dimensional complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] and let \(\mathfrak h\subset\mathfrak g\) be a [[lie-groups/cartan-subalgebra|Cartan subalgebra]]. A [[lie-groups/lie-subalgebra|Lie subalgebra]] \(\mathfrak k\subseteq\mathfrak g\) is **regular relative to \(\mathfrak h\)** if
\[
[\mathfrak h,\mathfrak k]\subseteq\mathfrak k.
\]
A subalgebra is called **regular** if it is regular relative to some Cartan subalgebra of \(\mathfrak g\).

## Root-space description

Write
\[
\mathfrak g=\mathfrak h\oplus\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha
\]
for the [[lie-groups/root-space-decomposition|root-space decomposition]]. Since the [[lie-groups/root-space|root spaces]] are the simultaneous [[lie-groups/weight-space|weight spaces]] for \(\operatorname{ad}(\mathfrak h)\), regularity is equivalent to a decomposition
\[
\mathfrak k=(\mathfrak k\cap\mathfrak h)
\oplus\bigoplus_{\alpha\in\Psi}\mathfrak g_\alpha
\]
for some subset \(\Psi\subseteq\Phi\), subject to the closure conditions required for the displayed vector space to be a Lie subalgebra.

When \(\mathfrak k\) is **reductive in \(\mathfrak g\)**—so that the restricted adjoint representation of \(\mathfrak k\) on \(\mathfrak g\) is completely reducible—\(\Psi\) is symmetric under \(\alpha\mapsto-\alpha\) and forms a [[lie-groups/root-subsystem|root subsystem]]. Its Cartan part contains the corresponding coroots and may be larger than their span; those extra toral directions account for part or all of the [[lie-groups/center-of-a-lie-algebra|center]] of \(\mathfrak k\). This embedded notion rules out, for example, a one-dimensional subalgebra spanned by a nilpotent root vector, even though that subalgebra is abstractly abelian.

## Distinctions

- “Regular” means normalized by an ambient Cartan; it does **not** mean that the subalgebra contains that Cartan.
- A reductive regular subalgebra that contains an ambient Cartan has [[lie-groups/maximal-rank-lie-subalgebra|maximal rank]], but regular subalgebras can have smaller rank.
- Regularity depends on an embedding \(\mathfrak k\hookrightarrow\mathfrak g\), not merely on the abstract isomorphism type of \(\mathfrak k\).

Regular embeddings let root-system calculations replace matrix calculations. This is the mechanism behind deleting [[lie-groups/simple-root|simple roots]], constructing [[lie-groups/levi-subalgebra|Levi subalgebras]], and computing many centralizers in exceptional [[lie-groups/lie-algebra|Lie algebras]].

## References

1. Eugene B. Dynkin, “Semisimple subalgebras of semisimple Lie algebras,” *Matematicheskii Sbornik* 30(72), no. 2 (1952), 349–462; English translation, *AMS Translations*, Series 2, vol. 6 (1957), 111–244. [Journal record](https://www.mathnet.ru/eng/sm5435).
2. John C. Baez, “Three Generations in \(E_7\),” 2026, §§2–3. [arXiv record](https://arxiv.org/abs/2608.06271).
