user_time: int(input("Введите время в секундах: "))
hours = user_time // 3600
minutes = user_time // 60
minutes_int = user_time % 60
seconds = user_time - minutes_int
print(f"{hours:02}:{minutes:02}:{seconds:02}")


