#include <gtk/gtk.h>

gchar *str = "Noturno rule´s...";

// função para tratar o click do botato
static void btn1_click(GtkWidget *widget){

    printf("\nClicou em btn1 \n");    
    gtk_main_quit();    
}

// função para tratar o click do botato
static void btn2_click(GtkWidget *widget, GtkLabel *label){

    printf("\nClicou em btn2 \n");    
    gtk_label_set_text(GTK_LABEL(label), "Mudei o texto");

}



// procedimento principal
int main(int argc, char * argv[]){

    GtkWidget *window;
    GtkWidget *fixed;
    GtkWidget *label;
    GtkWidget *btn1;
    GtkWidget *btn2;

    GtkWidget *entry;

    gtk_init(&argc, &argv);
    // instancia a janela
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    // muda o titulo da janela
    gtk_window_set_title(GTK_WINDOW(window), "Noturno");
    // definir um tamanh para a janela
    gtk_window_set_default_size(GTK_WINDOW(window), 300, 200);
    // setar posicionamento para meio da tela
    gtk_window_set_position(GTK_WINDOW(window), GTK_WIN_POS_CENTER);

    // trabalhando com posições fixas
    fixed = gtk_fixed_new();
    gtk_container_add(GTK_CONTAINER(window),fixed);
    gtk_widget_show(fixed);

    // criando o label
    label = gtk_label_new(str);
    gtk_label_set_selectable(GTK_LABEL(label), TRUE);
    gtk_fixed_put(GTK_FIXED(fixed), label, 20, 20);
    gtk_widget_show(label);

    // criando um botao e adicionado sinal para o botao
    btn1 = gtk_button_new_with_label("Sair");
    gtk_widget_set_tooltip_text(btn1, "Clique para sair");

    g_signal_connect(btn1, "clicked",
                    G_CALLBACK(btn1_click), NULL);

    gtk_fixed_put(GTK_FIXED(fixed), btn1, 20, 150);
    gtk_widget_show(btn1);

 // criando um botao2 e adicionado sinal para o botao2
    btn2 = gtk_button_new_with_label("Mudar");
    gtk_widget_set_tooltip_text(btn2, "Clique para mudar texto");

    g_signal_connect(btn2, "clicked",
                    G_CALLBACK(btn2_click), label);

    gtk_fixed_put(GTK_FIXED(fixed), btn2, 120, 50);
    gtk_widget_show(btn2);


    entry = gtk_entry_new ();
    gtk_entry_set_max_length (GTK_ENTRY (entry), 50);
 //   g_signal_connect (entry, "activate",
//		      G_CALLBACK (enter_callback),
//		      entry);
    gtk_entry_set_text (GTK_ENTRY (entry), "hello");


    gtk_fixed_put(GTK_FIXED(fixed), entry, 120, 180);
    gtk_widget_show(entry);



    gtk_widget_show_all(window);

    g_signal_connect(window, "destroy",
                G_CALLBACK(gtk_main_quit),NULL);

    gtk_main();

    return 0;                

}