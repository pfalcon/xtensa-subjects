def make_data_arr(aspace, start, end, sz):
    addr = start
    while addr < end:
        aspace.set_flags(addr, sz, aspace.DATA, aspace.DATA_CONT)
        addr += sz


FUNCS_BLACKLIST = {
    # Parse issues
    "__addsf3",
    "__subdf3",
    "__divsi3",
    "__udivsi3",
    "__floatunsisf",
    "__floatsidf",
    # multiple entries issues
    "conv_str_decimal",
    "ets_vprintf",
    "UartDwnLdProc",
    "rom_set_channel_freq",
    "rom_chip_50_set_channel",
    # too complex, trips propagator
    "MD5Transform",
    "SHA1Transform",
}


def dump_funcs(APP):
    import sys
    import os
    from scratchabit import actions
    try:
        os.makedirs("funcs")
    except OSError:
        pass
    for addr, func in APP.aspace.iter_funcs():
        funcname = APP.aspace.get_label(addr)
        print("%08x %s" % (addr, funcname))
        # Dump only BootROM funcs so far
        if 0x40000000 <= addr < 0x40010000 and funcname not in FUNCS_BLACKLIST:
            with open("funcs/%08x-%s.lst" % (addr, funcname), "w") as fobj:
                actions.write_func_stream(APP, func, fobj, comments=False)

    sys.exit(1)


def main(APP):
    APP.aspace.memcpy(0x3fffc000, 0x4000e388, 0x857)
    APP.aspace.memcpy(0x3fffc860, 0x4000ebe8, 0x3fffdaac - 0x3fffc860)
    APP.aspace.memcpy(0x3fffdaac, 0x4000fe34, 4)

    #make_data_arr(APP.aspace, 0x3fffccf0, 0x3fffccf0 + 0x400, 4)
    #make_data_arr(APP.aspace, 0x3fffd100, 0x3fffd100 + 0x400, 4)
    #make_data_arr(APP.aspace, 0x3fffd500, 0x3fffd500 + 0x100, 1)
    #make_data_arr(APP.aspace, 0x3fffd600, 0x3fffd600 + 0x40, 1)
    #make_data_arr(APP.aspace, 0x4000e388, 0x4000fe38, 1)

    # Uncomment to dump funcs on startup and exit
    #dump_funcs(APP)
