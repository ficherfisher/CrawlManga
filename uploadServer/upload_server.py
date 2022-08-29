import shutil

import yaml
import time
import os
import datetime
import paramiko
from upload_class import ParamikoFolderUploader


class connect_server:
    def __init__(self, host, port, user, password):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        t = paramiko.Transport((host, port))
        t.connect(username=user, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(t)

    def mkdir(self, remote_full_file_name):
        try:
            self.sftp.mkdir(remote_full_file_name)
        except Exception as e:
            print(e)


def load_config():
    fp = open("config.yaml", encoding="utf-8")
    return yaml.load(fp.read(), Loader=yaml.FullLoader)


def judge_upload(file_path=r"D:\programmeProject\pycharmProject\scrapy\maoflymanhua\maoflymanhua\images\ONE PIECE航海王"):
    dir_time = os.path.getctime(file_path)
    today = datetime.datetime.now()
    offset = datetime.timedelta(days=-3)
    re_date = (today + offset)
    re_date_unix = time.mktime(re_date.timetuple())
    if dir_time <= re_date_unix:
        return False
    else:
        return True


def _del_all_file(tmp, delDir):
    for filePath in delDir:
        tmp_file = os.path.join(tmp, filePath)
        if len(os.listdir(tmp_file)) == 0:
            shutil.rmtree(tmp_file, True)


def upload(file_path):
    mangas_path = os.listdir(file_path)
    change_dict = load_config()
    server_path = "/home/admin/cartoon/cartoon-cat-server-master/public/store/"
    for i in mangas_path:
        source_ = os.path.join(file_path, i)
        if judge_upload(source_):
            if i not in change_dict:
                change_dict[i] = i
                connect_server1 = connect_server('host', 22, 'username', 'password',)
                connect_server1.mkdir(server_path + change_dict[i])
            target_ = server_path + change_dict[i]
            uploader = ParamikoFolderUploader('host', 22, 'username', 'password', source_, target_)
            uploader.upload()
            _del_all_file(source_, os.listdir(source_))
        fp_yaml_config = open(os.path.join(os.path.dirname(__file__), "config.yaml"), "w", encoding="utf-8")
        yaml.safe_dump(change_dict, fp_yaml_config, encoding="utf-8", allow_unicode=True)
        fp_yaml_config.close()


def produce_index(file_path):
    config_path = os.path.join(file_path, "config.yaml")
    fp = open(config_path, encoding="utf-8")
    config_dict = yaml.load(fp.read(), Loader=yaml.FullLoader)
    for key, value in zip(list(config_dict.keys()), list(config_dict.values())):
        key_path = os.path.join(file_path, "images/"+key+"/index")
        fp = open(key_path, "w")
        for j in range(0, value):
            fp.write(str(j+1)+"\n")
        fp.close()
        print("写入"+key+":index文件")


if __name__ == '__main__':
    upload_list = [r"D:\programmeProject\pycharmProject\CrawlManga\maoflymanhua\maoflymanhua",
                   r"D:\programmeProject\pycharmProject\CrawlManga\xingqiumanhua\xingqiumanhua"]
    for i in upload_list:
        produce_index(i)
        upload(os.path.join(i, "images"))

