<?
  require_once 'dbconnect.php';
  extract($_POST);

  $query = "select * from users where email = '".$id."'"."and pwd = '".$pwd."'";
  $result = mysqli_query($conn, $query);
  if(mysqli_num_rows($result) === 0){
      echo "사용자 정보를 찾을 수 없습니다. 아이디, 비밀번호를 확인하시고 다시 시도해 주세요.";
  }
  else{
    $_SESSION['id'] = $id;
    echo "success";
  }
?>
