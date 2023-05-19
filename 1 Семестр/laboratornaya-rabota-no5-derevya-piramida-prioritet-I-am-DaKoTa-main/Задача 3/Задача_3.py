def simulation(arrival_time, process_time):

    while len(finish_time) > 0 and finish_time[0] <= arrival_time:
        finish_time.pop(0)
        
    if len(finish_time) < buffer_size:
        if len(finish_time) == 0:
            finish_time.append(arrival_time + process_time)
            with open('output.txt', 'a') as f:
                f.write(str(arrival_time) + '\n')
        else:
            arrival_time_new = arrival_time
            if finish_time[-1] > arrival_time_new:
                arrival_time_new = finish_time[-1]
            elif finish_time[-1] == arrival_time_new:
                arrival_time_new = finish_time[-1] + 1
            finish_time.append(arrival_time_new + process_time)
            with open('output.txt', 'a') as f:
                f.write(str(arrival_time_new)+'\n')
    else:
        with open('output.txt', 'a') as f:
            f.write("-1\n")


with open('input.txt', 'r') as f:
    buffer_size, count = list(map(int, f.readline().strip().split()))
    finish_time = []
    if (1 <= buffer_size <= 10 ** 5) and (1 <= count <= 10 ** 5):
        for _ in range(count):
            request = [int(x) for x in f.readline().split(' ')]
            if (0 <= request[0] <= 10**6) and (0 <= request[1] <= 10**3):
                simulation(request[0], request[1])
            else:
                with open('output.txt', 'w') as f:
                    f.write("ERROR")
    else:
        with open('output.txt', 'w') as f:
            f.write("")
