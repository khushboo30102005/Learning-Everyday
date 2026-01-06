# Sigmoid Function Explained

## Day-94 | #100DaysLearningChallenge

## What is the Sigmoid Function?
The **Sigmoid function** is a mathematical function used in Machine Learning to map any real-valued number into a value between **0 and 1**.

Because of this property, it is widely used in **classification problems**, especially binary classification.

---

## Mathematical Formula
σ(x) = 1 / (1 + e^(-x))

Where:
- `e` is Euler’s number (~2.718)
- `x` is the input value

---

## Why Sigmoid is Important?
- Converts raw scores into **probabilities**
- Helps in **binary decision-making (0 or 1)**
- Core function in **Logistic Regression**
- Commonly used in **Neural Network output layers**

---

## Behavior of Sigmoid Function
| Input (x) | Output σ(x) |
|----------|-------------|
| Large positive value | Close to 1 |
| 0 | 0.5 |
| Large negative value | Close to 0 |

---

## Real-World Example
If a model predicts:
- σ(x) = 0.85 → 85% probability of class 1
- σ(x) = 0.20 → 20% probability of class 1

Threshold (usually 0.5) is used to make final predictions.

---

## Limitations
- Suffers from **vanishing gradient** problem
- Not zero-centered
- Slower convergence for deep networks

---

## Where It Is Used?
- Logistic Regression
- Binary Classification Models
- Neural Network Output Layers

---

## Key Takeaway
Understanding the Sigmoid function builds a strong foundation for:
- Machine Learning
- Deep Learning
- Probability-based models