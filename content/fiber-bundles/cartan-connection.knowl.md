+++
id = "fiber-bundles/cartan-connection"
title = "Cartan connection"
kind = "knowl"
summary = "A Lie-algebra-valued one-form on a principal H-bundle that identifies each tangent space with the model Lie algebra."
aliases = ["cartan-connection", "Cartan connection"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/cartan-connection.md"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), and let \(H\subseteq G\) be a closed subgroup with Lie algebra \(\mathfrak h\). Let \(\pi:P\to M\) be a principal \(H\)-bundle.

A **Cartan connection** on \(P\), modeled on \((G,H)\), is a \(\mathfrak g\)-valued one-form
\[
\omega \in \Omega^1(P;\mathfrak{g})
\]
satisfying:

1. \(\omega_p:T_pP\to\mathfrak g\) is a linear isomorphism for every \(p\in P\);
2. \(R_h^*\omega=\operatorname{Ad}(h^{-1})\omega\) for every \(h\in H\); and
3. \(\omega(X^\#)=X\) for every \(X\in\mathfrak h\), where \(X^\#\) is the corresponding fundamental vector field.

## Curvature

The curvature is the \(\mathfrak g\)-valued two-form
\[
\Omega := d\omega + \tfrac12[\omega,\omega],
\]
where the bracket uses the [[fiber-bundles/lie-bracket|Lie bracket]] on \(\mathfrak g\). Unlike a [[fiber-bundles/principal-connection|principal connection]] form, \(\omega\) identifies every tangent space \(T_pP\) with \(\mathfrak g\).

## Examples
1. **Homogeneous model geometry.** On the principal \(H\)-bundle \(G\to G/H\), the Maurer–Cartan form is a Cartan connection with zero curvature.
2. **Riemannian geometry as Cartan geometry.** On the orthonormal frame bundle of a Riemannian manifold, combining the Levi–Civita connection one-form with the solder form produces a Cartan connection modeled on Euclidean space, with stabilizer \(O(n)\).
3. **Projective and conformal geometries.** Standard projective or conformal structures can be encoded as Cartan geometries modeled on appropriate homogeneous spaces; the Cartan curvature measures deviation from the flat model.
