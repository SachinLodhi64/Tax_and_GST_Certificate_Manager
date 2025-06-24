import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import shutil
import pandas as pd  # Added pandas for Excel saving

client_data = {}
gst_data = {}

assessment_years = [f"{year}-{str(year+1)[-2:]}" for year in range(2021, 2050)]

# ---------- Utility Functions ----------
def open_file(title, filetype=[("PDF files", "*.pdf"), ("All files", "*.*")]):
    return filedialog.askopenfilename(title=title, filetypes=filetype)

def download_file(file_path):
    dest = filedialog.asksaveasfilename(initialfile=os.path.basename(file_path), defaultextension=".pdf")
    if dest:
        shutil.copy(file_path, dest)
        messagebox.showinfo("Downloaded", f"File saved to: {dest}")

def print_file(file_path):
    try:
        os.startfile(file_path, "print")
        messagebox.showinfo("Printed", "File sent to printer")
    except Exception as e:
        messagebox.showerror("Error", f"Could not print file: {e}")

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# ---------- Login Page ----------
def login_page():
    clear_window()
    tk.Label(root, text="Login", font=("Arial", 18)).pack(pady=20)

    tk.Label(root, text="Enter Name").pack()
    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=5)

    tk.Label(root, text="Enter Password").pack()
    pass_entry = tk.Entry(root, show="*", width=30)
    pass_entry.pack(pady=5)

    def validate_login():
        name = name_entry.get()
        password = pass_entry.get()
        if name == "RAJIV WASON" and password == "Rajiv@12345":
            main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid Credentials")

    tk.Button(root, text="Login", command=validate_login, width=20).pack(pady=15)

# ---------- Main Menu ----------
def main_menu():
    clear_window()
    tk.Label(root, text="Choose an Option", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="1. Fill ITR Form", command=itr_form, width=30).pack(pady=5)
    tk.Button(root, text="2. Fill GST Form", command=gst_form, width=30).pack(pady=5)
    tk.Button(root, text="3. Download ITR and Computation", command=download_itr, width=30).pack(pady=5)
    tk.Button(root, text="4. Download GST Certificate", command=download_gst, width=30).pack(pady=5)

# ---------- ITR Form ----------
def itr_form():
    clear_window()
    entries = {}
    labels = ["Client Name", "PAN Number", "Date of Birth", "Contact Number",
              "Father's Name", "Assessment Year", "Address"]

    for idx, label in enumerate(labels):
        tk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(root, width=40)
        entry.grid(row=idx, column=1, padx=10, pady=5)
        entries[label] = entry

    assessment_dropdown = ttk.Combobox(root, values=assessment_years, width=37)
    assessment_dropdown.grid(row=5, column=1, padx=10, pady=5)
    entries["Assessment Year"] = assessment_dropdown

    itr_path = tk.StringVar()
    computation_path = tk.StringVar()

    def upload_itr():
        file = open_file("Upload ITR File")
        if file:
            itr_path.set(file)
            messagebox.showinfo("Uploaded", "ITR File Uploaded")

    def upload_computation():
        file = open_file("Upload Computation File")
        if file:
            computation_path.set(file)
            messagebox.showinfo("Uploaded", "Computation File Uploaded")

    tk.Button(root, text="Upload ITR File", command=upload_itr).grid(row=7, column=0, columnspan=2, pady=5)
    tk.Button(root, text="Upload Computation File", command=upload_computation).grid(row=8, column=0, columnspan=2, pady=5)

    def search():
        pan = entries["PAN Number"].get()
        ay = entries["Assessment Year"].get()
        key = (pan, ay)
        if key in client_data:
            record = client_data[key]
            for k, v in record["data"].items():
                if k in entries:
                    entries[k].delete(0, tk.END)
                    entries[k].insert(0, v)
            itr_path.set(record["ITR"])
            computation_path.set(record["Computation"])
            messagebox.showinfo("Found", "Details loaded for this PAN and AY")
        else:
            messagebox.showinfo("Not Found", "Kindly fill the details")

    def add_details():
        pan = entries["PAN Number"].get()
        ay = entries["Assessment Year"].get()
        if pan and ay and itr_path.get() and computation_path.get():
            data_row = {k: v.get() for k, v in entries.items()}
            data_row["ITR File Path"] = itr_path.get()
            data_row["Computation File Path"] = computation_path.get()
            file_path = "ITR_Data.xlsx"
            try:
                df_existing = pd.read_excel(file_path)
                df = pd.concat([df_existing, pd.DataFrame([data_row])], ignore_index=True)
            except FileNotFoundError:
                df = pd.DataFrame([data_row])
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Success", f"ITR Details Saved to {file_path}")
            main_menu()
        else:
            messagebox.showerror("Missing Data", "Please fill all fields and upload both files")

    tk.Button(root, text="Search", command=search).grid(row=9, column=0, pady=15)
    tk.Button(root, text="Add Details", command=add_details).grid(row=9, column=1, pady=15)
    tk.Button(root, text="⬅ Back", command=main_menu).grid(row=10, column=0, columnspan=2, pady=10)

