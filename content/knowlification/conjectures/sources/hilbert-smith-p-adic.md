The Hilbert–Smith conjecture asks whether a locally compact topological group that acts faithfully and continuously on a connected finite-dimensional topological manifold must be a Lie group.

Fix a prime number \(p\). The ring of \(p\)-adic integers \(\mathbb Z_p\) is the inverse limit \(\varprojlim_n \mathbb Z/p^n\mathbb Z\), equipped with its compact Hausdorff topology and additive group law. A continuous action of \(\mathbb Z_p\) on a space \(X\) is a continuous map \(\alpha:\mathbb Z_p\times X\to X\) satisfying \(\alpha(0,x)=x\) and \(\alpha(a+b,x)=\alpha(a,\alpha(b,x))\). It is faithful when \(\alpha(a,x)=x\) for every \(x\) forces \(a=0\).

## Conjecture

If \(X\) is a connected finite-dimensional topological manifold and \(p\) is prime, then no faithful continuous action of the additive group \(\mathbb Z_p\) on \(X\) exists.

This is the standard \(p\)-adic formulation of Hilbert–Smith. A reduction theorem says that excluding these actions is enough to prove the general locally compact-group formulation. The conclusion “the acting group is a Lie group” means that its topology and group operations arise from a compatible finite-dimensional smooth-manifold structure.

## Known boundary

The conjecture is known for manifolds of dimension at most three. It also holds under stronger regularity hypotheses, for example for effective isometric actions on Riemannian manifolds. The unresolved case permits merely continuous actions, where differential-geometric tools are unavailable.

## Formal source

This page follows `FormalConjectures/HilbertProblems/5.lean`. The formalization records both the general statement and the equivalent obstruction by additive actions of `PadicInt p`.
