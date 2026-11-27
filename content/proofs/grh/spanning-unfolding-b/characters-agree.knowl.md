+++
id = "proofs/grh/spanning-unfolding-b/characters-agree"
title = "Terms whose unipotent characters agree"
kind = "definition"
summary = "A rational isometry respects the unipotent character if the finite character takes equal values at u and u' whenever u times the isometry equals the isometry times u'."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Filling.CharsAgree"]
lean_files = ["src/New/Spanning/Unfolding/Terms.lean"]
+++

Let \(S\) be a [[proofs/grh/spanning-unfolding-b/filling-data|filling datum]] with [[proofs/grh/spanning-unfolding-b/unipotent-character-agreement-stability|unipotent character]] \(\psi_{\mathsf U}\). For a rational isometry \(\gamma\in G(E)\), **the characters agree at \(\gamma\)** if for all \(u,u'\) in the rational Bessel unipotent group \(\mathsf{U}(E)\) with \(u\gamma=\gamma u'\),
\[
\psi_{\mathsf U}(u_{\mathrm{fin}})=\psi_{\mathsf U}(u'_{\mathrm{fin}}).
\]
Equivalently, \(u\mapsto\psi_{\mathsf U}(u_{\mathrm{fin}})\) and \(u\mapsto\psi_{\mathsf U}((\gamma^{-1}u\gamma)_{\mathrm{fin}})\) coincide on \(\mathsf{U}(E)\cap\gamma\mathsf{U}(E)\gamma^{-1}\).

## References

1. Lean: `New.Filling.CharsAgree` in `src/New/Spanning/Unfolding/Terms.lean`.
