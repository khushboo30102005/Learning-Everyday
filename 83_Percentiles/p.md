# Percentiles   
### Day-83 | #100DaysLearningChallenge  

---

## 📌 What is a Percentile?

A **percentile** is a statistical measure that indicates the **relative position of a value in a dataset**.

👉 The *k-th percentile* is the value below which **k% of the observations fall**.

### Example:
- **90th percentile** means:
  - 90% of the data values are **less than or equal to** this value
  - Only 10% values are above it

---

## 📊 Why Percentiles are Important?

Percentiles are widely used because they:
- Describe **data distribution clearly**
- Work well with **skewed data**
- Are **less affected by extreme values (outliers)**

---

## 🧠 Percentiles in Data Science & AI

Percentiles play a key role in:

### ✔ Data Analysis
- Understanding score distributions
- Comparing relative performance

### ✔ Machine Learning
- Feature scaling
- Outlier detection
- Data preprocessing

### ✔ Visualization
- Box plots
- Quartile-based analysis

---

## 📝 Formula to Calculate Percentiles

### Step 1: Arrange the data
Arrange the data in ascending order.

### Step 2: Find the rank of the percentile (Pᵢ)

Rank is calculated using:

Pᵢ Rank = (i / 100) × (n + 1)

Where:
- i = required percentile
- n = number of observations

### Step 3: Interpret the rank
- If rank is an integer → take the value at that position
- If rank is a decimal (e.g., 1.1):
  - k = integer part
  - d = decimal part

### Step 4: Calculate the percentile value

Pᵢ = Xₖ + d × (Xₖ₊₁ − Xₖ)

Where:
- Xₖ = value at position k
- Xₖ₊₁ = value at position k+1
