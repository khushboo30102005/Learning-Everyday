# Quartiles, IQR & Coefficient of Quartile Deviation

## Quartiles

Quartiles divide the ordered data set into **four equal parts**.

Let **N** be the total number of observations.

### Formulas

- **Lower Quartile (Q1)**  
  **Q1 = (N + 1) * 1/4**

- **Middle Quartile (Q2 / Median)**  
  **Q2 = (N + 1) * 1/2**

- **Upper Quartile (Q3)**  
  **Q3 = (N + 1) * 3/4**

---

## Interpolation Rule

If the calculated position is **not a whole number**, interpolation is used.

### Example:
If the result is **1.2th term**:

**
\Q = 1st term + (2nd term - 1st term) * 0.2**

---

## InterQuartile Range (IQR)

**IQR = Q3 - Q1**

- Represents the **middle 50% of the data**
- Better than **Range** as it ignores extreme values

---

## Outlier Detection

A value is considered an **outlier** if:

- **Below:**  
  **Q1 - 1.5 * IQR**

- **Above:**  
  **Q3 + 1.5 * IQR**

---

## Numerical Example

Given data set (already sorted):

**13, 18, 19, 20, 21, 22, 23, 35**

### Step 1: Find Quartile Positions

- **Q1** = 2.25th term  
- **Q2** = 4.5th term  
- **Q3** = 6.75th term  

### Step 2: Calculate Quartile Values

- **Q1 = 18.25**
- **Q2 = 20.5**
- **Q3 = 22.75**

---

## InterQuartile Range Calculation

**IQR = Q3 - Q1 = 22.75 - 18.25 = 4.50**

Here, **4.50** is an **absolute value**, which does **not fully describe dispersion** for comparison across different data sets.

---

## Coefficient of Quartile Deviation (CQD)

To overcome this limitation, we use:

**CQD = (Q3 - Q1)/(Q3 + Q1)**

### Importance of CQD

- Provides **relative comparison** between datasets  
- More suitable than IQR alone  
- Helps in **fair statistical comparison**

---

## Summary

- Quartiles divide data into four parts
- IQR measures spread of the middle 50%
- Outliers are detected using IQR
- CQD gives a **better comparative measure** of dispersion

---

**Day-84 | #100dayslearningchallenge**  
📊 *Quartile Deviation & IQR Explained*
