<?php
// 0≤Y≤2 ならば、X-
// 3≤Y≤6 ならば、X
// 7≤Y≤9 ならば、X+

//読取
[$x, $y] = explode(".", trim(fgets(STDIN)));

//計算
if($y>=0 && $y<=2){
	$y = '-';
}else if($y>=3 && $y<=6){
	$y = '';
}else{
	$y = '+';
}

//結果
echo $x.$y;

//関数
