<div>
<a href="logout.php" style="display:block;text-align:right;" target=_top>LOGOUT</a>
</div>
<?php
$i = $_REQUEST["r1"];
if($i =='delhi')
	header("Location:delhireport1.php");
else if($i=='hyderabad')
	header("Location:hyderabadreport1.php");
else if($i=='gannavaram')
	header("Location:gannavaramreport1.php");
else if($i=='all')
	header("Location:centraloverall.php");
?>