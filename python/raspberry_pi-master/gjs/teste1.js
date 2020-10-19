imports.gi.versions.Gtk = "3.0";
const { Gtk } = imports.gi;

Gtk.init(null);

const box = new Gtk.Box({ orientation: Gtk.Orientation.VERTICAL });

const entry = new Gtk.Entry({
    buffer: new Gtk.EntryBuffer()
});

box.add(entry);

const button = new Gtk.Button({
    label: 'Enter'
});

button.connect('clicked', () => {
    log('Entered in the entry: ' + entry.get_buffer().text);
});

box.add(button);

const win = new Gtk.Window({ defaultHeight: 200, defaultWidth: 300 });
win.connect('destroy', () => { Gtk.main_quit(); });
win.add(box);
win.show_all();

Gtk.main();
