<?php
$n = trim(fgets(STDIN));
$p = explode(" ", trim(fgets(STDIN)));
$q = range(1, $n);
// var_dump($q);
for($i=0; $i<$n; $i++){
	$r = $p[$i] - 1;
	$q[$r] = $i+1;
}

echo implode(" ", $q);