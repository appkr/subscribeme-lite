DOCUMENTATION - UNIX README  06/22/2000

Suscribe Me Lite 2.0 by
CGI Script Center (support@cgiscriptcenter.com)

http://www.cgiscriptcenter.com
===============================
Released: 1.0 03/06/98

Tranlasted by JuWon,Kim (webweaver@webweaver.pe.kr)
Redistribution : http://www.webweaver.pe.kr

Korean Readme starts ------------------------------------------------------

�ȳ��ϼ���? �������� �������̳�/���α׷��� ���ֿ��Դϴ�.
���� happycgi.com�� �����ٰ� ���� ���ϸ� ����Ʈ�� �ϳ� �߰��ϰ��
������ �ؾ߰ڴٴ� ������ �߽��ϴ�.

���ϸ� ������ �������? 100�븸 �Ѵ´� ������ ������ �ٿ�Ǵ� ��찡 ������?
�� ��ũ��Ʈ�� cgiscriptcenter.com���� ������ ���� �ణ�� ������ �ѱ�ȭ �۾���
�� ���Դϴ�. ������ �� ���δ� 4�� 6õ����� �����ߴٰ� �ϴ�����..

����ư �ѹ� ��ġ�� ���ñ���. �� �����ؾ� �����̳� ���������� ������ ���� (**)/
���ֿ� : webweaver@webweaver.pe.kr, http://www.webweaver.pe.kr

��ɼ���
1. �������� ���ϸ� ����Ʈ
2. ������, �Ǵ� ���� �߰� ���� (���� : email.txt)
3. ����� ���� header, footer (���� : default.header, default,footer)
4. �����ּҿ� �Բ�, REMOTE_ADDR ȯ�溯��(ip�ּ�) ����, ���� ��
5. �������� ��ũ ����
6. html ���� ����

��~ �׷� �ѹ� ��ġ�� �����?

1. ������ Ǯ���� forminput.htm, subscribe.cgi, default.header, default.footer,
email.txt���� ������ �ֽ��ϴ�.

2. �ϴ� ������ ���ε��Ͻñ���. subscribe.cgi�� ù���� �ް�� �����ϴ� �� 
�˰� �����? �ڳ� �����ؼ� which perl �����ؼ� /usr/bin/perl �� �ƴϸ���
��� �������ּ���.

3. �׷� �۹̼� ���� �ѹ� �غ����? cgi ������ 755��...
cd ���ε��� ���丮
chmod 777 ���ε��� ���丮
chmod 755 *.cgi

4. �׷�, ���������� �ҷ�������. http://yourdomain.co.kr/��ġ���丮/subscribe.cgi

5. ���⼭ ȭ���� �߸��� ����!! ��й�ȣ�� �Է��ϰ� ���� password.txt������
�����Ǿ��� Ȯ���ϼ���. ���� �� �Ǿ��ٸ� 3������ ��~

6. Permission denied �� �޽����� �߸��� 3������ ���ư��� �۹̼� ������ �ٽ�..

7. Internal Server Error �� �޽����� �߸��� subscribe.cgi������ ��� ȯ�� ����
�� �ٽ�.. (�ڼ��� �ּ��� ������ ����������)

8. forminput.htm�� �ִ� �ڵ带 �����ؼ� ���ϴ� html������ ����.
�������� ���� ���¿��� �ѹ� �׽�Ʈ �غ�����. address.txt������ �����ǰ� �����ּҰ�
����Ǿ� ������ ���� ����. �ȵǾ����� 3������ ����~

9. �ȵǸ� �ɶ�����~~ No pain, No gain.. Good luck


����� ���ϴ�. ���� �Ϸ絵 ���� �Ϸ� �ǽñ���. �� Ȩ�������� �ѹ� ����ּ���

                                               2000-08-20 ���ֿ�
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