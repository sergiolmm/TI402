#include <gtk/gtk.h>

gchar *str = "Noturno rule´s...";

struct edita
{
    /* data */
    GtkWidget *label;
    GtkWidget *EditText;
} edt;


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

static void enter_callback(GtkWidget *widget, GtkWidget *EditText)
{
    const gchar *texto;
    texto = gtk_entry_get_text(GTK_ENTRY(EditText));
    printf ("Digitou a seguinte frase %s\n", texto);

}

static void mudaTexto(GtkWidget *widget, GtkWidget *widge2)
{
    const gchar *texto;
    texto = gtk_entry_get_text(GTK_ENTRY(edt.EditText));
    gtk_label_set_text(GTK_LABEL(edt.label), texto);
    
}

static void checkEditavel(GtkWidget *checkBtn, GtkWidget *EditText)
{
    gboolean estado;
    
    estado = gtk_toggle_button_get_active(GTK_TOGGLE_BUTTON(checkBtn));
    gtk_editable_set_editable(GTK_EDITABLE(EditText),estado);
    gtk_widget_grab_focus(GTK_WIDGET(EditText));
}

// procedimento principal
int main(int argc, char * argv[]){

    GtkWidget *window;
    GtkWidget *fixed;
    GtkWidget *label;
    GtkWidget *btn1;
    GtkWidget *btn2;
    GtkWidget *btn3;

    GtkWidget *EditText;
    GtkWidget *check;

    

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

    EditText = gtk_entry_new();
    gtk_entry_set_max_length(GTK_ENTRY(EditText), 50);
    gtk_entry_set_text(GTK_ENTRY(EditText),"Alo turma");
    gtk_editable_set_editable(GTK_EDITABLE(EditText),FALSE);
    g_signal_connect(EditText, "activate",
                    G_CALLBACK(enter_callback), EditText);


    gtk_fixed_put(GTK_FIXED(fixed), EditText, 60,100);
    gtk_widget_show(EditText);

    edt.EditText = EditText;
    edt.label = label;

    btn3 = gtk_button_new_with_label("Mudar Texto");
    g_signal_connect(btn3, "clicked",
                    G_CALLBACK(mudaTexto), btn3);

    gtk_fixed_put(GTK_FIXED(fixed), btn3, 120, 150);
    gtk_widget_show(btn3);

    check = gtk_check_button_new_with_label("Editável");
    g_signal_connect(check, "toggled",
                    G_CALLBACK(checkEditavel), EditText);

    gtk_toggle_button_set_active(GTK_TOGGLE_BUTTON(check), FALSE);
    gtk_fixed_put(GTK_FIXED(fixed), check, 120, 20);
    gtk_widget_show(check);






    gtk_widget_show_all(window);

    g_signal_connect(window, "destroy",
                G_CALLBACK(gtk_main_quit),NULL);

    gtk_main();

    return 0;                

}