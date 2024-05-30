## build a phishing website by gophish

### Gophish: Open-Source Phishing Toolkit

[Gophish](https://getgophish.com/) is an open-source phishing toolkit designed for businesses and penetration testers. It provides the ability to quickly and easily setup and execute phishing engagements and security awareness training. Gophish can be obtained from [gophish/gophish: Open-Source Phishing Toolkit (github.com)](https://github.com/gophish/gophish).

### before start gophish

<img src="build a phishing website by gophish/image-20240528203818108.png" alt="image-20240528203818108" style="zoom: 67%;" />

After downloading gophish-v0.12.1-windows-64bit, you should check the config.json file, which contains information about the listen urI for administrator server and phish server. If your port 80 or 3333 is occupied, you need to consider changing the port number.

<img src="build a phishing website by gophish/image-20240528203622328.png" alt="image-20240528203622328" style="zoom: 50%;" />

### Run gophish.exe  and login into admin page

Double-click to run gophish.exe, and the terminal information shown below will pop up.

![image-20240528204232784](build a phishing website by gophish/image-20240528204232784.png)

Log in to the admin server using the username and password displayed in the terminal

<img src="build a phishing website by gophish/image-20240528204437918.png" alt="image-20240528204437918" style="zoom: 50%;" />

Enter the administrator page

<img src="build a phishing website by gophish/image-20240528204516517.png" alt="image-20240528204516517" style="zoom: 50%;" />

### Configuration

To send a phishing email containing a phishing website, you need to configure the following four modules: user & groups, email templates, landing pages, sending profiles. There is no requirement for the order of configuration.

#### Sending Profiles

In this section, the mailbox for sending phishing emails will be configured

<img src="build a phishing website by gophish/image-20240528205822442.png" alt="image-20240528205822442" style="zoom:67%;" />

The configuration information about SMTP can be obtained from the SMTP settings of the mail website used. If you use SSL connection, the SMTP HOST port needs to be filled in 465, otherwise it is 25

When the configuration is complete, you can click send test email to check whether the configuration is successful.

#### email templates

You can configure the template for phishing emails here

![image-20240528211115883](build a phishing website by gophish/image-20240528211115883.png)

Users can first design a phishing email in their own mailbox system, and then send it to themselves or other partners. After receiving the designed email, open it and choose to export it as an eml file or display the original email, and then copy the content into gophish's Import Email to import the designed phishing email into. Don’t forget to include a hyperlink in your email, as it will be replaced with a phishing link.

#### Users & Groups

You can configure the users to whom phishing emails will be sent here

<img src="build a phishing website by gophish/image-20240528211743708.png" alt="image-20240528211743708" style="zoom: 50%;" />

#### Landing Pages

Loading the phishing page is the most important part of the entire phishing process. You need to build a phishing page that is exactly the same as the original login page.

<img src="build a phishing website by gophish/image-20240528212146309.png" alt="image-20240528212146309" style="zoom: 50%;" />

Click import site and enter the page you want to emulate, for example https://api.hanyang.ac.kr/oauth/login. The source code of the web page will be automatically crawled, but this is not the end.

<img src="build a phishing website by gophish/image-20240528212459553.png" alt="image-20240528212459553" style="zoom:50%;" />

These two buttons are very important. One button can make necessary edits to the web page source code, and the other button can preview the page.

The imported front-end source code must strictly contain the <form method="post" ···><input name="aaa" ··· /> ··· <input type="submit" ··· /></form> structure. If it is not satisfied, the submitted data cannot be captured.

Although we do not have the necessary network editing knowledge, all of this can be done through ChatGPT. This will solve most or all of your problems.

<img src="build a phishing website by gophish/image-20240528212910668.png" alt="image-20240528212910668" style="zoom:50%;" />

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <base href="https://api.hanyang.ac.kr/oauth/login"/>
    <meta http-equiv="content-type" content="text/html; charset=euc-kr"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
    <title>한양대학교 인증센터</title>
    <link href="/resources/css/oauth_css.css" rel="stylesheet" type="text/css"/>
    <script type="text/javascript" src="/resources/js/core/jquery-2.1.0.min.js"></script>
    <script type="text/javascript" src="/resources/js/enc_base64.js"></script>
    <script type="text/javascript" src="/resources/js/enc_core.js"></script>
    <script type="text/javascript">
        // Your existing JavaScript code remains here.
    </script>
</head>
<body>
<div id="wrap">
    <div id="header">
        <div class="box">
            <h1 class="logo"><img alt="" src="/resources/images/common/logo.png"/><span class="title">한양대학교 | 로그인</span></h1>
            <h2 class="title_txt mt30">고객님의 정보에 접근하기 위하여 인증이 필요합니다.<br/>
            한양대학교 포털 한양인(HY-in)계정으로 로그인 하시기 바랍니다.</h2>
        </div>
    </div>
    <div id="container">
        <div class="box">
            <div class="c_b mt30"> </div>
            <div class="login">
                <div class="login_con">
                    <p class="login_tit">Portal Login</p>
                    <form method="post" action="/oauth/login_submit.json">
                        <dl>
                            <dt><label for="userId">ID</label></dt>
                            <dd><input name="userId" id="uid" placeholder="아이디를 입력하세요" type="text" value=""/></dd>
                            <dt><label for="userPassword">Password</label></dt>
                            <dd><input name="userPassword" id="upw" placeholder="비밀번호를 입력하세요" type="password" value=""/></dd>
                        </dl>
                        <div class="btn"><button type="submit" id="login_btn">로그인</button></div>
                    </form>
                </div>
            </div>
            <div class="c_b mt50"> </div>
        </div>
    </div>
    <div id="bottom">
        <div class="box">
            <h2><span>한양대학교API 개발자센터</span></h2>
            <address><span>우)133-791 서울특별시 성동구 왕십리로 222</span></address>
            <p class="copyright">Copyright 2014 Hanyang University. All Rights Reserved.</p>
        </div>
    </div>
