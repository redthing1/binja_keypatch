import sys
import binaryninja

if binaryninja.core_ui_enabled():
    from binaryninjaui import (UIAction, UIActionHandler, Menu)

    from . import keypatch

    UIAction.registerAction("Keypatch")
    UIActionHandler.globalActions().bindAction("Keypatch", UIAction(keypatch.launch_keypatch))
    Menu.mainMenu("Plugins").addAction("Keypatch", "Keypatch")
else:
    # probably being loaded by headless BinaryNinja
    pass
