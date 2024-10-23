import gi
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def search_package(package_name):
    result = subprocess.run(['apt-cache', 'search', package_name], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def install_package(package_name):
    result = subprocess.run(['sudo', 'apt-get', 'install', '-y', package_name], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def remove_package(package_name):
    result = subprocess.run(['sudo', 'apt-get', 'remove', '-y', package_name], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

class StoreWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My Linux Store")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)
        self.package_entry = Gtk.Entry()
        self.package_entry.set_placeholder_text("Search for a package")
        box.pack_start(self.package_entry, False, False, 0)
        self.search_button = Gtk.Button(label="Search")
        self.search_button.connect("clicked", self.on_search_clicked)
        box.pack_start(self.search_button, False, False, 0)
        self.result_label = Gtk.Label(label="Results will appear here")
        box.pack_start(self.result_label, False, False, 0)
        self.install_button = Gtk.Button(label="Install")
        self.install_button.connect("clicked", self.on_install_clicked)
        box.pack_start(self.install_button, False, False, 0)
        self.remove_button = Gtk.Button(label="Remove")
        self.remove_button.connect("clicked", self.on_remove_clicked)
        box.pack_start(self.remove_button, False, False, 0)

    def on_search_clicked(self, widget):
        package_name = self.package_entry.get_text()
        result = search_package(package_name)
        self.result_label.set_text(result)

    def on_install_clicked(self, widget):
        package_name = self.package_entry.get_text()
        result = install_package(package_name)
        self.result_label.set_text(result)

    def on_remove_clicked(self, widget):
        package_name = self.package_entry.get_text()
        result = remove_package(package_name)
        self.result_label.set_text(result)

win = StoreWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
