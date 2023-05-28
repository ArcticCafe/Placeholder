#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from additional_urwid_widgets import IndicativeListBox    # installed via pip
import urwid                                              # installed via pip


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

if __name__ == "__main__":
    
    with open("process_list", "r") as process_list:
        process = process_list.read().splitlines()

    # Color schemes that specify the appearance off focus and on focus.
    PALETTE = [("reveal_focus", "black", "light cyan", "standout")]
    
    # The list box is filled with buttons.
    body = [urwid.Button(letter) for letter in process]
    
    # Wrap the list items into an 'urwid.AttrMap', so that they have an other appearance when focused.
    # Instead of an simple list-like object you can/should create a 'urwid.ListWalker'.
    attr_body = [urwid.AttrMap(entry, None, "reveal_focus") for entry in body]
    
    ilb = IndicativeListBox(attr_body)
    
    loop = urwid.MainLoop(ilb,
                        PALETTE,
                        unhandled_input=exit_on_q)
    loop.run()
