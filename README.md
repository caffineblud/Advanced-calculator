# 🧮 Advanced Calculator

A powerful command-line calculator built with Python that supports basic arithmetic, scientific calculations, trigonometric operations, logarithms, factorials, custom expression evaluation, and more.

## ✨ Features

**🔢 Basic Arithmetic Operations**
* Addition (➕)
* Subtraction (➖)
* Multiplication (✖️)
* Division (➗)

**📈 Advanced Mathematical Functions**
* Power calculation
* Nth root
* Exponential function (e^x)
* Percentage calculation
* Factorial (!)

**🔬 Scientific & Trigonometric Functions**
* Logarithms with custom base
* Sine, Cosine, Tangent (📐)
* Degree to radian conversion

**🔣 Custom Expression Evaluator**
Supports complex string expressions like:
```python
sin(30) + sqrt(16) + log(100, 10)
```
## 🛡️ Robust Error Handling
​-Division by zero prevention
-​Invalid logarithm inputs
​-Invalid factorial values
​-Safe expression evaluation

**Calculation history tracking**

## 🛠️ Technologies Used
*🐍 Python 3
​*🧮 Built-in math module

## 📁 Project Structure
```text
advanced-calculator/
│
├── calculator.py
└── README.md
```
## installation->
**1.clone the repository**
```text
git clone [https://github.com/your-username/advanced-calculator.git](https://github.com/your-username/advanced-calculator.git)
```
**2.navigate to the project**
```python
cd advanced-calculator
```
**3.run the program**
```python
python calculator.py
```
## Menu Options
```text
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Nth root
7. Factorial
8. Logarithm
9. Trigonometry
10. Percentage
11. Exponential
12. Evaluate custom expression
0. Exit
```
## 💡 Example Usage
### Addition
```text
Enter first number: 10
Enter second number: 20
Result: 30

```
### Trigonometry
```text
Enter angle in degrees: 30
Choose sine
Result: 0.5

```
### Custom Expression
```text
Expression: sin(45) + sqrt(25)
Output: 5.707106781186548

```
## 🧮 Supported Functions in Custom Expressions
| Function | Description |
|---|---|
| sin(x) | Sine in degrees |
| cos(x) | Cosine in degrees |
| tan(x) | Tangent in degrees |
| sqrt(x) | Square root |
| log(x, base) | Logarithm |
| log10(x) | Base-10 logarithm |
| pow(x, y) | Power |
| abs(x) | Absolute value |
| round(x) | Round value |
## ⚠️ Error Handling Examples
```text
Error: Cannot divide by zero.

```
```text
Error: Factorial is only defined for non-negative integers.

```
## 🔮 Future Improvements
 * [ ] GUI version using Tkinter or PyQt
 * [ ] Scientific notation support
 * [ ] Save calculation history to file
 * [ ] Unit converter
 * [ ] Complex number operations
## 📜 License
This project is open-source and available under the **MIT License**.
## 👨‍💻 Author
Developed by **Yash Kr Singh**.
