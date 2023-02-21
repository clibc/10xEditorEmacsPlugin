# Emacs plugin for [10xEditor](https://10xeditor.com/)

This is not, in any way, a fully functional Emacs emulation. There are only features that I use (which is not much).

#### Features
- Mark emulation
- Block jump

#### Commands
- `EmacsSetCursor` - set mark
- `EmacsCopy` - copy region
- `EmacsCut` - cut region
- `EmacsDelete` - delete-region
- `EmacsCursorJumpBack` - exchange-point-and-mark
- `EmacsScrollUp` - Scrolls up by `ScrollLineCount`
- `EmacsScrollDown` - Scrolls down by `ScrollLineCount`
- `EmacsJumpBlockUp` - Jumps to previous empty line
- `EmacsJumpBlockDown` - Jumps to next empty line

Scroll amount can be changed via `ScrollLineCount` variable in `Emacs.py`.

#### Installation
Copy `Emacs.py` to `%appdata%/10x/PythonScripts` .

Set keyboard shortcuts in 10xEditor.