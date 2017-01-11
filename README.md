# fms 
 
######Version: 0.1.0-SNAPSHOT

FMS works as the fontman client application's backend. All the tasks like 
installing fonts, updating font cache are covered by this application. FMS 
uses a SQLite database to store data, you can find it under "data" directory 
under fms home directory.
<br><br>

#####Requirements

Make sure you have `python 3` and `pip` installed. Then install 
following packages.

```bash
pip3 install -r requirements.txt
```

#####Run for the first time

To initialize the application data, if you are running it for the first time,

```bash
python3 fms.py init
```


#####Run fms

```bash
python3 fms.py start
```

Once the flask application started you can start using fontman-gui, 
fontman-client frontend.
