# Variance & Standard Deviation

## 1. Variance

**Variance** measures how far each data point is from the mean by squaring the deviations.

### Formula

- **Population Variance (σ²):**  
  σ² = Σ(x − μ)² / N

- **Sample Variance (s²):**  
  s² = Σ(x − x̄)² / (n − 1)

### Short Explanation

- Higher variance → data is more spread out
- Lower variance → data is close to the mean
- Units are **squared**, so interpretation is less intuitive

---

## 2. Standard Deviation

**Standard Deviation** is the square root of variance and shows spread in original units.

### Formula

- **Population SD (σ):**  
  σ = √(Σ(x − μ)² / N)

- **Sample SD (s):**  
  s = √(Σ(x − x̄)² / (n − 1))

### Short Explanation

- Easy to interpret
- Same unit as data
- Widely used in statistics, data science & AI

---

## 3. Variance vs Standard Deviation

| Aspect           | Variance              | Standard Deviation       |
| ---------------- | --------------------- | ------------------------ |
| Unit             | Squared               | Original                 |
| Interpretability | Less intuitive        | More intuitive           |
| Usage            | Mathematical analysis | Real-world understanding |

---

## 4. Example

### Given Data

2, 4, 6

### Step 1: Mean

Mean = (2 + 4 + 6) / 3 = 4

### Step 2: Deviations

(2 − 4)² = 4
(4 − 4)² = 0
(6 − 4)² = 4

### Step 3: Variance

Variance = (4 + 0 + 4) / 3 = 2.67

### Step 4: Standard Deviation

SD = √2.67 ≈ 1.63

---

## Key Takeaway

- **Variance** shows spread mathematically
- **Standard Deviation** shows spread practically
- Both are core foundations of **statistics & data science**