</div>
</body>
</html>
```

Click the preview button, they look exactly the same

<img src="build a phishing website by gophish/image-20240528213410085.png" alt="image-20240528213410085" style="zoom:50%;" />

Don't forget to check these two buttons, it will record all the information entered by the phishing user, including the password. And redirect to the normal interface, the user will not notice and log in again, as if the website just froze for a while.

<img src="build a phishing website by gophish/image-20240528213436635.png" alt="image-20240528213436635" style="zoom: 67%;" />

#### Create New Campaigns

Now, fill in the name configured during the configuration phase. Send phishing emails and wait for users to take the bait.

<img src="build a phishing website by gophish/image-20240528213832329.png" alt="image-20240528213832329" style="zoom: 50%;" />

You can monitor the results of phishing link feedback in real time here

<img src="build a phishing website by gophish/image-20240528214308202.png" alt="image-20240528214308202" style="zoom:50%;" />

### Victims’ perspective

Seeing that the midterm exam was about to end, I immediately clicked on the link in the email without considering the fake link in the lower left corner.

![image-20240528214555069](build a phishing website by gophish/image-20240528214555069.png)

This page is not much different from the normal login page, so I feel comfortable entering my account password and clicking Login.

<img src="build a phishing website by gophish/image-20240528214405431.png" alt="image-20240528214405431" style="zoom: 50%;" />

After entering the password, I was redirected to the exact same web page. I didn’t care and thought it was just an error caused by network fluctuations. And this time I logged in successfully

<img src="build a phishing website by gophish/image-20240528214827989.png" alt="image-20240528214827989" style="zoom:50%;" />

In some dark corner of the Internet, my account and password were stolen. One day later, the hacker deliberately handed in a blank paper in my important exam.

<img src="build a phishing website by gophish/image-20240528215022719.png" alt="image-20240528215022719" style="zoom:50%;" />

### reference link:

 [钓鱼工具gophish史上最详细教程（附实例） —— 手把手教你成为“捕鱼人”-CSDN博客](https://blog.csdn.net/qq_42939527/article/details/107485116)