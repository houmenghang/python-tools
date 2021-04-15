import os
workpath = os.getcwd()
#workpath = 'test'


def reanme(target_str, result_str=''):
    file_list = os.listdir(workpath)
    for filename in file_list:
        if target_str in filename:
            rename_str = filename.replace(target_str, result_str)
            cmd = 'move "{}" "{}"'.format(os.path.join(
                workpath, filename), os.path.join(workpath, rename_str))
            os.system(cmd)
            print('已将 {} 改为 {}'.format(filename, rename_str))


if __name__ == "__main__":
    print('请输入需要替换的字符串：')
    target_str = input()
    print('target_str:{}'.format(target_str))
    print('请输入目标字符串：')
    result_str = input()
    print('result_str:{}'.format(result_str))
    reanme(target_str, result_str)
