<?php
    require_once("dbconnect.php");
    extract($_POST);
    $dup = "select * from users where email='".$id."'";
    $dup_result = mysqli_query($conn,$dup);
    if(mysqli_num_rows($dup_result)>0){
      echo "이미 사용중인 아이디 입니다.";
      return;
    }
    $data_stream = "'".$id."','".$pwd."'";
    $query = "insert into users(email, pwd) values (".$data_stream.")";
    $result = mysqli_query($conn, $query);
    $_SESSION['id'] = $id;
    echo "success";

    mysqli_close($conn);
?>
