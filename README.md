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
python3 fms.py run
```

Once the flask application started you can start using fontman-gui, 
fontman-client frontend.
<br><br>

#####Building the FMS binary
We use [PyInstaller](http://www.pyinstaller.org/) to build the FMS binary for all platforms.
To install PyInstaller simply do,
```bash
pip3 install pyinstaller
```

Now build the FMS binary by,
```bash
pyinstaller --onefile fms.py
```
If you don't want to compromize Flask terminal output simply do,
```bash
pyinstaller --onefile --noconsole fms.py
```
Once the PyInstaller is done, FMS binary can be found in the **dist** 
directory. Named as **fms** on Linux, **fms.exe** on Windows and **fms.dmg** 
on Mac.
