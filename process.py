import sys, os

rootpath = sys.argv[1]

# do not determine!
if sys.argv[2] == "ab200":
    model = "~/.config/kraken/arabic-beirut-200.clstm"
    sub   = "_200"
elif sys.argv[2] == "ab":
    model = "~/.config/kraken/arabic-beirut.clstm"
    sub   = ""
else:
    print("unknown model; use `ab` or `ab200`!")
    sys.exit()

# generate manifests


# run ocr > with both models


os.system("ketos -v extract -o "+sys.argv[2]+" --normalization NFD --no-reorder "+ filesstring);


def listFiles(rootdir):
    result = []
    print('Searching {0} ...'.format(rootdir))
    for root, dirs, files in os.walk(rootdir):
        for f in files:
            p = os.path.join(root,f)
            result.append(os.path.abspath(p))
    print('Found {0} files in the specified directory tree.'.format(len(result)))
    return result

def main():
    files_to_convert = listFiles(sys.argv[1])
    filesstring = "";
    for f in files_to_convert:
        filesstring = filesstring + f + " "
    os.system("ketos -v extract -o "+sys.argv[2]+" --normalization NFD --no-reorder "+ filesstring);
    print("run complete")

main()

