<?php
$n = (int) trim(fgets(STDIN));
$a = array_map('intval', explode(" ", trim(fgets(STDIN))));
$a_sub = $a;
rsort($a);
$target = $a[1];
echo array_search($target, $a_sub) + 1;