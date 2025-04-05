# Chord Drawer

Chord Drawer 是一個用於繪製吉他和弦圖的 Python 函式庫。

## Installation

使用 `pip` 安裝：

```bash
pip install git+https://github.com/j20001020/chord-drawer.git
```

## Example


```python
from chord_drawer.chordDrawer import draw_chord

draw_chord("C", [-1, 3, 2, 0, 1, 0])  # C 和弦
draw_chord("G", [3, 2, 0, 0, 0, 3], 3)  # G 和弦，從第 3 品開始
draw_chord("F", [1, 3, 3, 2, 1, 1])  # F 和弦
```