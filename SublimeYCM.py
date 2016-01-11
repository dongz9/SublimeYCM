import sublime, sublime_plugin
import os

def plugin_loaded():
    print("SublimeYCM loaded, ST version = %s" % sublime.version())
    settings = sublime.load_settings("SublimeYCM.sublime-settings")
    python_executable = settings.get("python_executable")
    print("python_executable = %s" % python_executable)
    global_extra_config = settings.get("global_extra_config")
    print("global_extra_config = %s" % global_extra_config)

def plugin_unloaded():
    print("SublimeYCM unloaded")
