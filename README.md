# Quantum_Algorithm_Simulator_Independent
This program takes theoretical algorithms from Wolfgang Scherer’s QC intro textbook, implementing them in Python to evaluate their behavior under simulated real-world quantum noise cleanly ties together my math background, coding skills, and analytical mindset. 

# Comparative Quantum Algorithm Simulator

A Python-based simulation benchmark evaluating the performance of Grover's Search Algorithm across ideal quantum simulators and noisy, hardware-realistic decoherence environments using Qiskit.

## Project Overview

In quantum computing and intellectual property evaluation, theoretical gate counts rarely reflect physical hardware execution. This project quantifies the fidelity decay of quantum algorithms when subjected to depolarizing noise models across single-qubit ($H, Z$) and two-qubit ($CZ$) gates.

## Key Technical Insights

- **Two-Qubit Error Dominance:** Controlled-$Z$ ($CZ$) gate noise accounts for over 70% of total state fidelity loss compared to single-qubit transformations.
- **Error Thresholds:** At a 5% 2-qubit depolarizing error rate, target state probability ($|11\rangle$) decays from 100% to ~65%, highlighting the strict threshold requirements for error-mitigated quantum patent claims.

## Repository Structure
