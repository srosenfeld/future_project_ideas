import time

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()

print('Started')

startTime = time.time()

lastTime = startTime

lap = 1


try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap %s: %s (Total: %s)' % (lap, lapTime, totalTime))
        lap += 1
        lastTime = time.time()

except KeyboardInterrupt:
    print('\nDone.')

