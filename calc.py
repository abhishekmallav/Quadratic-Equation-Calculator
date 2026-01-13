import customtkinter as ctk
import matplotlib.pyplot as plt
from logic import determinant, roots

# -------------------- App Setup --------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Quadratic Equation Calculator")
root.geometry("600x700")

# -------------------- Design System --------------------
COLOR_PRIMARY = "#22c55e"
COLOR_PRIMARY_DARK = "#16a34a"
COLOR_ACCENT = "#000000"
COLOR_BG = "#ffffff"
COLOR_TEXT = "#000000"
COLOR_TEXT_SECONDARY = "#404040"
COLOR_BORDER = "#e5e5e5"
HOVER_COLOR = "#daf7c8"

FONT_HEADING = ("Poppins", 24, "bold")
FONT_SUBHEADING = ("Poppins", 16, "bold")
FONT_BODY = ("Inter", 14)
FONT_BUTTON = ("Inter", 14, "bold")

# -------------------- Globals --------------------
coeff_a = coeff_b = coeff_c = None

# -------------------- Logic Functions --------------------
def clear_all():
    print("\n" + "="*50)
    print("CLEARING ALL DATA")
    print("="*50)
    global coeff_a, coeff_b, coeff_c
    coeff_a = coeff_b = coeff_c = None
    print("✓ Global coefficients reset to None")

    entry_a.delete(0, "end")
    entry_b.delete(0, "end")
    entry_c.delete(0, "end")
    print("✓ Input fields cleared")

    label_discriminant.configure(text="Discriminant (b² - 4ac):")
    label_roots.configure(text="Roots:")
    print("✓ Result labels reset")
    graph_button.configure(state="disabled")
    print("✓ Graph button disabled")
    plt.close("all")
    print("✓ All matplotlib windows closed")
    print("="*50 + "\n")


def calculate():
    print("\n" + "="*50)
    print("CALCULATE BUTTON PRESSED")
    print("="*50)
    global coeff_a, coeff_b, coeff_c
    try:
        print("\nStep 1: Reading input values...")
        coeff_a = float(entry_a.get())
        coeff_b = float(entry_b.get())
        coeff_c = float(entry_c.get())
        print(f"✓ Coefficient a (x²): {coeff_a}")
        print(f"✓ Coefficient b (x): {coeff_b}")
        print(f"✓ Coefficient c (constant): {coeff_c}")
        print(f"\nQuadratic Equation: {coeff_a}x² + {coeff_b}x + {coeff_c} = 0")

        print("\nStep 2: Calculating discriminant...")
        d = determinant.det(coeff_a, coeff_b, coeff_c)
        print(f"✓ Discriminant (b² - 4ac) = {d:.2f}")

        label_discriminant.configure(
            text=f"Discriminant (b² - 4ac): {d:.2f}"
        )

        print("\nStep 3: Calculating roots...")
        r1, r2 = roots.root(coeff_a, coeff_b, coeff_c)

        if d < 0:
            print("⚠ Discriminant is NEGATIVE")
            print("→ Real roots don't exist")
            print(f"✓ Imaginary Root 1: {r1:.4f}")
            print(f"✓ Imaginary Root 2: {r2:.4f}")
            # Negative discriminant - show complex roots with message
            label_roots.configure(
                text=f"Discriminant is Negative\nReal Roots Don't Exist\n\nImaginary Roots:\n{r1:.4f}\n{r2:.4f}"
            )
        else:
            print("✓ Discriminant is POSITIVE or ZERO")
            print("→ Real roots exist")
            print(f"✓ Root 1: {r1:.4f}")
            print(f"✓ Root 2: {r2:.4f}")
            # Positive or zero discriminant - show real roots
            roots_text = f"Roots:\n{r1:.4f}\n{r2:.4f}"
            label_roots.configure(text=roots_text)

        print("\nStep 4: Enabling graph button...")
        graph_button.configure(state="normal")
        print("✓ Graph button enabled")
        print("\n" + "="*50)
        print("CALCULATION COMPLETE")
        print("="*50 + "\n")

    except ValueError as e:
        print("\n" + "!"*50)
        print("ERROR: Invalid input detected")
        print(f"Details: {e}")
        print("!"*50 + "\n")
        label_discriminant.configure(text="Error: Enter valid numbers")
        label_roots.configure(text="")
        graph_button.configure(state="disabled")



