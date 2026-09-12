+++
id = "algebra-groups/projective-special-linear-group-over-ring"
title = "Projective special linear group over a ring"
kind = "definition"
summary = "The determinant-one matrix group modulo its scalar determinant-one matrices."
aliases = ["PSL over a commutative ring"]
domains = ["algebra-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/special-linear-group-over-ring", "algebra-groups/quotient-group"]
+++

For a nonzero commutative ring \(R\) with identity and \(n\ge2\), use the convention
\[
\operatorname{PSL}_n(R)=\operatorname{SL}_n(R)/\{uI_n:u\in R^\times,\ u^n=1\}.
\]
The denominator is the central subgroup of scalar matrices in the [[algebra-groups/special-linear-group-over-ring|special linear group]], so the [[algebra-groups/quotient-group|quotient group]] is defined.

## The case needed for Bianchi groups

If \(R\subseteq\mathbb C\) and \(n=2\), then \(u^2=1\) forces \(u=\pm1\). Consequently
\[
\operatorname{PSL}_2(R)=\operatorname{SL}_2(R)/\{\pm I\}
\hookrightarrow\operatorname{PSL}_2(\mathbb C).
\]
The kernel calculation proves the displayed injection.

## Convention warning

This is an abstract group quotient. It makes no assertion that forming points of a group-scheme quotient commutes with quotienting groups of points. Over fields it agrees with the existing [[algebra-groups/projective-special-linear-group|field-valued definition]].
