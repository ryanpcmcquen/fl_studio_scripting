# name=Axiom Air Mini
# url=https://github.com/ryanpcmcquen/fl_studio_scripting

#
# Author: Ryan McQuen
#
# Changelog:
# ----------
#
# 0.1.0 - October 15 2020
# Initial release. Add support for transport and ui controls.

# 0.2.0 - October 16 2020
# Add support for mixer controls on knobs 1-8.


import midi
import mixer
import transport
import ui

Buttons = {
    'Stop': 0x10,
    'Start':  0x11,
    'Record': 0x12,
    'Up': 0x13,
    'Down': 0x14,
    'Right': 0x15,
    'Left': 0x16,
    'Center': 0x17,
}

Knobs = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]


def OnMidiMsg(event):
    # If the script does not recognize the event, do nothing.
    # It's then passed onto FL Studio to use.
    event.handled = False

    # Prints the data recieved to the 'Script output' window (for debugging):
    print(event.midiId, event.data1, event.data2)
    # Prints the whole kit and kaboodle:
    print(event)

    # Use midi.MIDI_NOTEON for note events.
    if event.midiId == midi.MIDI_CONTROLCHANGE:
        if event.data2 > 0:
            if event.data1 == Buttons['Stop']:
                transport.stop()
                event.handled = True
            elif event.data1 == Buttons['Start']:
                transport.start()
                event.handled = True
            elif event.data1 == Buttons['Record']:
                transport.record()
                event.handled = True

            elif event.data1 == Buttons['Up']:
                ui.up()
                event.handled = True
            elif event.data1 == Buttons['Down']:
                ui.down()
                event.handled = True
            elif event.data1 == Buttons['Right']:
                ui.right()
                event.handled = True
            elif event.data1 == Buttons['Left']:
                ui.left()
                event.handled = True
            elif event.data1 == Buttons['Center']:
                ui.enter()
                event.handled = True

            elif event.data1 in Knobs:
                mixer.setTrackVolume(
                    event.data1, event.data2 / 100)
                event.handled = True
