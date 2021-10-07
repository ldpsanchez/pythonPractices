from datetime import datetime, timedelta, time

start_time = datetime.strptime("2021/1/1 00:00:00", "%Y/%m/%d %H:%M:%S")
end_time = datetime.strptime("2021/1/2 00:00:00" ,"%Y/%m/%d %H:%M:%S")
add_time = timedelta(hours=1)

while start_time <= end_time:
    example_time_1 = start_time.time()

    if example_time_1 >= time(6) and example_time_1 <= time(12) :
        print(example_time_1)
        # print(type(example_time_1))
        # print(example_time_1 == time(hour=6))
        print(example_time_1 > time(hour=10))

    start_time += add_time
