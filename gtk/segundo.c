#include <gtk/gtk.h>


// procedimento para tratar o botao e/ou sinal 
static void btnMudou_click(GtkWidget * widget, GtkLabel *label)
{
    gtk_label_set_text(GTK_LABEL(label), "Mudei o texto");
}

static void btn1_click(GtkWidget *widget){

    printf("\nClicou em btn1 \n");    
    gtk_main_quit();    
}

int main(int argc, char * argv[])
{
    GtkWidget *window;
    GtkWidget *fixed;
    GtkWidget *lblTexto;
    GtkWidget *btnMudar;


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


    // cria um container para uso de posição fixa no gtk
    fixed = gtk_fixed_new();
    gtk_container_add(GTK_CONTAINER(window), fixed);
    gtk_widget_show(fixed);

    //  criando um label
    lblTexto = gtk_label_new("Alo mundo");
 //   gtk_label_set_selectable(GTK_LABEL(lblTexto), TRUE);
    gtk_fixed_put(GTK_FIXED(fixed), lblTexto, 30, 50);
    gtk_widget_show(lblTexto);

    // criar o botao e associa-lo ao um sinal de controle
    btnMudar = gtk_button_new_with_label("Mudar");
    gtk_widget_set_tooltip_text(btnMudar, "Clique para mudar");

    g_signal_connect(btnMudar, "clicked",
                        G_CALLBACK(btnMudou_click), lblTexto);
    gtk_fixed_put(GTK_FIXED(fixed), btnMudar, 100, 100);
    gtk_widget_show(btnMudar);


    gtk_widget_show_all(window);

    gtk_main();


    return 0;
}


