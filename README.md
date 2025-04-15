# Chord Drawer

Chord Drawer is a Python tool that uses matplotlib to **draw guitar chord diagrams**.

## Installation

Install with `pip`:

```bash
pip install git+https://github.com/j20001020/chord-drawer.git
```

## Example


```python
from chord_drawer import draw_chord

draw_chord("C", [-1, 3, 2, 0, 1, 0])  # C chord

draw_chord(chord_name="G", frets=[3, 2, 0, 0, 0, 3], start_fret=3)  # G chord, starting from fret 3

draw_chord("F", [1, 3, 3, 2, 1, 1])  # F chord
```

![image](https://github.com/user-attachments/assets/3685a6e6-25f7-4691-80e9-4e29e90ae1fb)
