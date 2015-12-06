DOCUMENTATION - UNIX README  06/22/2000

Suscribe Me Lite 2.0 by
CGI Script Center (support@cgiscriptcenter.com)

http://www.cgiscriptcenter.com
===============================
Released: 1.0 03/06/98

Tranlasted by JuWon,Kim (webweaver@webweaver.pe.kr)
Redistribution : http://www.webweaver.pe.kr

Korean Readme starts ------------------------------------------------------

안녕하세요? 프리랜서 웹디자이너/프로그래머 김주원입니다.
얼마전 happycgi.com을 뒤지다가 멋진 메일링 리스트를 하나 발견하고는
수정을 해야겠다는 생각을 했습니다.

메일링 보내기 힘드시죠? 100통만 넘는다 싶으면 서버가 다운되는 경우가 많았죠?
이 스크립트는 cgiscriptcenter.com에서 개발한 것을 약간의 수정과 한글화 작업을
한 것입니다. 개발자 측 말로는 4만 6천통까지 성공했다고 하더군요..

여하튼 한번 설치해 보시구요. 더 수정해야 할점이나 개선사항이 있으면 연락 (**)/
김주원 : webweaver@webweaver.pe.kr, http://www.webweaver.pe.kr

기능설명
1. 안정적인 메일링 리스트
2. 꼬리말, 또는 서명 추가 가능 (편집 : email.txt)
3. 사용자 정의 header, footer (편집 : default.header, default,footer)
4. 메일주소와 함께, REMOTE_ADDR 환경변수(ip주소) 저장, 관리 편리
5. 구독해지 링크 제공
6. html 메일 가능

자~ 그럼 한번 설치해 볼까요?

1. 압축을 풀면은 forminput.htm, subscribe.cgi, default.header, default.footer,
email.txt등의 파일이 있습니다.

2. 일단 서버에 업로드하시구요. subscribe.cgi맨 첫줄의 펄경로 수정하는 건 
알고 계시죠? 텔넷 접속해서 which perl 엔터해서 /usr/bin/perl 이 아니면은
경로 수정해주세요.

3. 그럼 퍼미션 설정 한번 해볼까요? cgi 파일은 755로...
cd 업로드한 디렉토리
chmod 777 업로드한 디렉토리
chmod 755 *.cgi

4. 그럼, 브라우저에서 불러보세요. http://yourdomain.co.kr/설치디렉토리/subscribe.cgi

5. 여기서 화면이 뜨면은 성공!! 비밀번호를 입력하고 나서 password.txt파일이
생성되었나 확인하세요. 만약 안 되었다면 3번으로 빽~

6. Permission denied 란 메시지가 뜨면은 3번으로 돌아가서 퍼미션 설정을 다시..

7. Internal Server Error 란 메시지가 뜨면은 subscribe.cgi파일을 열어서 환경 설정
을 다시.. (자세한 주석이 있으니 걱정마세요)

8. forminput.htm에 있는 코드를 복사해서 원하는 html문서에 삽입.
삽입하지 않은 상태에서 한번 테스트 해보세요. address.txt파일이 생성되고 메일주소가
기재되어 있으면 최종 성공. 안되었으면 3번으로 빠꾸~

9. 안되면 될때까지~~ No pain, No gain.. Good luck


행운을 빕니다. 오늘 하루도 좋은 하루 되시구요. 제 홈페이지도 한번 들려주세요

                                               2000-08-20 김주원
Korean Readme ends here ------------------------------------------------------

Updates:

1.01 - (Unix only) 03/16/98
Typo in the Unix Mail script
that kept the program from entering the mail subject in the actual
mail message.

1.1 - 4/8/98
Upgrades include:
- Administration password requirement before entering the
Mailing Form.
- File Locking option to keep address.txt file from being
corrupted during heavy usage.
- Mail-back confirmation of mailing list subscription and
removal.

1.12 - 05/05/98
-- UNIX ONLY UPGRADE/FIXES --  Still working on NT upgrades.
Upgrades include:
- Added a "closing" text file that can be included in your
general mailings.  This will allow you to add a personalized
message to your mailings, or list removal information.
Fixes include:
- Added an error message to the Password creation routine
that will notify you if your password.txt file wasn't properly
created during initial setup.
- Squashed the "timeout" bug by bypassing the browser for
the mailings, altogether.  Subscribe Me has now been
successfully tested on a 2,500 member mailing list. If you
sucessfully use Subscribe Me on a larger list, please
forward the number to:  cgi@elitehost.com

1.13 - 10/20/98
Skipped for superstitious reasons.  ;)  Too close to
Halloween.

1.14 - 10/20/98
Two fixes.  Each deals with security issues, so we
thought it best not to explain the details, however,
we do highly recommend that you install this version
as soon as possible.


2.0 - 06/25/2000

Released version 2.0 of Subscribe Me Lite.  Upgrades include:

