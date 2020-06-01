<?php
$list = $_REQUEST['list'];
$num_dept= $_REQUEST['num_dept'];
$nb1=$_REQUEST['nb'];
$list1=str_split($list);
$nb=sizeof($list1);
$num_dept=(string)($num_dept);
// $command  = escapeshellcmd('python extrapole.py '.$list1." ".$list2." ".$list3);
// $output = shell_exec($command);
// $opq=exec($command1,$s,$r);
$command1='python extrapole.py '.$num_dept." ".$nb1;
$str="";
for ($i=0; $i<$nb; $i++) {
	
    if($list1[$i]==","){
    	if($str!=""){
    		$command1.=" ".$str;
    		$str="";
    	}
    }
    else{if($list1[$i]!=" "){$str.=$list1[$i];}
    	else{$str.=",";}
    }
}
$opq=exec($command1,$s,$r);
echo $opq


#echo "file:".$file."<br>";
#echo "cmd:".$command."<br>";
#echo $return_var."<br>";

?>