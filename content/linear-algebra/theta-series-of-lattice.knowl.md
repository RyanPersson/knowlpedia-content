+++
id = "linear-algebra/theta-series-of-lattice"
title = "Theta series of a positive definite lattice"
kind = "definition"
summary = "The generating series that counts lattice vectors by their quadratic norm."
aliases = ["lattice theta series", "theta series", "theta series of a quaternion order"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-lattice", "linear-algebra/quadratic-form"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
Let \(L\) be a [[linear-algebra/euclidean-lattice|lattice]] and \(Q\) a positive definite [[linear-algebra/quadratic-form|quadratic form]] on its real span such that \(Q(L)\subseteq\mathbb Z\). Its **theta series**, with the norm normalization used here, is
\[
\Theta_{L,Q}(z)=\sum_{x\in L}q^{Q(x)}
=\sum_{n\ge0}r_{L,Q}(n)q^n,
\qquad q=e^{2\pi iz},\quad\operatorname{Im}z>0,
\]
where \(r_{L,Q}(n)=\#\{x\in L:Q(x)=n\}\). Positive definiteness makes these counts finite and the series convergent.

## Quaternion orders

For an order in a definite rational [[algebra-rings/quaternion-algebra|quaternion algebra]], take \(Q=\operatorname{nrd}\). Its theta coefficients count elements of each reduced norm. Related lattices give the coefficients of [[algebra-representation-theory/brandt-matrix|Brandt matrices]].

## Normalization

If a lattice is presented with an even integral [[linear-algebra/bilinear-form|bilinear form]] \(b\), a common convention is \(Q(x)=b(x,x)/2\). Replacing \(Q\) by \(2Q\) replaces \(z\) by \(2z\); it can change the modular level. Consequently one must specify both the lattice and its quadratic form when comparing theta series, including those associated with [[lie-groups/d4-root-lattice|\(D_4\)]] and Hurwitz quaternions.

## References

1. John Voight, *Quaternion Algebras*, [§40.4](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_40), equation (40.4.1), Lemma 40.4.2, and the level convention in Definition 40.4.3.
