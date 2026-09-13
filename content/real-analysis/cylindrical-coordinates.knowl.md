+++
id = "real-analysis/cylindrical-coordinates"
title = "Cylindrical coordinates and their orthonormal frame"
kind = "definition"
summary = "The coordinates x=r cos(theta), y=r sin(theta), z=z and their moving unit vectors."
aliases = ["cylindrical frame", "cylindrical basis", "cylindrical coordinate system"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/cartesian-coordinates", "real-analysis/sine-function", "real-analysis/cosine-function", "real-analysis/nonnegative-square-root", "real-analysis/chain-rule-multivariable"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

Away from the \(z\)-axis, **cylindrical coordinates** are
\[
x=r\cos\theta,\qquad y=r\sin\theta,\qquad z=z,
\qquad r=\sqrt{x^2+y^2}>0.
\]
The [[real-analysis/sine-function|angle in radians]] is taken modulo \(2\pi\), or on a local angular interval. The corresponding orthonormal frame is
\[
e_r=(\cos\theta,\sin\theta,0),\quad
e_\theta=(-\sin\theta,\cos\theta,0),\quad e_z=(0,0,1).
\]
Its angular derivatives are \(\partial_\theta e_r=e_\theta\) and \(\partial_\theta e_\theta=-e_r\).

## Scalar derivatives and volume

The chain rule gives
\[
\partial_x=\cos\theta\,\partial_r-\frac{\sin\theta}{r}\partial_\theta,
\qquad
\partial_y=\sin\theta\,\partial_r+\frac{\cos\theta}{r}\partial_\theta.
\]
Consequently \(\nabla f=e_r\partial_r f+e_\theta r^{-1}\partial_\theta f+e_z\partial_z f\). The coordinate Jacobian has absolute determinant \(r\), so Euclidean volume is \(r\,dr\,d\theta\,dz\).

## The axis

At \(r=0\), the angle and horizontal frame vectors are not defined. A field may nevertheless extend smoothly there; this is checked through its [[real-analysis/cylindrical-axis-regularity|Cartesian components]].

## References

- [MIT 6.013, Differential operators in cylindrical and spherical coordinates](https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-fall-2005/59e100001186c03a19ca3361dcd3b240_formula_sheet2.pdf).

## Fluid components

In fluid mechanics these coordinates distinguish [[fluid-dynamics/radial-velocity|radial velocity]], [[fluid-dynamics/swirl|swirl]], and [[fluid-dynamics/axial-velocity|axial velocity]]. [[fluid-dynamics/axisymmetric-field|Axisymmetry]] means that the cylindrical components are independent of the angle, even though their moving basis is not.
