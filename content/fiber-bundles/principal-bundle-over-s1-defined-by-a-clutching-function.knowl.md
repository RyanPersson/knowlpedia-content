+++
id = "fiber-bundles/principal-bundle-over-s1-defined-by-a-clutching-function"
title = "Principal bundle over S1 from a clutching function"
kind = "knowl"
summary = "A principal G-bundle over the circle obtained by gluing the ends of a trivial bundle."
aliases = ["principal-bundle-over-s1-defined-by-a-clutching-function", "Principal bundle over S1 from a clutching function"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/principal-bundle-over-s1-defined-by-a-clutching-function.md"
+++

Let \(G\) be a Lie group and \(g\in G\). Regard \(S^1\) as \([0,1]/(0\sim1)\), and define
\[
P_g := \big([0,1]\times G\big)\big/\sim,
\]
where
\[
(0,h)\sim (1,gh)\qquad\text{for all }h\in G.
\]
The projection to \(S^1\), together with the right action
\[
[(t,h)]\cdot k := [(t,hk)]
\]
turns \(P_g\to S^1\) into a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]]. This is the one-dimensional [[fiber-bundles/clutching-function|clutching construction]].

## Classification

The isomorphism class depends only on the conjugacy class of the component of \(g\) in \(\pi_0(G)\), and every principal \(G\)-bundle over \(S^1\) arises this way. Thus connected \(G\) gives only the [[fiber-bundles/trivial-principal-bundle-mgm|trivial principal bundle]]. For discrete \(G\), the classes are the conjugacy classes of elements of \(G\).
