+++
id = "lie-groups/indefinite-spin-group"
title = "Indefinite spin group"
kind = "definition"
summary = "Pin and spin groups associated with a nondegenerate real quadratic form of mixed signature."
aliases = ["Spin(p,q)", "Pin(p,q)", "pseudo-Riemannian spin group"]
domains = ["lie-groups", "differential-geometry"]
section_mode = "progressive"
+++

Let \((V,q)\) be a real [[linear-algebra/quadratic-form|quadratic space]] of signature \((p,q)\), where this collection lists the \(p\) negative and then the \(q\) positive directions, and form its [[differential-geometry/clifford-algebra|Clifford algebra]] using \(v^2=-q(v)1\). The **pin group** \(\operatorname{Pin}(p,q)\) is generated inside \(\operatorname{Cl}(V,q)^\times\) by vectors \(v\) with \(q(v)=\pm1\). The **spin group** \(\operatorname{Spin}(p,q)\) is its even part,
\[
\operatorname{Spin}(p,q)=\operatorname{Pin}(p,q)\cap\operatorname{Cl}^0(V,q).
\]
The twisted adjoint action gives a double covering \(\operatorname{Pin}(p,q)\to O(p,q)\) with kernel \(\{\pm1\}\).

## Identity components

The even group maps onto \(SO(p,q)\), but in indefinite signature neither group need be connected. In this collection,
\[
\operatorname{Spin}^+(p,q):=\rho^{-1}\bigl(SO^+(p,q)\bigr)
\]
denotes the full preimage of the identity component \(SO^+(p,q)\) under the spin covering \(\rho\). Its restricted map
\[
\rho:\operatorname{Spin}^+(p,q)\longrightarrow SO^+(p,q)
\]
is therefore always a double covering with kernel \(\{\pm1\}\). In the usual mixed signatures of total dimension at least \(3\), this preimage is connected and hence is the identity component of \(\operatorname{Spin}(p,q)\). The low signature \((1,1)\) is an exception: the full preimage has two components, and restricting further to the identity component would make the map to \(SO^+(1,1)\) one-to-one rather than two-to-one. In particular,
\[
\operatorname{Spin}^+(1,3)\cong SL(2,\mathbb C)_{\mathbb R}.
\]

## Convention warning

Authors also use Clifford relations \(v^2=+q(v)\), interchange the order of \(p\) and \(q\), or use \(\operatorname{Spin}_0(p,q)\) specifically for the identity component. In low signature, that last group can differ from the full preimage denoted \(\operatorname{Spin}^+(p,q)\) here. These choices can alter the notation for the Clifford algebra and its components but not the associated orthogonal group. The positive-definite construction is treated separately at [[lie-groups/spin-group|spin group]].

## References

1. H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry*, Princeton University Press, 1989, Chapter I, §§2–4. [Publisher record](https://doi.org/10.1515/9781400883912).
2. Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge University Press, 1995, Chapters 13–15. [Publisher record](https://doi.org/10.1017/CBO9780511470912).
