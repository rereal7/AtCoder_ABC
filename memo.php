<?php


//関数
// function int($N=1){
// 	return fscanf(STDIN, str_repeat("%d", $N));
// }
// function str($N=1){
// 	return fscanf(STDIN, str_repeat("%s", $N));
// }
// function float($N=1){
// 	return fscanf(STDIN, str_repeat("%f", $N));
// }

function istr():string{
	return trim(fgets(STDIN));
}
function istrs():array{
	return explode(" ", trim(fgets(STDIN)));
}
function iint():int{
	return trim(fgets(STDIN));
}
function iints():array{ 
	return array_map('intval', explode(" ", trim(fgets(STDIN))));
}