# PassingUnderTankGUIv1.2
# Author: Austin Smith
# Unix timestamp: 1704593553
# Email: ThatSmittyDude@outlook.com
# GitHub.com/ThatSmittydude
# passingunderyellow.com

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def calculate_recommendation():
    full_laps = float(entry_full_laps.get())
    adj_laps = float(entry_adj_laps.get())

    # Calculate the recommended fuel percentage
    adj_percentage = (adj_laps / full_laps) * 100

    # Display the result
    label_result.configure(text=f"Recommended Fuel Percentage: {adj_percentage:.2f}%")

root = customtkinter.CTk()
root.geometry("350x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label_full_laps = customtkinter.CTkLabel(master=frame, text="Laps on Full Tank:")
label_full_laps.pack(pady=5)
entry_full_laps = customtkinter.CTkEntry(master=frame, width=175)
entry_full_laps.pack(pady=10)

label_adj_laps = customtkinter.CTkLabel(master=frame, text="Desired Fuel Run in Laps:")
label_adj_laps.pack(pady=5)
entry_adj_laps = customtkinter.CTkEntry(master=frame, width=175)
entry_adj_laps.pack(pady=5)

button_calculate = customtkinter.CTkButton(master=frame, text="Calculate Recommendation", command=calculate_recommendation)
button_calculate.pack(pady=5)

label_result = customtkinter.CTkLabel(master=frame, text="")
label_result.pack(pady=5)

# Bind the Enter key to the calculate_recommendation function
root.bind('<Return>', lambda event=None: calculate_recommendation())

root.mainloop()

