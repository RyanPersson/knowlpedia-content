+++
id = "harmonic-analysis/direct-integral-unitary-representations"
title = "Direct integral of unitary representations"
kind = "definition"
summary = "A unitary representation assembled fiberwise from a measurable field of representations on a direct-integral Hilbert space."
aliases = ["continuous direct sum of representations", "disintegration of representations"]
domains = ["harmonic-analysis", "functional-analysis", "lie-groups"]
prerequisites = ["topology/locally-compact-group", "measure-theory/measure-space", "functional-analysis/measurable-field-hilbert-spaces", "lie-groups/strongly-continuous-unitary-representation", "functional-analysis/direct-integral-hilbert-spaces", "measure-theory/almost-everywhere"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a second-countable
[[topology/locally-compact-group|locally compact group]], \((X,\mu)\) a
standard \(\sigma\)-finite
[[measure-theory/measure-space|measure space]], and \((H_x)_{x\in X}\) a
[[functional-analysis/measurable-field-hilbert-spaces|measurable field of Hilbert spaces]]. Suppose \(\pi_x\) is a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]] of \(G\) on \(H_x\), and the action field
\((x,g)\mapsto\pi_x(g)\) is measurable. The **direct
integral representation**
\[
\pi=\int_X^\oplus\pi_x\,d\mu(x)
\]
acts on the
[[functional-analysis/direct-integral-hilbert-spaces|direct-integral Hilbert space]] by \((\pi(g)\xi)_x=\pi_x(g)\xi_x\) [[measure-theory/almost-everywhere|almost everywhere]]. Equalities and
changes of fibers are understood modulo \(\mu\)-null sets.

## Fiberwise integrated form

For \(f\in C_c(G)\), the [[harmonic-analysis/integrated-operator-continuous-representation|integrated operator]] is decomposable:
\[
\pi(f)=\int_X^\oplus\pi_x(f)\,d\mu(x).
\]
Thus operator-algebraic questions about \(\pi(f)\) can often be reduced to
almost-everywhere questions about the fibers. This relation also transports
direct-integral decompositions between [[algebra-representation-theory/group-representation|group representations]] and
representations of the
[[operator-algebras/full-group-cstar-algebra|full group \(C^*\)-algebra]].

## Decomposition and multiplicity

For suitable separable type I groups, a unitary representation decomposes
over the [[harmonic-analysis/unitary-dual|unitary dual]] into irreducible
fibers with a measurable multiplicity function. The
[[harmonic-analysis/regular-representations-locally-compact-group|regular representation]] then yields the nonabelian
[[harmonic-analysis/plancherel-measure-nonabelian|Plancherel measure]].
Outside the type I setting, irreducible decompositions can have severe
nonuniqueness, so direct integrals are often taken instead over factor
representations.

## Conventions and scope

“Continuous direct sum” is suggestive but does not mean that
\(x\mapsto H_x\) or \(x\mapsto\pi_x\) is continuous in an ordinary bundle
topology; measurability is the defining regularity. A direct sum is the
special case of counting measure. The phrase “disintegration” may refer
either to constructing this representation from fibers or to a theorem
asserting that a given representation admits such a decomposition.

## References

1. Gerald B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: §7.4 on direct-integral decompositions of representations.
2. Jacques Dixmier, *\(C^*\)-Algebras*, North-Holland, 1977. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/15). Relevant: §§8.5 and 18.7 on measurable fields and disintegration.
