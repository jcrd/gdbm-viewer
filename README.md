# gdbm-viewer

gdbm-viewer displays the keys and values in a [gdbm][gdbm] database and reflects
changes live.

[<img src="https://github.com/jcrd/gdbm-viewer/blob/assets/screenshot.png" width="300"/>][scrn]

[gdbm]: https://www.gnu.org.ua/software/gdbm/
[scrn]: https://github.com/jcrd/gdbm-viewer/blob/assets/screenshot.png

## Usage

```txt
usage: gdbm-viewer [-h] [--max [MAX]] path

positional arguments:
  path         Path to gdbm file

options:
  -h, --help   show this help message and exit
  --max [MAX]  Maximum lines per column
```

Right-clicking an entry will delete it from the database.

## License

This project is licensed under the MIT License (see [LICENSE](LICENSE)).
