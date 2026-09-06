+++
id = "supergeometry/super-harish-chandra-pair"
title = "Super Harish–Chandra pair"
kind = "definition"
summary = "A Lie group and Lie superalgebra with compatible adjoint data encoding a smooth Lie supergroup."
aliases = ["Harish-Chandra pair for a Lie supergroup", "SHCP"]
domains = ["supergeometry", "lie-groups"]
prerequisites = ["fiber-bundles/lie-group", "supergeometry/lie-superalgebra", "algebra-groups/group-action", "lie-groups/harish-chandra-module"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **super Harish–Chandra pair** over \(\mathbb R\) is a pair
\((G_0,\mathfrak g)\) consisting of:

1. a finite-dimensional real [[fiber-bundles/lie-group|Lie group]] \(G_0\);
2. a finite-dimensional real
   [[supergeometry/lie-superalgebra|Lie superalgebra]]
   \(\mathfrak g=\mathfrak g_{\bar0}\oplus\mathfrak g_{\bar1}\);
3. an identification
   \(\mathfrak g_{\bar0}\cong\operatorname{Lie}(G_0)\);
4. a smooth action
   \(\operatorname{Ad}:G_0\to\operatorname{Aut}_{\bar0}(\mathfrak g)\)
   by even Lie-superalgebra automorphisms.

The action restricts on \(\mathfrak g_{\bar0}\) to the ordinary adjoint
action of \(G_0\), and its differential at the identity is the adjoint action
of \(\mathfrak g_{\bar0}\) on all of \(\mathfrak g\).

A morphism
\((G_0,\mathfrak g)\to(H_0,\mathfrak h)\) is a Lie-group homomorphism
\(\Phi_0:G_0\to H_0\) and an even Lie-superalgebra homomorphism
\(\phi:\mathfrak g\to\mathfrak h\), compatible with the even-part
identifications and the two [[algebra-groups/group-action|group actions]].

The adjective “super” is important: this object is not a
[[lie-groups/harish-chandra-module|Harish–Chandra module]] from the representation theory of real reductive
groups.

## References

1. A. Alldridge, J. Hilgert, and T. Wurzbacher, “Singular superspaces,” *Mathematische Zeitschrift* 278, 2014, 441–492. [Article](https://doi.org/10.1007/s00209-014-1328-7). Relevant: super Harish–Chandra pair conventions.
2. C. Carmeli, L. Caston, and R. Fioresi, *Mathematical Foundations of Supersymmetry*, EMS, 2011. [Publisher record](https://doi.org/10.4171/097). Relevant: Chapter 7.
