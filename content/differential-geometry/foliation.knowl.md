+++
id = "differential-geometry/foliation"
title = "Smooth foliation"
kind = "definition"
summary = "A manifold partitioned into immersed leaves that appear locally as parallel coordinate slices."
aliases = ["leaf of a foliation"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/smooth-manifold"]
+++

A **smooth foliation of dimension \(p\)** on an [[fiber-bundles/smooth-manifold|\(n\)-manifold]] is an atlas of charts into open subsets of \(\mathbb R^p\times\mathbb R^{n-p}\) whose transition maps preserve the local slices with fixed second coordinate. Equivalently, locally a transition has the form \((x,y)\mapsto(f(x,y),g(y))\). The connected immersed submanifolds obtained by joining these slices are the **leaves**.

## Leaf space

The quotient that identifies points on the same leaf is the leaf space. It can fail to be Hausdorff, even when the original manifold is compact and smooth. The [[differential-geometry/kronecker-foliation|irrational linear foliation of a torus]] is a basic example.
