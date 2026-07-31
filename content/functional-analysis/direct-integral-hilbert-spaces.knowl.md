+++
id = "functional-analysis/direct-integral-hilbert-spaces"
title = "Direct integral of Hilbert spaces"
kind = "construction"
summary = "The Hilbert space of square-integrable measurable sections of a measurable field of Hilbert spaces."
aliases = ["Hilbert direct integral", "continuous Hilbert sum", "continuous direct sum"]
domains = ["functional-analysis", "measure-theory"]
section_mode = "progressive"
+++

Let \((X,\Sigma,\mu)\) be a [[measure-theory/measure-space|measure space]] and \(\{\mathcal H_x\}_{x\in X}\) a [[functional-analysis/measurable-field-hilbert-spaces|measurable field of Hilbert spaces]]. Its **direct integral** is
\[
\int_X^\oplus \mathcal H_x\,d\mu(x),
\]
the space of measurable sections \(\xi\), modulo equality [[measure-theory/almost-everywhere|almost everywhere]], for which the [[measure-theory/lebesgue-integral|Lebesgue integral]] \(\int_X\|\xi(x)\|^2\,d\mu(x)\) is finite. Addition and scalar multiplication are fiberwise, and
\[
\langle\xi,\eta\rangle=\int_X\langle\xi(x),\eta(x)\rangle_{\mathcal H_x}\,d\mu(x).
\]
After quotienting by null sections, this is a [[linear-algebra/hilbert-space|Hilbert space]]. The construction is the measure-theoretic analogue of a Hilbert direct sum.

## Constant fields and direct sums

For a constant field \(\mathcal H_x=K\), the direct integral is the vector-valued space \(L^2(X,\mu;K)\). If \(X\) has counting measure, it reduces to the Hilbert direct sum \(\bigoplus_{x\in X}\mathcal H_x\). Atomic and continuous parts of the measure therefore interpolate between discrete sums and continuously indexed decompositions.

## Decomposable operators

Suppose \(T_x:\mathcal H_x\to\mathcal K_x\) is a measurable field of bounded operators with essentially bounded norms. Then
\[
\left(\int_X^\oplus T_x\,d\mu(x)\right)\xi(x)=T_x\xi(x)
\]
defines a bounded operator between the corresponding direct integrals. Such [[functional-analysis/decomposable-operator|decomposable operators]] preserve the fiberwise structure and are basic tools in spectral and representation-theoretic decompositions.

## Conventions and use

The phrase “measurable field” includes the chosen measurable structure on sections; a bare family of Hilbert spaces is not enough. Changing fibers or sections on a [[measure-theory/null-set|null set]] does not change the direct integral. Standard decomposition theorems usually impose \(\sigma\)-finiteness and separability hypotheses, which must be stated separately from the construction [Takesaki, Chapter IV, §8].

## References

1. Masamichi Takesaki, *Theory of Operator Algebras I*, Springer, 1979. [DOI record](https://doi.org/10.1007/978-1-4612-6188-9). Relevant: Chapter IV, §8 on direct integrals.
2. Jacques Dixmier, *Von Neumann Algebras*, North-Holland, 1981. [Publisher record](https://www.sciencedirect.com/bookseries/north-holland-mathematical-library/vol/27/suppl/C). Relevant: Chapter II, §1 on measurable fields and direct integrals.
