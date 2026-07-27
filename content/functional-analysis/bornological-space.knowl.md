+++
id = "functional-analysis/bornological-space"
title = "Bornological space"
kind = "definition"
summary = "A locally convex space whose topology is determined by its bounded subsets."
aliases = ["bornologic space"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(E\) be a Hausdorff [[functional-analysis/locally-convex-space|locally convex space]]. A convex balanced set \(D\subseteq E\) is **bornivorous** if it absorbs every [[functional-analysis/bounded-subset-tvs|bounded subset]] \(B\) of \(E\): for each \(B\), some \(r>0\) satisfies \(B\subseteq tD\) whenever \(\lvert t\rvert\ge r\). The space \(E\) is **bornological** if every bornivorous convex balanced set is a neighborhood of \(0\). Equivalently, the locally convex topology of \(E\) is the finest locally convex topology having the same bounded subsets.

## Mapping characterization

The defining condition is equivalent to a useful test: for every locally convex space \(F\), a [[linear-algebra/linear-map|linear map]] \(T:E\to F\) is continuous whenever it maps bounded subsets of \(E\) to bounded subsets of \(F\). Thus boundedness controls continuity on the source. The converse implication—continuous linear maps preserve bounded sets—holds for every [[functional-analysis/topological-vector-space|topological vector space]] and does not require bornologicality [Hogbe-Nlend, Chapters I–II](https://shop.elsevier.com/books/bornologies-and-functional-analysis/hogbe-nlend/978-0-7204-0712-9).

## Examples and permanence

Every metrizable locally convex space, hence every normed or [[functional-analysis/frechet-space|Fréchet space]], is bornological. [[functional-analysis/inductive-limit-locally-convex-spaces|Locally convex inductive limits]] of bornological spaces are bornological, so [[functional-analysis/lf-space|LF-spaces]] provide important nonmetrizable examples. Quotients and locally convex direct sums preserve bornologicality. Arbitrary subspaces need not: the bounded subsets inherited by a subspace may fail to determine its [[topology/subspace-topology|subspace topology]].

## Conventions and contrasts

“Bornological” here is a property of a locally convex topology, not merely the data of an abstract bornology. It differs from [[functional-analysis/barreled-space|barreledness]]: bornologicality detects continuity of bounded linear maps, whereas barreledness supports uniform-boundedness principles for [[real-analysis/pointwise-bounded-family|pointwise bounded families]]. Neither property implies the other without additional hypotheses. Some sources say **bornologic**, but **bornological** is the usual English form.

## References

1. Henri Hogbe-Nlend, *Bornologies and Functional Analysis*, North-Holland Mathematics Studies 26, 1977. [Elsevier publisher record](https://shop.elsevier.com/books/bornologies-and-functional-analysis/hogbe-nlend/978-0-7204-0712-9). Relevant: Chapters I–II on bounded structures and fundamental bornological constructions.
2. Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces*, 2nd ed., Springer, 1999. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1468-7). Relevant: Chapter IV on bornological spaces and dual topologies.
