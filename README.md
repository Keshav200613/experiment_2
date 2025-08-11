# Hamming Code Generator & Solver

This repository contains two Python scripts that demonstrate **Hamming Code** generation for error detection and correction, as well as decoding and error correction from a received codeword.

## 📂 Files

- **`hamming_code.py`** — Generates the Hamming code for a given binary message.
- **`hamming_solver.py`** — Detects and corrects single-bit errors in a received Hamming codeword.

---

## 🚀 Features

- **Generation** of Hamming codes from binary messages.
- **Error Detection** using parity bits.
- **Single-bit Error Correction** in received codewords.
- Command-line based interactive execution.

---

## 🧮 Theory Overview

**Hamming Code** is a linear error-correcting code that adds redundant bits (parity bits) to data bits so that single-bit errors can be detected and corrected.

- For `m` data bits, we choose `r` parity bits such that:

  \[
  2^r \geq m + r + 1
  \]

- Parity bits are placed at positions which are powers of 2.
- The parity check uses even parity to find and correct errors.

---

## 📌 Usage

###  Generate Hamming Code

```bash
python hamming_code.py
