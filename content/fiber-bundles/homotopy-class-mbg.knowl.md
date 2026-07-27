+++
id = "fiber-bundles/homotopy-class-mbg"
title = "Homotopy class [M,BG]"
kind = "knowl"
summary = "The set of unbased homotopy classes of maps from a manifold to a classifying space."
aliases = ["homotopy-class-mbg", "Homotopy class [M,BG]"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/homotopy-class-mbg.md"
+++

Let $M$ be a [[fiber-bundles/smooth-manifold|smooth manifold]] and $BG$ a classifying space for a [[fiber-bundles/lie-group|Lie group]] $G$. The notation
$$
[M,BG]
$$
denotes the set of unbased homotopy classes of continuous maps $M\to BG$.

Thus $f_0,f_1:M\to BG$ represent the same class exactly when there is a continuous map
$$
H\colon M\times [0,1] \to BG,\qquad H(\cdot,0)=f_0,\; H(\cdot,1)=f_1.
$$

If $\phi:M'\to M$ is a [[fiber-bundles/diffeomorphism|diffeomorphism]], precomposition induces a bijection
$$
[M,BG] \xrightarrow{\;\cong\;} [M',BG], \quad [f]\mapsto [f\circ \phi].
$$

Under the usual hypotheses of the classifying-space theorem, $[M,BG]$ classifies principal $G$-bundles over $M$ by sending a bundle to the homotopy class of a [[fiber-bundles/classifying-map-of-a-principal-bundle|classifying map]].

## Examples
1. **Spheres.** The based homotopy set satisfies $[S^n,BG]_*=\pi_n(BG)$. Passing to unbased classes may further identify elements through the fundamental-group action, so it should not be suppressed without an additional hypothesis.
2. **Contractible bases.** If $M$ is nonempty and contractible and $BG$ is path-connected, then $[M,BG]$ has one element.
3. **Line bundles.** For $G=U(1)$, one has $BG\simeq \mathbb CP^\infty$, and $[M,BG]$ corresponds to isomorphism classes of principal $U(1)$-bundles, equivalently complex line bundles, over $M$.
