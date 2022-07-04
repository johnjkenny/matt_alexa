# matt_alexa

the loop listener runs in a separate process as requested:<br>
```bash
➜  ~ ps -aux | grep -i ./app.py
jkenny    135563  0.4  0.0  30096 11228 pts/14   S+   09:30   0:00 python3 ./app.py
jkenny    135564  0.0  0.0  30096  7692 pts/14   S+   09:30   0:00 python3 ./app.py
```
