# FileBase
FileBase is an open source project that provides **fast** and **easy** file transmission.

### Synopsis
    $ python filebase.py upload -f filebase.py -u KEO
    [+] uploading...
    [+] usage: python filebase.py download -f filebase.py -u KEO
    
    $ python filebase.py list -u KEO
    filebase.py
    yemre.m4a
    
    $ python filebase.py download -f yemre.m4a
    [+] downloading...
    [+] done
    
    $ python filebase.py download -f wrongfile.py
    [-] file not found!

### Notation Rules
    
    usage: filebase.py [-h] -f FILENAME [-u USERNAME] {upload,download,list}

* Argument order is insignificant.

* There are three operation:
    *     upload
    *     download
    *     list

* You can upload your files as different user with -u parameter. (default user = default)
    *     --username USER
    *     --username=USER
    *     -u USER

* Three ways to set the filename or path (filename for downloading, path for uploading)
    *     --filename value
    *     --filename=value
    *     -f value


    