1) Banned addresses - if admin wants to ban an addresses or entire domains
from joining the mailing list.
2) Editable HTML and Email responses.
3) Better error response screens, with more information to make install easier
4) HTML or Text e-mail capability
5) Optional Unsubscribe link capability.  Subscribers can unsubscribe
with a single click, from their mailings.
6) Running total of Subscribed and Banned addresses
7) Improved interface.  Easier to use and prettier to look at.
8) Improved error handling.  Error messages much easier to understand.
9) Optional e-mail sent to subscriber when administrator adds subscriber
through the administration interface.


==========================================================

Subscribe Me is a program designed to allow prospects/customers
the ability to subscribe and/or unsubscribe themselves from your
mailing list, automatically! You can use the built-in mass mailing
form to send your updates/information to your prospects/customers.
Simply call the program from your web browser, and the mailing form
automatically loads.  On your first use of the mailing form, you will
have to set your password.  

Start by opening the subscribe.pl file in a text editor, preferably
Wordpad (but any text editor will do).  Find the:

################################################################
# EDIT USER INFORMATION BELOW
################################################################

title heading.

The first item on the list is the absolute path to the UNIX Sendmail
program. Below is the line you will needto edit in the subscribe.pl
file:

# Type the full path to your Mail program
# If you don't know the correct directory, contact your server
# administrator.
$mailprog = "/usr/sbin/sendmail";


Next, you will need to type in the full path to the Subscribe Me
web directory.  We suggest creating an empty folder in a *NON-WEB*
directory and name it "subscribe".  Using a directory located
outside your server's web root will help protect your addresses
from prying eyes.  If you are not sure if you have a NON-WEB
directory, contact your host to find out.
Below is the line you will need to edit in the subscribe.pl file:

# Type the full path to your Subscribe Me directory
$memberinfo = "/full/path/to/subscribe";

Third, enter the full path to your password.txt file directory.
The file itself will be created when you load your mailing form for
the fist time and enter your password.  Make sure this directory
had read and write permission settings. Below is the line you will
need to edit in the subscribe.pl file:

# Type the full path to your Administration Password directory
$passfile = "/full/path/to/pass";


Fourth, enter the email address that you would like to use as your
mailing list address.  This could be your main email address, or
a forwarding address that you may have, like maillist@yoursite.com.
Below is the line you will need to edit in the subscribe.pl file:

# Type your email address.  Make sure to place a \ in front of the @
# As an example:  cgi\@elitehost.com
$list_mail = "you\@yourdomain.com";

Fifth, enter the name of your company or name of your mailing list.
This will be used in the script.  Below is the line you will need to
edit in the subscribe.pl file:

# Type the name of your mailing list
$list_name = "Subscribe Me List";

Next, enter your website address.  This will allow people to add
and/or remove themselves without having to contact you.  Below is
the line you will need to edit in the subscribe.pl file:

# Type your website URL (example: http://www.yoursite.com)
$websiteurl = "http://www.yoursite.com";

Next, we added a way for you to add a personalized message
or instructions on how to remove your users that do not
want to receive further mailings.  Simply create a text file
and call it:  email.txt
Upload the file to the directory that you define in the script
that appears like the line below.  You may want to keep it
simple and upload the email.txt file to the same directory
as everything else.  If so, just place the path to your
memberinfo directory in the $closing line also. Below is
the line you will need to edit in the subscribe.pl file:

# If you would like your mailings to have a closing message,
# create a text file called email.txt and upload it to the
# directory that you define below.  This message will be added
# to the end of your mailings.
$closing = "/full/path/to/directory";


If you would like to "ban" an address or even an entire domain
from adding their address(es) to your mailing list, you can do
so by entering their address(es) in the @banned_array.

be sure to add your addresses in the following format:

'bob@domain.com',

address between single quotation marks, and a comma at the end
of the line, then press the ENTER key, to go t the next line.

If you wish to block an entire domain, you can use:

'domain.com',

or if you prefer,

'*@domain.com',

Both will work.  We recommend the first/former.  Easier to remember.

# Enter addresses that you would like to ban from signing up for
# your mailing list.
@banned_array = (

'bob@smith.com',
'jack@yahoo.com',
'somedomain.com',

);



The HTML e-mail option allows you to send your subscribers HTML
formatted e-mail messages.  In order for your subscribers to read
your HTML formatted e-mailings, your subscribers will need an
HTML "aware" or compliant e-mail reading program.

# If you would like to send your mailings as HTML e-mail, place
# the number 1 between the quotes below, like so:
# $HTML = "1";
# If, however, you wish to send your mailings as Text only, leave
# the variable below as it is.
$HTML = "";


To make unsubscribing from your mailing list simpler, you can opt
to offer your subscribers an easy one-click link in their mailings.
By following the directions below.  The Unsubscribe link is NOT placed
in your mailings by default.  If you do not wish to offer this
link.

# If you would like to provide your subscriber's a way to unsubscribe
# from a link in your mailings, place the number 1 between the quotes
# below, like so:  $unsubscribelink = "1";

# If you do not wish to provide an unsubscribe link, leave the variable
# the way it is.
$unsubscribelink = "";


$nocredit = "";
################ End Required Configurations ################
#############################################################


##############################################################
########## Start Optional Customize Responses ################

# This is the subject of the "Blocked/Banned" Address
# response screen that your subscribers will receive,
# if you choose to use the "Address Blocking" feature.
# To enable the customized responses, remove the # pound
# sybmol from before the variables below.

