import os  
  
# 网站文件所在目录  
website_dir = "/path/to/website"  
  
# 创建网站目录结构  
os.makedirs(website_dir, exist_ok=True)  
os.makedirs(os.path.join(website_dir, "css"), exist_ok=True)  
os.makedirs(os.path.join(website_dir, "js"), exist_ok=True)  
os.makedirs(os.path.join(website_dir, "images"), exist_ok=True)  
  
# 创建index.html文件  
with open(os.path.join(website_dir, "index.html"), "w") as f:  
    f.write("""  
<!DOCTYPE html>  
<html>  
<head>  
    <title>My Website</title>  
    <link rel="stylesheet" type="text/css" href="css/style.css">  
    <script src="js/script.js"></script>  
</head>  
<body>  
    <h1>Welcome to my website!</h1>  
    <img src="images/image.jpg">  
</body>  
</html>  
    """)  
  
# 创建style.css文件  
with open(os.path.join(website_dir, "css", "style.css"), "w") as f:  
    f.write("""  
body {  
    font-family: Arial, sans-serif;  
    margin: 0;  
    padding: 0;  
}  
h1 {  
    color: #333;  
}  
img {  
    max-width: 100%;  
    height: auto;  
}  
    """)  
  
# 创建script.js文件  
with open(os.path.join(website_dir, "js", "script.js"), "w") as f:  
    f.write("""  
// JavaScript code goes here  
    """)  
  
# 创建image.jpg文件（可选）  
with open(os.path.join(website_dir, "images", "image.jpg"), "w") as f:  
    f.write("""  
<!-- Image file goes here -->  
    """)
