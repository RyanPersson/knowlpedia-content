+++
id = "harmonic-analysis/unramified-representation-p-adic-group"
title = "Unramified representation of a p-adic group"
kind = "definition"
summary = "An irreducible admissible representation with a nonzero hyperspecial-fixed vector."
aliases = ["unramified p-adic representation", "spherical unramified representation"]
domains = ["harmonic-analysis", "langlands", "lie-groups"]
prerequisites = ["algebraic-geometry-foundations/unramified-reductive-group", "algebra-fields-galois/nonarchimedean-local-field", "langlands-letter/knowls/maximal-compact-hyperspecial", "harmonic-analysis/admissible-representation-p-adic-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(\mathbf G\) be an
[[algebraic-geometry-foundations/unramified-reductive-group|unramified
connected reductive group]] over a
[[algebra-fields-galois/nonarchimedean-local-field|nonarchimedean local field]] \(F\), and let \(K\leq G=\mathbf G(F)\) be a
[[langlands-letter/knowls/maximal-compact-hyperspecial|hyperspecial maximal
compact subgroup]]. An irreducible
[[harmonic-analysis/admissible-representation-p-adic-group|admissible smooth
representation]] \(\pi\) of \(G\) is **unramified with respect to \(K\)** if

\[
\pi^K\ne0.
\]

The pair \((G,K)\) is spherical, so \(\dim\pi^K=1\). A nonzero vector in this
line is an unramified, or spherical, vector.

## Satake classification

The [[harmonic-analysis/hecke-algebra-locally-compact-group-pair|spherical Hecke algebra]] acts on \(\pi^K\) through a character. The
normalized Satake isomorphism turns this character into the
[[langlands/satake-parameter|Satake parameter]] of \(\pi\), a semisimple
[[algebra-groups/conjugacy-class|conjugacy class]] in the appropriate Frobenius coset of the
[[langlands/l-group|\(L\)-group]].

## Choice and terminology

The adjective depends on the chosen integral model, hence on \(K\), although
hyperspecial subgroups are suitably conjugate in the standard unramified
setting. “Spherical representation” is also used more broadly for any
representation with [[lie-groups/fixed-vector-subspace|fixed vectors]] under a chosen maximal compact subgroup;
the present definition is specifically nonarchimedean and hyperspecial.

## References

1. Armand Borel, “Automorphic \(L\)-functions,” in *Automorphic Forms,
   Representations and \(L\)-Functions*, Proceedings of Symposia in Pure
   Mathematics 33, part 2, 1979, §§3–4.
2. Jayce R. Getz, *An Introduction to Automorphic Representations*, §9.
   [Author notes](https://sites.math.duke.edu/~jgetz/aut_reps.pdf).
