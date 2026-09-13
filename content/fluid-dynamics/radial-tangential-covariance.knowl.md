+++
id = "fluid-dynamics/radial-tangential-covariance"
title = "Radial-tangential velocity covariance"
kind = "definition"
summary = "The pair of averaged products transporting azimuthal and axial momentum in the radial direction."
aliases = ["radial transport covariance", "radial-tangential covariance pair"]
domains = ["fluid-dynamics"]
section_mode = "progressive"
prerequisites = ["fluid-dynamics/velocity-field", "real-analysis/cylindrical-coordinates", "measure-theory/averaged-second-moment-matrix", "fluid-dynamics/angular-average", "harmonic-analysis/normalized-torus-average", "linear-algebra/quadratic-map"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a real velocity field expressed in cylindrical components and square-integrable in the averaging variables, define its **radial-tangential covariance pair** by
\[
C(w)=\bigl(\langle w_rw_\theta\rangle,\langle w_rw_z\rangle\bigr).
\]
These are two off-diagonal entries of the [[measure-theory/averaged-second-moment-matrix|averaged second-moment tensor]]. The average may include the angular variable and independent auxiliary torus variables, at fixed slow coordinates. Centering is not part of this definition.

## Cross term and amplitude weights

Writing \(w_{\rm tan}=(w_\theta,w_z)\), expansion gives
\[
C(w+v)=C(w)+B(w,v)+C(v),\qquad
B(w,v)=\langle w_rv_{\rm tan}+v_rw_{\rm tan}\rangle.
\]
Thus \(DC(w)[v]=B(w,v)\). If fields \(b_j\) have vanishing cross products and real coefficients \(a_j\) are independent of every averaging variable, then \(C(\sum_j a_jb_j)=\sum_j a_j^2C(b_j)\). Coefficients that depend on an averaging variable cannot in general be taken outside its integral.
