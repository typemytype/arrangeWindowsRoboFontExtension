## cascade windows
import AppKit

def cascade():

    windows = [w for w in AppKit.NSApp().orderedWindows() if w.isVisible()]

    screen = AppKit.NSScreen.mainScreen()
    (x, y), (w, h) = screen.visibleFrame()

    altDown = AppKit.NSEvent.modifierFlags() & AppKit.NSAlternateKeyMask

    AppKit.NSApp().arrangeInFront_(None)

    leftTop = (x, y + h)
    for window in reversed(windows):
        window.setFrameTopLeftPoint_(leftTop)
        leftTop = window.cascadeTopLeftFromPoint_(leftTop)
