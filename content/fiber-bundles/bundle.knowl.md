+++
id = "fiber-bundles/bundle"
title = "Bundle"
kind = "definition"
summary = "A space equipped with a continuous surjection to a base, organizing its points into fibers."
aliases = ["bundle", "bundle projection"]
domains = ["fiber-bundles", "topology"]
section_mode = "progressive"
prerequisites = ["topology/topological-space", "topology/continuous-map", "shared-foundations/surjective-function", "shared-foundations/preimage"]
+++

A **bundle** in the broad topological sense used here is a triple \((E,\pi,B)\), where \(E\) and \(B\) are [[topology/topological-space|topological spaces]] and \(\pi:E\to B\) is a [[topology/continuous-map|continuous]] [[shared-foundations/surjective-function|surjection]]. The space \(E\) is the **total space**, \(B\) is the **base space**, and \(\pi\) is the **bundle projection**. Its [[fiber-bundles/fiber-of-a-map|fiber]] over \(b\in B\) is the subspace
\[
E_b=\pi^{-1}(b)=\{e\in E:\pi(e)=b\}.
\]
This definition alone imposes no local product condition.

## Local triviality and terminology

A [[fiber-bundles/fiber-bundle|fiber bundle]] adds local triviality with a fixed model fiber. A [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]] requires smooth local product charts. Many authors use “bundle” as shorthand for one of these stronger notions; the surrounding category and adjectives specify the intended meaning.

## Example without local triviality

The map \(\pi:\mathbb R\to[0,\infty)\), \(\pi(t)=t^2\), is a continuous surjection. Its fiber over \(0\) has one point, whereas each positive fiber has two. Thus it is a bundle in the broad sense above, but no neighborhood of \(0\) admits a trivialization with one fixed fiber.