# ---------- GST Form ----------
def gst_form():
    clear_window()
    entries = {}

    labels = ["Firm Name", "Active GST Number", "Proprietor Name", "Contact Number",
              "Inactive GST Number (if any)", "Address"]

    for idx, label in enumerate(labels):
        tk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(root, width=40)
        entry.grid(row=idx, column=1, padx=10, pady=5)
        entries[label] = entry

    cert_path = tk.StringVar()

    def upload_cert():
        file = open_file("Upload GST Certificate", [("PDF files", "*.pdf")])
        if file:
            cert_path.set(file)
            messagebox.showinfo("Uploaded", "Certificate Uploaded")

    def save():
        gst = entries["Active GST Number"].get()
        if gst and cert_path.get():
            data_row = {k: v.get() for k, v in entries.items()}
            data_row["Certificate File Path"] = cert_path.get()
            file_path = "GST_Data.xlsx"
            try:
                df_existing = pd.read_excel(file_path)
                df = pd.concat([df_existing, pd.DataFrame([data_row])], ignore_index=True)
            except FileNotFoundError:
                df = pd.DataFrame([data_row])
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Saved", f"GST Certificate Saved to {file_path}")
            main_menu()
        else:
            messagebox.showerror("Missing", "Please fill fields and upload certificate")

    tk.Button(root, text="Upload Certificate (PDF)", command=upload_cert).grid(row=6, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Save GST Details", command=save).grid(row=7, column=0, columnspan=2, pady=10)
    tk.Button(root, text="⬅ Back", command=main_menu).grid(row=8, column=0, columnspan=2, pady=10)

# ---------- Download ITR ----------
def download_itr():
    clear_window()
    tk.Label(root, text="Enter PAN Number").grid(row=0, column=0, padx=10, pady=5)
    pan_entry = tk.Entry(root, width=40)
    pan_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Enter Assessment Year").grid(row=1, column=0, padx=10, pady=5)
    ay_entry = ttk.Combobox(root, values=assessment_years, width=37)
    ay_entry.grid(row=1, column=1, padx=10, pady=5)

    def show_files():
        pan = pan_entry.get()
        ay = ay_entry.get()
        key = (pan, ay)
        if key in client_data:
            info = client_data[key]
            itr = info["ITR"]
            comp = info["Computation"]

            tk.Label(root, text=f"ITR File: {itr}").grid(row=3, column=0, columnspan=2, pady=5)
            tk.Button(root, text="Download ITR", command=lambda: download_file(itr)).grid(row=4, column=0, pady=5)
            tk.Button(root, text="Print ITR", command=lambda: print_file(itr)).grid(row=4, column=1, pady=5)

            tk.Label(root, text=f"Computation File: {comp}").grid(row=5, column=0, columnspan=2, pady=5)
            tk.Button(root, text="Download Computation", command=lambda: download_file(comp)).grid(row=6, column=0, pady=5)
            tk.Button(root, text="Print Computation", command=lambda: print_file(comp)).grid(row=6, column=1, pady=5)
        else:
            messagebox.showerror("Not Found", "Details not found for the given PAN and Assessment Year.")

    tk.Button(root, text="Show Files", command=show_files).grid(row=2, columnspan=2, pady=10)
    tk.Button(root, text="⬅ Back", command=main_menu).grid(row=7, columnspan=2, pady=10)

# ---------- Download GST ----------
def download_gst():
    clear_window()
    tk.Label(root, text="Enter GST Number").grid(row=0, column=0, padx=10, pady=5)
    gst_entry = tk.Entry(root, width=40)
    gst_entry.grid(row=0, column=1, padx=10, pady=5)

    def show_cert():
        gst = gst_entry.get()
        if gst in gst_data:
            cert = gst_data[gst]["Certificate"]
            tk.Label(root, text=f"Certificate: {cert}").grid(row=2, column=0, columnspan=2, pady=5)
            tk.Button(root, text="Download Certificate", command=lambda: download_file(cert)).grid(row=3, column=0, pady=5)
            tk.Button(root, text="Print Certificate", command=lambda: print_file(cert)).grid(row=3, column=1, pady=5)
        else:
            messagebox.showerror("Inactive", "Inactive GST number")

    tk.Button(root, text="Check & Download", command=show_cert).grid(row=1, columnspan=2, pady=10)
    tk.Button(root, text="⬅ Back", command=main_menu).grid(row=4, columnspan=2, pady=10)

# ---------- Run GUI ----------
root = tk.Tk()
root.title("Tax & Certificate Manager")
root.geometry("550x600")
login_page()
root.mainloop()
