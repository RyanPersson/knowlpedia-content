+++
id = "real-analysis/pi"
title = "The constant pi"
kind = "definition"
summary = "The least positive zero of the series-defined sine function fixes the standard angular scale."
aliases = ["pi constant", "π"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["real-analysis/sine-function", "real-analysis/cosine-function", "real-analysis/intermediate-value-theorem", "real-analysis/infimum"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

The constant **\(\pi\)** is the least positive zero of the [[real-analysis/sine-function|sine function]] defined by its power series. Thus \(\sin\pi=0\) and \(\sin x>0\) for \(0<x<\pi\). This definition fixes the usual radian scale without first assuming a geometric angle convention.

## Existence and period

Cosine has a first positive zero \(c\). To see existence, if cosine stayed positive, sine would increase and be bounded below by a positive constant after some positive time. Then \(\cos'=-\sin\) would force cosine to become negative, a contradiction. Continuity gives a least positive zero, with cosine positive before it.

The identities \(\sin^2c+\cos^2c=1\) and \(\sin'>0\) before \(c\) give \(\sin c=1\). Addition formulas show \(\sin(2c)=0\), and \(\sin(c+y)=\cos y>0\) for \(0<y<c\). Hence \(\pi=2c\). Also \(\cos\pi=-1\), and sine and cosine have period \(2\pi\). Their unit-circle parametrization has unit speed and one full turn over that period, giving the usual circumference-to-diameter interpretation.
