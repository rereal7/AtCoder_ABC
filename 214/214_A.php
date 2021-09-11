<?php
$n = (int) trim(fgets(STDIN));
$count = '8';
if($n<=125){
	$count = '4';
}else if($n>=126 && $n<=211){
	$count = '6';
}

echo $count;