<?php
[$s, $t] = array_map('intval', explode(" ", trim(fgets(STDIN))));
$count = 0;
for($a=0; $a<=$s; $a++){
	$r = $s-$a;
	for($b=0; $b<=$r; $b++){
		$q = $s-$a-$b;
		for($c=0; $c<=$q; $c++){
			$sum = $a+$b+$c;
			$multi = $a*$b*$c;
			if($sum <= $s && $multi<=$t){
				$count++;
			}
		}
	}
}
echo $count;