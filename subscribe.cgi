#!/usr/bin/perl
#
############################################
##                                        ##
##           Subscribe Me Lite            ##
##          by CGI Script Center          ##
##  (e-mail support@cgiscriptcenter.com)  ##
##                                        ##
##             version:  2.0              ##
##      last modified:  05/22/2000        ##
##       copyright (c) 1998 - 2000        ##
##                                        ##
##    latest version is available from    ##
##          The CGI Script Center         ##
##     http://www.cgiscriptcenter.com     ##
##                                        ##
############################################

#=====================================================#
# 한글화 작업 : 김주원 (translation: JuWon,Kim)       #
# 재배포 : http://www.webweaver.pe.kr                 #
# 연락처 : webweaver@webweaver.pe.kr, 011-9119-0979   #
#=====================================================#

# COPYRIGHT NOTICE:
#
# Copyright 1998 - 2000 Diran Alemshah.  All Rights Reserved.
#
# This program may be used and modified free of charge by anyone, so
# long as:

# 1) This copyright notice and the header above remain intact.
# 2) Our Subscribe Me Lite links are not removed from the response
# HTML pages. If our links are removed from the response pages, you
# will be liable for the full registration fee of our Subscribe Me
# Professional.  Links can be removed from e-mailings by using the
# $no_credit variable in the variables section.
# 3) Subscribe Me Lite will not be modified in a manner that makes it appear
# that Subscribe Me Lite was created by anyone other than CGI Script Center.

# By using this program you agree to indemnify Diran
# Alemshah and Elite Web Design and Marketing, Inc. from any liability.
#
# Selling, redistributing, reverse compiling the code for this program
# and any modification of this program without prior written consent is
# expressly forbidden.  In all cases copyright and header must remain
# intact.
#
# Subscribe Me Lite is registered with the Library of Congress in the
# United States of America, and is copyrighted material.
#
# PROGRAM DESCRIPTION:
#
# This program is designed to assist users by creating an automatic
# customer/prospect mailing list that the customer/prospect can add or
# remove themselves from without the assistance of the webmaster.
# Subscribe Me has a built-in encrypted password protected form to allow 
# webmasters to mass mail their mailing list database with.
# 
# Please read the README file that comes with this program for complete
# installation and usage instructions, or visit http://www.cgiscriptcenter.com
# for posted instructions.
#
#################################################################
# VERSION HISTORY: See README.txt file
#################################################################

		#---url decoding...

read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	if ($INPUT{$name}) { $INPUT{$name} = $INPUT{$name}.",".$value; }
	else { $INPUT{$name} = $value; }
}

		#---환경설정시작
$mailprog = '/usr/sbin/sendmail';				#---메일 프로그램 위치
$memberinfo = ".";								#---이 프로그램이 설치된 디렉토리 (절대경로 추천), address.txt파일이 위치할 경로
$passfile = ".";								#---이 프로그램이 설치된 디렉토리 (절대경로 추천), password.txt파일이 위치할 경로
$list_mail = "webweaver\@webweaver.pe.kr";		#---관리자 메일주소 (@문자 앞에 반드시 \, 예:abc\@abc.com)
$list_name = "This Maillist";					#---메일링 리스트 이름
$websiteurl = "http://www.webweaver.pe.kr";		#---홈페이지 URL
$LOCK_EX = "2";									#---UNIX,NT -> "2", Windows -> 공백으로
$closing = ".";									#---이 프로그램이 설치된 디렉토리 (절대경로 추천), email.txt파일이 위치할 경로
												#---email.txt파일은 메일 끝에 붙일 서명등을 저장. 필요한 경우 주석(#)을 제거
@banned_array = (								#---등록거부할 주소들...

);

$HTML = "";										#---html 형식의 메일 -> "1", txt 형식 -> 공백으로..
$unsubscribelink = "1";							#---구독해지링크 출력 -> "1", 출력안함 -> 공백으로..
$nocredit = "";									#---정식구입자를 위한 것입니다. 손대지 마세요

		#---CGI 프로그램 실행결과 출력 메시지에 대한 환경 설정. 필요한 경우 주석을 제거.

		#---banned_array에 있는 메일주소입력이 들어 왔을 경우 에러메시지
#$blocked_subject = "Unable to Process";
#$blocked_message = "We are unable to add your address: <B><E-MAIL></B> to our list at this time.";

		#---입력받은 메일주소가 이미 가입되어 있을 경우
#$alreadylisted_subject = "Already Listed!";
#$alreadylisted_message = "Your e-mail address: <B><E-MAIL></B> is already listed in our database.";

		#---메일주소입력완료 메시지
#$addressadded_subject = "Success: Address Added";
#$addressadded_message = "Success!  Your e-mail address: <B><E-MAIL></B> has been added to our <LIST_NAME> mailing list!";

		#---메일주소제거완료 메시지
#$addressremoved_subject = "Removed!";
#$addressremoved_message = "Your email address:  <B><E-MAIL></B> has been removed from our <LIST_NAME> mailing list. We are sorry to see you go!";

		#---입력받은 메일주소가 리스트에 없을 경우
#$addressnotfound_subject = "Address Not Found!";
#$addressnotfound_message = "Your email address: <B><E-MAIL></B> was not found in our database. Please make sure you spelled the address properly and that you used the same email address that you created your account with";

		#---틀린 메일 주소가 입력되었을 경우
