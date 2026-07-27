+++
id = "langlands-letter/knowls/l-group-satake-parameter"
title = "$L$-Group and Satake Parameter"
kind = "knowl"
summary = "The semidirect product and the conjugacy class encoding unramified local data"
aliases = ["l-group-satake-parameter", "$L$-Group and Satake Parameter"]
domains = ["langlands-letter"]
legacy_source_path = "langlands-letter/knowls/l-group-satake-parameter.md"
+++

For a reductive group $G$ over a field with Galois or Weil group $\Gamma$, the **$L$-group** is a semidirect product
$$
{}^LG=\widehat G\rtimes\Gamma,
$$
where $\widehat G$ is the dual group and $\Gamma$ acts through pinned automorphisms; see [[langlands-letter/knowls/pinned-automorphisms|pinning]]. For split $G$, this action is trivial.

At an unramified prime $p$, a Hecke eigencharacter determines a **Satake parameter** $\alpha_p$: a semisimple conjugacy class in ${}^LG$ whose projection to $\Gamma$ is a choice of [[langlands-letter/knowls/frobenius-unramified|Frobenius]].

## Local factor

Given a complex representation $\pi:{}^LG\to \operatorname{GL}(V)$, the associated local factor is
$$
L_p(s,\pi,\phi)=\det(1-\pi(\alpha_p)\,p^{-s})^{-1}.
$$
