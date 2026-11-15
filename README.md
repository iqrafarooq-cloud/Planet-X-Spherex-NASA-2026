# 🔭 Planet X and SPHEREx — NASA Space Apps Challenge 2026

An automated astronomical data retrieval, WCS sky-alignment, and multi-epoch transient detection pipeline built using **NASA's SPHEREx Data Release 1 (DR1)** archive via IRSA.

---

## 📌 Project Overview
The search for distant solar system objects, asteroids, and moving transients requires comparing astronomical observations taken months or years apart. To achieve this, our system analyzes multi-epoch infrared observations of the exact same sky region separated by **~407 days** (`2025-04-29` vs `2026-06-10` in the `SPHEREx-D1` spectral band).

---

## ⚡ Key Features
* **Automated NASA Data Extraction:** Queries NASA/Caltech IRSA SIA2 TAP services directly using Python (`astroquery`).
* **Astronomical Preprocessing:** Cleans detector artifacts (`NaN` values via median imputation) and applies `ZScale` intensity normalization to reveal faint celestial sources.
* **Precise WCS Sky Alignment:** Uses astronomical World Coordinate System (WCS) headers to reproject Epoch 2 onto Epoch 1's exact pixel grid (`reproject_interp`), ensuring stationary background stars cancel out cleanly during subtraction.
* **Transient & Motion Detection:** Generates difference maps to isolate moving objects from static background stars.

---

## 🛠️ Technical Architecture & Workflow

```text
 ┌─────────────────────────────┐
 │  NASA IRSA SPHEREx Archive  │  (Data Release 1 / QR3 via SIA2)
 └──────────────┬──────────────┘
                │ Query by RA, Dec & Band (SPHEREx-D1)
                ▼
 ┌─────────────────────────────┐
 │  Multi-Epoch FITS Retrieval │  (~407 Days Baseline: Apr 2025 vs Jun 2026)
 └──────────────┬──────────────┘
                │ Parse ImageHDU (2040 x 2040 pixels)
                ▼
 ┌─────────────────────────────┐
 │   Data Cleaning & Scaling   │  (NaN Imputation & ZScale Normalization)
 └──────────────┬──────────────┘
                │ WCS Header Extraction
                ▼
 ┌─────────────────────────────┐
 │    WCS Sky Reprojection     │  (Aligns Epoch 2 to Epoch 1 Pixel Grid)
 └──────────────┬──────────────┘
                │ Flux Differencing (Epoch 2 - Epoch 1)
                ▼
 ┌─────────────────────────────┐
 │   Transient / Motion Map    │  (Isolates Moving Objects & Asteroids)
 └─────────────────────────────┘
