import tkinter as tk
from tkinter import font as tkfont

# Features
# - Metric / Imperial toggle — switches between kg/cm and lbs/in seamlessly
# - Live gauge bar — a colour-coded progress bar spanning BMI 10–40
# - Category display — shows Underweight / Normal / Overweight / Obese with a matching colour
# - Health tip — a short contextual message per category
# - Enter key support — press Enter to calculate without clicking the button
# - Input validation — friendly error message for invalid inputs


# ── Color palette ──────────────────────────────────────────────
BG        = "#0F1724"   # deep navy
PANEL     = "#1A2535"   # card surface
ACCENT    = "#4FC3F7"   # sky blue
SUCCESS   = "#66BB6A"   # healthy green
WARN      = "#FFA726"   # amber – overweight
DANGER    = "#EF5350"   # coral – obese / underweight
TEXT_PRI  = "#E8EDF2"   # primary text
TEXT_SEC  = "#7A8FA6"   # secondary / labels
ENTRY_BG  = "#0F1724"
BORDER    = "#2C3E55"

# BMI category thresholds
CATEGORIES = [
    (0,   18.5, "Underweight", DANGER),
    (18.5, 25,  "Normal weight", SUCCESS),
    (25,   30,  "Overweight", WARN),
    (30,  100,  "Obese", DANGER),
]


def get_category(bmi):
    for lo, hi, label, color in CATEGORIES:
        if lo <= bmi < hi:
            return label, color
    return "Obese", DANGER


def calculate():
    try:
        if unit_var.get() == "metric":
            weight_kg = float(weight_entry.get())
            height_m  = float(height_entry.get()) / 100   # cm → m
        else:
            weight_kg = float(weight_entry.get()) * 0.453592   # lbs → kg
            height_m  = float(height_entry.get()) * 0.0254      # in  → m

        if weight_kg <= 0 or height_m <= 0:
            raise ValueError

        bmi = weight_kg / (height_m ** 2)
        label, color = get_category(bmi)

        # Update result widgets
        bmi_value_lbl.config(text=f"{bmi:.1f}", fg=color)
        category_lbl.config(text=label, fg=color)

        # Draw gauge bar
        draw_gauge(bmi, color)

        # Show tip
        tips = {
            "Underweight":    "Consider a nutrient-rich diet and consult a healthcare provider.",
            "Normal weight":  "Great! Maintain your balanced diet and active lifestyle.",
            "Overweight":     "Regular aerobic activity and mindful eating can help.",
            "Obese":          "Please consult a healthcare professional for a personalised plan.",
        }
        tip_lbl.config(text=tips[label], fg=TEXT_SEC)
        error_lbl.config(text="")

    except ValueError:
        bmi_value_lbl.config(text="--", fg=TEXT_SEC)
        category_lbl.config(text="", fg=TEXT_SEC)
        tip_lbl.config(text="", fg=TEXT_SEC)
        error_lbl.config(text="⚠  Please enter valid positive numbers.", fg=DANGER)
        gauge_canvas.delete("fill")


def draw_gauge(bmi, color):
    """Draw a horizontal progress bar clamped between 10 and 40."""
    gauge_canvas.delete("fill")
    clamped = max(10, min(bmi, 40))
    fraction = (clamped - 10) / 30          # 0→1 across range 10–40
    bar_w = int(fraction * GAUGE_W)
    if bar_w > 0:
        gauge_canvas.create_rectangle(
            0, 0, bar_w, GAUGE_H,
            fill=color, outline="", tags="fill"
        )


def toggle_units():
    is_metric = unit_var.get() == "metric"
    if is_metric:
        weight_lbl.config(text="Weight  (kg)")
        height_lbl.config(text="Height  (cm)")
        metric_btn.config(relief="sunken",  bg=ACCENT, fg=BG)
        imperial_btn.config(relief="flat",  bg=PANEL,  fg=TEXT_SEC)
    else:
        weight_lbl.config(text="Weight  (lbs)")
        height_lbl.config(text="Height  (in)")
        metric_btn.config(relief="flat",   bg=PANEL,  fg=TEXT_SEC)
        imperial_btn.config(relief="sunken", bg=ACCENT, fg=BG)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    bmi_value_lbl.config(text="--", fg=TEXT_SEC)
    category_lbl.config(text="", fg=TEXT_SEC)
    tip_lbl.config(text="")
    error_lbl.config(text="")
    gauge_canvas.delete("fill")


# ── Root window ────────────────────────────────────────────────
root = tk.Tk()
root.title("BMI Calculator")
root.configure(bg=BG)
root.resizable(False, False)
root.geometry("440x600")

TITLE_FONT  = tkfont.Font(family="Helvetica Neue", size=22, weight="bold")
LABEL_FONT  = tkfont.Font(family="Helvetica Neue", size=11)
ENTRY_FONT  = tkfont.Font(family="Helvetica Neue", size=13)
BIG_FONT    = tkfont.Font(family="Helvetica Neue", size=48, weight="bold")
CAT_FONT    = tkfont.Font(family="Helvetica Neue", size=14, weight="bold")
TIP_FONT    = tkfont.Font(family="Helvetica Neue", size=10)
BTN_FONT    = tkfont.Font(family="Helvetica Neue", size=11, weight="bold")

pad = dict(padx=30)

# ── Title ──────────────────────────────────────────────────────
tk.Label(root, text="BMI Calculator", font=TITLE_FONT,
         bg=BG, fg=TEXT_PRI).pack(pady=(28, 4))
