+++
id = "lie-groups/standard-module-real-reductive-group"
title = "Standard module of a real reductive group"
kind = "definition"
summary = "A standard module is a normalized parabolically induced representation with tempered Levi data and an inducing parameter in a chosen positive chamber."
aliases = ["Langlands standard representation", "standard induced module"]
domains = ["lie-groups"]
section_mode = "progressive"
+++

Let \(G\) be a [[lie-groups/real-reductive-lie-group|real reductive Lie group]],
let \(P=MAN\) be a [[lie-groups/langlands-decomposition-of-a-parabolic|Langlands decomposition]] of a standard parabolic subgroup, and choose
[[lie-groups/positive-root|positive roots]] for \((P,A)\). If \(\sigma\) is an
irreducible tempered representation of \(M\) and
\(\nu\in\mathfrak a_{\mathbb C}^{*}\) has real part in the open positive
chamber, the **standard module**
\[
I(P,\sigma,\nu)=\operatorname{Ind}_{P}^{G}
   \bigl(\sigma\otimes e^\nu\otimes 1_N\bigr)
\]
is formed using
[[lie-groups/normalized-parabolic-induction|normalized parabolic induction]].
The same name is used for its
smooth globalization and for its underlying admissible \((\mathfrak g,K)\)-module
when that choice is clear.

## Role in the Langlands classification

The positivity of \(\operatorname{Re}\nu\) orders the inducing data and is what
distinguishes a standard module from an arbitrary parabolically induced
representation. The Langlands classification theorem says that a standard
module has a unique irreducible quotient and that every irreducible admissible
representation occurs in this way, with its data unique up to the customary
conjugacies [Langlands, §3, Lemmas 3.13–3.14, and §4, Lemma 4.2].
That quotient is the [[lie-groups/langlands-quotient|Langlands quotient]].

## Example

For \(G=\mathrm{SL}(2,\mathbb R)\), take its upper-triangular minimal parabolic.
A character of the split diagonal factor with positive real parameter produces
a standard principal-series module. At reducibility parameters the induced
module can have several irreducible subquotients, but the positive-chamber
ordering still singles out one irreducible quotient.

## Conventions and scope

**Warning.** Authors may place \(e^\nu\), \(e^{\nu+\rho_P}\), or
\(e^{\nu-\rho_P}\) in the displayed inducing data. These formulas describe the
same normalized induction only after the half-density convention is accounted
for. Some treatments absorb the split center of \(M\) into \(A\), or begin with
relative discrete-series data rather than saying “tempered.” The chamber
condition must therefore be read together with the chosen \(MAN\) convention.

## References

1. Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton Mathematical Series 36, Princeton University Press, 1986. [Author-maintained record](https://www.math.stonybrook.edu/~aknapp/books/repthy1.html). Relevant: Chapter XIV on the Langlands classification and standard induced modules.
2. Robert P. Langlands, *On the Classification of Irreducible Representations of Real Algebraic Groups*, Institute for Advanced Study, 1973. [Author PDF](https://publications.ias.edu/sites/default/files/classification-algebraic-groups_rpl_7.pdf). Relevant: §3, Lemmas 3.13–3.14 on the canonical irreducible quotient and uniqueness, and §4, Lemma 4.2 on exhaustion.
