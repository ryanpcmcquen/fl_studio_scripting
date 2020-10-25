# fl_studio_scripting

Fun stuff for FL Studio.

To install the Axiom Air Mini 32 script, find your FL Studio data directory, and copy the `device_AxiomAirMini` directory, so that it lives _inside_ the `Settings\Hardware` directory (`Settings/Hardware` on Mac OS).

---

## Forum post:

https://forum.image-line.com/viewtopic.php?f=1994&t=240884

---

## Legend:

### Buttons:

| Name   | Hex  | Action           |
| ------ | ---- | ---------------- |
| Stop   | 0x10 | Stop / Tap Tempo |
| Start  | 0x11 | Start (Play)     |
| Record | 0x12 | Record           |
| Up     | 0x13 | UI Up            |
| Down   | 0x14 | UI Down          |
| Right  | 0x15 | UI Right         |
| Left   | 0x16 | UI Left          |
| Center | 0x17 | UI Enter         |
| Hyper  | 0x3A | Secondary Mode   |

### Knobs:

| Name | Hex  | Action         |
| ---- | ---- | -------------- |
| 1    | 0x01 | Mixer 1 Volume |
| 2    | 0x02 | Mixer 2 Volume |
| 3    | 0x03 | Mixer 3 Volume |
| 4    | 0x04 | Mixer 4 Volume |
| 5    | 0x05 | Mixer 5 Volume |
| 6    | 0x06 | Mixer 6 Volume |
| 7    | 0x07 | Mixer 7 Volume |
| 8    | 0x08 | Mixer 8 Volume |

### Pad Banks (Drum Pads):

**Note**:
All Pad Bank actions require _Secondary Mode_. To achieve this,
hold the Hyper button, then press the desired Pad.

#### Bank 1:

| Name | Hex  | Action           |
| ---- | ---- | ---------------- |
| 1    | 0x24 | Select Channel 1 |
| 2    | 0x25 | Select Channel 2 |
| 3    | 0x26 | Select Channel 3 |
| 4    | 0x27 | Select Channel 4 |
| 5    | 0x28 | Select Channel 5 |
| 6    | 0x29 | Select Channel 6 |
| 7    | 0x2A | Select Channel 7 |
| 8    | 0x2B | Select Channel 8 |

#### Bank 2:

| Name | Hex  | Action                          |
| ---- | ---- | ------------------------------- |
| 1    | 0x2C | Select Pattern 1 / Solo Track 1 |
| 2    | 0x2D | Select Pattern 2 / Solo Track 2 |
| 3    | 0x2E | Select Pattern 3 / Solo Track 3 |
| 4    | 0x2F | Select Pattern 4 / Solo Track 4 |
| 5    | 0x30 | Select Pattern 5 / Solo Track 5 |
| 6    | 0x31 | Select Pattern 6 / Solo Track 6 |
| 7    | 0x32 | Select Pattern 7 / Solo Track 7 |
| 8    | 0x33 | Select Pattern 8 / Solo Track 8 |

---

## Demo:

Video of my scratchpad workflow made possible through midi scripting:

[![Scratchpad workflow](https://img.youtube.com/vi/VGsCKOv_wKg/0.jpg)](https://www.youtube.com/watch?v=VGsCKOv_wKg)