#$improperaddress_subject = "Improper E-mail Address!";
#$improperaddress_message = "You have entered an improper email address. Please make sure your email address appears in this manner: username\@domain.com, or username\@domain.net, etc. !";

		#---역시 메일주소입력완료 메시지
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

		#---메일주소제거완료 메시지
$removed .= "Subject: You've Been Removed!\n\n";
$removed .= "This message is to confirm the removal of your\n";
$removed .= "email address: <E-MAIL> from the <LIST_NAME>\n";
$removed .= "Subscribe Me mailing list.\n\n";
$removed .= "We're sorry to see you go!\n\n";
$removed .= "If you change your mind, you may resubscribe\n";
$removed .= "at our website: <WEB_URL>\n";
$removed .= "Thank you,\n\n";
$removed .= "<LIST_NAME>\n\n";


$servername = $ENV{'SERVER_NAME'};		#---수정그지
$cgiurl = $ENV{'SCRIPT_NAME'};			#---수정금지

###############################################################
# 아래는 수정하지 마시오
###############################################################

$version = "2.0";

if ($ENV{'QUERY_STRING'}) {
	$ENV{'QUERY_STRING'} =~ s/\.\.//g;
	$ENV{'QUERY_STRING'} =~ s/\///g;
}


$imagetype = "gif";
$INPUT{'graphic'} = $ENV{'QUERY_STRING'} if $ENV{'QUERY_STRING'} eq 'sub3.gif';

		#---스크립트 분기
if ($INPUT{'subscribe'} eq "subscribe") { &subscribe; }
elsif ($INPUT{'subscribe'} eq "unsubscribe")  {&unsubscribe; }
elsif ($INPUT{'mailing'}) {&mailing; }
elsif ($INPUT{'setpwd'}) {&setpwd; }
elsif ($INPUT{'enterpass'}) {&passcheck; }
elsif ($ENV{'QUERY_STRING'} eq 'sub3.gif') {&display_graphic; }
elsif ($ENV{'QUERY_STRING'} =~ /\@/) {&unsubscribe; }
elsif ($INPUT{'passcheck'}) {&passcheck; }
else {&form; }
exit;
		#---스크립트 분기 끝

@days   = ('일','월','화','수','목','금','토');
#@months = ('January','February','March','April','May','June','July','August','September','October','November','December');

($sec,$min,$hour,$mday,$mon,$year,$wday) = (localtime(time))[0,1,2,3,4,5,6];
$time = sprintf("%02d:%02d:%02d",$hour,$min,$sec);
$year += 1900;
$months = $mon + 1;
$date = "$days[$wday], $months[$mon] $mday, $year at $time";
$date = "$year-$months-$mday ($days[$wday]) $time";

########################################################
# Subroutine FIND - Will find member info and email it
########################################################

		#---처음접속했을 경우 관리자 비밀번호 입력 양식
sub setpassword {
	&header;
	print<<EOF;
<form action="$cgiurl" method="POST">
  <br>
  <table border="0" width="400" align="center">
    <tr> 
      <td> 
        <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Set Password!</font></b></p>
        <p><font size="-1">처음 접속하셨군요? 관리자 비밀번호를 입력해 주세요.</font></p>
        <table border="0" align="center">
          <tr> 
            <td align="RIGHT"><input type="PASSWORD" name="pwd"></td>
            <td><font size="-2" face="verdana, arial, helvetica">password</font></td>
          </tr>
          <tr> 
            <td align="RIGHT"><input type="PASSWORD" name="pwd2"></td>
            <td><font size="-2" face="verdana, arial, helvetica">confirmation</font></td>
          </tr>
          <tr> 
            <td align="CENTER"><br><input type="SUBMIT" name="setpwd" value="  확인  "></td>
            <td><br><input type="RESET" name="Input" value="다시쓰기"></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</form>
EOF
	&footer;
	exit;
}

		#---&setpassword에 대한 실행결과 출력
