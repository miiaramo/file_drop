# File drop app in the making

### The following work atm:

Get a list of filenames in the Filesystem folder:
```
curl http://127.0.0.1:5000/
```

Posting a new file to the Filesystem folder:
```
curl -F 'file=@/path/to/file' http://127.0.0.1:5000
```

The path for accessing specific file works but no functionality yet:
```
curl http://127.0.0.1:5000/<file_name>
```
