<?php
[$a, $b] = int(2);
$ans = 'Alloy';
if($b===0){
	$ans = 'Gold';
}else if($a===0){
	$ans = 'Silver';
}
echo $ans;

//関数
function int($N=1){
	return fscanf(STDIN, str_repeat("%d", $N));
}
function str($N=1){
	return fscanf(STDIN, str_repeat("%s", $N));
}
function float($N=1){
	return fscanf(STDIN, str_repeat("%f", $N));
}