# If you choose not to use customized responses, Subscribe Me
# will issue its default responses.

#$blocked_subject = "Unable to Process";
#$blocked_message = "We are unable to add your address: <B><E-MAIL></B> to our list at this time.";


# This is the subject of the "Already Listed" Address
# response screen that your subscribers will receive,
# if their address is already listed in your database.
# To enable the customized responses, remove the # pound
# sybmol from before the variables below.

# If you choose not to use customized responses, Subscribe Me
# will issue its default responses.

#$alreadylisted_subject = "Already Listed!";
#$alreadylisted_message = "Your e-mail address: <B><E-MAIL></B> is already listed in our database.";


# This is the subject of the "Already Added" Address
# response screen that your subscribers will receive,
# if their address is added to your database.
# To enable the customized responses, remove the # pound
# sybmol from before the variables below.

# If you choose not to use customized responses, Subscribe Me
# will issue its default responses.

#$addressadded_subject = "Success: Address Added";
#$addressadded_message = "Success!  Your e-mail address: <B><E-MAIL></B> has been added to our <LIST_NAME> mailing list!";


# This is the subject of the "Address Removed" Address
# response screen that your subscribers will receive,
# when their address is removed from your database.
# To enable the customized responses, remove the # pound
# sybmol from before the variables below.

# If you choose not to use customized responses, Subscribe Me
# will issue its default responses.

#$addressremoved_subject = "Removed!";
#$addressremoved_message = "Your email address:  <B><E-MAIL></B> has been removed from our <LIST_NAME> mailing list. We are sorry to see you go!";


# This is the subject of the "Address Not Found" Address
# response screen that your subscribers will receive,
# when their address is not found in your database.
# To enable the customized responses, remove the # pound
# sybmol from before the variables below.

# If you choose not to use customized responses, Subscribe Me
# will issue its default responses.

#$addressnotfound_subject = "Address Not Found!";
#$addressnotfound_message = "Your email address: <B><E-MAIL></B> was not found in our database. Please make sure you spelled the address properly and that you used the same email address that you created your account with";


# This is the subject of the "Improper Address" Address
# response screen that your subscribers will receive,
# when their address is not found in your database.
# To enable the customized responses, remove the # pound
# sybmol from before the variables below.

# If you choose not to use customized responses, Subscribe Me
# will issue its default responses.

#$improperaddress_subject = "Improper E-mail Address!";
#$improperaddress_message = "You have entered an improper email address. Please make sure your email address appears in this manner: username\@domain.com, or username\@domain.net, etc. !";


# E-mail Addition Response - Added to List
# At the end of each line, you'll see the \n, which stands for New Line.
# To wrap the text to the next line, you will want to use the \n symbols.
# Feel free to create as many lines as you need, as long as each line starts
# with:  $line1 .=
# and that each section is enclosed in quotations marks, and there is a
# semi-colon at the end of each line.

$added .= "Subject: You've Been Added!\n\n";
$added .= "This message is to confirm the addition of your\n";
$added .= "email address: <E-MAIL> to the <LIST_NAME>\n";
$added .= "Subscribe Me mailing list.\n\n";
$added .= "If you feel you have received this notice in error,\n";
$added .= "please visit the <LIST_NAME> Subscribe Me mailing list\n";
$added .= "at our website: <WEB_URL>\n";
$added .= "to remove yourself automatically.\n\n";
$added .= "Thank you,\n\n";
$added .= "<LIST_NAME>\n\n";


# E-mail Removal Response - Removed from List
# At the end of each line, you'll see the \n, which stands for New Line.
# To wrap the text to the next line, you will want to use the \n symbols.
# Feel free to create as many lines as you need, as long as each line starts
# with:  $line1 .=
# and that each section is enclosed in quotations marks, and there is a
# semi-colon at the end of each line.

$removed .= "Subject: You've Been Removed!\n\n";
$removed .= "This message is to confirm the removal of your\n";
$removed .= "email address: <E-MAIL> from the <LIST_NAME>\n";
$removed .= "Subscribe Me mailing list.\n\n";
$removed .= "We're sorry to see you go!\n\n";
$removed .= "If you change your mind, you may resubscribe\n";
$removed .= "at our website: <WEB_URL>\n";
$removed .= "Thank you,\n\n";
$removed .= "<LIST_NAME>\n\n";


$servername = $ENV{'SERVER_NAME'};
$cgiurl = $ENV{'SCRIPT_NAME'};




To send mailings to your Subscribe Me mailing list, simply
call the script from your web browser like so:

http://www.yourserver.com/full/path/to/subscribe.pl

(if your server requires .cgi extensions, be sure to rename
the subscribe.pl file to subscribe.cgi).  This will bring
up your form.  The first time you use the form, you will
receive your Password entry page.  Make sure to set your
password as soon as possible, so somone else doesn't set
it for you!

You can find a help forum at: http://cgi.elitehost.com

Enjoy!

Diran Alemshah
The CGI Script Center team (Jennifer, Jack, Jeneth, Chris, and Teri).
CGI Script Center
http://cgi.elitehost.com