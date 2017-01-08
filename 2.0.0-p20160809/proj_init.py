def main(APP):
    APP.aspace.memcpy(0x3fffc000, 0x4000e388, 0x857)
    APP.aspace.memcpy(0x3fffc860, 0x4000ebe8, 0x3fffdaac - 0x3fffc860)
    APP.aspace.memcpy(0x3fffdaac, 0x4000fe34, 4)
