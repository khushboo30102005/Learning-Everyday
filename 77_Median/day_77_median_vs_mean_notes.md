# Day-77 | Why Median Matters More Than Average

## 1. Introduction
In statistics, measures of central tendency help us understand the *center* of a dataset. The most common measures are **Mean**, **Median**, and **Mode**. While the **mean (average)** is widely used, it can be misleading when data contains **outliers**. In such cases, the **median** provides a more realistic picture.

---

## 2. What is Mean (Average)?
**Mean** is calculated by adding all values and dividing by the total number of values.

**Formula:**  
Mean = (Sum of all values) / (Number of values)

### Example:
Data: 10, 20, 30, 40, 1000  
Mean = (10 + 20 + 30 + 40 + 1000) / 5 = 220

➡️ The mean is heavily affected by the extreme value (1000).

---

## 3. What is Median?
**Median** is the *middle value* of a dataset when arranged in ascending or descending order.

### Steps to find Median:
- Arrange the data in sorted order
- If the number of values is **odd**, median is the middle value
- If the number of values is **even**, median is the average of the two middle values

### Example:
Data: 10, 20, 30, 40, 1000  
Median = 30

➡️ The median is **not affected** by the extreme value.

---

## 4. Why Median is More Reliable Than Mean

| Aspect | Mean | Median |
|------|------|--------|
| Effect of Outliers | High | Very Low |
| Skewed Data | Misleading | Accurate |
| Real-world Use | Limited | Preferred |
| Robustness | Weak | Strong |

---

## 5. Real-World Scenarios Where Median is Better

### 1. Income & Salary Data
Few high earners can inflate the average income. Median income reflects what most people earn.

### 2. House Prices
Luxury properties distort averages. Median gives a realistic market value.

### 3. Response Time & Performance Metrics
Median avoids distortion caused by rare delays.

### 4. Data Science & AI
Median is used during **data preprocessing**, **feature analysis**, and **robust statistics**.

---

## 6. Mean vs Median: When to Use What?

- ✅ Use **Mean** when data is **uniform and symmetric**
- ✅ Use **Median** when data is **skewed or has outliers**

📌 Rule of Thumb:
> If extreme values exist, trust the **median**.

---

## 7. Key Takeaways
- Mean can be misleading in real-world data
- Median represents the true center
- Median is more robust and reliable
- Widely used in economics, statistics, and AI

---

## 8. Conclusion
Understanding when to use **median over mean** leads to better data interpretation and smarter decisions. Strong statistical fundamentals are essential for **Data Science, AI, and Analytics**.

---

📘 *Part of #100DaysLearningChallenge – building strong foundations step by step.*

