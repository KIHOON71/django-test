import re
#[a-zA-Z0-9/:=\-. ]+
p2 = re.compile(': [a-z:/.\- ]+')
a = '''
09:22:40	 발신자 서찬웅 강사 : https://drunkenpolarbear.tistory.com/20
09:42:33	 발신자 서찬웅 강사 : https://wayhome25.github.io/etc/2017/03/27/vi/
09:47:49	 발신자 서찬웅 강사 : sudo visudo
10:03:17	 발신자 서찬웅 강사 : ssh-keygen -t rsa
10:05:35	 발신자 서찬웅 강사 : cd ~/.ssh
10:11:47	 발신자 서찬웅 강사 : cat id_rsa.pub >> ~/.ssh/authorized_keys
10:11:54	 발신자 서찬웅 강사 : chmod 640 ~/.ssh/authorized_keys
10:12:46	 발신자 서찬웅 강사 : ssh localhost
10:32:00	 발신자 서찬웅 강사 : sudo dnf install java-1.8.0-openjdk ant -y
10:37:37	 발신자 서찬웅 강사 : sudo hostnamectl set-hostname client
10:39:34	 발신자 서찬웅 강사 : sudo vi /etc/selinux/config
10:40:03	 발신자 서찬웅 강사 : SELINUX=disabled
10:43:24	 발신자 서찬웅 강사 : whereis java
10:45:00	 발신자 서찬웅 강사 : cd /usr/lib/jvm
10:48:09	 발신자 서찬웅 강사 : vi ~/.bashrc
10:49:00	 발신자 서찬웅 강사 : export JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.282.b08-2.el8_3.x86_64"
11:20:52	 발신자 서근태 : https://downloads.apache.org/hadoop/common/hadoop-3.2.2/hadoop-3.2.2.tar.gz
11:23:09	 발신자 한세섭 : 다운 중....
11:26:07	 발신자 한세섭 : 28%...
11:32:02	 발신자 서찬웅 강사 : tar xvzf hadoop-3.2.2.tar.gz
11:40:42	 발신자 서찬웅 강사 : /home/hadoop/hadoop/etc/hadoop
11:42:45	 발신자 서찬웅 강사 : https://filezilla-project.org/
14:00:41	 발신자 오태영 : 출첵
14:00:48	 발신자 장민준 : 출첵
14:00:59	 발신자 유주아 : 출첵
14:01:02	 발신자 서근태 : 출첵
14:01:04	 발신자 태영 김 : 출첵!
14:01:13	 발신자 최희영 : 출첵
14:01:18	 발신자 김용균 : 출첵
14:01:22	 발신자 김동건 : 출첵
14:01:25	 발신자 영민 김 : 출첵
14:01:26	 발신자 김선정 : 출첵
14:01:49	 발신자 이미숙 : 출첵
14:07:27	 발신자 손기훈 : 출첵
14:16:51	 발신자 서찬웅 강사 : vi /etc/hosts
14:24:13	 발신자 서찬웅 강사 : 223.130.195.95
16:48:05	 발신자 서근태 : 오늘 회의안하나요
16:48:15	 발신자 서근태 : ㅋㅋㅋ
17:50:04	 발신자 유주아 : 퇴근
17:50:10	 발신자 김동건 : 퇴근
17:50:12	 발신자 손기훈 : 퇴근
17:50:17	 발신자 이미경 : 퇴근
17:50:18	 발신자 장민준 : 퇴근
17:50:28	 발신자 서근태 : 퇴근
17:50:29	 발신자 오태영 : 퇴근
17:50:43	 발신자 태영 김 : 퇴근
17:50:47	 발신자 한세섭 : 퇴근
17:50:52	 발신자 조성훈 : 퇴근
17:51:08	 발신자 영민 김 : 퇴근
17:51:37	 발신자 오태영 : 고생하셨습니다
17:51:42	 발신자 한세섭 : 수고하셨습니다.
17:51:52	 발신자 김선정 : 퇴근

'''
all = re.findall(p2, a)
for i in:
    i = re.sub(': ', '',i)
    print(i)
print(all)
