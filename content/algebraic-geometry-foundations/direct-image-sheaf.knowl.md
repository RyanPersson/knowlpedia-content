+++
id = "algebraic-geometry-foundations/direct-image-sheaf"
title = "Direct image of a sheaf"
kind = "definition"
summary = "The sheaf on the target whose sections are sections over inverse images of open sets."
aliases = ["direct image sheaf", "pushforward sheaf", "pushforward of a sheaf"]
domains = ["algebraic-geometry-foundations"]
+++

Let \(f:X\to Y\) be a [[topology/continuous-map|continuous map]] and let \(\mathcal F\) be a [[algebraic-geometry-foundations/sheaf|sheaf]] on \(X\). The **direct image**, or **pushforward**, of \(\mathcal F\) is the sheaf \(f_*\mathcal F\) on \(Y\) defined by

\[
(f_*\mathcal F)(V):=\mathcal F(f^{-1}(V))
\]

for every open subset \(V\subseteq Y\). Its restriction maps are those of \(\mathcal F\), applied to inclusions \(f^{-1}(W)\subseteq f^{-1}(V)\).

Thus the direct image does not alter the sections themselves; it regards sections on inverse images in \(X\) as sections over open sets of \(Y\). For a sheaf of rings, \(f_*\mathcal F\) is again a sheaf of rings.
