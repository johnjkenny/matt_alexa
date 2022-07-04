# matt_alexa

the loop listener runs in a separate process as requested:<br>
```bash
➜  ~ ps -aux | grep -i ./app.py
jkenny    135563  0.4  0.0  30096 11228 pts/14   S+   09:30   0:00 python3 ./app.py
jkenny    135564  0.0  0.0  30096  7692 pts/14   S+   09:30   0:00 python3 ./app.py
```

Ouput of app.py<br>
```bash
./app.py
starting module with pid: 135563
start loop listener
loop listener started with pid: 135564
Searching for wakeup word. Count: 1
Searching for wakeup word. Count: 2
Searching for wakeup word. Count: 3
Searching for wakeup word. Count: 4
Searching for wakeup word. Count: 5
Searching for wakeup word. Count: 6
Searching for wakeup word. Count: 7
Searching for wakeup word. Count: 8
Searching for wakeup word. Count: 9
Searching for wakeup word. Count: 10
Searching for wakeup word. Count: 11
Searching for wakeup word. Count: 12
Searching for wakeup word. Count: 13
stopping loop listener
ending module
```
