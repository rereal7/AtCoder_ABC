<?php
// $a ^ $b とした場合、一般的には$aの$b乗だが
// $a XOR $b となるので覚えておきたい
[$a, $b] = array_map('intval', explode(" ", trim(fgets(STDIN))));
echo $a^$b;