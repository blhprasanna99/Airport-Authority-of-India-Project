<?php
session_start();
$con = mysqli_connect("localhost","root","","airportservices");
if ($con -> connect_errno) {
  echo "Failed to connect to MySQL: " . $con -> connect_error;
  exit();
}
$u = $_REQUEST["t1"];
$p = $_REQUEST["t2"];
$r = $_REQUEST["r1"];
$_SESSION["user"] = $u;
$q = "select password from Credentials where userid='$u' and role='$r'";
$result = mysqli_query($con,$q);
if(($row = mysqli_fetch_array($result))!=null)
{
	if($row['password']==$p)
	{
		if($r == 'central')
		{
			header("Location:central.php");
		}
		else if($u=='delhila')
		{
			header("Location:delhireport1.php");
		}
		else if($u=='hyderabadla')
		{
			header("Location:hyderabadreport1.php");
		}
		else if($u=='gannavaramla')
		{
			header("Location:gannavaramreport1.php");
		}
		else
			header("Location:login.html");
	}
	else
		header("Location:login.html");
}
else
		header("Location:login.html");

?>