<?php
[$a, $b] = iints();
echo ($a-$b)/3+$b;

//関数
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