from os import path


def exception_handler(func):
    def wrapper(*args,**kwargs):
        file = kwargs.get('file', args[0] if args else None)
        try:
            return func(*args,**kwargs)
        except UnicodeDecodeError:
            print(f"File: {path.basename(file)} contains invalid encoding.")
            raise
        except MemoryError:
            print(f"File: {path.basename(file)} is too large to be processed.")
            raise
        except OSError as e:
            print(f"File: {path.basename(file)} cannot be opened. An error occurred: {e}")
            raise
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
    return wrapper


def countUtils(fileContent, args):
    ans = '  '
    used = False

    if args.bytes:
        ans += str(len(fileContent))+' ' 
        used=True
    if args.chars:
        ans += str(len(fileContent) + str(fileContent).count('\n')) + ' '
        used = True
    if args.lines:
        ans += str(len(fileContent.splitlines())) + ' '
        used = True
    if args.words:
        ans += str(len(fileContent.split()))  + ' '
        used = True
    
    if used == False:
        ans += str(len(fileContent))+' ' 
        ans += str(len(fileContent.splitlines()))  + ' '
        ans += str(len(fileContent.split()))  + ' '
    
    if args.filename:
        ans += args.filename
    print(ans)
        