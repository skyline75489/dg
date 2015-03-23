dg
==

A **d**irectory **g**enerator. Generate your dir like a boss.

Basically a crappy clone of [GKuChan/dir-genearte](https://github.com/GKuChan/dir-generate).

Requirement
-----------

* Python 2.7+ with pathlib installed or Python 3.4+

Usage
-----

```
usage: dg.py [-h] [-d DIR] [-f FILE]

A dir generator

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     set target dir path. defaults to ./
  -f FILE, --file FILE  set config file path. defaults to ./index.json
```

Example
-------

A JSON file like this:

```
[
	{
		"hello":[
			"123.txt",
			{
				"ok":[
					"abc.md",
					"good.js"
				]
			}
		]
	}
]
```

Results in dir structure like this:

```
.
└── hello
    ├── 123.txt
    └── ok
        ├── abc.md
        └── good.js

2 directories, 3 files
```

License
-------

The MIT License