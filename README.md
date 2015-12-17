## Update on Dec-2015: http://agar.io now supports party games officially! No need for hacking around anymore!

# agar.io Friends connector
A simple python script helps you connect you and your friends to connect to the same agar.io server.

### !!! WARNING: This script no longer works :( Please fork and make a pull request if you have a better solution!

## How does it work?
When you open [http://agar.io](http://agar.io) in your browser, it first make a ```POST``` request to ```http://m.agar.io``` and which then it returns a address of the server (agar.io room) and a password like session key that requires to authenticate the session when entering the room.

This script will constantly make request to ```m.agar.io``` until it matches the target address and generates a simple one line JavaScript code that you can use to connect to the room in your browser. Simple!

## How do I use this script?
You'd need to have [Python](http://python.org) installed on a linux or mac machine (Windows currently not available, development in progress! Stay tuned!).

Once installed, download the script and run with following command:

``` sh
python find.py
```

This will launch the script and from this point, you can follow the instructions in the script to connect yourself to a targeted agar.io server.

## Contribution
This script is simple but obviously not a clever approach to get a credential for connecting to the server.

If you have any suggestions, fork, make a pull request or post an issue on this repo!

Feel free to comment on the issue page too.

Hope you find this script useful! Happy agar-ing :) Stay safe.
