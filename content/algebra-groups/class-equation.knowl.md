+++
id = "algebra-groups/class-equation"
title = "Class Equation"
kind = "knowl"
summary = "The order of a finite group is the order of its center plus the sizes of its noncentral conjugacy classes."
aliases = ["class-equation", "Class Equation"]
domains = ["algebra-groups"]
legacy_source_path = "algebra-groups/class-equation.md"
+++

Let \(G\) be a finite [[algebra-groups/group|group]]. For \(g\in G\), set
\[
\operatorname{Cl}(g)=\{xgx^{-1}: x\in G\},
\]
and let the [[algebra-groups/centralizer|centralizer]] be
\[
C_G(g)=\{x\in G : xg=gx\}.
\]

Then \(|\operatorname{Cl}(g)|=[G:C_G(g)]\). If \(g_1,\dots,g_r\) represent the noncentral [[algebra-groups/conjugacy-class|conjugacy classes]], the **class equation** is
\[
|G| = |Z(G)| + \sum_{i=1}^r [G:C_G(g_i)].
\]

## Remarks

The class equation is the orbit decomposition of the [[algebra-groups/conjugation-action|conjugation action]] of \(G\) on itself, combined with the [[algebra-groups/orbit-stabilizer-theorem|orbit–stabilizer theorem]]. It is a standard tool for proving existence of normal subgroups, for example [[algebra-groups/p-group-nontrivial-center|a finite p-group has nontrivial center]].
