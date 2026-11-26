+++
id = "proofs/grh/onelift-comparison/inner-product-with-point-form"
title = "Inner product with a class form is evaluation at the point"
kind = "lemma"
summary = "The inner product of the class form with vector v at h against a form is the Gram pairing of v with the value of the form at h."
aliases = []
domains = ["proofs"]
section_mode = "progressive"
prerequisites = []
lean = ["New.Rows.inner_eq_stdClassSum_gramForm", "New.Rows.inner_classForm", "New.Rows.inner_pointForm"]
lean_files = ["src/New/OneLift/TestedForms.lean"]
proof_status = "full"
+++

**Lemma.** In the setting of [[proofs/grh/onelift-comparison/point-form|class forms and point forms]], let \(\langle\xi,\eta\rangle_G=\xi^*G\eta\) be the Gram form on the weight space \(\mathbb{C}^{\mathcal I}\) (the hermitian form of the integral Gram matrix \(G\) of the weight, which is \(\rho\)-invariant). The inner product of forms on \(V\) is the class sum
\[
\langle\varphi,\varphi'\rangle=\sum_{c\in U(V)(\mathbb{Q})\backslash U(V)(\mathbb{A}_f)/K}\frac{\langle\varphi(g_c),\varphi'(g_c)\rangle_G}{\#\operatorname{Aut}(g_c)},
\]
and for every \(h\in U(V)(\mathbb{A}_f)\), \(v\in\mathbb{C}^{\mathcal I}\) and form \(\varphi\),
\[
\langle\delta_h(v),\varphi\rangle=\langle v,\varphi(h)\rangle_G .
\]
In particular \(\langle\delta_{h,Y,e}(v),\varphi\rangle=\langle v,\varphi(hA_{Y,e})\rangle_G\) for a point form.

## Proof

The first formula is the definition of the inner product \(\langle\ ,\ \rangle=\langle\ ,\ \rangle_{\sigma=1}\) ([[?lean:New.LevelPlaces.LevelForm.innerAt_eq_stdClassSum|class sum formula for the pairing at \(\sigma\)]]). For the second, put \(L_g(\xi)=\langle\xi,\varphi(g)\rangle_G\), additive in \(\xi\). For rational \(\gamma\) and \(k\in K\),
\[
L_{\gamma hk}\bigl(\lambda(k)\rho(\gamma)v\bigr)=\overline{\lambda(k)}\lambda(k)\,\langle\rho(\gamma)v,\rho(\gamma)\varphi(h)\rangle_G=\langle v,\varphi(h)\rangle_G=L_h(v),
\]
using the transformation law of \(\varphi\), \(\lvert\lambda(k)\rvert=1\) (\(\lambda\) has finite order) and the invariance of the Gram form under \(\rho\). For a family \(L\) with this invariance the class sum of \(g\mapsto L_g(\delta_h(v)(g))\) equals \(L_h(v)\) ([[?lean:New.classSum_deltaForm|class sum against a class form]]): only the class of \(h\) contributes, and the sum over \(\gamma\) in the definition of \(\delta_h(v)\) exactly cancels the weight \(1/\#\operatorname{Aut}\). The statement for point forms is the case \(h\mapsto hA_{Y,e}\).

## References

1. Lean: `New.Rows.inner_eq_stdClassSum_gramForm`, `New.Rows.inner_classForm`, `New.Rows.inner_pointForm` in `src/New/OneLift/TestedForms.lean`.
