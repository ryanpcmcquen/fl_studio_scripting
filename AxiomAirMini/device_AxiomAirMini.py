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
# 0.4.0 - October 23 2020
# Allow drum pads to select channels
# if Hyper key is engaged.
#
# 0.5.0 - October 23 2020
# Allow pattern selection with
# numbered piano keys.
#

import channels
import midi
import mixer
import patterns
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

Pads = [
    0x24,
    0x25,
    0x26,
    0x27,
    0x28,
    0x29,
    0x2A,
    0x2B,
]

Numbered_Keys = [
    0x32,
    0x34,
    0x35,
    0x37,
    0x39,
    0x3B,
    0x3C,
    0x3E,
    0x40,
    0x41,
]

SECONDAY_MODE_HINT = '**SECONDARY MODE**'


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
    event.handled = False
    if event.data1 == Buttons['Hyper']:
        if event.data2 > 0:
            ui.setHintMsg(SECONDAY_MODE_HINT)
        else:
            ui.setHintMsg('')

    # Secondary mode!
    # This has to be handled in 'OnMidiIn',
    # because by the time it gets into
    # 'OnMidiMsg', the hint message
    # is already being
    # overwritten.
    if ui.getHintMsg() == SECONDAY_MODE_HINT:
        if event.data2 > 0:
            if event.data1 in Pads:
                channels.selectChannel(
                    Pads.index(event.data1),
                    1
                )
                event.handled = True
            if event.data1 in Numbered_Keys:
                patterns.selectPattern(
                    # These are off by 1, but the
                    # channels are not ...
                    Numbered_Keys.index(event.data1) + 1,
                    1
                )


def OnMidiMsg(event):
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
                    Knobs.index(event.data1),
                    event.data2 / 100
                )
                event.handled = True
