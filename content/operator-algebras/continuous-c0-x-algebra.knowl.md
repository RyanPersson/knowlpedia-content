+++
id = "operator-algebras/continuous-c0-x-algebra"
title = "Continuous C_0(X)-algebra"
kind = "definition"
summary = "A C_0(X)-algebra whose quotient-fiber norms are continuous functions of the base point."
aliases = ["continuous C*-algebra over X"]
domains = ["operator-algebras", "topology"]
section_mode = "progressive"
+++

Let \(X\) be a locally compact Hausdorff space and let \(A\) be a [[operator-algebras/c0-x-algebra|\(C_0(X)\)-algebra]]. For \(x\in X\), write \(A_x\) for its [[operator-algebras/fiber-c0-x-algebra|quotient fiber]] and \(a(x)\) for the image of \(a\in A\). The algebra \(A\) is a **continuous \(C_0(X)\)-algebra** when
\[
x\longmapsto\lVert a(x)\rVert
\]
is continuous on \(X\) for every \(a\in A\). These functions already vanish at infinity and are upper semicontinuous for an arbitrary \(C_0(X)\)-algebra; continuity is the additional axiom. The specified central nondegenerate action of \(C_0(X)\), and not merely the abstract \(C^*\)-algebra \(A\), is part of this definition.

## Bundle characterization

The canonical bundle \(\bigsqcup_x A_x\to X\) associated with any \(C_0(X)\)-algebra is upper semicontinuous. It is a [[operator-algebras/continuous-field-cstar-algebra|continuous field of \(C^*\)-algebras]] exactly when \(A\) is continuous in the sense above. Under this correspondence, \(A\) is recovered as the algebra of continuous sections vanishing at infinity [Nilsen, bundle realization and continuity criteria](https://doi.org/10.1512/iumj.1996.45.1086).

Continuity is checked element by element. It neither requires local triviality nor forces all fibers to be isomorphic.

## Examples and non-examples

For any \(C^*\)-algebra \(B\), \(C_0(X,B)\) is continuous: the fiber of \(f\) at \(x\) is \(f(x)\), and \(x\mapsto\lVert f(x)\rVert\) is continuous. Section algebras of locally trivial \(C^*\)-bundles give further examples.

A general upper-semicontinuous bundle can have a section \(a\) whose norm drops discontinuously at a point. Its section algebra remains a \(C_0(X)\)-algebra but is not continuous.

## References

1. M. Nilsen, “\(C^*\)-Bundles and \(C_0(X)\)-Algebras,” *Indiana University Mathematics Journal* 45 (1996), 463–477. [DOI record](https://doi.org/10.1512/iumj.1996.45.1086). Relevant: quotient fibers, sectional representation, and criteria for continuity.
2. É. Blanchard, “Déformations de \(C^*\)-algèbres de Hopf,” *Bulletin de la Société Mathématique de France* 124 (1996), 141–215. [DOI record](https://doi.org/10.24033/bsmf.2278). Relevant: continuous \(C(X)\)-algebras and their field interpretation.
