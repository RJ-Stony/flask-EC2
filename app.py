from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Flask + EC2 배포 완료</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #eef2f5;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .logos {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 20px;
        }
        .logos img {
            height: 80px;
        }
        h1 {
            color: #333;
        }
        p {
            color: #555;
            margin-bottom: 30px;
        }
        a.button {
            display: inline-block;
            background-color: #ff9900;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 16px;
        }
        a.button:hover {
            background-color: #cc7a00;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logos">
            <img src="https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png" alt="EC2 로고">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/768px-Flask_logo.svg.png" alt="Flask 로고">
        </div>
        <h1>🚀 Flask 앱이 EC2에 배포되었습니다!</h1>
        <p>GitHub를 통해 배포된 Flask 웹앱입니다. 지금 EC2에서 정상 작동 중입니다.</p>
        <a class="button" href="https://docs.aws.amazon.com/ko_kr/ec2/index.html" target="_blank">AWS EC2 공식 문서 보기</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