sub setpwd {
	print "Content-type: text/html\n\n";
	unless ($INPUT{'pwd'} && $INPUT{'pwd2'}) {
		&header;
		print<<EOF;
<form action="$cgiurl" method="POST">
  <br>
  <table border="0" width="400" align="center">
    <tr> 
      <td> 
        <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Password Error!</font></b></p>
        <p><font size="-1">두개의 비밀번호가 서로 일치하지 않습니다. 다시 한번 확인해 주세요.</font></p>
        <table border="0" align="center">
          <tr> 
            <td align="RIGHT"><input type="PASSWORD" name="pwd"></td>
            <td><font size="-2" face="verdana, arial, helvetica">password</font></td>
          </tr>
          <tr> 
            <td align="RIGHT"><input type="PASSWORD" name="pwd2"></td>
            <td><font size="-2" face="verdana, arial, helvetica">confirmation</font></td>
          </tr>
          <tr> 
            <td align="CENTER"><br><input type="SUBMIT" name="setpwd" value="  확인  "></td>
            <td><br><input type="RESET" name="Input" value="다시쓰기"></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</form>
EOF
		&footer;
		exit;
	}
	if ($INPUT{'pwd'} && $INPUT{'pwd2'}) {
	    if ($INPUT{'pwd'} ne $INPUT{'pwd2'}) {
			&header;
			print<<EOF;
<form action="$cgiurl" method="POST">
  <br>
  <table border="0" width="400" align="center">
    <tr> 
      <td> 
        <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Password Mismatch!</font></b></p>
        <p><font size="-1">두개의 비밀번호가 서로 일치하지 않습니다. 다시 한번 확인해 주세요.</font></p>
        <table border="0" align="center">
          <tr> 
            <td align="RIGHT"><input type="PASSWORD" name="pwd"></td>
            <td><font size="-2" face="verdana, arial, helvetica">password</font></td>
          </tr>
          <tr> 
            <td align="RIGHT"><input type="PASSWORD" name="pwd2"></td>
            <td><font size="-2" face="verdana, arial, helvetica">confirmation</font></td>
          </tr>
          <tr> 
            <td align="CENTER"><br><input type="SUBMIT" name="setpwd" value="  확인  "></td>
            <td><br><input type="RESET" name="Input" value="다시쓰기">
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</form>
EOF
			&footer;
			exit;
		}
	}

	chop ($pwd) if ($pwd =~ /\n$/);
	$newpassword = crypt($INPUT{'pwd'}, aa);

	open (PASSWORD, ">$passfile/password.txt")|| die &error('password.txt',$passfile,$!,'$passfile');
	if ($LOCK_EX){ 
		flock(PASSWORD, $LOCK_EX); #Locks the file
	}
	print PASSWORD "$newpassword";
	close (PASSWORD);

	&header;
	print<<EOF;
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Password Success!</font></b></p>
      <p><font size="-1">관리자 비밀번호가 성공적으로 저장되었습니다. 메일을 보내기 위해서는 비밀번호가 필요하니 꼭 기억하세요.</font></p>
      <p><font size="-1" face="verdana, arial, helvetica">SubScribe Me</font><font size="-1"> 메일리스트를 사용하시려면 <a href="$cgiurl">여기를 클릭</a> 하세요.</font></p>
    </td>
  </tr>
</table>
EOF
	&footer;
	exit;
}

		#---에러메시지 출력
sub error {
	$var1 = shift();
	$var2 = shift();
	$var3 = shift();
	$var4 = shift();

	&header;
	print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p align="CENTER"><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status:<br>Unable to create or edit file: $var1</font></b></p>
      <p><font size="-1" face="verdana, arial, helvetica">Server</font><font size="-1"> 
        메시지:</font><font size="-1" face="verdana, arial, helvetica"> &quot;<b>$var3</b>&quot;.<br>
        <br>
        &quot;<b>Permission Denied</b>&quot;</font><font size="-1"> 란 메시지를 받으셨다면, 
        귀하께서는</font><font size="-1" face="verdana, arial, helvetica"> <b>$var2</b></font><font size="-1"> 
        디렉토리에 대한 권한을 잘못 설정하신 것입니다. </font><font size="-1" face="verdana, arial, helvetica">($var4), 
        </font><font size="-1">디렉토리 권한을 </font><font size="-1" face="verdana, arial, helvetica">rwxrwxrwx</font><font size="-1">로 
        주세요.</font><font size="-1" face="verdana, arial, helvetica"> (chmod 777 
        $var2)<br>
        <br>
        &quot;<b>No such file or directory</b>&quot;</font><font size="-1"> 란 
        메시지를 받으셨다면, </font><font size="-1" face="verdana, arial, helvetica"><b>$var2</b> 
        </font><font size="-1">디렉토리를 프로그램 환경설정에서 잘못 설정하신 것입니다. </font><font size="-1" face="verdana, arial, helvetica">($var4), 
        </font><font size="-1">또는, 귀하가 설정하신 </font><font size="-1" face="verdana, arial, helvetica">$passfile</font><font size="-1"> 
        디렉토리를 만들지 않은 것은 아닌지 확인해 주세요.</font>
      </p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
	&footer;
	exit;
}

		#---입력받은 메일주소 쓰기
