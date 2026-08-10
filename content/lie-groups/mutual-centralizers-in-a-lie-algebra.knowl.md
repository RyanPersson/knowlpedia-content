+++
id = "lie-groups/mutual-centralizers-in-a-lie-algebra"
title = "Mutual centralizers in a Lie algebra"
kind = "definition"
summary = "Two subalgebras each equal to the full centralizer of the other in an ambient Lie algebra."
aliases = ["mutual centralizers in a Lie algebra", "mutually centralizing Lie subalgebras", "reductive dual pair in a Lie algebra"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Two [[lie-groups/lie-subalgebra|Lie subalgebras]] \(\mathfrak a,\mathfrak b\subseteq\mathfrak g\) are **mutual centralizers in \(\mathfrak g\)** if
\[
C_{\mathfrak g}(\mathfrak a)=\mathfrak b
\qquad\text{and}\qquad
C_{\mathfrak g}(\mathfrak b)=\mathfrak a,
\]
where \(C_{\mathfrak g}(-)\) denotes the [[lie-groups/centralizer-of-a-lie-subalgebra|Lie-algebra centralizer]].

## Consequences

Mutual centralizers commute elementwise:
\[
[\mathfrak a,\mathfrak b]=0.
\]
They also satisfy the double-centralizer property. Consequently, each is determined inside \(\mathfrak g\) by the other.

The converse fails: the condition \([\mathfrak a,\mathfrak b]=0\) gives only
\[
\mathfrak a\subseteq C_{\mathfrak g}(\mathfrak b),
\qquad
\mathfrak b\subseteq C_{\mathfrak g}(\mathfrak a),
\]
and either inclusion may be strict.

Their intersection is central in both:
\[
\mathfrak a\cap\mathfrak b
\subseteq Z(\mathfrak a)\cap Z(\mathfrak b).
\]
If both subalgebras are semisimple, their centers vanish, so the intersection is zero and \(\mathfrak a+\mathfrak b\cong\mathfrak a\oplus\mathfrak b\).

## Exceptional examples

Inside the complex exceptional [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak e_7\), there are embeddings for which
\[
\mathfrak{sl}_2\quad\text{and}\quad\mathfrak{so}_{12}
\]
are mutual centralizers. Another pair is
\[
\mathfrak{sl}_3\quad\text{and}\quad\mathfrak{sl}_6.
\]
Their direct sums are [[lie-groups/maximal-rank-lie-subalgebra|maximal-rank subalgebras]] of \(\mathfrak e_7\); the second is also a [[lie-groups/maximal-lie-subalgebra|maximal proper subalgebra]]. Such pairs are often called **reductive dual pairs** when both members are reductive, though usage of that term can impose further hypotheses in representation theory.

## References

1. Eugene B. Dynkin, “Semisimple subalgebras of semisimple Lie algebras,” *Matematicheskii Sbornik* 30(72), no. 2 (1952), 349–462; English translation, *AMS Translations*, Series 2, vol. 6 (1957), 111–244. [Journal record](https://www.mathnet.ru/eng/sm5435).
2. John C. Baez, “Three Generations in \(E_7\),” 2026, §§6–7. [arXiv record](https://arxiv.org/abs/2608.06271).
