#!/bin/bash

for i in {0..99}; do
	echo "Processando arquivo $i.in"
	diff --unified=0 "exemplos/solucoes/$i.out" <(./main.py <"exemplos/instancias/$i.in")
done
