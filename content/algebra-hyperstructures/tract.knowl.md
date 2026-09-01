+++
id = "algebra-hyperstructures/tract"
title = "Tract"
kind = "definition"
summary = "An abelian multiplicative group equipped with a null set of formal sums."
aliases = ["tract in matroid theory", "Baker-Bowler tract"]
domains = ["algebra-hyperstructures", "algebraic-geometry-foundations"]
prerequisites = ["algebra-groups/abelian-group", "algebra-groups/group-homomorphism"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **tract** is a pair \(F=(G,N_F)\), where \(G\) is an [[algebra-groups/abelian-group|abelian group]] and \(N_F\subseteq\mathbb N[G]\) is a set of formal sums, called the **null set**, satisfying:

1. the zero formal sum belongs to \(N_F\);
2. the one-term sum \(1\) does not belong to \(N_F\);
3. there is a unique \(\epsilon\in G\) with \(1+\epsilon\in N_F\);
4. \(N_F\) is stable under multiplication by every \(g\in G\).

The underlying pointed multiplicative set is \(F=G\sqcup\{0\}\), with \(F^\times=G\). A morphism of tracts is a [[algebra-groups/group-homomorphism|group homomorphism]] \(G\to G'\) whose linear extension \(\mathbb N[G]\to\mathbb N[G']\) carries \(N_F\) into \(N_{F'}\).

## What a tract remembers

The relation \(\sum g_i\in N_F\) means that the formal sum is declared to be zero. A tract need not provide a binary addition, even a multivalued one. It retains exactly the null relations needed to state orthogonality and Grassmann–Plücker relations for matroids with coefficients.

The distinguished \(\epsilon\) behaves as a formal \(-1\): one proves \(\epsilon^2=1\), and if \(x+y\in N_F\) then \(y=\epsilon x\).

## Examples and inclusions

Fields, [[algebra-hyperstructures/partial-field|partial fields]],
[[algebra-hyperstructures/hyperfield|hyperfields]], and
[[algebra-hyperstructures/partial-hyperfield|partial hyperfields]] determine
tracts through their respective
[[algebra-hyperstructures/partial-field-as-a-tract|partial-field]],
[[algebra-hyperstructures/hyperfield-as-a-tract|hyperfield]], and
[[algebra-hyperstructures/partial-hyperfield-as-a-tract|partial-hyperfield]]
constructions. These constructions do not imply that every tract is a
hyperfield. [[algebra-hyperstructures/pasture|Pastures]] form a structured
subcategory related to three-term null relations, and a tract has an
[[algebra-hyperstructures/tract-as-an-ordered-blueprint|associated ordered
blueprint]].

## References
Matthew Baker and Nathan Bowler, [*Matroids over partial hyperstructures*, §1](https://arxiv.org/abs/1709.09707).
