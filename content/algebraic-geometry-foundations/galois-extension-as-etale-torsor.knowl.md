+++
id = "algebraic-geometry-foundations/galois-extension-as-etale-torsor"
title = "Galois extension as an étale torsor"
kind = "theorem"
summary = "A finite Galois field extension gives a connected finite étale torsor on spectra."
aliases = ["Galois extension as an étale torsor", "Galois torsor of spectra"]
domains = ["algebraic-geometry-foundations"]
+++

Let \(K/F\) be a finite [[algebra-fields-galois/galois-extension|Galois extension]], let \(G=\operatorname{Gal}(K/F)\), and set \(P=\operatorname{Spec}K\) and \(X=\operatorname{Spec}F\). Then \(P\to X\) is finite étale and [[algebraic-geometry-foundations/connected-scheme|connected]]. The action of \(G\) on \(K\) by \(F\)-algebra automorphisms induces, contravariantly, an action on \(P\). With \(G_X\) the [[algebraic-geometry-foundations/constant-finite-group-scheme|constant finite group scheme]], the map

\[
P\times_X G_X\longrightarrow P\times_X P,
\qquad (p,g)\longmapsto(p,p\cdot g)
\]

is an isomorphism. Hence \(P\to X\) is a \(G_X\)-torsor on the [[algebraic-geometry-foundations/small-etale-site|étale site]] of \(X\), in the sense of a [[algebraic-geometry-foundations/g-torsor-on-a-site|\(G\)-torsor on a site]]. The algebra behind the isomorphism is the [[algebraic-geometry-foundations/galois-tensor-product-identity|Galois tensor-product identity]].

Conversely, a connected finite étale \(G_X\)-torsor over \(\operatorname{Spec}F\) has affine total space \(\operatorname{Spec}K\), where \(K/F\) is a finite Galois extension with group \(G\).

## Interpretation

The field inclusion \(F\hookrightarrow K\) reverses direction under \(\operatorname{Spec}\), giving \(P=\operatorname{Spec}K\to X=\operatorname{Spec}F\). The theorem is the precise form of the slogan “a Galois extension is a principal bundle.”

## Warning

The torsor is locally trivial in the [[algebraic-geometry-foundations/etale-topology|étale topology]], not generally in the [[algebra-commutative/zariski-topology|Zariski topology]]. Calling it a “principal bundle” does not turn \(\operatorname{Spec}K\to\operatorname{Spec}F\) into an ordinary smooth or topological bundle.
