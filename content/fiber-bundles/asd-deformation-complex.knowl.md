+++
id = "fiber-bundles/asd-deformation-complex"
title = "ASD deformation complex"
kind = "definition"
summary = "The elliptic complex whose cohomology records infinitesimal gauge symmetries, deformations, and obstructions of an anti-self-dual connection."
aliases = ["anti-self-dual deformation complex", "instanton deformation complex"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(A\) be an [[fiber-bundles/self-dual-and-anti-self-dual-connection|anti-self-dual connection]] on a principal \(G\)-bundle \(P\to X\) over an oriented Riemannian four-manifold. The **ASD deformation complex at \(A\)** is
\[
0\longrightarrow\Omega^0(X;\operatorname{ad}P)
\xrightarrow{\,d_A\,}
\Omega^1(X;\operatorname{ad}P)
\xrightarrow{\,d_A^+\,}
\Omega^{2,+}(X;\operatorname{ad}P)
\longrightarrow0,
\]
where \(d_A\) is the [[fiber-bundles/covariant-exterior-derivative-on-ad-valued-forms|covariant exterior derivative]] and \(d_A^+=\operatorname{pr}_+\circ d_A\). The identity \(d_A^+d_A\phi=[F_A^+,\phi]=0\) makes this a complex. Its cohomology groups \(H_A^0,H_A^1,H_A^2\) record, respectively, infinitesimal stabilizers, infinitesimal ASD deformations modulo infinitesimal [[fiber-bundles/gauge-transformation|gauge transformations]], and obstructions to extending infinitesimal deformations.
It is precisely the linear complex obtained from the ASD equation and the infinitesimal gauge action at the connection.

## Ellipticity

The symbol sequence is exact away from the [[fiber-bundles/zero-section|zero section]], so the complex is elliptic. On a [[topology/closed-manifold|closed manifold]] its Sobolev completions are Fredholm and all three cohomology groups are finite-dimensional. Combining the last differential with the [[fiber-bundles/formal-adjoint-of-covariant-exterior-derivative|formal adjoint]] of the first gives the elliptic operator
\[
d_A^*\oplus d_A^+:
\Omega^1(X;\operatorname{ad}P)\longrightarrow
\Omega^0(X;\operatorname{ad}P)\oplus\Omega^{2,+}(X;\operatorname{ad}P).
\]
Its kernel is a canonical harmonic model for \(H_A^1\).

## Interpretation of the cohomology

The [[lie-groups/lie-algebra|Lie algebra]] of the stabilizer of \(A\) is \(H_A^0=\ker d_A\). The Zariski [[differential-geometry/tangent-space|tangent space]] to the [[fiber-bundles/anti-self-dual-moduli-space|ASD moduli space]] is \(H_A^1=\ker d_A^+/\operatorname{im}d_A\). Finally,
\[
H_A^2=\Omega^{2,+}(X;\operatorname{ad}P)/\operatorname{im}d_A^+
\]
is the cokernel of the linearized ASD equation after [[fiber-bundles/gauge-fixing-condition|gauge fixing]]. Vanishing of \(H_A^2\) is the regularity condition used in the implicit-function theorem.

## Index and conventions

The index \(\dim H_A^1-\dim H_A^0-\dim H_A^2\) is computed topologically by the Atiyah–Singer index theorem. Some sources study self-dual connections instead; they then replace \(\Omega^{2,+}\) by \(\Omega^{2,-}\). Reversing the orientation exchanges the two complexes.

## References

1. Michael F. Atiyah, Nigel J. Hitchin, and Isadore M. Singer, “Self-Duality in Four-Dimensional Riemannian Geometry,” *Proceedings of the Royal Society A* 362 (1978), 425–461. [DOI record](https://doi.org/10.1098/rspa.1978.0143). Relevant: the elliptic deformation complex and its index.
2. Simon K. Donaldson and Peter B. Kronheimer, *The Geometry of Four-Manifolds*, Oxford University Press, 1990. [DOI record](https://doi.org/10.1093/oso/9780198535539.001.0001). Relevant: §§4.2–4.3, infinitesimal deformations and obstruction spaces.
