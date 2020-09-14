#include <gtk/gtk.h>


int main(int argc, char * argv[])
{
    GtkWidget *window;

    // inicializa o GTK
    gtk_init(&argc, &argv); 
    // instancia da janela

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);

    // adicionar um titulo
    gtk_window_set_title(GTK_WINDOW(window), "Matutino");

    // define o tamanho da janela
    gtk_window_set_default_size(GTK_WINDOW(window), 300, 200);

    // centralizar na janela principla
    gtk_window_set_position(GTK_WINDOW(window), GTK_WIN_POS_CENTER);

    g_signal_connect(window, "destroy",
                G_CALLBACK(gtk_main_quit), NULL);

    gtk_widget_show_all(window);

    gtk_main();


    return 0;
}


