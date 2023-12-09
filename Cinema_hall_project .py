class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

        self._initialize_seats()

        Star_Cinema().entry_hall(self)

    def _initialize_seats(self):
        for row in range(1, self._rows + 1):
            for col in range(1, self._cols + 1):
                seat_id = f"{row}{col}"
                self._seats[seat_id] = None

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)

        show_seats = [[None] * self._cols for _ in range(self._rows)]
        self._seats[show_id] = show_seats

    def book_seats(self, show_id, need_book_seats):
        if show_id not in self._seats:
            print(f"Error: Show with ID {show_id} not found.")
            return

        show_seats = self._seats[show_id]

        for single_seats in need_book_seats:
            row,col = single_seats
            if not (1 <= row <= self._rows) or not (1 <= col <= self._cols):
                print(f"Error: Invalid seat ({row}, {col}).")
                return

            if show_seats[row - 1][col - 1] is not None:
                print(f"Error: Seat ({row}, {col}) is already booked.")
                return

            show_seats[row - 1][col - 1] = "Booked"

        print("Seats booked successfully!")

    def view_show_list(self):
        print("Show List:")
        for show_info in self._show_list:
            print(f"ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print(f"Error: Show with ID {show_id} not found.")
            return

        print(f"Available Seats for Show {show_id}:")
        show_seats = self._seats[show_id]
        for row in range(self._rows):
            for col in range(self._cols):
                if show_seats[row][col] is None:
                    print(f"({row + 1}, {col + 1})")
cs=Hall(5,5,100)
cs1=Hall(7,7,101)
cs.entry_show(10,"Jawann","16:00")
cs1.entry_show(11,"Leo","18:00")
while True:
    print("1. View All show Today")
    print("2. View available seats")
    print("3. Book seats")
    print("4. Exit")
    option=int(input("Enter Option: "))

    if(option == 1):
        cs.view_show_list()
    elif(option == 2):
        showid=int(input("Enter show id:"))
        cs.view_available_seats(showid)

    elif(option == 3):
        show_id=int(input("Enter show id: "))
        numberofseat = int(input("How Many Seat: "))
        seats = []
        while numberofseat > 0:
            row=int(input("Enter row:"))
            col=int(input("Enter col:"))
            seats.append((row,col))
            numberofseat-= 1

        cs.book_seats(show_id,seats)
    elif(option == 4):
        break
    else:
        print("Enter a valid option !!")


        



    