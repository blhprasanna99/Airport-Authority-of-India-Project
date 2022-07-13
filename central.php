<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Login Page</title>
<style>
.login-card {
  width: 400px;
  background-color: black;
  margin: 0px auto ;
  border-radius: 9px;
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
  min-height:400px;
 
}
.log_head{ background:#4DC889; width:400px; height:80px; border-radius:9px 9px 0 0px; }
.login-card h1 {
  text-align: center;
  font-family:open Sans;
  color:#FFFFFF;
  font-weight:700px;
  font-size:20px;
  line-height:27px;
  padding-top: 24px;
  
}
.lock{ padding-left:181px; width:30px; height:37px; padding-top:10px;}
.log_body{ padding:40px 20px 20px 20px;}
.log_user{ background:#FEFEFE; color:#999999; border-radius: 10px; width:349px; height:31px; padding:5px; font-family:open Sans; font-weight:700px; font-size:15px; border:none; }
.log_Pass{background:#FEFEFE; color:#999999; border-radius: 10px; width:349px; height:31px; padding:5px; font-family:open Sans; font-weight:700px; font-size:15px; border:none;}
.login-submit{ background:#4DC889; border:none; border-radius: 10px; width:359px; height:36px; cursor:pointer; font-family:open Sans; font-weight:700px; font-size:15px; color:#FFFFFF; }
.log_body a{ text-decoration:none; color:white; font-family:open Sans; font-weight:900px; font-size:15px; line-height:21px;}</code>
</style>
</head>

<body style="background:url('background.png')">
<br />
<br />

<div class="login-card">
<div class="log_head">
<h1>Choice of Visualization</h1>
</div>

<div class="log_body">
<form action="centralreport.php" method=get">
 <table width="200" border="0" align="center">
 <tr>
   <td><p style="color:white"><input name="r1" type="radio" value="delhi">&nbsp;&nbsp;Delhi Airport</p></td>
  </tr>
    <tr>
    <td>&nbsp;</td>
  </tr>
  <tr>
   <td><p style="color:white"><input name="r1" type="radio" value="hyderabad">&nbsp;&nbsp;Hyderabad Airport</p></td>
  </tr>
    <tr>
    <td>&nbsp;</td>
  </tr>
  <tr>
   <td><p style="color:white"><input name="r1" type="radio" value="gannavaram">&nbsp;&nbsp;Gannavaram Airport</p></td>
  </tr>
  <tr>
    <td>&nbsp;</td>
  </tr>
  <tr>
   <td><p style="color:white"><input name="r1" type="radio" value="all">&nbsp;&nbsp;All Airports</p></td>
  </tr>
  <tr>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td><input type="submit" name="login" class="login-submit" value="Submit"></td>
  </tr>
  <tr>
    <td>&nbsp;</td>
  </tr>
  </table>

</form> 
</div>

</div>
</body>
</html>
</code>