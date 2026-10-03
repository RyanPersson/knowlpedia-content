+++
id = "catalog/finite-groups/relationships/cyclic-group-homomorphisms"
title = "Hom, End, and Aut for finite cyclic groups"
kind = "theorem"
summary = "A map from C_m to C_n is determined by an m-torsion element of C_n; there are gcd(m,n) such homomorphisms."
aliases = ["homomorphisms of finite cyclic groups"]
domains = ["catalog", "algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/group-homomorphism", "algebra-groups/finite-cyclic-isomorphic-zn", "algebra-groups/automorphism-group-cyclic"]
dependency_heuristic = "finite-groups-semantic-review-v1"
dependency_review_count = 1
+++

Let \(m,n\geq1\) be integers and write the [[algebra-groups/finite-cyclic-isomorphic-zn|cyclic groups]] additively as \(C_m=\mathbb Z/m\mathbb Z\) and \(C_n=\mathbb Z/n\mathbb Z\). Evaluation at \(1\) identifies the [[algebra-groups/group-homomorphism|group homomorphisms]] with the residues \(a\in\mathbb Z/n\mathbb Z\) satisfying \(ma=0\): the corresponding map is \(f_a([k]_m)=[ka]_n\). Thus
\[
|\operatorname{Hom}_{\mathbf{Grp}}(C_m,C_n)|=\gcd(m,n),\qquad
\operatorname{End}_{\mathbf{Grp}}(C_n)\cong\mathbb Z/n\mathbb Z,
\qquad
\operatorname{Aut}_{\mathbf{Grp}}(C_n)\cong(\mathbb Z/n\mathbb Z)^\times.
\]
The middle isomorphism is of rings, with pointwise addition of endomorphisms and composition as multiplication. The last is an [[algebra-groups/automorphism-group-cyclic|isomorphism of groups]].

## Verification

A homomorphism must send \([k]_m\) to \(k f([1]_m)\). It is well-defined exactly when the relation \(m[1]_m=0\) is preserved, which says \(n\mid ma\). Put \(d=\gcd(m,n)\). This divisibility is equivalent to \(n/d\mid a\), giving the \(d\) residues \(0,n/d,\ldots,(d-1)n/d\).

For \(m=n\), every residue is allowed and \(f_a\circ f_b=f_{ab}\). Such a map is invertible precisely when \(a\) is a unit modulo \(n\). The formula also covers \(n=1\): there is one map and it is the identity on the trivial group.

## Forgetting the group structure changes the answer

The underlying sets admit \(n^m\) functions from \(C_m\) to \(C_n\), while the groups admit only \(\gcd(m,n)\) homomorphisms. In particular, \(C_2\to C_3\) has nine set maps but just one group map, the zero map.

For one group \(C_n\), the set endomorphisms number \(n^n\) and the set automorphisms number \(n!\); the group endomorphisms number \(n\). The categories of groups, [[catalog/categories/finite-groups|finite groups]], and [[catalog/categories/abelian-groups|abelian groups]] give the same homomorphisms on these objects.
