+++
id = "ergodic-theory/gaussian-integer-translations"
title = "Translations on the Gaussian-integer torus"
kind = "example"
summary = "A concrete distinction between ergodicity of one translation and joint ergodicity of an algebraic-integer action."
aliases = []
domains = ["ergodic-theory"]
section_mode = "progressive"
prerequisites = ["ergodic-theory/number-field-translation-ergodicity", "ergodic-theory/ring-of-integers-translation-action"]
+++

For \(K=\mathbb Q(i)\), the [[ergodic-theory/number-field-torus|number-field torus]] is \(\mathbb C/\mathbb Z[i]\). Write \(\omega=u+iv\). Translation by \(\omega\) is ergodic exactly when \(1,u,v\) are linearly independent over \(\mathbb Q\).

## Fourier calculation

Here \(\mathcal O_K^\vee=\tfrac12\mathbb Z[i]\) and \(\operatorname{Tr}_\infty z=2\operatorname{Re}z\). With \(a=(p-iq)/2\),
\[
\operatorname{Tr}_\infty(a\omega)=pu+qv,
\]
recovering the ordinary two-torus criterion. The increment \(\sqrt2+i\sqrt3\) gives an ergodic translation.

## One translation can fail while the joint action succeeds

For \(\omega=\sqrt2\), translation fixes the imaginary coordinate modulo one, so it is not ergodic. Nevertheless \(k\sqrt2\notin\mathbb Z[i]\) for every nonzero \(k\in\mathbb Z[i]\).

The joint action includes translation by \(\sqrt2\) and by \(i\sqrt2\). A character \(e^{2\pi i(p\operatorname{Re}z+q\operatorname{Im}z)}\) is fixed by both only if \(p\sqrt2,q\sqrt2\in\mathbb Z\), forcing \(p=q=0\). The action is therefore ergodic although neither generator is individually ergodic.
