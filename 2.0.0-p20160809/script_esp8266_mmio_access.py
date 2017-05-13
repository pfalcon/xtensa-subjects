# Minimal processing required to collect MMIO references.
from xform import *


def is_mmio(addr):
    if 0x3ff00000 <= addr <= 0x3ff10000:
        return True
    if 0x3ff20000 <= addr <= 0x3ff30000:
        return True
    if 0x60000000 <= addr <= 0x60010000:
        return True


def apply(cfg):
    # Various algos below require single-exit CFG
#    cfg_single_exit(cfg)

    cfg_single_entry(cfg)
    remove_unreachable_entries(cfg)

    analyze_reach_defs(cfg)

    #const_propagation(cfg)
    #copy_propagation(cfg)
    #mem_propagation(cfg)
    expr_propagation(cfg)

    collect_mem_refs(cfg, is_mmio, "mmio_refs")
