import webbrowser
import time

total_breaks = 3
break_count = 0

print ("This program started on " + time.ctime())
while total_breaks < break_count:
    time.sleep(2*60*60)
    webbrowser.open("http://v.youku.com/v_show/id_XMTgwOTEzNjkxNg==.html")
    break_count += 1