sub subscribe {

	&checkaddress;

	open (DAT,"<$memberinfo/address.txt");
	if ($LOCK_EX){ 
		flock(DAT, $LOCK_EX); #Locks the file
	}
	@database_array = <DAT>;
	close(DAT);

	foreach $lines(@database_array) {
		chomp($lines);
		($lines,$user_id) = split (/\|/, $lines);
		&parseemail;

		foreach $blockedaddress(@banned_array) {
			chomp($blockedaddress);
			$blockedaddress =~ tr/A-Z/a-z/;

			if (($blockedaddress =~ /\*\@/) || ($blockedaddress !~ /\@/)) {
				$blockeddomain = $blockedaddress;
				$blockeddomain =~ s/.*\@//;
			}

			if (($email eq $blockedaddress) || ($blockeddomain eq $edomain)) {
				if ($blocked_subject) {&response($blocked_subject,$blocked_message);}
				else {
					print "Content-type: text/html\n\n";
					&header;
					print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p align="CENTER"><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status:<br>Unable to Subscribe</font></b></p>
      <p><font size="-1">귀하의 메일 주소: </font><font size="-1" face="verdana, arial, helvetica"><b>$email</b></font><font size="-1">는 
        가입될 수 없는 주소입니다.</font><font size="-1" face="verdana, arial, helvetica"><br>
        <br>
        </font><font size="-1">문의하실 내용을 </font><font size="-1" face="verdana, arial, helvetica"><a href="mailto:$orgmail">$orgmail</a></font><font size="-1"> 
        로 보내주세요. 감사합니다.</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
					&footer;
				}
				exit;
			}
		}

		if ($existing eq $email) {
			if ($alreadylisted_subject) {&response($alreadylisted_subject,$alreadylisted_message);}
			else {
				print "Content-type: text/html\n\n";
				&header;
				print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Already Listed!</font></b></p>
      <p><font size="-1" face="verdana, arial, helvetica">귀하의 메일 주소: <b>$INPUT{'email'}</b> 는 이미 가입되어 있습니다.</font></p>
      <p><font size="-1" face="verdana, arial, helvetica">귀하에게 메일이 전달되지 않는 다면 <a href="mailto:$list_mail">관리자</a> 에게 알려 주세요.</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
				&footer;
			}
			exit;
		} 
	}

	open (DAT,">>$memberinfo/address.txt") || die &error('address.txt',$memberinfo,$!,'$memberinfo');
	if ($LOCK_EX){ 
		flock(DAT, $LOCK_EX); #Locks the file
	}
	print DAT "$INPUT{'email'}|$ENV{'REMOTE_ADDR'}\n" || die &error('address.txt',$memberinfo,$!,'$memberinfo');
	close (DAT);

	if ($addressadded_subject) {&response($addressadded_subject,$addressadded_message);}
	else {
		print "Content-type: text/html\n\n";
		&header;
		print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Success!</font></b></p>
      <p><font size="-1">귀하의 메일 주소: </font><font size="-1" face="verdana, arial, helvetica">$INPUT{'email'}</font><font size="-1"> 
        가 </font><font size="-1" face="verdana, arial, helvetica">$list_name</font><font size="-1"> 
        에 성공적으로 가입되었습니다.</font></p>
      <p><font size="-1">언제든지 해지를 원하시면 <a href="$websiteurl">저희 홈페이지</a>를 방문해 
        주세요. 더 자세한 정보를 원하시면 <a href="mailto:$list_mail">관리자</a> 에게 연락 주세요.</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
		&footer;
	}


	unless ($INPUT{'notify_subscriber'} eq "no") { 
		$added =~ s/<E-MAIL>/$INPUT{'email'}/g;
		$added =~ s/<LIST_NAME>/$list_name/g;
		$added =~ s/<LIST_MAIL>/$list_mail/g;
		$added =~ s/<WEB_URL>/$websiteurl/g;

		open (MAIL, "|$mailprog -t") || print "Can't start mail program";
			print MAIL "To: $INPUT{'email'}\n";
			print MAIL "From: $list_mail\n";
			print MAIL "$added\n\n";
		close (MAIL);
	}
	exit;
}

		#---입력받은 메일주소 지우기
sub unsubscribe {

	if (($ENV{'QUERY_STRING'}) && ($ENV{'QUERY_STRING'} =~ /\@/)) {$INPUT{'email'} = $ENV{'QUERY_STRING'};}
	&checkaddress;

	open (DAT,"<$memberinfo/address.txt");
	if ($LOCK_EX){ 
		flock(DAT, $LOCK_EX); #Locks the file
	}
	@database_array = <DAT>;
	close(DAT);

	foreach $lines(@database_array) {
		chomp($lines);
		($lines,$user_id) = split (/\|/, $lines);
		&parseemail;

		if ($existing eq $email) {
			if ($addressremoved_subject) {&response($addressremoved_subject,$addressremoved_message);} 
			else {
				print "Content-type: text/html\n\n";
				&header;
				print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Removed!</font></b></p>
      <p><font size="-1">귀하의 메일 주소: </font><font size="-1" face="verdana, arial, helvetica">$INPUT{'email'}</font><font size="-1"> 가 목록에서 삭제되었습니다. 아쉽지만...</font></p>
      <p><font size="-1">만약 다시 가입을 원하시면 <a href="$websiteurl">홈페이지</a>를 방문해 주세요. 더 자세한 정보를 원하시면 <a href="mailto:$list_mail">관리자</a> 에게 연락 주세요.</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
				&footer;
			}
			open (DAT,">$memberinfo/address.txt");
			if ($LOCK_EX){flock(DAT, $LOCK_EX);}

			foreach $lines(@database_array) {
				chomp($lines);
				($lines,$user_id) = split (/\|/, $lines);
				&parseemail;
				if ($existing ne $email) {print DAT "$lines|$user_id\n";}
			}
			close (DAT);

			unless ($INPUT{'notify_subscriber'} eq "no") { 
				$removed =~ s/<E-MAIL>/$INPUT{'email'}/g;
				$removed =~ s/<LIST_NAME>/$list_name/g;
				$removed =~ s/<LIST_MAIL>/$list_mail/g;
				$removed =~ s/<WEB_URL>/$websiteurl/g;

				open (MAIL, "|$mailprog -t") || print "Can't start mail program";
					print MAIL "To: $INPUT{'email'}\n";
					print MAIL "From: $list_mail\n";
					print MAIL "$removed\n\n";
				close (MAIL);
			}
			exit;
		}
	}

	if ($addressnotfound_subject) {
		&response($addressnotfound_subject,$addressnotfound_message);
		exit;
	}
	else {
		print "Content-type: text/html\n\n";
		&header;
		print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Not Found!</font></b></p>
      <p><font size="-1">귀하의 메일 주소: </font><font size="-1" face="verdana, arial, helvetica">$INPUT{'email'}</font><font size="-1"> 는 저희 목록에 존재하지 않습니다. 정확한 철자를 입력하셨는지 다시 한번 확인해 주세요.</font></p>
      <p><font size="-1">더 자세한 정보를 원하시면 <a href="mailto:$list_mail">관리자</a>에게 연락 주세요</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
		&footer;
		close (DAT);
		exit;
	}
}

		#---처음접속인지 아닌지를 구분해서 화면출력 분기
