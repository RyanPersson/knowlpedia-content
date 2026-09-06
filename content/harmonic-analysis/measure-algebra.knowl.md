+++
id = "harmonic-analysis/measure-algebra"
title = "Measure algebra of a locally compact group"
kind = "definition"
summary = "The measure algebra of a locally compact group is the Banach algebra of bounded regular complex Borel measures under convolution."
aliases = ["measure convolution algebra", "M(G)"]
domains = ["harmonic-analysis", "measure-theory", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["topology/locally-compact-group", "linear-algebra/vector-space", "measure-theory/product-measure", "functional-analysis/banach-algebra", "harmonic-analysis/convolution-on-locally-compact-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[topology/locally-compact-group|locally compact Hausdorff group]]. Its **measure algebra** \(M(G)\) is the [[linear-algebra/vector-space|vector space]] of bounded regular complex Borel measures on \(G\), equipped with the total-variation norm and convolution determined by
\[
\int_G f(z)\,d(\mu*\nu)(z)
=\int_G\int_G f(xy)\,d\mu(x)\,d\nu(y)
\]
for every \(f\in C_0(G)\). Equivalently, \((\mu*\nu)(E)\) is obtained by pushing the [[measure-theory/product-measure|product measure]] forward along group multiplication. With this product, \(M(G)\) is a unital [[functional-analysis/banach-algebra|Banach algebra]] whose identity is the point mass \(\delta_e\).

## Point masses and the group law

For \(x,y\in G\), convolution satisfies
\[
\delta_x*\delta_y=\delta_{xy}.
\]
Thus \(x\mapsto\delta_x\) embeds the group law into the invertible elements of \(M(G)\). The involution is characterized by \(\delta_x^*=\delta_{x^{-1}}\) and, on test functions, by conjugation after inversion. Unlike the density formula for \(L^1(G)\), this measure-level description requires no chosen Haar measure.

## Relation to the group algebra

After fixing a left [[harmonic-analysis/haar-measure|Haar measure]] \(m\), each \(f\in L^1(G,m)\) determines the measure \(f\,dm\). This identifies the [[harmonic-analysis/l1-group-algebra|\(L^1\) group algebra]] isometrically with a closed [[algebra-rings/two-sided-ideal|two-sided ideal]] in \(M(G)\). Point masses at nondiscrete points are singular with respect to Haar measure, so \(M(G)\) is generally strictly larger than \(L^1(G)\).

## Examples and scope

If \(G\) is discrete, every bounded measure is an absolutely summable family and \(M(G)\cong\ell^1(G)\). For nondiscrete \(G\), \(M(G)\) simultaneously contains integrable densities and atomic measures. On an [[algebra-groups/abelian-group|abelian group]] it is commutative; on a nonabelian group the point-mass calculation shows immediately that it need not be commutative.

**Warning.** Here “bounded” means finite [[real-analysis/total-variation|total variation]], not compact support and not bounded density with respect to Haar measure.

## References

1. E. Hewitt and K. A. Ross, *Abstract Harmonic Analysis*, Volume I, Springer, 1963. [DOI record](https://doi.org/10.1007/978-3-662-40409-6). Relevant: measure algebras and convolution of measures.
2. H. Reiter and J. D. Stegeman, *Classical Harmonic Analysis and Locally Compact Groups*, 2nd ed., Oxford University Press, 2000. [Publisher record](https://global.oup.com/academic/product/classical-harmonic-analysis-and-locally-compact-groups-9780198511892). Relevant: convolution algebras on locally compact groups.
