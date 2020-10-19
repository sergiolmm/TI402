#include <gtk/gtk.h>

void togg(GtkWidget *widget, gpointer *data){
    if (gtk_toggle_button_get_active(GTK_TOGGLE_BUTTON(data)))
        g_print("State is 1\n");
    else
        g_print("State is 0\n");
}
int main( int argc,char *argv[] )
{
    GtkWidget *window;
    GtkWidget *button;
    gtk_init (&argc, &argv);
    
    /* Create a new window */
    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title (GTK_WINDOW (window), "Toggle Button");
 
    /* Connect destroy event to the window. */
    g_signal_connect (window, "destroy",
                        G_CALLBACK(gtk_main_quit), NULL);
    
    /* Creates a toggle button */
    button=gtk_toggle_button_new_with_label("I’m a toggle button");
    
    /* Add the button to window */
    gtk_container_add(GTK_CONTAINER(window),button);
 
    /* Connect "toggled" event to the button */
    g_signal_connect ( (button), "toggled",
                    G_CALLBACK(togg),(gpointer *)button);
    gtk_widget_show(button);
    gtk_widget_show (window);
    gtk_main ();
    return(0);
}