<?php

// No php 7 foi introduzido oc aracter de escape Unicode.
// permite apresentar caracteres a partir do seu codico hexadecimal

// https://www.utf8-chartable.de/

echo "\u{A9}"; // copyright
echo "\u{BC}"; // 1/4
echo "\u{AE}"; // registered trademark

// com HTML entities
// https://dev.w3.org/html5/html-author/charref
echo '<br>';
echo '&copy;';
echo '&frac14;';
echo '&reg;';