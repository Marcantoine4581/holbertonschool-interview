# Star Wars API

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. [Rules of Standard](https://intranet.hbtn.io/rltoken/a_-JUY7U-raFrkWWqUYnTg "Rules of Standard") + [semicolons on top](https://intranet.hbtn.io/rltoken/fVMR90inNe58a0NEksB4gQ "semicolons on top"). Also as reference: [AirBnB style](https://intranet.hbtn.io/rltoken/zaOEoMbNJXHqlH5YqNx4Kg "AirBnB style")
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

## More Info

### Install Node 10

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

[Documentation](https://intranet.hbtn.io/rltoken/fVMR90inNe58a0NEksB4gQ "Documentation")

```
$ sudo npm install semistandard --global
```

### Install `request` module and use it

[Documentation](https://intranet.hbtn.io/rltoken/w9hNGjGRL6LR-FK9aE-Eqg "Documentation")

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks

### 0. Star Wars Characters

mandatory

Write a script that prints all characters of a Star Wars movie:

- The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”
- Display one character name per line **in the same order as the “characters” list in the `/films/` endpoint**
- You must use the [Star wars API](https://intranet.hbtn.io/rltoken/JC6IIW1wGzUGbEWQdaPR9w "Star wars API")
- You must use the `request` module

```
alexa@ubuntu:~/$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/$ 
```