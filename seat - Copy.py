import tkinter as tk

class AuditoriumReservationSystem:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Auditorium Reservation")

        # Auditorium layout (number of rows and columns)
        self.rows = 5
        self.columns = 6

        # Create a Frame to hold seat buttons
        self.seating_frame = tk.Frame(parent)
        self.seating_frame.pack()

        # Create and display seat buttons in a grid
        self.create_seats()

    def create_seats(self):
        self.seat_buttons = []

        for row in range(self.rows):
            seat_row = []
            for col in range(self.columns):
                seat_button = tk.Button(self.seating_frame, text=f"Seat {row+1}-{col+1}", width=8, height=2, command=lambda r=row, c=col: self.reserve_seat(r, c))
                seat_button.grid(row=row, column=col, padx=5, pady=5)
                seat_row.append(seat_button)
            self.seat_buttons.append(seat_row)

    def reserve_seat(self, row, col):
        seat_button = self.seat_buttons[row][col]
        if seat_button['state'] == 'normal':
            seat_button.configure(bg='lightgreen', state='disabled')
            print(f"Reserved Seat {row+1}-{col+1}")
           
        else:
            print(f"Seat {row+1}-{col+1} is already reserved.")

if __name__ == "__main__":
    parent = tk.Tk()
    app = AuditoriumReservationSystem(parent)
    parent.mainloop()
