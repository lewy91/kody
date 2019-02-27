<?php
    $tekst='Siemanko dripo';
    echo hash('sha1', $tekst);
    echo "\n";
    echo hash('sha256', $tekst);
    echo "\n";
    $haslo='bardzo tajne mainy w lolu';
    echo hash('sha1', $haslo);

?>
