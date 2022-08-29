import os
import re
import time
import paramiko
from tqdm import tqdm


class ParamikoFolderUploader:
    def __init__(self, host, port, user, password, local_dir: str, remote_dir: str,
                 path_pattern_exluded_tuple=('/.git/', '/.idea/'),
                 file_suffix_tuple_exluded=('.pyc', '.log', '.gz', '.txt'),
                 only_upload_within_the_last_modify_time=3650 * 24 * 60 * 60,
                 file_volume_limit=1000 * 1000, ):
        """
        :param path_pattern_exluded_tuple: 命中了这些正则的直接排除
        :param file_suffix_tuple_exluded: 这些结尾的文件排除
        :param only_upload_within_the_last_modify_time: 仅仅上传最近多少天修改的文件
        :param file_volume_limit: 大于这个体积的不上传，单位b。
        """
        self._host = host
        self._port = port
        self._user = user
        self._password = password

        self._local_dir = str(local_dir).replace('\\', '/')
        if not self._local_dir.endswith('/'):
            self._local_dir += '/'
        self._remote_dir = str(remote_dir).replace('\\', '/')
        if not self._remote_dir.endswith('/'):
            self._remote_dir += '/'
        self._path_pattern_exluded_tuple = path_pattern_exluded_tuple
        self._file_suffix_tuple_exluded = file_suffix_tuple_exluded
        self._only_upload_within_the_last_modify_time = only_upload_within_the_last_modify_time
        self._file_volume_limit = file_volume_limit

        t = paramiko.Transport((host, port))
        t.connect(username=user, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(t)

        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=user, password=password, compress=True)
        self.ssh = ssh

    def _judge_need_filter_a_file(self, filename: str):
        ext = filename.split('.')[-1]
        if '.' + ext in self._file_suffix_tuple_exluded:
            return True
        for path_pattern_exluded in self._path_pattern_exluded_tuple:
            if re.search(path_pattern_exluded, filename):
                return True
        file_st_mtime = os.stat(filename).st_mtime
        volume = os.path.getsize(filename)
        if time.time() - file_st_mtime > self._only_upload_within_the_last_modify_time:
            return True
        if volume > self._file_volume_limit:
            return True
        return False

    def _make_dir(self, dir, final_dir):
        try:
            self.sftp.mkdir(dir)
            if dir != final_dir:
                self._make_dir(final_dir, final_dir)
        except (FileNotFoundError,):
            parrent_dir = os.path.split(dir)[0]
            self._make_dir(parrent_dir, final_dir)

    def _sftp_put(self, file_full_name, remote_full_file_name):
        self.sftp.put(file_full_name, remote_full_file_name)

    def upload(self):
        for parent, dirnames, filenames in os.walk(self._local_dir):
            for filename in tqdm(filenames, desc=" ".join(parent.split("/")[-2:])):
                file_full_name = os.path.join(parent, filename).replace('\\', '/')
                if not self._judge_need_filter_a_file(file_full_name):
                    remote_full_file_name = re.sub(f'^{self._local_dir}', self._remote_dir, file_full_name)
                    try:
                        self._sftp_put(file_full_name, remote_full_file_name)
                    except (FileNotFoundError,) as e:
                        self._make_dir(os.path.split(remote_full_file_name)[0], os.path.split(remote_full_file_name)[0])
                        self._sftp_put(file_full_name, remote_full_file_name)
                    os.remove(file_full_name)  # 删除文件
        source_update_inf_path = "update_inf.json"
        target_inf_path = "/home/admin/cartoon/cartoon-cat-server-master/public/userinfo.json"
        self._sftp_put(source_update_inf_path, target_inf_path)


if __name__ == '__main__':
    source_ = r"D:\programmeProject\pycharmProject\CrawlManga\maoflymanhua\maoflymanhua\images\落第骑士的英雄谭"
    target_ = r"/home/admin/cartoon/cartoon-cat-server-master/public/store/落第骑士英雄谭"
    uploader = ParamikoFolderUploader('host', 22, 'username', 'password', source_, target_)
    uploader.upload()
