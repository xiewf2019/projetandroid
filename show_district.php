<?php
$list1 = $_REQUEST['list1'];
$list2 = $_REQUEST['list2'];
$list3 = $_REQUEST['list3'];
$d='python3 extrapole.py ';
$command1='python extrapole.py '.$list1." ".$list2." ".$list3." 2>&1";

$command  = escapeshellcmd('python extrapole.py '.$list1." ".$list2." ".$list3);
$output = shell_exec($command);
$opq=exec($command1,$s,$r);

echo $opq



#echo "file:".$file."<br>";
#echo "cmd:".$command."<br>";
#echo $return_var."<br>";

?>