+++
id = "real-analysis/composition-preserves-riemann-integrability"
title = "Composition preserves Riemann integrability"
kind = "knowl"
summary = "Composing a Riemann integrable function with a continuous function preserves integrability."
aliases = ["composition-preserves-riemann-integrability", "Composition preserves Riemann integrability"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/riemann-integrable-function"]
dependency_review_count = 1
legacy_source_path = "real-analysis/composition-preserves-riemann-integrability.md"
+++

**Composition preserves Riemann integrability.** Let \(f:[a,b]\to\mathbb R\) be [[real-analysis/riemann-integrable-function|Riemann integrable]], and let \(\varphi:J\to\mathbb R\) be continuous on an interval \(J\) containing \(f([a,b])\). Then \(\varphi\circ f\) is Riemann integrable on \([a,b]\).

## Remarks

Taking \(\varphi(t)=t^2\) shows that \(f^2\) is integrable; taking \(\varphi(t)=|t|\) gives [[real-analysis/absolute-value-preserves-integrability|integrability of \(|f|\)]].
