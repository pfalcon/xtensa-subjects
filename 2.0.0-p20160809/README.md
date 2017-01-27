This is a test how well ScratchABit https://github.com/pfalcon/ScratchABit
works, taking ESP8266 BootROM/SDK binary blobs as an example.

As a quick start, you can browse `out.lst` which is complete disassembly
listing at given point of time (updated). Note that it represents more
or less complete ESP8266 address space, with BootROM, iRAM, FlashROM-mapped
code, dRAM, and even memory-mapped IO. You probably want to search e.g.
`40000000` to start looking at the BootROM disassembly.

A better approach is however use ScratchABit for browsing the code and
to continue researching it. For this:

1. Install ScratchABit as described in its README.
2. Install Xtensa CPU plugin as described in the same README.
3. Make ScratchABit.py available via PATH.
4. Run `start.sh` from this repository to load the project.

Some more info available at
https://groups.google.com/forum/#!topic/esp8266-re/SJicbstg5TQ and in
https://groups.google.com/forum/#!forum/esp8266-re in general.
