+++
id = "real-analysis/algebraic-properties-sup-inf"
title = "Algebraic properties of sup and inf"
kind = "knowl"
summary = "Supremum and infimum behave predictably under inclusion, translation, scaling, and unions"
aliases = ["algebraic-properties-sup-inf", "Algebraic properties of sup and inf"]
domains = ["real-analysis"]
legacy_source_path = "real-analysis/algebraic-properties-sup-inf.md"
+++

Let \(E,F\subseteq\mathbb R\) be nonempty and bounded above or below as required, and let \(c\in\mathbb R\).

## Order and translation

- If \(E\subseteq F\), then \(\sup E\le\sup F\) when both sets are bounded above, and \(\inf E\ge\inf F\) when both are bounded below.
- For \(E+c=\{x+c:x\in E\}\),
  \[
  \sup(E+c)=\sup E+c,\qquad\inf(E+c)=\inf E+c.
  \]

## Scaling

For \(\lambda E=\{\lambda x:x\in E\}\):

- If \(\lambda\ge0\), then
  \[
  \sup(\lambda E)=\lambda\,\sup E,\qquad \inf(\lambda E)=\lambda\,\inf E.
  \]
- If \(\lambda<0\), then
  \[
  \sup(\lambda E)=\lambda\,\inf E,\qquad \inf(\lambda E)=\lambda\,\sup E.
  \]

In particular,
\[
\sup(-E)=-\inf E,\qquad \inf(-E)=-\sup E.
\]

## Finite unions

If \(E\) and \(F\) are bounded above, then
\[
  \sup(E\cup F)=\max\{\sup E,\sup F\}.
\]
If they are bounded below, then
\[
\inf(E\cup F)=\min\{\inf E,\inf F\}.
\]
