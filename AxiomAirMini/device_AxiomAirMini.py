# name=Axiom Air Mini
# url=https://github.com/ryanpcmcquen/fl_studio_scripting

#
# Author: Ryan McQuen
#
# Changelog:
# ----------
# 0.1.0 - October 15 2020
# Initial release. Add support for transport and ui controls.
#
# 0.2.0 - October 16 2020
# Add support for mixer controls on knobs 1-8.
#
# 0.2.1 - October 16 2020
# Comment out debug output.
#
# 0.3.0 - October 19 2020
# Map the HyperControl switcher to focusing
# the channel rack. This allows easy track
# switching with the ui arrows.
#
# 0.3.1 - October 21 2020
# Add a function for printing all
# useful object properties (for
# use in debugging scripts).
#
# IN DEVELOPMENT:
# 0.4.0 - October 23 2020
# Allow drum pads to select channels
# if Hyper key is engaged.
#

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
    'Hyper': 0x3A,
}

Knobs = [
    0x01,
    0x02,
    0x03,
    0x04,
    0x05,
    0x06,
    0x07,
    0x08,
]

Pads = {
    1: 36,
    2: 37,
    3: 38,
    4: 39,
    5: 40,
    6: 41,
    7: 42,
    8: 43,
}


def OnInit():
    # global keyboard_state_file
    # keyboard_state_file = open(".__axiom_state__", "x")
    # keyboard_state_file.write("0")
    # keyboard_state_file.close()
    global hyper_engaged
    hyper_engaged = False

# Known event properties:
# 'controlNum', 'controlVal', 'data1',
# 'data2', 'handled', 'inEv',
# 'isIncrement', 'midiChan', 'midiChanEx',
# 'midiId', 'note', 'outEv',
# 'pitchBend', 'pmeFlags', 'port',
# 'pressure', 'progNum', 'res',
# 'senderId', 'status', 'sysex',
# 'timestamp', 'velocity', 'write'


def debug_obj(obj):
    # Snippet to  debug all available
    # properties and their
    # values on objects:
    for prop in dir(obj):
        # Filter out all 'private' methods:
        if prop[:2] != '__':
            print(prop + ': ')
            print(getattr(obj, prop))


def OnMidiIn(event):
    # debug_obj(event)
    event.handled = False
    if event.data1 == Buttons['Hyper']:
        debug_obj(device)
        global hyper_engaged
        hyper_engaged = True
        # global keyboard_state_file
        # keyboard_state_file.write("1")
        # keyboard_state_file.close()
        print('OnMidiIn:')
        print(hyper_engaged)


def OnMidiMsg(event):
    # print("OnMidiMsg event:")
    # debug_obj(event)

    # If the script does not recognize the event, do nothing.
    # It's then passed onto FL Studio to use.
    event.handled = False

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

            elif event.data1 == Buttons['Hyper']:
                # FL window constants
                # -------------------
                # Parameter       Value   Documentation
                # widMixer        0       Mixer
                # widChannelRack  1       Channel rack
                # widPlaylist     2       Playlist
                # widPianoRoll    3       Piano roll
                # widBrowser      4       Browser
                # widPlugin       5       Plugin window
                ui.setFocused(1)
                event.handled = True

            elif event.data1 in Knobs:
                mixer.setTrackVolume(
                    event.data1, event.data2 / 100)
                event.handled = True

    elif event.midiId == midi.MIDI_NOTEON:
        if event.data2 > 0:
            if event.data1 == Pads[1]:
                print('OnNoteOn:')
                print(hyper_engaged)
                # print(keyboard_state_file.read())
