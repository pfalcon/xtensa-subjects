def make_data_arr(aspace, start, end, sz):
    addr = start
    while addr < end:
        aspace.set_flags(addr, sz, aspace.DATA, aspace.DATA_CONT)
        addr += sz


def main(APP):
    APP.aspace.memcpy(0x3fffc000, 0x4000e388, 0x857)
    APP.aspace.memcpy(0x3fffc860, 0x4000ebe8, 0x3fffdaac - 0x3fffc860)
    APP.aspace.memcpy(0x3fffdaac, 0x4000fe34, 4)

    #make_data_arr(APP.aspace, 0x3fffccf0, 0x3fffccf0 + 0x400, 4)
    #make_data_arr(APP.aspace, 0x3fffd100, 0x3fffd100 + 0x400, 4)
    #make_data_arr(APP.aspace, 0x3fffd500, 0x3fffd500 + 0x100, 1)
    #make_data_arr(APP.aspace, 0x3fffd600, 0x3fffd600 + 0x40, 1)
    #make_data_arr(APP.aspace, 0x4000e388, 0x4000fe38, 1)
