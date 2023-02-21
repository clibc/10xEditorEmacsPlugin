# 10xEditorEmacsPlugin

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

Scroll amount changed via `ScrollLineCount` variable in `Emacs.py`.

#### Installation
Copy `Emacs.py` to `%appdata%/10x/PythonScripts` .

Set keyboard shortcuts in 10xEditor.
