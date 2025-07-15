# Quadratic Equation Calculator

I created this project to test my Python knowledge as part of my academic studies. It helped me learn how to build GUI applications, work with custom modules, and visualize mathematical concepts using Python and Matplotlib.
## Overview

**Quadratic Equation Calculator** is a Python-based GUI application designed to solve quadratic equations of the form _ax² + bx + c = 0_. Built using Tkinter, it provides a user-friendly interface to calculate determinants, roots (real or complex), and visualize the quadratic curve.

---

## Features

- **Intuitive GUI:** Enter coefficients and interact with easy-to-use buttons.
- **Determinant Calculation:** Instantly compute the determinant (_b² - 4ac_) of the quadratic equation.
- **Root Calculation:** Get both real and complex roots using robust custom logic.
- **Interactive Graph:** Visualize the equation’s curve and save the plot as an image.
- **Clear & Exit:** Easily reset input fields or exit the application.

---

## Dependencies

Install required dependencies with:

```bash
pip install -r requirements.txt
```

**Packages Used:**
- `matplotlib` (for plotting graphs)
- `tkinter` (GUI, comes pre-installed with Python)
- `math` (real root calculations, comes pre-installed)
- `cmath` (complex root calculations, comes pre-installed)

---

## How It Works

1. **Enter Coefficients:** Input values for `x²`, `x`, and the constant term in the respective fields.
2. **Calculate Roots:** Click **Calculate Roots** to view the determinant and roots.
3. **View Graph:** Click **Graph** for an interactive plot of the quadratic equation. You can save the graph as an image.
4. **Clear Fields:** Click **Clear** to reset all fields and close any open graph window.
5. **Exit:** Click **Exit** or close the window to quit.

---

## Application Structure

```
Quadratic-Equation-Calculator/
├── README.md
├── calc.py                  # Main GUI and application logic
├── LICENSE                  # GNU GPL v3 License
├── requirements.txt         # Required Python packages
└── logic/
    ├── __init__.py
    ├── determinant.py       # Function to compute determinant
    └── roots.py             # Function to compute roots (real/complex)
```

---

## Code Highlights

- **Custom Modules:**
  - `logic/determinant.py`: Calculates the determinant (D = b² - 4ac).
  - `logic/roots.py`: Calculates both real and complex roots using `math` and `cmath` modules.

- **Main GUI (`calc.py`):**
  - Uses Tkinter for input fields, labels, and buttons.
  - Handles placeholder text, root calculation, graph plotting, and GUI layout.

---

## Example Usage

```python
# Calculate determinant
from logic import determinant
d = determinant.det(a, b, c)

# Calculate roots
from logic import roots
r = roots.root(a, b, c)
```

---

## Screenshots

![Calculator UI](https://github.com/abhishekmallav/Quadratic-Equation-Calculator/blob/main/preview/calculator-01.png)

![Graph Example](https://github.com/abhishekmallav/Quadratic-Equation-Calculator/blob/main/preview/screenshot.png)

---

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).



## Author

Created by [abhishekmallav](https://github.com/abhishekmallav)



## Contribution

Feel free to fork, contribute, or raise issues. Pull requests are welcome!



## Contact

For any questions or feedback, please open an issue or reach out via GitHub.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhishekmallav)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abhimallav1439@gmail.com?subject=Hello%20There&body=Just%20wanted%20to%20say%20hi!)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/abhishekmallav)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://www.x.com/abhishekmallav)