sub form {
	print "Content-type: text/html\n\n";
	unless (-e "$passfile/password.txt") {&setpassword;}
	&adminpass;
}

		#---메일링 리스트 보내기 폼 출력
sub form2 {
	&blindcheck;

	open (DAT,"<$memberinfo/address.txt");
	if ($LOCK_EX){flock(DAT, $LOCK_EX);}
	@database_array = <DAT>;
	close(DAT);

	$count_subscribers = @database_array;
	$count_banned = @banned_array;

	if ($count_subscribers == 1) {
		$countline = "현재 <B><FONT COLOR=\"#FF0000\" FACE=\"Arial, Helvetica\">$count_subscribers</FONT></B>명의 구독자가 있습니다.";
	} else {
		$countline = "현재 <B><FONT COLOR=\"#FF0000\" FACE=\"Arial, Helvetica\">$count_subscribers</FONT></B>명의 구독자가 있습니다.";
	}


	if ($count_banned == 1) {
		$countline2 = "현재 <B><FONT COLOR=\"#FF0000\" FACE=\"Arial, Helvetica\">$count_banned</FONT></B>개의 금지 메일 주소가 존재합니다.";
	} else {
		$countline2 = "현재 <B><FONT COLOR=\"#FF0000\" FACE=\"Arial, Helvetica\">$count_banned</FONT></B>개의 금지 메일 주소가 존재합니다.";
	}

	print "Content-type: text/html\n\n";
	&header;
	&header2;
	print<<EOF;
<form action="$cgiurl" method="POST">
  <input type="HIDDEN" name="pwd" value="$INPUT{'pwd'}">
  <table border="0" width="400" align="center">
    <tr> 
      <td align="CENTER"><font size="-1">$countline</font><br>
EOF

	if ($count_banned) {
		print "<FONT SIZE=\"-1\">$countline2</FONT><BR>";
	}

	print<<EOF;
        <br>
        <table border="0" align="center">
          <tr> 
            <td valign="TOP"><font size="-1"><b>제목:</b></font></td>
            <td valign="TOP"><input type="TEXT" size="40" name="mail_subject"></td>
          </tr>
          <tr> 
            <td><font size="-1"><b>비밀번호:</b></font></td>
            <td valign="TOP"> 
              <input type="PASSWORD" name="password">
            </td>
          </tr>
        </table>
        <textarea name="message" rows="12" cols="50" wrap="OFF"></textarea>
        <br>
        <input type="SUBMIT" value="    보내기    " name="mailing">
        <input type="RESET" name="Input" value="다시쓰기">
      </td>
    </tr>
  </table>
</form>
<form action="$cgiurl" method="POST">
  <input type="HIDDEN" name="pwd2" value="$INPUT{'pwd'}">
  <table border="0" align="center">
    <tbody> 
    <tr> 
      <td align="CENTER">
        <hr size="1" width="400">
        <font size="-2" face="verdana, arial, helvetica"><b>Subscribe or Unsubscribe<br>
        any addresses here</b></font> 
          <input type="TEXT" size="15" name="email">
        <table border="0">
          <tr> 
            <td>
              <input type="RADIO" name="subscribe" value="subscribe" checked align="TOP">
              <font size="-2" color="#000000" face="verdana, arial, helvetica"><b>subscribe</b></font><br>
              <input type="RADIO" name="subscribe" value="unsubscribe" align="TOP">
              <font size="-2" color="#000000" face="verdana, arial, helvetica"><b>unsubscribe</b></font><br>
              <input type="CHECKBOX" name="notify_subscriber" value="no" checked>
              <font size="-2" color="#000000" face="verdana, arial, helvetica"><b>Do 
              NOT notify subscriber via e-mail</b></font>
            </td>
          </tr>
        </table>
        <input type="SUBMIT" value="  확인  " name="SUBMIT">
      </td>
    </tr>
  </table>
</form>
EOF
	&footer2;
	&footer;
	exit;
}

		#---실제 메일보내기를 하는 서브루틴
