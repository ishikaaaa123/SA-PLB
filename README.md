# Staleness-Aware Predictive Load Balancer (SA-PLB)

## Overview
SA-PLB is a research project exploring predictive load balancing
with monitoring-data freshness awareness.

## Objectives
- Compare Round Robin (RR) and Weighted Round Robin (WRR).
- Develop a machine-learning model to predict microservice time.
- Design SA-PLB to use predictions when monitoring data is fresh
  and fall back to WRR when monitoring data is stale.
- Evaluate the policies using a clearly documented simulation.

## Dataset
The project currently investigates Alibaba Cloud microservice traces
containing microservice time, call rate, replica count, and identifiers.

Dataset source:
https://zenodo.org/records/14245634

## Project Status
Day 1: Dataset inspection and exploratory analysis.
