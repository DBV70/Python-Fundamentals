times = list(map(int, input().split()))

middle = len(times) // 2
left_racer_times = times[:middle]
right_racer_times = times[-1: middle: -1]

left_racer_time = 0
right_racer_time = 0

for time in left_racer_times:
    left_racer_time += time
    if time == 0:
        left_racer_time *= 0.8

for time in right_racer_times:
    right_racer_time += time
    if time == 0:
        right_racer_time *= 0.8

if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
