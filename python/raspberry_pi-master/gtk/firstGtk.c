#include <gtk/gtk.h>

#include <string.h>
#include <stdlib.h>

gchar *str = "<b>ZetCode</b>, knowledge only matters";

void updateLabel(GtkLabel *sum, int num)
{
    gchar *display;
    display = g_strdup_printf("%d", num);         //convert num to str
    gtk_label_set_text (GTK_LABEL(sum), display); //set label to "display"
    g_free(display);                              //free display
}

static void close_button( GtkWidget *widget){
    printf("Alo");
    gtk_main_quit();
}

static void button1_click( GtkWidget *widget,  GtkLabel *label){
    printf("\nAcionei o botao 1\n");
    //updateLabel(label, 100);
    gtk_label_set_text(GTK_LABEL(labek), str); //set label to "display"
}


int main(int argc , char * argv[]){

    GtkWidget *window;
    GtkWidget *button;
    GtkWidget *button2;
    GtkWidget *halign;
    GtkWidget *fixed;
    GtkWidget *label;

    gtk_init(&argc, &argv);

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    //mudar titulo da janela
    gtk_window_set_title(GTK_WINDOW(window),"Vespertino");

 /* Sets the border width of the window. */
 // gtk_container_set_border_width (GTK_CONTAINER (window), 10);  

    // mudar o tamanho da janela
    gtk_window_set_default_size(GTK_WINDOW(window), 250,180);
    // posiciona no centro da tela
    gtk_window_set_position(GTK_WINDOW(window), GTK_WIN_POS_CENTER);

    // criando lable
    label = gtk_label_new ("Valor 0");
    gtk_label_set_selectable       (GTK_LABEL(label), TRUE);


    //criando um botao
    button = gtk_button_new_with_label("Botão");
    gtk_widget_set_tooltip_text(button,"Clique no botão");


    //alinhamento do botao
   // halign = gtk_alignment_new(0,0,0,0);
   // gtk_container_add(GTK_CONTAINER(halign),button);
   // gtk_container_add(GTK_CONTAINER(window), halign);


    
    fixed = gtk_fixed_new ();
    gtk_container_add (GTK_CONTAINER (window), fixed);
    gtk_widget_show (fixed);
    button2 = gtk_button_new_with_label("Botão2");
    gtk_widget_set_tooltip_text(button2,"Clique no botão");
    
    g_signal_connect (button2, "clicked",
		      G_CALLBACK (close_button),NULL );

    g_signal_connect (button, "clicked",
		        G_CALLBACK (button1_click),label );              
    


    gtk_fixed_put(GTK_FIXED(fixed), button2, 50,50);
    gtk_widget_show (button2);

    gtk_fixed_put(GTK_FIXED(fixed), button, 0,0);
    gtk_widget_show (button);

    gtk_fixed_put(GTK_FIXED(fixed), label, 100,10);
    gtk_widget_show (label);



    gtk_widget_show_all(window);


//    gtk_widget_show(window);

    g_signal_connect(window, "destroy",
            G_CALLBACK(gtk_main_quit), NULL);

    gtk_main();

 

    return 0;            

}