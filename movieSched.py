
holidayMovies = {"The Grinch": "11:00am",
                 "Rudolph": "1:00pm",
                 "Frosty the Snowman": "3:00pm",
                 "Christmas Vacation": "5:00pm",
                 "Elf": "8:00pm",
                 "Die Hard": "11:00pm"}

print("We're currently showing the following movies: ")
for key in holidayMovies:
    print(key)

movie = input("\nWhat movie would you like the showtime for?\n")

showtime = holidayMovies.get(movie) # Give key value to return time

if showtime == None:
    print("\nRequested movie isn't playing\n")
else:
    print(f"\n{movie} is playing at {showtime}\n")