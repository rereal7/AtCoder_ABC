<?php
//読取
$n = trim(fgets(STDIN));

//計算
//nが奇数の場合と偶数の場合の２通りを考える
$ans = '';
while($n>0){
	if($n%2 == 0){
		$n = $n/2;
		$ans .= 'B';
	}else{
		$n--;
		$ans .= 'A';
	}
}

//結果
echo strrev($ans);