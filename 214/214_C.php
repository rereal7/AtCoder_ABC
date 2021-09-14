<?php
$n = (int) trim(fgets(STDIN));
$s = array_map('intval', explode(" ", trim(fgets(STDIN))));
$t = array_map('intval', explode(" ", trim(fgets(STDIN))));

//$n*2 にしているのは、$s+$t の合計要素数が$n*2 のため
for($i=0; $i<$n*2; $i++){
	//%$n にしているのは、$i=n*2 の時、インデックスエラーが出てしまうのを回避するため
	$t[($i+1)%$n] = min($t[($i+1)%$n], $t[$i%$n]+$s[$i%$n]);
}

echo implode(PHP_EOL, $t);