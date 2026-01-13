# Quadratic Equation Calculator - AI Agent Instructions

## Project Overview

A **CustomTkinter** GUI application applying **Modern Minimal Brutalist** design principles to solve quadratic equations (ax² + bx + c = 0), calculate determinants, find roots (real/complex), and visualize parabolas using Matplotlib.

## Architecture

**Modular Design:**
- [calc.py](../calc.py): Main GUI (CustomTkinter) with design system styling and event handlers
- [logic/determinant.py](../logic/determinant.py): Pure calculation function `det(a, b, c)` returns b² - 4ac
- [logic/roots.py](../logic/roots.py): Pure calculation function `root(a, b, c)` returns tuple of roots

**Data Flow:** User inputs → `calc.py` event handlers → `logic` module functions → GUI display/plot

## Design System (Modern Minimal Brutalist)

### Color Palette
```python
COLOR_PRIMARY = "#22c55e"      # Vibrant green - primary actions
COLOR_PRIMARY_DARK = "#16a34a" # Darker green - hover states
COLOR_ACCENT = "#000000"       # Pure black - structure & emphasis
COLOR_TEXT_SECONDARY = "#404040" # Gray - secondary text
COLOR_BORDER = "#e5e5e5"       # Light gray - borders
```

### Typography
- **Headings**: Poppins (bold, size 16-24)
- **Body**: Inter (regular, size 14)
- **Buttons**: Inter (bold, size 14)

### Spacing & Layout
- Main container: 20px padding
- Between sections: 16-24px
- Button height: 40-44px
- Corner radius: 8-12px
- Entry width: 120px, height: 40px

## Key Patterns & Conventions

### 1. Module Organization
- **Pure functions only** in `logic/` - no side effects, no GUI dependencies
- Functions accept coefficients `(a, b, c)` in consistent order
- Return plain Python types (floats, tuples) - never GUI objects

### 2. CustomTkinter Widget Usage
```python
# CTkEntry (not Text widgets)
entry = ctk.CTkEntry(parent, placeholder_text="Value", ...)
value = entry.get()  # Direct .get(), not .get("1.0", "end")

# CTkLabel for results
label = ctk.CTkLabel(parent, text="...", font=FONT_BODY)
label.configure(text="New value")  # Update with .configure()

# CTkButton with design system colors
button = ctk.CTkButton(
    parent, 
    fg_color=COLOR_PRIMARY,
    hover_color=COLOR_PRIMARY_DARK,
    border_width=2  # For secondary buttons
)
```

### 3. GUI State Management
```python
# Global variables store coefficients after calculation
global x, y, z  # Set in equal_click(), used by show_graph()
```

### 4. Placeholder Handling (CustomTkinter Built-in)
CustomTkinter handles placeholders natively via `placeholder_text` parameter:
```python
a = ctk.CTkEntry(parent, placeholder_text="x²")
# No manual placeholder management needed
```

### 5. Complex vs Real Roots
[logic/roots.py](../logic/roots.py) handles both cases:
- `d >= 0`: Use `math.sqrt()` for real roots
- `d < 0`: Use `cmath.sqrt()` for complex roots (prints warning to console)

### 6. Button Hierarchy
- **Primary (green)**: Main action (Calculate Roots)
- **Secondary (white with black border)**: Supporting actions (Graph, Clear)
- **Accent (black)**: Exit/destructive actions

## Development Workflows

**Install Dependencies:**
```bash
pip install -r requirements.txt
```

**Run Application:**
```bash
python calc.py
```

**Design System Reference:**
See [DESIGN_SYSTEM_PROMPT.md](../DESIGN_SYSTEM_PROMPT.md) for full philosophy

## Critical Implementation Details

1. **CustomTkinter initialization:**
   ```python
   ctk.set_appearance_mode("light")
   ctk.set_default_color_theme("green")
   ```

2. **Entry widget access:** Use `.get()` for CTkEntry, NOT `.get("1.0", "end-1c")` (old Text widget syntax)

3. **Plot styling:** Uses `COLOR_PRIMARY` (#22c55e) for curve, `COLOR_ACCENT` for axes

4. **Plot cleanup:** `plt.close('all')` in `clear_labels()` prevents memory leaks

5. **Layout system:** Uses `.pack()` with `fill="x"` and `pady` for vertical stacking

6. **Error handling:** `equal_click()` wraps calculations in try/except for invalid inputs

## When Adding Features

- **New calculations:** Create new functions in `logic/` following pure function pattern
- **New UI elements:** Use `ctk.CTk*` widgets, maintain design system colors/fonts
- **Graph modifications:** Edit `plot_quadratic_eq()` - uses hardcoded range `x = list(range(-10, 11))`
- **Button actions:** Follow button hierarchy (primary green, secondary bordered, accent black)
- **Spacing:** Maintain 8px grid (use multiples: 8, 16, 24, 32px)
