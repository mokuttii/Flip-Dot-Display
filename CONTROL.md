
### CONTROL.md

```markdown
# Control Instructions

This section explains how to control the Alfa Zeta Flip Dot Display XY5 28x7. The control commands are sent via a serial interface and consist of a specific byte structure.

## Command Structure

The command to control the display is structured as follows:

```python
all_dark = bytearray([
    0x80,  # Header
    0x83,  # 28 bytes, refresh
    0xFF,  # Address
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, # 28 bytes of data
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
    0x8F # End of Transmission (EOT)
])
```

- **0x80**: Header byte
- **0x83**: 28 bytes, refresh
- **0xFF**: Address byte
- **0x00 to 0x7F**: 28 bytes of data
- **0x8F**: End of Transmission (EOT)

## Byte Explanation

- **0x00 to 0x7F**: These bytes represent the 28 columns of the 7x28 grid. Each column is represented by a hexadecimal value, with a maximum value of 0x7F (127 in decimal). This value corresponds to the 7 bits of data for that column, with each bit representing the state (on or off) of a dot.

For example, the binary value `1111111` translates to the hexadecimal value `0x7F`, indicating that all seven dots in the column should be on.

### 7x28 Grid Representation

Below is a visual representation of the 7x28 grid. Each dot can be either on (`*`) or off (`.`).

```plaintext
    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
1   .  .  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *
2   .  .  .  *  .  *  .  *  .  *  .  *  .  *  .  *  .  *  .  *  .  *  .  *  .  *  .  *
3   .  .  .  .  *  *  .  .  *  *  .  .  *  *  .  .  *  *  .  .  *  *  .  .  *  *  .  .
4   .  .  .  .  .  .  *  *  *  *  .  .  .  .  *  *  *  *  .  .  .  .  *  *  *  *  .  .
5   .  .  .  .  .  .  .  .  .  *  *  *  *  *  *  .  .  .  .  .  *  *  *  *  *  .  .  .
6   .  .  .  .  .  .  .  .  .  .  .  .  .  *  *  *  *  .  .  .  .  .  .  *  *  *  .  .
7   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  *  *  *  .  .  .  .  .  *  *  .  .
    0x00 0x00 0x01 0x03 0x05 0x07 0x09 0x0B 0x0D 0x0F 0x11 0x13 0x15 0x17 0x19 0x1B 0x1D 0x1F 0x21 0x23 0x25 0x27 0x29 0x2B 0x2D 0x2F 0x31 0x33 0x35 0x37
