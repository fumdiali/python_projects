import webbrowser #get webbrowser module
import time #for our delay

def chill():

    total_runs = 2
    run_count = 0

    print("This program ran on ",time.ctime())
    while run_count < total_runs:
      time.sleep(2)
      webbrowser.open("https://youtu.be/-K48_2lmuZU")
      run_count += 1


chill()
