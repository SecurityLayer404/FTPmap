import ftplib
import sys
import os

def ftp_connect(host, user='anonymous', passwd='anonymous@'):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user=user, passwd=passwd)
        print(f"[+] IP: {host}:21\t\tName: {host}\t\tStatus: Authenticated")
        print()
        print(f"{'Path':<60} {'Read':<10} {'Write':<10} Comment")
        print(f"{'-'*60} {'-'*10} {'-'*10} {'-'*20}")
        return ftp
    except ftplib.all_errors as e:
        print(f"[-] Error al conectar: {e}")
        return None

def check_write_permission(ftp, path):
    testfile = "perm_test.txt"
    try:
        ftp.cwd(path)
        ftp.storbinary(f"STOR {testfile}", open(os.devnull, 'rb'))
        ftp.delete(testfile)
        return True
    except Exception:
        return False

def check_read_permission(ftp, filepath):
    try:
        ftp.retrbinary(f"RETR {filepath}", lambda data: None)
        return True
    except Exception:
        return False

def list_recursive(ftp, path="/"):
    try:
        ftp.cwd(path)
        items = ftp.nlst()
    except ftplib.error_perm:
        return

    for item in items:
        item_path = os.path.join(path, item).replace("\\", "/")
        try:
            ftp.cwd(item_path)  # Es directorio
            read_perm = "-"
            write_perm = "YES" if check_write_permission(ftp, item_path) else "-"
            print(f"{item_path + '/':<60} {read_perm:<10} {write_perm:<10} FTP directory")
            list_recursive(ftp, item_path)
            ftp.cwd("..")
        except ftplib.error_perm:
            read_perm = "YES" if check_read_permission(ftp, item_path) else "-"
            write_perm = "-"
            print(f"{item_path:<60} {read_perm:<10} {write_perm:<10} FTP file")
        except Exception as e:
            continue

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 ftpmap.py <host> [user] [password]")
        sys.exit(1)

    host = sys.argv[1]
    user = sys.argv[2] if len(sys.argv) > 2 else 'anonymous'
    passwd = sys.argv[3] if len(sys.argv) > 3 else 'anonymous@'

    ftp = ftp_connect(host, user, passwd)
    if ftp:
        list_recursive(ftp)
        ftp.quit()
