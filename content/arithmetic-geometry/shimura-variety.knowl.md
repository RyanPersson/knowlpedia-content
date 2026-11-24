+++
id = "arithmetic-geometry/shimura-variety"
title = "Shimura variety"
kind = "definition"
summary = "The arithmetic variety associated with a Shimura datum and a compact open level subgroup of its finite adelic group."
aliases = ["Shimura varieties"]
domains = ["arithmetic-geometry"]
section_mode = "progressive"
prerequisites = ["arithmetic-geometry/shimura-datum", "algebra-fields-galois/adeles-restricted-product"]
+++

Given a [[arithmetic-geometry/shimura-datum|Shimura datum]] \((G,X)\) and a compact open subgroup \(K\subset G(\mathbb A_f)\), the **Shimura variety of level \(K\)** has complex points
\[
\operatorname{Sh}_K(G,X)(\mathbb C)=G(\mathbb Q)\backslash\bigl(X\times G(\mathbb A_f)/K\bigr).
\]
Here \(\mathbb A_f\) is the ring of finite [[algebra-fields-galois/adeles-restricted-product|adeles]] of \(\mathbb Q\). The rational group acts on both coordinates. This quotient carries an algebraic structure and has a canonical model over a number field called the reflex field of the datum.

## Modular curves

For the modular datum with \(G=\mathrm{GL}_2\), one obtains modular curves. With full level \(N\ge3\), a complex point describes an [[algebraic-geometry-foundations/elliptic-curve|elliptic curve]] together with an ordered basis for its \(N\)-torsion. Changing the level changes which markings are remembered.

## References

- J. S. Milne, [Introduction to Shimura Varieties, §5, the double quotient, and §§12–13, canonical models](https://jmilne.org/math/xnotes/svi.pdf).
