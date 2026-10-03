+++
id = "ergodic-theory/first-return-map"
title = "First-return map"
kind = "definition"
summary = "The dynamics induced by recording the next visit to a chosen subset or transverse section."
aliases = ["Poincare return map", "Poincaré return map"]
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/measure-preserving-system"]
+++

For a transformation \(T:X\to X\) and a subset \(E\), define the **first-return time**
\[
r_E(x)=\min\{n\geq1:T^nx\in E\}
\]
where this set is nonempty. The **first-return map** is \(T_E(x)=T^{r_E(x)}x\). In a [[ergodic-theory/measure-preserving-system|probability-preserving system]] it is defined for almost every \(x\in E\), by recurrence.

## Flows and sections

For a smooth flow and a transverse section, a Poincaré return map records the next intersection at positive time wherever a first such intersection exists. The flow's invariant volume need not restrict to a useful measure on a lower-dimensional section; an invariant transverse measure is a separate construction.

For the flow \((x,y)\mapsto(x+t,y+\theta t)\) on \(\mathbb T^2\), the section \(x=0\) has constant return time one and return map \(y\mapsto y+\theta\).
