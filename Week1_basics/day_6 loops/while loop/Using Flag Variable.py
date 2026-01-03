running = True

while running:
    choice = input("Enter q to quit: ")
    if choice.lower() == 'q':
        running = False
    else:
        print("Loop running...")
print("Loop ended.")