sub mailing {
	&blindcheck;

	open (PASSWORD, "<$passfile/password.txt");
	$password = <PASSWORD>;
	close (PASSWORD);
	chop ($password) if ($password =~ /\n$/);

	if ($INPUT{'password'}) {$newpassword = crypt($INPUT{'password'}, aa);}
	else {
		print "Content-type: text/html\n\n";
		&header;
		print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Password Error!</font></b></p>
      <p><font size="-1">비밀번호를 입력하세요!</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
		&footer;
		exit;
	}
	unless ($newpassword eq $password) {
		print "Content-type: text/html\n\n";
		&header;
		print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Password Error!</font></b></p>
      <p><font size="-1">비밀번호가 틀립니다. 다시 한번 확인해 주세요.</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
		&footer;
		exit;
	}

	$pid = fork();
	print "Content-type: text/html \n\n fork failed: $!" unless defined 

	$pid;
	if ($pid) {
		print "Content-type: text/html \n\n";
		&header;	
		print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Mailing Success!</font></b></p>
      <p><font size="-1">메일이 발송되었습니다</font>!</p>
      <p><font size="-1">서버에서 메일 발송이 완료되면 귀하에게 총 몇 통의 메일을 발송했는지에 대한 결과 메일을 보내게 됩니다.</font></p>
      <p><font size="-1">고칠점이나 개선사항등을 보내 주시면 즉시 반영하겠습니다. 감사합니다. </font><font size="-1" face="verdana, arial, helvetica"><a href="mailto:$list_mail">$list_mail</a><br>
      <br>
      Thank you for using Subscribe Me. Please let us know if there any improvements 
      you would like us to consider for the next release of our program, at 
      <a href="mailto:support\@cgiscriptcenter.com">support\@cgiscriptcenter.com</a>.</font></p>
    </td>
  </tr>
</table>
EOF
		&footer;
		exit(0);
	}
	else {
		close (STDOUT);

######### Here is where we did the addition ###################
###############################################################

		open (FILE,"$closing/email.txt");
		@closing  = <FILE>;
		close(FILE);

		open (LIST,"<$memberinfo/address.txt");
		if ($LOCK_EX){flock(LIST, $LOCK_EX);}
		@database_array = <LIST>;
		close (LIST);

		$countaddresses = @database_array;

		foreach $lines(@database_array) {
			chomp($lines);
			($lines,$user_id) = split (/\|/, $lines);

			open (MAIL, "|$mailprog -t") || print "Can't start mail program";

			if ($HTML) {print MAIL "Content-type:text/html\n";}
			print MAIL "To: $lines\n";
			print MAIL  "From: $list_mail\n";
			print MAIL  "Subject: $INPUT{'mail_subject'}\n\n";
			print MAIL "$INPUT{'message'}";
				  
			foreach $line(@closing) {print MAIL "$line";}

			if ($unsubscribelink) {
				if ($HTML) {
					print MAIL "<BR><BR>";
					print MAIL "-" x 75 . "<BR>";
					print MAIL<<EOF; 
$list_name 구독해지<BR><BR>
<A HREF="http://$servername$cgiurl?$lines">http://$servername$cgiurl?$lines</A><BR>
EOF
					print MAIL "-" x 75 . "\n\n";
				} else {
					print MAIL "\n\n";
					print MAIL "$list_name 구독해지\n";
					print MAIL "http://$servername$cgiurl?$lines\n\n";
				}
			}

			unless ($nocredit) {
				if ($HTML) {
					print MAIL "<P><B><FONT SIZE=\"-2\" FACE=\"Arial, Helvetica\">Proudly powered by<A HREF=\"http://www.cgiscriptcenter.com/subscribe/index2.html\">SubscribeMe Lite</A></FONT></B></P><BR><BR>";
				} else {
					print MAIL "\n\nProudly powered by Subscribe Me Lite (http://www.cgiscriptcenter.com)\n\n";
				}
			}
			print MAIL"\n\n";
			close (MAIL);
		}
	}
	&mailingcomplete($countaddresses);
	exit;
}

		#---메일발송완료시 몇통의 메일을 성공적으로 전송했는지 관리자에게 메일로 알려줌
sub mailingcomplete {
	$_ = shift();

	open (MAIL, "|$mailprog -t") || print "Can't start mail program";
		print MAIL "To: $list_mail\n";
		print MAIL "From: $list_mail\n";
		print MAIL "Subject: Mailing Complete!\n";
		print MAIL "Your Subscribe Me mailing to your $list_name mailing list is now complete! \n\n";
		print MAIL "Your mailing was sent to: $_ email addresses.\n\n";
	close (MAIL);
}

		#---메일주소규칙 검사
sub checkaddress {

	$INPUT{'email'} =~ s/\s//g;

	unless ($INPUT{'email'} =~ /(@.*@)|(\.\.)|(@\.)|(\.@)|(^\.)|(,)/ || $INPUT{'email'} !~ /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$/) {$legalemail = 1;}
	else {$legalemail = 0;}

	if ($legalemail !~ 1) {
		if ($improperaddress_subject) {
			&response($improperaddress_subject,$improperaddress_message);
			exit;
		} else {
			print "Content-type: text/html\n\n";
			&header;
			print<<EOF; 
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Improper Email Address!</font></b></p>
      <p><font size="-1">틀린 메일 주소를 입력하셨습니다. 다시 한번 확인해 주세요. 예) </font><font size="-1" face="verdana, arial, helvetica">username\@domain.co.kr, 또는 username\@domain.net, ... !</font></p>
      <p><font size="-1">더 자세한 정보를 원하시면 <a href="mailto:$list_mail">관리자</a>에게 연락 주세요.</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
			&footer;
			exit;
		}
	}
}

		#---관리자 비밀번호 입력 폼
