+++
id = "fiber-bundles/complete-flag-bundle"
title = "Complete flag bundle"
kind = "definition"
summary = "The smooth bundle of complete flags in the fibers of a complex vector bundle."
aliases = ["full flag bundle", "flag bundle of a complex vector bundle"]
domains = ["fiber-bundles"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/complex-vector-bundle", "fiber-bundles/frame-bundle-frame-bundle-of-a-rank-n-vector-bundle", "fiber-bundles/associated-bundle", "lie-groups/homogeneous-space", "convex-analysis/linear-subspace"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(E\to X\) be a smooth complex vector bundle of rank \(n\ge0\). Its **complete flag bundle** \(p:\operatorname{Fl}(E)\to X\) has fiber at \(x\) the set of chains of complex vector subspaces
\[
0=V_0\subset V_1\subset\cdots\subset V_n=E_x,
\qquad \dim_{\mathbb C}V_j=j.
\]
The standard flag manifold \(\operatorname{Fl}(\mathbb C^n)\) is the smooth homogeneous space \(\operatorname{GL}(n,\mathbb C)/B\), where \(B\) is the closed subgroup of invertible upper-triangular matrices, the stabilizer of the coordinate flag. Local trivializations of \(E\) identify \(\operatorname{Fl}(E)|_U\) with \(U\times\operatorname{Fl}(\mathbb C^n)\); these charts specify the topology and smooth structure. Equivalently,
\[
\operatorname{Fl}(E)=\operatorname{Fr}(E)\times_{\operatorname{GL}(n,\mathbb C)}\operatorname{Fl}(\mathbb C^n)
\]
is the [[fiber-bundles/associated-bundle|associated bundle]] for the natural left action on flags and the right action on the complex frame bundle. The projection sends a flag in \(E_x\) to \(x\). For \(n=0\), the unique empty flag gives \(\operatorname{Fl}(E)=X\).

## Tautological filtration

The pulled-back bundle \(p^*E\) has subbundles \(F_j\) whose fiber at a flag \((V_\bullet)\) is \(V_j\). The quotients \(L_j=F_j/F_{j-1}\) are complex line bundles. A Hermitian metric splits this filtration smoothly, while the filtration and quotients require no chosen metric.
