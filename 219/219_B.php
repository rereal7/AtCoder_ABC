<?php
$ans = '';

$S = [];
for($i=0; $i<3; $i++){
	$S[] = trim(fgets(STDIN));
}
$T = str_split(trim(fgets(STDIN)));

foreach($T as $t){
	$ans .= $S[$t-1];
}
echo $ans;