sub adminpass {
	my $removebreak = 1;

	&header;
	&header2;
	print<<EOF;
<form action="$cgiurl" method="POST">
  <input type="HIDDEN" name="enterpass" value="1">
  <table border="0" width="400" align="center">
    <tr> 
      <td> 
        <center><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Administration Password</font></b></center>
        <p><font size="-1">접근 제한된 구역에 들어 오셨습니다. 들어가시려면 관리자 비밀번호를 입력하세요.</font></p>
        <table border="0" align="center">
          <tr> 
            <td align="CENTER"><font size="-1"><b>비밀번호</b></font><br><input type="PASSWORD" name="pwd"></td>
          </tr>
          <tr> 
            <td align="CENTER"><br>
              <input type="SUBMIT" name="passcheck" value="  확인  ">
              <input type="RESET" name="Input" value="다시쓰기">
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</form>
<table border="0" width="400" align="center">
  <tr> 
    <td align="CENTER"><font size="-1" face="arial, helvetica"><b>Information Updates</b></font></td>
  </tr>
  <tr> 
    <td bgcolor="#000000"> 
      <table border="0" width="400" bgcolor="#FFFFFF" cellpadding="4" cellspacing="0">
<script language="javascript1.1" src="http://news.cgiscriptcenter.com/subscribe/jsnews.js"></script>
      </table>
    </td>
  </tr>
</table>
EOF
	&footer2;
	&footer;
	exit;
}

		#---관리자 비밀번호 확인
sub passcheck {

	open (PASSWORD, "$passfile/password.txt");
	if ($LOCK_EX){flock(PASSWORD, $LOCK_EX);}
	$password = <PASSWORD>;
	close (PASSWORD);

	chop ($password) if ($password =~ /\n$/);

	if ($INPUT{'pwd'}) {$newpassword = crypt($INPUT{'pwd'}, aa);}
	else {
		print "Content-type: text/html\n\n";
		&header;
		print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Password Error!</font></b></p>
      <p><font size="-1">비밀번호를 입력하세요!</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
		&footer;
		exit;
	}
	unless ($newpassword eq $password) {
		print "Content-type: text/html\n\n";
		&header;
		print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Password Error!</font></b></p>
      <p><font size="-1">비밀번호가 틀립니다. 다시 한번 확인해 주세요.</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
		&footer;
		exit;
	}
	&form2;
}

		#---CGI 프로그램 실행결과 출력
sub response {

	$var1 = shift();
	$var2 = shift();

	$var1 =~ s/<E-MAIL>/$email/g;
	$var1 =~ s/<LIST_NAME>/$list_name/g;
	$var2 =~ s/<E-MAIL>/$email/g;
	$var2 =~ s/<LIST_NAME>/$list_name/g;

	print "Content-type: text/html\n\n";
	&header;
	print<<EOF;
<br>
<table border="0" width="400" align="center">
  <tr> 
    <td> 
      <p align="CENTER"><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status:<br>$var1</font></b></p>
      <p><font size="-1" face="verdana, arial, helvetica">$var2</font></p>
      <p align="center"><a href="javascript:history.back()">이전화면</a>
    </td>
  </tr>
</table>
EOF
	&footer;
}

		#---HTML Header
