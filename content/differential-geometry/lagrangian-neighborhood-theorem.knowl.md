+++
id = "differential-geometry/lagrangian-neighborhood-theorem"
title = "Lagrangian neighborhood theorem"
kind = "theorem"
summary = "A neighborhood of a Lagrangian submanifold has the cotangent bundle as its canonical local symplectic model."
aliases = ["Weinstein neighborhood theorem", "Lagrangian tubular-neighborhood theorem"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/lagrangian-submanifold", "differential-geometry/symplectic-manifold", "fiber-bundles/zero-section", "fiber-bundles/cotangent-bundle", "differential-geometry/symplectomorphism", "differential-geometry/canonical-symplectic-form-cotangent"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(L\) be an embedded [[differential-geometry/lagrangian-submanifold|Lagrangian submanifold]] of a [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\). There are neighborhoods \(U\) of the [[fiber-bundles/zero-section|zero section]] in the [[fiber-bundles/cotangent-bundle|cotangent bundle]] \(T^*L\) and \(V\) of \(L\) in \(M\), together with a [[differential-geometry/symplectomorphism|symplectomorphism]]
\[
\Phi:(U,\omega_{\mathrm{can}})\longrightarrow(V,\omega)
\]
whose restriction to the zero section is the given inclusion \(L\hookrightarrow M\). Thus the germ of the ambient symplectic structure along \(L\) is modeled by the canonical [[differential-geometry/canonical-symplectic-form-cotangent|cotangent symplectic form]]. The neighborhoods and the symplectomorphism are generally not unique, and the theorem makes no global claim about all of \(T^*L\) or \(M\).

## Relative formulation

A useful equivalent form compares two symplectic manifolds containing copies of the same Lagrangian \(L\). If a diffeomorphism between those copies is fixed, then it extends, after shrinking neighborhoods, to a symplectomorphism near \(L\). Taking one ambient manifold to be \(T^*L\) and one copy to be its zero section gives the stated form. This is the Lagrangian case of Weinstein's neighborhood results.

## Proof idea

The symplectic form identifies the [[differential-geometry/normal-bundle|normal bundle]] \(TM|_L/TL\) with \(T^*L\): the class of \(v\) is sent to the covector \(w\mapsto\omega(v,w)\). A tubular-neighborhood choice realizes this bundle identification by a diffeomorphism near the zero section. The pulled-back ambient form and the canonical cotangent form agree along \(L\). A relative Moser argument then corrects the diffeomorphism to a symplectomorphism while fixing \(L\).

The correction step explains both the local nature of the theorem and its nonuniqueness: auxiliary tubular data and the Moser primitive can vary.

## Consequences and limitations

Nearby sections of \(T^*L\) are Lagrangian exactly when their defining one-forms are closed. Consequently, sufficiently small Lagrangian deformations of \(L\), once placed in a Weinstein neighborhood and transverse to the cotangent fibers, are represented by closed one-forms. Exact one-forms describe the corresponding local Hamiltonian deformations.

**Warning.** This theorem is not the symplectic-neighborhood theorem for [[differential-geometry/symplectic-submanifold|symplectic submanifolds]], whose model depends on the symplectic normal bundle. Nor does it assert that \(M\) is globally symplectomorphic to \(T^*L\).

## References

1. Alan Weinstein, “Symplectic Manifolds and Their Lagrangian Submanifolds,” *Advances in Mathematics* 6 (1971), 329–346. [DOI record](https://doi.org/10.1016/0001-8708%2871%2990020-X). Relevant: Theorem 6.1 and the neighborhood-equivalence argument.
2. Dusa McDuff and Dietmar Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press, 2017. [DOI record](https://doi.org/10.1093/oso/9780198794899.001.0001). Relevant: §3.4, the Weinstein neighborhood theorem and local Lagrangian graphs.
