<?php
$N = trim(fgets(STDIN));
[$x, $y] = int(2);
for($i=0; $i<$N; $i++){
	[$A[], $B[]] = int(2);
}

var_dump($x);
var_dump($y);
var_dump($A);
var_dump($B);


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
