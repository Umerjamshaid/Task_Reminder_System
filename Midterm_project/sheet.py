import requests
import smtplib
from datetime import datetime
import tkinter as tk 
from tkinter import messagebox

# Sheety API URL
SHEETY_API_URL = 'https://api.sheety.co/347a860d7c6079a6e6250616420962dc/taskReminderSystemExpanded/taskReminderSystemExpandedCsv'

# Function to fetch tasks from Google Sheet
def fetch_tasks():
    response = requests.get(SHEETY_API_URL)
    if response.status_code == 200:
        return response.json().get('taskReminderSystemExpanded', [])
    else:
        print("Failed to fetch tasks:", response.text)
        return []

# Function to send email reminder
def send_email(to_address, task, due_date):
    from_address = "umerjamshaid481@gmail.com"
    password = "axrb pkxc kpqf liit"
    subject = f"Task Reminder: {task}"
    body = f"Dear User,\n\nThis is a reminder for your task: {task}\nDue Date: {due_date}\n\nBest Regards,\nyour boss over here"

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address, message)
        print(f"Reminder email sent to {to_address} for task: {task}")

# Function to fetch tasks and send reminders
def run_task_reminders():
    tasks = fetch_tasks()
    today = datetime.today().strftime('%Y-%m-%d')
    
    tasks_due_today = [task for task in tasks if task['DueDate'] == today]

    if tasks_due_today:
        for task in tasks_due_today:
            send_email(task['Email'], task['Task'], task['DueDate'])
        messagebox.showinfo("Task Reminder", "Reminders sent for today's tasks!")
    else:
        messagebox.showinfo("Task Reminder", "No tasks due today.")

# Create the GUI
root = tk.Tk()
root.geometry("400x300")
root.title("Task Reminder System")
def create_gui():

    guilabel = tk.Label(root, text="Task Reminder System", font=("Arial", 16))
    guilabel.pack()

    # Create a button
    button = tk.Button(root, text="Run Task Reminders", command=run_task_reminders, font=("Arial", 14), fg="gray", bg="black")
    button.pack()

    root.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
