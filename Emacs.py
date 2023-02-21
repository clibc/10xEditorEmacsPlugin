from N10X import Editor

ScrollLineCount = 10
CursorStartPos = (0, 0)

def EmacsSetCursor():
	global CursorStartPos
	CursorStartPos = Editor.GetCursorPos()
	Editor.SetStatusBarText("Cursor set " + str(CursorStartPos))

def EmacsCopy():
	CurrentCursorPos = Editor.GetCursorPos()
	Editor.SetSelection(CursorStartPos, CurrentCursorPos)
	Editor.ExecuteCommand("Copy")
	Editor.ClearSelection()

def EmacsCut():
	CurrentCursorPos = Editor.GetCursorPos()
	if CursorStartPos == CurrentCursorPos:
		return
	Editor.SetSelection(CursorStartPos, CurrentCursorPos)
	Editor.ExecuteCommand("Cut")
	Editor.ClearSelection()

def EmacsDelete():
	CurrentCursorPos = Editor.GetCursorPos()
	if CursorStartPos == CurrentCursorPos:
		return
	Editor.SetSelection(CursorStartPos, CurrentCursorPos)
	Editor.ExecuteCommand("Delete")
	Editor.ClearSelection()

def EmacsCursorJumpBack():
	global CursorStartPos
	JumpPos = CursorStartPos
	CursorStartPos = Editor.GetCursorPos()
	Editor.SetCursorPos(JumpPos)

def EmacsScrollUp():
	for I in range(ScrollLineCount):
		Editor.ExecuteCommand("ScrollOneLineUp")

def EmacsScrollDown():
	for I in range(ScrollLineCount):
		Editor.ExecuteCommand("ScrollOneLineDown")

def EmacsJumpBlockUp():
	CursorPos = Editor.GetCursorPos()
	CursorY = CursorPos[1]
	CursorYStart = CursorPos[1]
	while CursorY > 0:
		CursorY -= 1
		Line = Editor.GetLine(CursorY)
		if Line.isspace():
			break
	Editor.SetCursorPos((0, CursorY))

def EmacsJumpBlockDown():
	LineCount = Editor.GetLineCount()
	CursorPos = Editor.GetCursorPos()
	CursorY = CursorPos[1]
	CursorYStart = CursorPos[1]
	while CursorY < LineCount:
		CursorY += 1
		Line = Editor.GetLine(CursorY)
		if Line.isspace():
			break
	Editor.SetCursorPos((0, CursorY))

try:
	import clipboard
	print("Emacs: clipboard module is found")
	RingBuffer = ""

	def EmacsKillLine():
		global RingBuffer
		Editor.ExecuteCommand("Cut")
		RingBuffer += clipboard.paste()
		clipboard.copy(RingBuffer)
		print(RingBuffer)

	def __OnCharKey(Key, Shift, Control, Alt):
		global RingBuffer
		if Key == "Up" or Key == "Down" or Key == "Left" or Key == "Right":
			RingBuffer = ""
	Editor.AddOnInterceptKeyFunction(__OnCharKey)
except ModuleNotFoundError:
    print("Emacs: clipboard module is not found, kill line is disabled")