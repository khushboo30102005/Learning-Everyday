# Day-96 | #100DaysLearningChallenge  
## What Is a Neuron in Neural Networks?

A **neuron** is the **fundamental building block of a neural network**.  
It is inspired by the **biological neuron** in the human brain but works using **mathematical operations**.

In Machine Learning and Deep Learning, neurons help models **learn patterns, relationships, and representations** from data.

---

## 1. Biological Neuron vs Artificial Neuron

### Biological Neuron
- **Dendrites** → receive signals  
- **Cell body** → processes signals  
- **Axon** → sends signals to other neurons  

### Artificial Neuron
- **Inputs** → features/data  
- **Weights** → importance of each input  
- **Summation + Bias** → computation  
- **Activation Function** → decision-making  

👉 Artificial neurons mathematically mimic biological neurons.

---

## 2. Structure of an Artificial Neuron

An artificial neuron consists of:

### 1️⃣ Inputs (x₁, x₂, …, xₙ)
- Represent features of the dataset  
- Example: height, weight, pixels, words, etc.

### 2️⃣ Weights (w₁, w₂, …, wₙ)
- Show how important each input is  
- Learned during training

### 3️⃣ Bias (b)
- Helps shift the output  
- Allows the model to fit data better

### 4️⃣ Weighted Sum
The neuron computes:

\[
z = (x₁w₁ + x₂w₂ + ... + xₙwₙ) + b
\]

### 5️⃣ Activation Function
- Converts the weighted sum into an output  
- Adds **non-linearity**, which is essential for learning complex patterns

---

## 3. Common Activation Functions

### 🔹 ReLU (Rectified Linear Unit)
\[
f(x) = \max(0, x)
\]
- Most widely used
- Fast and efficient

### 🔹 Sigmoid
\[
f(x) = \frac{1}{1 + e^{-x}}
\]
- Output between 0 and 1
- Used in binary classification

### 🔹 Tanh
- Output between -1 and 1
- Zero-centered

---

## 4. Output of a Neuron

- The activated value is the **output**
- This output is:
  - Sent to the next neuron (hidden layers)
  - Or used as final prediction (output layer)

---

## 5. Neurons and Layers

- **Input Layer** → receives data
- **Hidden Layers** → process and learn patterns
- **Output Layer** → produces final result

📌 **Deep Learning** = many layers of neurons working together

---

## 6. Why Neurons Are Important

- Learn complex patterns from data
- Enable decision-making in models
- Foundation of:
  - Image Recognition
  - Speech Recognition
  - NLP
  - Recommendation Systems
  - Chatbots

---

## 7. Simple Example

If:
- Inputs: x₁ = 2, x₂ = 3  
- Weights: w₁ = 0.5, w₂ = 1  
- Bias: b = 1  

Then:
\[
z = (2 × 0.5) + (3 × 1) + 1 = 5
\]

After applying activation → final output is produced.

---

## 8. Key Takeaway

> **A neuron takes inputs, applies weights, adds bias, passes through an activation function, and produces an output.**

Neural Networks = **Neurons + Weights + Activation + Learning**

---

### ✅ Summary
- Neuron is the core unit of neural networks
- Inspired by biology, powered by mathematics
- Multiple neurons together create intelligent systems

---

