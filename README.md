# FileBase
FileBase is an open source project that provides **fast** and **easy** file transmission.

### Synopsis
    $ python filebase.py upload -f filebase.py -u KEO
    [+] uploading...
    [+] usage: python filebase.py download -f filebase.py -u KEO
    
    $ python filebase.py download -f yemre.m4a
    [+] downloading...
    [+] done
    
    $ python filebase.py download -f wrongfile.py
    [-] file not found!

### Notation Rules

Notation rules for setting command-line options.
    
    usage: filebase.py [-h] -f FILENAME [-u USERNAME] {upload,download}

* Argument order is insignificant.

* There are two operation:
    *     upload
    *     download
    *     list

* (Optional) You can upload your files as different user with -u parameter. (default user = default)
    *     --username USER
    *     --username=USER
    *     -u USER

* (Required) Three ways to set the filename or path (filename for downloading, path for uploading)
    *     --filename value
    *     --filename=value
    *     -f value


    
