# Chord Drawer

Chord Drawer is a Python library that allows you to easily draw guitar chord diagrams. It provides a simple interface to visualize chords based on the fret and string information you provide.

## Features

- Draws guitar chord diagrams for any chord name.
- Supports specifying which frets to press on each string.
- Displays open strings and muted strings clearly.

## Installation

You can install the Chord Drawer library using pip. First, clone the repository:

```bash
git clone https://github.com/yourusername/chord-drawer.git
cd chord-drawer
```

Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To use the Chord Drawer library, you can import it and call the `draw_chord` function with the desired chord name and fret information. Here’s an example:

```python
from chord_drawer.chord_drawer import draw_chord

# Draw a C major chord
draw_chord("C", [-1, 3, 2, 0, 1, 0])

# Draw a G major chord with a starting fret of 3
draw_chord("G", [3, 2, 0, 0, 0, 3], start_fret=3)
```

## Running Tests

To ensure everything is working correctly, you can run the tests provided in the `tests` directory. Make sure you have pytest installed, then run:

```bash
pytest tests/test_chord_drawer.py
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.