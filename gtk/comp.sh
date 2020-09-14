#!/bin/bash

echo "Compilando o programa "


gcc `pkg-config --cflags gtk+-3.0` -o $1 $1.c `pkg-config --libs gtk+-3.0`

echo "terminou"
echo "Tecle algo para terminar"
read n