def plot_graph():
    print("\n" + "="*50)
    print("GRAPH BUTTON PRESSED")
    print("="*50)
    if coeff_a is None or coeff_b is None or coeff_c is None:
        print("⚠ ERROR: No coefficients available")
        print("Please calculate roots first before plotting graph")
        print("="*50 + "\n")
        return

    print(f"\nUsing equation: {coeff_a}x² + {coeff_b}x + {coeff_c} = 0")
    print("\nStep 1: Generating x values from -10 to 10...")
    x_vals = list(range(-10, 11))
    print(f"✓ Generated {len(x_vals)} x-values")
    
    print("\nStep 2: Calculating y values...")
    y_vals = [
        coeff_a * x**2 + coeff_b * x + coeff_c
        for x in x_vals
    ]
    print(f"✓ Calculated {len(y_vals)} y-values")

    print("\nStep 3: Creating matplotlib figure...")
    plt.figure(figsize=(6, 4))
    print("✓ Figure created (6x4 inches)")
    
    print("\nStep 4: Plotting the curve...")
    plt.plot(
        x_vals,
        y_vals,
        color=COLOR_PRIMARY,
        linewidth=2.5,
        label="y = ax² + bx + c"
    )
    print(f"✓ Curve plotted with color {COLOR_PRIMARY}")

    print("\nStep 5: Adding axes and grid...")
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.axvline(0, linestyle="--", linewidth=1)
    print("✓ X and Y axes added")

    plt.title("Quadratic Equation Graph", fontweight="bold")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.grid(True, alpha=0.3)
    plt.legend()
    print("\nStep 6: Displaying graph window...")
    print("✓ Graph ready to display")
    print("="*50 + "\n")
    plt.show()

# -------------------- UI Layout --------------------
main_frame = ctk.CTkFrame(root, fg_color=COLOR_BG)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# -------------------- Hero Section --------------------
hero = ctk.CTkFrame(
    main_frame,
    fg_color=COLOR_BG,
    border_width=2,
    border_color=COLOR_ACCENT,
    corner_radius=12
)
hero.pack(fill="x", pady=(0, 24))

ctk.CTkLabel(hero, text="🧮", font=("Segoe UI Emoji", 48)).pack(pady=(20, 10))
ctk.CTkLabel(
    hero,
    text="Quadratic Equation Calculator",
    font=FONT_HEADING
).pack()

ctk.CTkLabel(
    hero,
    text="Solve ax² + bx + c = 0",
    font=FONT_BODY,
    text_color=COLOR_TEXT_SECONDARY
).pack(pady=(0, 20))

# -------------------- Input Section --------------------
ctk.CTkLabel(
    main_frame,
    text="Enter Coefficients",
    font=FONT_SUBHEADING
).pack(pady=(0, 12))

inputs = ctk.CTkFrame(main_frame, fg_color=COLOR_BG)
inputs.pack(pady=(0, 16))

entry_a = ctk.CTkEntry(inputs, width=120, height=40, placeholder_text="x²")
entry_b = ctk.CTkEntry(inputs, width=120, height=40, placeholder_text="x")
entry_c = ctk.CTkEntry(inputs, width=120, height=40, placeholder_text="const")

entry_a.grid(row=0, column=0, padx=8)
entry_b.grid(row=0, column=1, padx=8)
entry_c.grid(row=0, column=2, padx=8)

# -------------------- Calculate Button --------------------
ctk.CTkButton(
    main_frame,
    text="Calculate Roots",
    command=calculate,
    fg_color=COLOR_PRIMARY,
    hover_color=COLOR_PRIMARY_DARK,
    text_color="white",
    font=FONT_BUTTON,
    height=44
).pack(pady=12)

# -------------------- Results Section --------------------
results = ctk.CTkFrame(
    main_frame,
    fg_color=COLOR_BG,
    border_width=1,
    border_color=COLOR_BORDER,
    corner_radius=12
)
results.pack(fill="both", expand=True, pady=(0, 16))

ctk.CTkLabel(
    results,
    text="Results",
    font=FONT_SUBHEADING
).pack(pady=(16, 12))

label_discriminant = ctk.CTkLabel(
    results,
    text="Discriminant (b² - 4ac):",
    font=FONT_BODY,
    text_color=COLOR_TEXT_SECONDARY
)
label_discriminant.pack(pady=4)

label_roots = ctk.CTkLabel(
    results,
    text="Roots:",
    font=FONT_BODY,
    text_color=COLOR_TEXT_SECONDARY
)
label_roots.pack(pady=4)

# -------------------- Action Buttons --------------------
actions = ctk.CTkFrame(main_frame, fg_color=COLOR_BG)
actions.pack(fill="x")

graph_button = ctk.CTkButton(
    actions,
    text="📊 Graph",
    command=plot_graph,
    state="disabled",
    border_width=2,
    border_color=COLOR_ACCENT,
    fg_color=COLOR_BG,
    hover_color=HOVER_COLOR,
    text_color=COLOR_ACCENT,
    height=40
)
graph_button.pack(side="left", expand=True, fill="x", padx=4)

ctk.CTkButton(
    actions,
    text="Clear",
    command=clear_all,
    border_width=2,
    border_color=COLOR_ACCENT,
    fg_color=COLOR_BG,
    hover_color=HOVER_COLOR,
    text_color=COLOR_ACCENT,
    height=40
).pack(side="left", expand=True, fill="x", padx=4)

ctk.CTkButton(
    actions,
    text="Exit",
    command=root.quit,
    border_width=2,
    border_color=COLOR_ACCENT,
    fg_color=COLOR_ACCENT,
    hover_color="#1a1a1a",
    text_color="white",
    height=40
).pack(side="left", expand=True, fill="x", padx=4)

# -------------------- Run App --------------------
root.mainloop()
