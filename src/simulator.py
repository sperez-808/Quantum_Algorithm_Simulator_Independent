import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error


def build_grover_circuit() -> QuantumCircuit:
    """Builds a 2-qubit Grover's search circuit targeting state |11|."""
    qc = QuantumCircuit(2, 2)

    # 1. Uniform Superposition
    qc.h([0, 1])

    # 2. Oracle for |11> (Controlled-Z gate)ls
    qc.cz(0, 1)

    # 3. Diffuser Operator
    qc.h([0, 1])
    qc.z([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])

    # 4. Measurement
    qc.measure([0, 1], [0, 1])
    return qc


def create_depolarizing_noise_model(
    gate_1q_error: float = 0.01, gate_2q_error: float = 0.05
) -> NoiseModel:
    """Creates a noise model with single-qubit and two-qubit gate depolarizing errors."""
    noise_model = NoiseModel()
    err_1q = depolarizing_error(gate_1q_error, 1)
    err_2q = depolarizing_error(gate_2q_error, 2)

    noise_model.add_all_qubit_quantum_error(err_1q, ["h", "z"])
    noise_model.add_all_qubit_quantum_error(err_2q, ["cz"])
    return noise_model


def run_benchmark(shots: int = 1024):
    qc = build_grover_circuit()

    # Ideal Execution
    ideal_sim = AerSimulator()
    ideal_result = ideal_sim.run(qc, shots=shots).result()
    ideal_counts = ideal_result.get_counts()

    # Noisy Execution
    noise_model = create_depolarizing_noise_model(
        gate_1q_error=0.01, gate_2q_error=0.05
    )
    noisy_sim = AerSimulator(noise_model=noise_model)
    noisy_result = noisy_sim.run(qc, shots=shots).result()
    noisy_counts = noisy_result.get_counts()

    # Visualization
    states = ["00", "01", "10", "11"]
    ideal_probs = [ideal_counts.get(s, 0) / shots for s in states]
    noisy_probs = [noisy_counts.get(s, 0) / shots for s in states]

    x = np.arange(len(states))
    width = 0.35

    plt.style.use("seaborn-v0_8-darkgrid" if "seaborn-v0_8-darkgrid" in plt.style.available else "default")
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(x - width / 2, ideal_probs, width, label="Ideal Simulator", color="#2b5c8f")
    ax.bar(x + width / 2, noisy_probs, width, label="Noisy (Depolarizing Error)", color="#d95f02")

    ax.set_ylabel("Measured Probability")
    ax.set_title("Grover's Algorithm (|11> Target) — Ideal vs Noisy Execution")
    ax.set_xticks(x)
    ax.set_xticklabels(states)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig("benchmark_results.png", dpi=300)
    print("Benchmark complete. Result saved to 'benchmark_results.png'.")


if __name__ == "__main__":
    run_benchmark()
