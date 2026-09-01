+++
id = "lie-groups/centralizer-of-a-regular-reductive-subalgebra"
title = "Centralizer of a regular reductive subalgebra"
kind = "theorem"
summary = "A root-space formula for the centralizer of a regular reductive subalgebra of a complex semisimple Lie algebra."
aliases = ["centralizer of a regular reductive subalgebra", "root formula for a Lie centralizer"]
domains = ["lie-groups"]
prerequisites = ["lie-groups/semisimple-lie-algebra", "lie-groups/cartan-subalgebra", "lie-groups/regular-lie-subalgebra", "lie-groups/centralizer-of-a-lie-subalgebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a complex [[lie-groups/semisimple-lie-algebra|semisimple Lie algebra]] with [[lie-groups/cartan-subalgebra|Cartan subalgebra]] \(\mathfrak h\) and root-space decomposition
\[
\mathfrak g=\mathfrak h\oplus\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha.
\]
Suppose \(\mathfrak k\subseteq\mathfrak g\) is [[lie-groups/regular-lie-subalgebra|regular and reductive in \(\mathfrak g\)]], so that it can be written
\[
\mathfrak k=\mathfrak t\oplus\bigoplus_{\alpha\in\Psi}\mathfrak g_\alpha,
\qquad \mathfrak t=\mathfrak k\cap\mathfrak h,
\]
with \(\Psi=-\Psi\) and with \(\mathfrak t\) containing the coroots of \(\Psi\).
Then its [[lie-groups/centralizer-of-a-lie-subalgebra|centralizer]] is
\[
C_{\mathfrak g}(\mathfrak k)
=\mathfrak t_0\oplus\bigoplus_{\beta\in\Omega}\mathfrak g_\beta,
\]
where
\[
\mathfrak t_0
=\{H\in\mathfrak h:\alpha(H)=0\text{ for all }\alpha\in\Psi\}
\]
and \(\Omega\) consists of the roots \(\beta\in\Phi\) satisfying
\[
\beta|_{\mathfrak t}=0
\quad\text{and}\quad
[\mathfrak g_\beta,\mathfrak g_\alpha]=0
\text{ for every }\alpha\in\Psi.
\]

## Simply laced simplification

Assume \(\Phi\) is [[lie-groups/simply-laced-root-system|simply laced]]. Because \(\mathfrak t\) contains the coroots of \(\Psi\), the condition \(\beta|_{\mathfrak t}=0\) makes \(\beta\) orthogonal to every root in \(\Psi\). In a simply laced system this already implies \(\beta\pm\alpha\notin\Phi\) for all \(\alpha\in\Psi\). Hence
\[
\Omega=\{\beta\in\Phi:\beta|_{\mathfrak t}=0\}.
\]

Using the [[lie-groups/killing-form|Killing form]] to identify \(\mathfrak h\) and \(\mathfrak h^*\), this says: retain the Cartan directions orthogonal to the root span of \(\mathfrak k\), and retain exactly those ambient [[lie-groups/root-space|root spaces]] whose roots are orthogonal to the entire toral part \(\mathfrak t\).

## Why the toral part matters

If \(\mathfrak k\) has a nontrivial center, then \(\mathfrak t\) can be strictly larger than the span of its coroots. A root can be orthogonal to every root of \(\mathfrak k\) while failing to vanish on these extra central directions. Such a root space does **not** centralize \(\mathfrak k\). Thus replacing \(\beta|_{\mathfrak t}=0\) merely by orthogonality to \(\Psi\) is not valid without an additional hypothesis.

## Non-simply-laced caution

In a non-simply-laced [[lie-groups/root-system|root system]], two orthogonal roots can have a sum that is a root. The bracket condition in the definition of \(\Omega\) must then be checked explicitly; orthogonality alone is insufficient.

## References

1. Eugene B. Dynkin, “Semisimple subalgebras of semisimple Lie algebras,” *Matematicheskii Sbornik* 30(72), no. 2 (1952), 349–462; English translation, *AMS Translations*, Series 2, vol. 6 (1957), 111–244. [Journal record](https://www.mathnet.ru/eng/sm5435).
2. John C. Baez, “Three Generations in \(E_7\),” 2026, §§3, 6–7. [arXiv record](https://arxiv.org/abs/2608.06271).
