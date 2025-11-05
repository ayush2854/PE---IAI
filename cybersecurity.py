import tkinter as tk
from tkinter import messagebox

def get_cybersecurity_advice_gui():
    def evaluate():
        advice = []

        if password_var.get() == "yes":
            advice.append("Avoid reusing passwords. Use a password manager to generate and store strong, unique passwords.")
        if updates_var.get() == "no":
            advice.append("Enable automatic updates to patch security vulnerabilities promptly.")
        if wifi_var.get() == "yes":
            advice.append("Use a VPN when accessing sensitive data on public networks.")
        if two_factor_var.get() == "no":
            advice.append("Enable 2FA to add an extra layer of security to your accounts.")
        if phishing_var.get() == "no":
            advice.append("Be cautious of phishing emails. Always verify the sender and avoid clicking suspicious links.")

        if advice:
            result = "🔐 Cybersecurity Advice:\n\n" + "\n".join(f"- {item}" for item in advice)
        else:
            result = "✅ Great job! Your cybersecurity habits are solid. Keep it up!"

        messagebox.showinfo("Cybersecurity Advice", result)

    # GUI setup
    root = tk.Tk()
    root.title("Cybersecurity Advice Expert System")
    root.geometry("500x400")

    tk.Label(root, text="Answer the following questions:", font=("Arial", 14)).pack(pady=10)

    # Questions
    def create_question(text, var):
        frame = tk.Frame(root)
        frame.pack(anchor="w", padx=20, pady=5)
        tk.Label(frame, text=text, font=("Arial", 11)).pack(side="left")
        tk.Radiobutton(frame, text="Yes", variable=var, value="yes").pack(side="left", padx=5)
        tk.Radiobutton(frame, text="No", variable=var, value="no").pack(side="left", padx=5)

    password_var = tk.StringVar(value="no")
    updates_var = tk.StringVar(value="yes")
    wifi_var = tk.StringVar(value="no")
    two_factor_var = tk.StringVar(value="yes")
    phishing_var = tk.StringVar(value="yes")

    create_question("Do you reuse the same password across multiple accounts?", password_var)
    create_question("Do you regularly update your operating system and software?", updates_var)
    create_question("Do you access sensitive accounts over public Wi-Fi?", wifi_var)
    create_question("Do you use two-factor authentication (2FA) for your accounts?", two_factor_var)
    create_question("Do you verify email sender addresses before clicking links?", phishing_var)

    tk.Button(root, text="Get Advice", command=evaluate, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=20)

    root.mainloop()

get_cybersecurity_advice_gui()