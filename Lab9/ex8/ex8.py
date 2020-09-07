# 8. Write a function that has the following parameters: path, tree_depth, filesize, filecount, dircount and create a
# directory structure as follows: starting from the root path it will create <dircount> directories and <filecount>
# files. Each file will have a size equal to <filesize>. This process will be repeated recursively for each created
# directory until the desired depth is reached - no directories will be created for the directories on the last level.
import os


def eight(path, tree_depth, filesize, filecount, dircount):
    def create_file(name):
        f = open(name, "wb")
        f.seek(filesize - 1)
        f.write(b"\0")
        f.close()

    if not os.path.exists(path):
        os.mkdir(path)  # creates root path

    def create_dir_tree(route, tree_depth):
        for i in range(dircount):
            if not os.path.exists(route + '/' + 'dir' + str(i)):
                os.mkdir(route + '/' + 'dir' + str(i))
                create_file(route + '/' + 'file' + str(i + 1))
                for j in range(filecount):
                    create_file(route + '/' + 'dir' + str(i) + '/' + 'file' + str(j + 1))

        tree_depth -= 1
        if tree_depth > 1:
            for i in range(dircount):
                create_dir_tree(route + '/' + 'dir' + str(i), tree_depth)
        pass

    create_dir_tree("test", tree_depth)


eight('test', 2, 1024, 3, 3)
