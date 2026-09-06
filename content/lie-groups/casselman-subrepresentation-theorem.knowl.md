+++
id = "lie-groups/casselman-subrepresentation-theorem"
title = "Casselman subrepresentation theorem"
kind = "theorem"
summary = "Every irreducible Harish–Chandra module for a real reductive group embeds into the Harish–Chandra module of a minimal principal-series representation."
aliases = ["subrepresentation theorem", "embedding into principal series"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/real-reductive-lie-group", "lie-groups/maximal-compact-subgroup-real-reductive-group", "lie-groups/minimal-parabolic-subgroup", "lie-groups/harish-chandra-module", "algebra-representation-theory/irreducible-representation", "lie-groups/principal-series-representation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive group]],
\(K\) a
[[lie-groups/maximal-compact-subgroup-real-reductive-group|maximal compact subgroup]], and \(P=MAN\) a
[[lie-groups/minimal-parabolic-subgroup|minimal parabolic subgroup]]. The
**Casselman subrepresentation theorem** states that every
irreducible [[lie-groups/harish-chandra-module|Harish–Chandra module]] \(V\) for \((\mathfrak g,K)\) admits an
injective \((\mathfrak g,K)\)-homomorphism
\[
V\hookrightarrow
\operatorname{Ind}_{P}^{G}(\sigma\otimes e^\nu\otimes 1_N)_{K\text{-finite}}
\]
for some finite-dimensional [[algebra-representation-theory/irreducible-representation|irreducible representation]] \(\sigma\) of \(M\)
and some \(\nu\in\mathfrak a_{\mathbb C}^{*}\). Thus every irreducible
admissible module occurs as a submodule of a generally nonunitary
[[lie-groups/principal-series-representation|principal series]]. The embedding
is algebraic and need not split.

## Meaning of the hypotheses

A Harish–Chandra module here is a finitely generated admissible
\((\mathfrak g,K)\)-module on which the \(K\)-action is algebraic and compatible
with the differentiated \(\mathfrak g\)-action. Irreducibility is taken in this
algebraic category. The principal series in the target is likewise replaced by
its \(K\)-finite vectors, so the theorem does not assert an embedding between
arbitrary Hilbert completions.

## Proof mechanism and uses

Casselman’s Jacquet-module construction produces a nonzero exponent and
finite-dimensional \(MA\)-data. Frobenius reciprocity then converts the
resulting quotient of a Jacquet module into an embedding of \(V\) into induced
representation data. This connects asymptotic expansions of matrix
coefficients with principal series and underlies comparison results for
globalizations.

## Scope and contrast

The theorem is complementary to the [[lie-groups/langlands-classification-real-reductive-groups|Langlands quotient theorem]]: Casselman
embeds an irreducible module into some principal series, whereas Langlands
realizes it as the unique quotient of a positively ordered standard module.
Neither statement says that every irreducible representation is itself a full
principal-series module, and the inducing data in Casselman’s embedding need
not be unique.

## References

1. William Casselman, “Jacquet Modules for Real Reductive Groups,” in *Proceedings of the International Congress of Mathematicians, Helsinki 1978*, vol. 1, Academia Scientiarum Fennica, 1980, 557–563. [IMU proceedings PDF](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1978.2/ICM1978.2.ocr.pdf). Relevant: Jacquet modules, asymptotics, and embeddings into induced representations.
2. William Casselman, “Jacquet Modules for Real Reductive Groups.” [Author-maintained publication record](https://personal.math.ubc.ca/~cass/research/publications.html). Relevant: bibliographic record and original article pagination.
