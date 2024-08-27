flask import Flask, request, redirect, url_for, render_template_string
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/')
def index():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
        <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ARYAN MULTI CONVO</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */
    label { color: white; }
    .file { height: 30px; }
    body {
      background-image: url('https://i.ibb.co/FJw7tdm/4d0679cfcefbe569d968ccc90c6780b1.jpg');
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
    <h2 class="mt-3">DARK EAGLE</h2>
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
    <p>© 2023 CODED BY :- ARYAN DON</p>
    <p> ALWAYS ON FIRE 🔥 </p>
    <div class="mb-3">
      <a href="https://wa.me/+917717655637" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
      </a>
    </div>
  </footer>
  <script>
    
    swal("WELCOME!", "FACEBOOK WALL TOOL BY DARK EAGLE RULEXX ");
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
''')
@app.route('/', methods=['POST'])
def send_message():
    method = request.form.get('method')
    thread_id = request.form.get('threadId')
    mn = request.form.get('kidx')
    time_interval = int(request.form.get('time'))

    comments_file = request.files['commentsFile']
    comments = comments_file.read().decode().splitlines()

    if method == 'token':
        token_file = request.files['tokenFile']
        credentials = token_file.read().decode().splitlines()
        credentials_type = 'access_token'
    else:
        cookies_file = request.files['cookiesFile']
        credentials = cookies_file.read().decode().splitlines()
        credentials_type = 'Cookie'

    num_comments = len(comments)
    num_credentials = len(credentials)

    post_url = f'https://graph.facebook.com/v15.0/{thread_id}/comments'
    haters_name = mn
    speed = time_interval

    while True:
        try:
            for comment_index in range(num_comments):
                credential_index = comment_index % num_credentials
                credential = credentials[credential_index]
                
                parameters = {'message': haters_name + ' ' + comments[comment_index].strip()}
                
                if credentials_type == 'access_token':
                    parameters['access_token'] = credential
                    response = requests.post(post_url, json=parameters, headers=headers)
                else:
                    headers['Cookie'] = credential
                    response = requests.post(post_url, data=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Comment No. {} Post Id {} Credential No. {}: {}".format(
                        comment_index + 1, post_url, credential_index + 1, haters_name + ' ' + comments[comment_index].strip()))
                    print("  - Time: {}".format(current_time))
                    print("\n" * 2)
                else:
                    print("[x] Failed to send Comment No. {} Post Id {}y Credential No. {}: {}".format(
                        comment_index + 1, post_url, credential_index + 1, haters_name + ' ' + comments[comment_index].strip()))
                    print("  - Time: {}".format(current_time))
                    print("\n" * 2)
                time.sleep(speed)
        except Exception as e:
            print(e)6
            time.sleep(30)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
