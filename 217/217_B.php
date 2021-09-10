<?php
$a = ['ABC', 'ARC', 'AGC', 'AHC'];
for($i=0; $i<3; $i++){
	$s = trim(fgets(STDIN));
	$find = array_search($s, $a);
	unset($a[$find]);
}
echo implode($a);