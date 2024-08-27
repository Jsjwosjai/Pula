<!DOCTYPE html>
<html lang="en">
<head>
        <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ARick💚</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */
    label { color: white; }
    .file { height: 30px; }
    body {
      background-image: url('https://i.postimg.cc/ZY80hKfQ/1719284886906.jpg');
      background-size: cover;
      background-repeat: no-repeat;
      color: white;
    }
    h1{
        font-size: 14px;
    }
    .container {
      max-width: 350px;
      height: auto;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
      border: none;
      resize: none;
    }
    .form-control {
      outline: 1px red;
      border: 1px double white;
      background: transparent;
      width: 100%;
      height: 40px;
      padding: 7px;
      margin-bottom: 20px;
      border-radius: 20px;
      color: none;
    }
    .header { text-align: center; padding-bottom: 20px; }
    .btn-submit { width: 100%; margin-top: 10px; }
    .footer { text-align: center; margin-top: 20px; color: #888; }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    h2{
        font-display: cursive;
    }
    .whatsapp-link i { margin-right: 5px; }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h2 class="mt-3">tmkc</h2>
  </header>
      <form method="POST" enctype="multipart/form-data">
  <div class="container text-center">
       <h1>MULTI COOKIE WALL</h1>
      <h2></h2>
      <div class="mb-3">
        <label for="post_id" class="form-label">Post Id:</label>
        <input type="text" class="form-control" id="post_id" name="post_id" required>
      </div>
      <div class="mb-3">
        <label for="commenter_name" class="form-label">Enter Your Hater Name</label>
        <input type="text" class="form-control" id="commenter_name" name="commenter_name" required>
      </div>
      <div class="mb-3">
        <label for="cookie" class="form-label">Choose Your Cookie:</label>
        <input type="file" class="form-control" id="cookie" name="cookie" required>
      </div>
      <div class="mb-3">
        <label for="comments" class="form-label">Choose Your Comment File</label>
        <input type="file" class="form-control" id="comments" name="comments" required>
      </div>
      <div class="mb-3">
        <label for="delay" class="form-label">Enter Time (seconds)</label>
        <input type="number" class="form-control" id="delay" name="delay" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Run</button>
    </form>
    <form method="post" action="/stop"
    id="stop">
      <div class="mb-3">
          
    </form>
  </div>
  <footer class="footer">
    <p>© 2023 CODED BY :- ARICK</p>
    <p> ALWAYS ON FIRE 🔥 </p>
    <div class="mb-3">
      <a href="https://wa.me/+917717655637" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
      </a>
    </div>
  </footer>
  <script>
    
    swal("WELCOME!", "FACEBOOK POST TOOL);
    document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();
    swal({
      title: "Are you sure?",
      text: "This will send comments to the Post ID.",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
    .then((willSend) => {
      if (willSend) {
        this.submit();
      }
    });
  });
  
  </script>
</body>
</html>
