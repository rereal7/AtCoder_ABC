<?php
$n = (int) trim(fgets(STDIN));
$ans = 0;
if($n < 40){
	$ans = 40-$n;
}else if($n < 70){
	$ans = 70-$n;
}else if($n < 90){
	$ans = 90-$n;
}else{
	$ans = 'expert';
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