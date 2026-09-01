+++
id = "algebraic-geometry-foundations/connected-scheme"
title = "Connected scheme"
kind = "definition"
summary = "A scheme whose underlying Zariski topological space cannot be split into two nonempty open-and-closed pieces."
aliases = ["connected scheme", "scheme connectedness"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/scheme", "topology/topological-space", "algebra-commutative/zariski-topology", "algebraic-geometry-foundations/affine-scheme"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

A [[algebraic-geometry-foundations/scheme|scheme]] \(X\) is **connected** if its underlying [[topology/topological-space|topological space]] in the [[algebra-commutative/zariski-topology|Zariski topology]] is connected: there do not exist disjoint nonempty open subsets \(U,V\subseteq X\) with \(X=U\cup V\). Equivalently, the only subsets that are both open and closed are \(\varnothing\) and \(X\).

For an [[algebraic-geometry-foundations/affine-scheme|affine scheme]] \(X=\operatorname{Spec}A\), this is equivalent to \(A\) having no idempotents other than \(0\) and \(1\):

\[
e^2=e\quad\Longrightarrow\quad e\in\{0,1\}.
\]

## Example

The decomposition
\[
\operatorname{Spec}(K_1\times K_2)
\cong
\operatorname{Spec}K_1\amalg\operatorname{Spec}K_2
\]
shows that the spectrum of a product of two fields is disconnected, whereas the one-point spectrum of a field is connected.

## Warning

Connected does not mean [[topology/irreducible-space|irreducible]], path connected, or connected in a Euclidean topology. Schemes are being tested in their Zariski topology, whose open sets are usually much larger than familiar analytic open sets.
