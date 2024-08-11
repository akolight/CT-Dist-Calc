import tkinter as tk
import tkinter.ttk as ttk
import math

root = tk.Tk()  # This creates the root, needs root.mainloop() to work
root.geometry("400x200")
root.title("Distance Calculator")

frm_entry = tk.Frame(master=root, width=100, height=100)
frm_ansBox = tk.Frame(master=root, width=100, height=100)

lbl_A1 = ttk.Label(master=frm_entry, text="Enter start point:")
lbl_A1.pack()
ent_A1 = ttk.Entry(master=frm_entry)
ent_A1.pack()

txt_B1 = ttk.Label(master=frm_entry, text="Enter scheduled distance:")
txt_B1.pack()
ent_B1 = ttk.Entry(master=frm_entry)
ent_B1.pack()

lbl_C1 = ttk.Label(master=frm_entry, text="Enter T point:")
lbl_C1.pack()
ent_C1 = ttk.Entry(master=frm_entry)
ent_C1.pack()

distance = 0
percentage = 0

station_dict = {
    "SFK": 0,
    "TWE": 1.16,
    "BAY": 5.06,
    "SSF": 9.16,
    "SBR": 11,
    "MIL": 13.56,
    "BWY": 15.13,
    "BUR": 16.23,
    "SMT": 17.6,
    "HPK": 18.93,
    "HIL": 19.84,
    "BEL": 21.83,
    "SCS": 23.09,
    "RWC": 25.3,
    "MPK": 28.74,
    "PAL": 30,
    "STF": 30.57,
    "CAL": 31.63,
    "SAT": 33.99,
    "MVW": 35.97,
    "SUN": 38.62,
    "LAW": 40.62,
    "SCL": 44.3,
    "CPK": 45.59,
    "CEMOF": 45.85,
    "SJD": 46.85,
    "TAM": 48.56,
    "CAP": 52.45,
    "BHL": 55.73,
    "MHL": 67.5,
    "SMR": 71.23,
    "GIL": 77.46,
    "0": 20
}
def calculate(event):
    point_a = ent_A1.get()
    point_b = ent_C1.get()
    scheduled = ent_B1.get()

    global distance
    global percentage

    if point_a.isalpha():
        point_a.upper()
        point_a = station_dict[point_a]
    elif isinstance(point_a, (float, int)):
        point_a = float(point_a)

    distance = (distance * 0) + (float(point_b) - float(point_a))
    percentage = round((distance / int(scheduled)), 1)

    print("The difference between", point_a, "and", point_b, "is:", distance, "miles")
    print("The percentage between", distance, "and", scheduled, "is:", percentage, "%")

    frm_answer = tk.Frame(master=frm_ansBox, width=100, height=100)
    frm_answer.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    dist_miles = ttk.Label(master=frm_answer, text="Distance", anchor=tk.CENTER)
    dist_miles.pack()
    lbl_difference = ttk.Label(master=frm_answer, text=distance)
    lbl_difference.pack()

    dist_pct = ttk.Label(master=frm_answer, text="Percentage")
    dist_pct.pack()
    lbl_percentage = ttk.Label(master=frm_answer, text=percentage)
    lbl_percentage.pack()


btn_calculate = ttk.Button(master=frm_entry, text="Calculate")
btn_calculate.pack()
btn_calculate.bind("<Button-1>", calculate)

root.bind('<Return>', calculate)
root.bind('<KP_Enter>', calculate)


def reset_click(event):
    for frames in frm_ansBox.winfo_children():
        frames.destroy()


btn_reset = ttk.Button(master=frm_entry, text="Reset")
btn_reset.pack()
btn_reset.bind("<Button-1>", reset_click)

frm_entry.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frm_ansBox.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
root.mainloop()  # This goes at the end of the root code
