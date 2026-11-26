+++
id = "proofs/grh/derivatives-divisibility/resolution-of-the-identity"
title = "Resolution of the identity by vectors over a CM field"
kind = "definition"
summary = "A family of vectors u_j in E^n with multiplicities m_j such that z = sum m_j (u_j-dagger z) u_j for all complex vectors z indexed by places and coordinates; a Parseval frame."
aliases = ["resolution of the identity", "dagger form", "linear form u-dagger z"]
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.dagger", "New.IsResolution", "New.IsResolution.sum_conj_mul", "New.daggerForms", "New.IsResolution.sum_smul_linearSeries"]
lean_files = ["src/New/Derivatives/FormalGroup/Resolution.lean"]
+++

**Definition (resolution of the identity).** Let \(E\) be a [[?c:CM field|CM field]] with a [[?c:CM type|CM type]], that is, an embedding \(\Phi_w\colon E\to\mathbb{C}\) chosen at each [[?c:infinite place of a number field|infinite place]] \(w\) of \(E\). Let \(n\) and \(J\) be finite sets. A vector \(u\in E^n\) is read as the complex vector with coordinates \(\Phi_w(u_c)\), indexed by the pairs \(x=(w,c)\) of an infinite place and an element of \(n\); its **dagger form** is the linear form
\[
u^\dagger z=\sum_{(w,c)}\overline{\Phi_w(u_c)}\;z_{(w,c)}
\]
in variables \(z_{(w,c)}\). A family \((u_j)_{j\in J}\) of vectors of \(E^n\) with multiplicities \(m_j\in\mathbb{N}\) is a **resolution of the identity** if
\[
\sum_{j\in J}m_j\,\Phi_w(u_{j,c})\,\overline{\Phi_{w'}(u_{j,c'})}=\begin{cases}1&(w,c)=(w',c'),\\0&\text{otherwise,}\end{cases}
\]
for all pairs \((w,c)\), \((w',c')\); equivalently \(z=\sum_jm_j\,(u_j^\dagger z)\,u_j\) for every complex vector \(z\).

## Properties

1. (*Parseval's identity.*) For complex vectors \(z,z'\): \(\sum_jm_j\,\overline{u_j^\dagger z'}\;u_j^\dagger z=\sum_x\overline{z'_x}\,z_x\).
2. Let \(p\) be a prime with a \(p\)-adic place \(\iota_p\) (see the [[proofs/grh/derivatives-divisibility/p-adic-setting|\(p\)-adic setting]]) and suppose the numbers \(\mu_{j,x}=\iota_p\bigl(\overline{\Phi_w(u_{j,c})}\bigr)\) and \(\nu_j=\iota_p(\Phi_{w_0}(u_{j,c_0}))\), for a fixed pair \(x_0=(w_0,c_0)\), are integral. Then, as power series over \(\mathcal{O}\),
\[
\sum_jm_j\,\nu_j\cdot\Bigl(\sum_x\mu_{j,x}z_x\Bigr)=z_{x_0}.
\]

Both follow by expanding the sums and applying the defining relation (for 2, after applying the ring homomorphism \(\iota_p\) to it).

## Remarks

In the terminology of [[?c:Parseval frame|frame theory]] a resolution of the identity is a Parseval frame of the hermitian space \(\mathbb{C}^{\Phi\times n}\), each \(u_j\) taken \(m_j\) times.

## References

1. Lean: `New.dagger`, `New.IsResolution`, `New.IsResolution.sum_conj_mul`, `New.daggerForms`, `New.IsResolution.sum_smul_linearSeries` in `src/New/Derivatives/FormalGroup/Resolution.lean`.
