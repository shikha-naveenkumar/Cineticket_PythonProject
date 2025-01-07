# Ticket Booking System.
def print_tickets():
    """Print the tickets of the user."""
    for user_name, seats in user_tickets.items():
        print(f"\nYou, {user_name.title()}, have chosen {len(seats)} seat(s).")
        for seat in seats:
            print(f"\tSeat number: {seat}")


# Empty dictionary to store info later on.
user_tickets = {}

# List of seats the user can choose from.
available_seats = ['1a', '2a', '19b', '20d', '21e', '13g', '15f', '14f', '13a', '12g' ]


# All prompts.
start_prompt = "\nWould you like to start booking your ticket? (yes/no) "
wanted_seats_prompt = "\nHow many seats are you booking today?"
wanted_seats_prompt += "\nEnter the number: "
name_prompt = "What is your name? "
seat_prompt = "\nPlease enter the number of the seat you would like to book: "
go_again_prompt = "Would you like to let someone else book their tickets? (yes/no) "


print("Welcome To The Seat Booking Portal!")

# Ask the user if he would like to start booking their tickets.
start = input(start_prompt)
if start.lower() == 'yes':
    # Runs until it reaches a break statement.
    while True:
        # Empty list to store the seat(s) the user has chosen.
        seats = []

        # Find out how many times to run the while loop.
        wanted_seats = input(wanted_seats_prompt)
        # Convert the string representation of the number to an integer representation.
        wanted_seats = int(wanted_seats)
        # If the user has asked for more seats than the number of seats
        # available execute this block.
        if wanted_seats > len(available_seats):
            print(f"\n--I'm sorry, we only have {len(available_seats)} "
                "seats available--")
            print("--Please try again--")
            continue

        # Ask for the users name.
        user_name = input(name_prompt)

        # Run until the user has chosen the requested number of seats.
        while True:

            # Show the user the available seats.
            print("\nHere are the available seats:")
            for seat in available_seats:
                print(seat)

            # Ask the user for their chosen seat number.
            seat = input(seat_prompt)

            # If the user has entered a seat that is in the 'available_seats' 
            # list; remove it from the 'available_seats' list.
            if seat in available_seats:
                available_seats.remove(seat)
            # The user has entered a seat that is not in the 'avialbe_seats' list.
            # Ask for their seat again.
            else:
                print("\n--I'm sorry you have chosen an invalid seat--"
                    "\n-Please try again-")
                continue

            # Add the chosen seat to the 'seats' list
            seats.append(seat)

            # If the user has said that they are going to book more than one seat
            # go through this seat booking 'while' loop again.
            if wanted_seats > 1:
                print("\nYou can now choose another seat.")
                # The loop will run a limited number of times.
                # It will only 'continue' when there is more than one 'wanted_seat'.
                wanted_seats-=1
                continue
            else:
                break

        # Add the 'user_name' variable and 'seats' list to the 'user_tickets' dictionary.
        user_tickets[user_name] = seats

        #If their are any available seats left ask the user if he
        # wants to let another person book their tickets. 
        if available_seats:
            go_again = input(go_again_prompt)
            if go_again == 'no':
                break
        else:
            break

    print_tickets()
    print("\nWe will now redirect you to the payment portal."
        "\nThank You for choosing us.")

else:
    print("You can always come by later!")
