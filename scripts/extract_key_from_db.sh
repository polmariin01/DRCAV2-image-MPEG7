#!/bin/bash

PATH_MCGILL=db/McGill-Billboard/complete_annotations
PATH_1=003/salami_chords.txt
PATH_RESULTS=../results
PATH_STEPS=db/giantsteps-key-dataset

how_to() {
    echo "Empleo: $0 [db]"
    echo "Exemple: $0 mcgill"
    echo ""
    echo "[db] possibles:"
    echo "mcgill [complete/lab/mirex]"
    echo "mirex []"
    echo ""
}


if [[ $# -lt 1 ]]; then
    how_to
    exit 0
elif [[ $# -eq 1 ]];
then
    echo "Hi ha un argument"
    MODE=$1
elif [[ $# -ge 2 ]];
then
    echo "Hay $# argumentos (demasiados)"
    exit 0
fi


extract_mcgill() {
    echo "prova mcgill"
    echo "$PATH_MCGILL"
    echo
    cd ../$PATH_MCGILL
    #ls

    for file in *
    do
    #    echo
#        pwd
        cd "$file"/
#        ls
#        ton=$(cat *.txt | fgrep "tonic" | cut -c 1-9 --complement | tee ../../../../results/McGill/$file.txt)
        if [[ ! -f ../key/$file.txt ]]; then
            touch ../../key/$file.txt
        fi
        ton=$(cat *.txt | fgrep "tonic" | cut -c 1-9 --complement | tee ../../key/$file.txt)
        echo "$file - $ton"
#            echo "Wav file not found: $filewav" >&2
#            exit 1
#        fi
        cd ../
#        touch ../../results/$
    done
    pwd
}

extract_mirex() {
    echo "La de la mirex"
    echo "No existe ara mateix"
}

extract_giantsteps() {
    cd ../$PATH_STEPS
    for file in ./md5/*.md5; do
        echo "Converting : ${file} ..."
        sox $file ${file%md5}wav rate 44100 gain -0.1 remix -;
        echo " done!\n"
    done;
}


#echo -e "abans del case \nmode = $MODE"
case $MODE in

  mcgill | MCGILL | Mcgill | McGill)
    extract_mcgill
    exit 1
    ;;

  mirex | MIREX | Mirex)
    extract_mirex
    exit 1
    ;;

  giant | giantsteps | GiantSteps | steps)
    extract_giantsteps
    exit 1
    ;;

  *)
    echo "$MODE no es valido" 
    how_to
    ;;
esac

#echo "should if error"
exit 1
#echo "should no"

#AQUI NO ARRIBA MAI, METODE ANTERIOR PER TRIAR LA OPCIÓ AMB IF ELSE, ARA AMB CASE
if [[ "$MODE" == "mcgill" ]];
then
    echo "prova mcgill"
    echo "$PATH_MCGILL"
    cd $PATH_MCGILL
    mkdir prova
    exit 1
fi

if [[ $MODE == "mirex" ]];
then
    echo "La de la mirex"
    exit 1
fi
exit 0