sub header {
	open (FILE,"<$memberinfo/default.header"); #### Full path name from root.
	if ($LOCK_EX){flock(FILE, $LOCK_EX);}
	@headerfile = <FILE>;
	close(FILE);

	print <<HEADER;
<HTML>
<HEAD>
<TITLE>$list_name</TITLE>
<style type="text/css">
<!--
A:link{COLOR: #0000FF;TEXT-DECORATION: none}
A:visited{COLOR: #0000FF;TEXT-DECORATION: none}
A:active{COLOR: #0000FF;TEXT-DECORATION: none}
A:hover{COLOR: #0000FF;TEXT-DECORATION: underline}
BODY,TABLE,TR,TD,P,{FONT-FAMILY: "굴림", "굴림체", "돋움", "돋움체";FONT-SIZE: 10pt}
-->
</style>
</HEAD>
<BODY>
HEADER

	foreach $line(@headerfile) {
		print "$line";
	}
}

		#---HTML Footer
sub footer {
	open (FILE,"<$memberinfo/default.footer"); #### Full path name from root.
	if ($LOCK_EX){flock(FILE, $LOCK_EX);} 
	@footerfile = <FILE>;
	close(FILE);

#	foreach $line(@footerfile) {
#		print "$line";
#	}

	print<<EOF;
<TABLE BORDER="0" WIDTH="400" align="center">
  <TR>
    <TD><HR SIZE="1"></TD>
  </TR>
  <TR>
    <TD ALIGN="CENTER"><FONT SIZE="-2" FACE="verdana, arial, helvetica">
      $list_name Maintained with <A HREF="http://www.cgiscriptcenter.com/subscribe/index2.html" TARGET="_blank"><B>Subscribe
      Me Lite $version</B></A></FONT>
    </TD>
  </TR>
</TABLE>
EOF
	foreach $line(@footerfile) {
		print "$line";
	}
	print "</BODY>\n";
	print "</HTML>\n";
}

		#---빈 비밀번호 입력 방지
sub blindcheck {
	open (PASSWORD, "$passfile/password.txt");
	if ($LOCK_EX){flock(PASSWORD, $LOCK_EX);}
	$password = <PASSWORD>;
	close (PASSWORD);

	chop ($password) if ($password =~ /\n$/);

	if ($INPUT{'pwd'}) {$newpassword = crypt($INPUT{'pwd'}, aa);}
	else {
		print "Content-type: text/html\n\n";
		&header;
		print<<EOF;
<form action="$cgiurl" method="POST">
  <br>
  <table border="0" width="400" align="center">
    <tr> 
      <td> 
        <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me</font> Status: Password Error!</font></b></p>
        <p><font size="-1">비밀번호를 입력하세요!</font></p>
      </td>
    </tr>
  </table>
</form>
EOF
		&footer;
		exit;
	}
	unless ($newpassword eq $password) {
		print "Content-type: text/html\n\n";
		&header;
		print<<EOF;
<form action="$cgiurl" method="POST">
  <br>
  <table border="0" width="400" align="center">
    <tr> 
      <td> 
        <p><b><font face="verdana, arial, helvetica"><font color="#FF0000">Subscribe Me </font> Status: Password Error!</font></b></p>
        <p><font size="-1">비밀번호가 틀립니다. 다시 한번 확인해 주세요.</font></p>
      </td>
    </tr>
  </table>
</form>
EOF
		exit;
	}
}

		#---HTML Footer 2
sub footer2 {

	print "<P>";
	print "<BR></P>
    </TD>
  </TR>
</TABLE>\n";
}

		#---HTML Header 2
sub header2 {
	if (-e "$memberinfo/sub3.gif") {

		print<<EOF;
<TABLE BORDER="0" CELLPADDING="1" CELLSPACING="0" BGCOLOR="#FFFF80" WIDTH="500" align="center">
  <TR>
    <TD BGCOLOR="#FFB500" ALIGN="CENTER" WIDTH="100%">
      <TABLE BORDER="0" BGCOLOR="#FFFFFF" CELLSPACING="0" CELLPADDING="5" WIDTH="100%">
        <TR>
          <TD ALIGN="CENTER"><IMG SRC="$cgiurl?sub3.gif" ALT="Subscribe Me logo" WIDTH="129" HEIGHT="77"></TD>
          <TD ALIGN="CENTER" VALIGN="MIDDLE"><FONT FACE="verdana, arial, helvetica" SIZE="-1"><B>Subscribe Me Lite $version<BR>Administration Panel</B></FONT>
            <HR SIZE="1" WIDTH="150">
            <FONT SIZE="-2" FACE="verdana, arial, helvetica"><A HREF="http://www.cgiscriptcenter.com/sharewarefaq/" TARGET="_blank">Frequently Asked Questions</A></FONT><BR>
            <FONT SIZE="-2" FACE="verdana, arial, helvetica"><A HREF="http://www.subscribemepro.com/" TARGET="_blank">Read about Subscribe Me Pro</A></FONT><BR>
          </TD>
        </TR>
      </TABLE>
      <BR>
EOF
	} 
	else {
		print<<EOF;
<TABLE BORDER="0" CELLPADDING="1" CELLSPACING="0" BGCOLOR="#FFFF80" WIDTH="500" align="center">
  <TR>
    <TD BGCOLOR="#FFB500" ALIGN="CENTER" WIDTH="100%">
      <TABLE BORDER="0" BGCOLOR="#FFFFFF" CELLSPACING="0" CELLPADDING="5" WIDTH="100%">
        <TR>
          <TD ALIGN="CENTER" VALIGN="MIDDLE"><FONT FACE="verdana, arial, helvetica" SIZE="-1"><B>Subscribe Me Lite $version<BR>Administration Panel</B></FONT>
            <HR SIZE="1" WIDTH="150">
            <FONT SIZE="-2" FACE="verdana, arial, helvetica"><A HREF="http://www.cgiscriptcenter.com/sharewarefaq/" TARGET="_blank">Frequently Asked Questions</A></FONT><BR>
            <FONT SIZE="-2" FACE="verdana, arial, helvetica"><A HREF="http://www.subscribemepro.com/" TARGET="_blank">Read about Subscribe Me Pro</A></FONT>
          </TD>
        </TR>
      </TABLE>
      <BR>
EOF
	}
}

		#---subscribe me LOGO 가 있을 경우 출력
sub display_graphic {
	if ($INPUT{'graphic'}) {
		print "Content-type: image/$imagetype\n";
		print "\n";

		$file = "$memberinfo/$INPUT{'graphic'}";
		open (IMAGE, "<$file") || die "Can't open $file: $!";

		if ($os eq 'nt') {
			binmode(IMAGE); ## If used on an NT server, remove the "#" at front.
			binmode(STDOUT); ## If used on an NT server, remove the "#" at front.
		}

		while (<IMAGE>){
			print $_;
		}
		close(IMAGE);
	}
}

		#---메일주소 파싱
sub parseemail {
	$email = $INPUT{'email'};
	$existing = $lines;
	$existing =~ tr/A-Z/a-z/;
	$email =~ tr/A-Z/a-z/;
	$edomain = $email;
	$edomain =~ s/.*\@//;
}