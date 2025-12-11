time_24 = input("Enter time in 24-hour format (HH:MM): ")

hour, minute = map(int, time_24.split(":"))

if hour == 0:
    print(f"12:{minute:02d} AM")
elif hour < 12:
    print(f"{hour}:{minute:02d} AM")
elif hour == 12:
    print(f"12:{minute:02d} PM")
else:
    print(f"{hour - 12}:{minute:02d} PM")
