+++
id = "differential-geometry/grassmannian"
title = "Grassmannian"
kind = "definition"
summary = "The parameter space of all subspaces of a fixed dimension in a finite-dimensional vector space."
aliases = ["Grassmann manifold", "k-plane Grassmannian"]
domains = ["differential-geometry", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(V\) be an \(n\)-dimensional [[linear-algebra/vector-space|vector space]] over \(\mathbb F=\mathbb R\) or \(\mathbb C\), and let \(0\leq k\leq n\). The **Grassmannian**
\[
\operatorname{Gr}_k(V)=\{W\subseteq V:\dim_{\mathbb F}W=k\}
\]
is the set of all \(k\)-dimensional [[convex-analysis/linear-subspace|linear subspaces]] of \(V\), equipped with its natural smooth-manifold structure. It has real dimension \(k(n-k)\) when \(\mathbb F=\mathbb R\), and complex dimension \(k(n-k)\) when \(\mathbb F=\mathbb C\). The cases \(k=0,n\) are single points.

## Local charts and tangent spaces

Choose a decomposition \(V=W\oplus W'\). Every \(k\)-plane sufficiently near \(W\) is uniquely the graph of a [[linear-algebra/linear-map|linear map]] \(A:W\to W'\), giving a chart modeled on \(\operatorname{Hom}(W,W')\). Intrinsically, the [[differential-geometry/tangent-space|tangent space]] at \(W\) is
\[
T_W\operatorname{Gr}_k(V)\cong\operatorname{Hom}(W,V/W).
\]
These charts exhibit the stated dimension and make the construction independent of a chosen basis.

## Homogeneous-space models

After choosing an [[linear-algebra/inner-product|inner product]], the real Grassmannian is
\[
\operatorname{Gr}_k(\mathbb R^n)\cong O(n)/(O(k)\times O(n-k)).
\]
With a Hermitian inner product, the complex Grassmannian is \(U(n)/(U(k)\times U(n-k))\). These presentations show that the Grassmannians are compact [[fiber-bundles/smooth-manifold|smooth manifolds]] and relate their geometry to transitive Lie-group actions.

## Algebraic and bundle structure

For complex \(V\), the Plücker map sends \(W\) to the line \(\bigwedge^kW\subseteq\bigwedge^kV\), realizing the Grassmannian as a smooth projective algebraic variety cut out by quadratic Plücker relations. Over the Grassmannian, the fibers \(W\) themselves form the tautological rank-\(k\) [[fiber-bundles/vector-bundle|vector bundle]].

## References

1. J. Harris, *Algebraic Geometry: A First Course*, Springer, 1992. [Springer DOI record](https://doi.org/10.1007/978-1-4757-2189-8). Relevant: Lecture 6.
2. J. Milnor and J. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [Princeton DOI record](https://doi.org/10.1515/9781400881826). Relevant: §5 and Grassmannians as classifying spaces.
