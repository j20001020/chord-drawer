# Chord Drawer

Chord Drawer 是一個用於繪製吉他和弦圖的 Python 函式庫。

## Installation

使用 `pip` 安裝：

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
