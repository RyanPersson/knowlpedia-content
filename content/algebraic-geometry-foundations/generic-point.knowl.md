+++
id = "algebraic-geometry-foundations/generic-point"
title = "Generic point"
kind = "definition"
summary = "A point whose closure is an entire irreducible closed subset."
aliases = ["generic point", "generic point of an irreducible subset"]
domains = ["algebraic-geometry-foundations"]
+++

The extra point \((0)\) in \(\operatorname{Spec}k[x]\) is not a missing numerical value of \(x\). It records the behavior true away from every proper algebraic condition, which is why it is called generic.

Let \(X\) be a [[algebraic-geometry-foundations/scheme|scheme]] and \(Z\subseteq X\) an [[topology/irreducible-space|irreducible closed subset]]. A point \(\eta\in Z\) is a **generic point of \(Z\)** if

\[
\overline{\{\eta\}}=Z.
\]

Every irreducible closed subset of a scheme has a unique generic point. In particular, if \(A\) is an [[algebra-rings/integral-domain|integral domain]], the [[algebra-rings/prime-ideal|prime ideal]] \((0)\) is the generic point of

\[
\operatorname{Spec}A,
\]

because its closure is all of the [[algebra-commutative/prime-spectrum|prime spectrum]]. Generic points of [[topology/irreducible-space|irreducible components]] encode the components themselves.

**Warning.** A generic point is an actual point of the Zariski topological space, not an informal “typical point” selected by probability or a limiting point in a metric topology. It need not be closed.
