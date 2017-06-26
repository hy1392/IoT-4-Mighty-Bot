<?php
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}

$db_host = "localhost";
  //$db_host = "localhost";
  $db_user = "root";
  //$db_passwd = "apmsetup";
  $db_passwd = "root";
  $db_name = "iot";
  $conn = mysqli_connect($db_host, $db_user, $db_passwd, $db_name);
  mysqli_set_charset($conn,"utf8");

  if(mysqli_connect_errno($conn)){
    echo "데이터베이스 연결 실패 : ".mysqli_connect_error();
  }
?>