tk.Label(root, text="Body Mass Index", font=TIP_FONT,
         bg=BG, fg=TEXT_SEC).pack()

# ── Unit toggle ────────────────────────────────────────────────
unit_var = tk.StringVar(value="metric")

toggle_frame = tk.Frame(root, bg=PANEL, bd=0, highlightthickness=1,
                        highlightbackground=BORDER)
toggle_frame.pack(pady=18, **pad, fill="x")

metric_btn = tk.Button(
    toggle_frame, text="Metric", font=BTN_FONT,
    bg=ACCENT, fg=BG, bd=0, relief="sunken", cursor="hand2",
    activebackground=ACCENT, activeforeground=BG,
    command=lambda: [unit_var.set("metric"), toggle_units()]
)
metric_btn.pack(side="left", fill="x", expand=True, ipady=6)

imperial_btn = tk.Button(
    toggle_frame, text="Imperial", font=BTN_FONT,
    bg=PANEL, fg=TEXT_SEC, bd=0, relief="flat", cursor="hand2",
    activebackground=BORDER, activeforeground=TEXT_PRI,
    command=lambda: [unit_var.set("imperial"), toggle_units()]
)
imperial_btn.pack(side="left", fill="x", expand=True, ipady=6)

# ── Input fields ───────────────────────────────────────────────
def make_field(parent, label_text):
    frame = tk.Frame(parent, bg=BG)
    frame.pack(fill="x", **pad, pady=6)
    lbl = tk.Label(frame, text=label_text, font=LABEL_FONT,
                   bg=BG, fg=TEXT_SEC, anchor="w")
    lbl.pack(fill="x")
    entry_frame = tk.Frame(frame, bg=ENTRY_BG, highlightthickness=1,
                           highlightbackground=BORDER)
    entry_frame.pack(fill="x")
    entry = tk.Entry(entry_frame, font=ENTRY_FONT, bg=ENTRY_BG,
                     fg=TEXT_PRI, insertbackground=ACCENT,
                     relief="flat", bd=8)
    entry.pack(fill="x")
    # Highlight border on focus
    entry.bind("<FocusIn>",  lambda e: entry_frame.config(highlightbackground=ACCENT))
    entry.bind("<FocusOut>", lambda e: entry_frame.config(highlightbackground=BORDER))
    return lbl, entry

weight_lbl, weight_entry = make_field(root, "Weight  (kg)")
height_lbl, height_entry = make_field(root, "Height  (cm)")

# ── Calculate button ───────────────────────────────────────────
calc_btn = tk.Button(
    root, text="Calculate BMI", font=BTN_FONT,
    bg=ACCENT, fg=BG, bd=0, relief="flat", cursor="hand2",
    activebackground="#81D4FA", activeforeground=BG,
    command=calculate
)
calc_btn.pack(fill="x", **pad, pady=(14, 0), ipady=10)

# Bind Enter key
root.bind("<Return>", lambda e: calculate())

# ── Error label ────────────────────────────────────────────────
error_lbl = tk.Label(root, text="", font=TIP_FONT, bg=BG, fg=DANGER)
error_lbl.pack(pady=(4, 0))

# ── Result card ────────────────────────────────────────────────
result_card = tk.Frame(root, bg=PANEL, bd=0, highlightthickness=1,
                       highlightbackground=BORDER)
result_card.pack(fill="x", **pad, pady=14)

bmi_value_lbl = tk.Label(result_card, text="--", font=BIG_FONT,
                          bg=PANEL, fg=TEXT_SEC)
bmi_value_lbl.pack(pady=(14, 0))

category_lbl = tk.Label(result_card, text="", font=CAT_FONT,
                         bg=PANEL, fg=TEXT_SEC)
category_lbl.pack()

# Gauge bar
GAUGE_W, GAUGE_H = 340, 8
gauge_bg = tk.Frame(result_card, bg=BORDER, height=GAUGE_H, width=GAUGE_W)
gauge_bg.pack(pady=10)
gauge_bg.pack_propagate(False)

gauge_canvas = tk.Canvas(gauge_bg, bg=BORDER, bd=0, highlightthickness=0,
                          height=GAUGE_H, width=GAUGE_W)
gauge_canvas.pack()

# Scale labels
scale_frame = tk.Frame(result_card, bg=PANEL)
scale_frame.pack(fill="x", padx=30)
for txt, anchor in [("10", "w"), ("25", "center"), ("40", "e")]:
    tk.Label(scale_frame, text=txt, font=TIP_FONT,
             bg=PANEL, fg=TEXT_SEC).pack(side="left", expand=True, anchor=anchor)

tip_lbl = tk.Label(result_card, text="", font=TIP_FONT, wraplength=340,
                    bg=PANEL, fg=TEXT_SEC, justify="center")
tip_lbl.pack(pady=(4, 16), padx=20)

# ── Category legend ────────────────────────────────────────────
legend_frame = tk.Frame(root, bg=BG)
legend_frame.pack(**pad, pady=(0, 20))

for _, _, cat_name, cat_color in CATEGORIES:
    row = tk.Frame(legend_frame, bg=BG)
    row.pack(anchor="w", pady=1)
    dot = tk.Canvas(row, width=10, height=10, bg=BG, highlightthickness=0)
    dot.create_oval(1, 1, 9, 9, fill=cat_color, outline="")
    dot.pack(side="left", padx=(0, 6))
    tk.Label(row, text=cat_name, font=TIP_FONT,
             bg=BG, fg=TEXT_SEC).pack(side="left")

root.mainloop()