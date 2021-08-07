#  This file is part of os-installer
#
#  Copyright 2013-2021 Solus <copyright@getsol.us>.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#

import logging

from gi.repository import Gdk, Gio, Gtk

from os_installer2 import join_resource_path
from os_installer2.mainwindow import MainWindow

APP_ID = "com.solus_project.Installer"


class InstallerApplication(Gtk.Application):
    window = None

    def __init__(self, fatal_err: str = None):
        Gtk.Application.__init__(self,
                                 application_id=APP_ID,
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.fatal_err = fatal_err

    def do_startup(self):
        Gtk.Application.do_startup(self)
        self._set_style()

    def do_activate(self):
        if self.fatal_err:
            logging.critical(self.fatal_err)
            self._show_dialog(self.fatal_err)
            return

        if self.window is None:
            self.window = MainWindow(self)
        self.window.present()

    def _set_style(self):
        try:
            f = Gio.File.new_for_path(join_resource_path("styling.css"))
            css = Gtk.CssProvider()
            css.load_from_file(f)
            screen = Gdk.Screen.get_default()
            prio = Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
            Gtk.StyleContext.add_provider_for_screen(screen, css, prio)
        except Exception as e:
            logging.error("Cannot load CSS: %s", e)

    def _show_dialog(self, msg: str):
        dialog = Gtk.MessageDialog(
            parent=None,
            flags=Gtk.DialogFlags.MODAL,
            type=Gtk.MessageType.ERROR,
            buttons=Gtk.ButtonsType.CLOSE,
            message_format=msg)
        dialog.run()
        dialog.destroy()
