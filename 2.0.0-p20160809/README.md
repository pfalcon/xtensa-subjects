This is a test how well [ScratchABit](https://github.com/pfalcon/ScratchABit)
works, taking the ESP8266 BootROM/SDK binary blobs as an example.

As a quick start, you can browse `out.lst` which is a complete disassembly
listing at given point of time (updated). Note that it represents more
or less the complete ESP8266 address space, with BootROM, iRAM,
FlashROM-mapped code, dRAM, and even memory-mapped IO. You probably
want to search e.g. `40000000` address to start looking at the BootROM
disassembly.

A better approach is however to use ScratchABit for browsing the code and
to continue researching it. For this:

1. Install ScratchABit as described in its README.
2. Install Xtensa CPU plugin as described in the same README.
3. Make ScratchABit.py available via PATH.
4. Run `start.sh` from this repository to load the project.

More info available at
[https://groups.google.com/forum/#!topic/esp8266-re/SJicbstg5TQ](https://groups.google.com/forum/#!topic/esp8266-re/SJicbstg5TQ)
and in
[https://groups.google.com/forum/#!forum/esp8266-re](https://groups.google.com/forum/#!forum/esp8266-re)
in general.

There is now support for producing a call graph of BootROM functions.
For this:

1. Install [ScratchABlock](https://github.com/pfalcon/ScratchABlock),
   a sister project to ScratchABit, a program transformation/decompilation
   framework. Add it to PATH.
2. Uncomment the corresponding line in `start.sh`, run it once, and
   comment the line again. This will produce function listings in
   `funcs/` directory.
3. Run `callgraph.sh`.
4. The generated callgraph is in `callgraph.dot` and `callgraph.svg`
   files. You can browse the latter using a web browser. But it's
   recommended to install `xdot` tool and use it to browse
   `callgraph.dot` directly. `xdot` is available in the popular Linux
   distros, but you may get more features (e.g. search) if you install
   the latest version from the repository:
   https://github.com/jrfonseca/xdot.py
