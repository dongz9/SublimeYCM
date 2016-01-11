import sublime, sublime_plugin
import os
import socket

def find_unused_port():
    sock = socket.socket()
    sock.bind(("",0))
    port = sock.getsockname()[1]
    sock.close()
    return port

class YcmdServer:
    @classmethod
    def start_ycmd():
        return None

def plugin_loaded():
    print("SublimeYCM loaded, ST version = %s" % sublime.version())
    settings = sublime.load_settings("SublimeYCM.sublime-settings")
    python_executable = settings.get("python_executable")
    print("python_executable = %s" % python_executable)
    global_extra_config = settings.get("global_extra_config")
    print("global_extra_config = %s" % global_extra_config)
    port = find_unused_port()
    print("port = %d" % port)

def plugin_unloaded():
    print("SublimeYCM unloaded")

class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
