# name=Axiom Air Mini
# url=https://github.com/ryanpcmcquen/fl_studio_scripting


import midi
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
    'Center': 0x17
}


def OnMidiMsg(event):
    # If the script does not recognize the event, do nothing.
    # It's then passed onto FL Studio to use.
    event.handled = False

    # Prints the data recieved to the 'Script output' window (for debugging).
    # print(event.midiId, event.data1, event.data2)

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
