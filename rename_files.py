def rename_files(path, new_name, file_extension):
    """
        Perform renaming imges names

        Parameters
        ----------
        path : str 
            path to your images directory
        new_name : str
            new name for an image
        file_extension : str
            extension format
    """
    dirs = os.listdir( path )
    for i,file in enumerate(dirs):
        try:
            os.rename(path + "/" + file, path + "/" + new_name + '.' + str(i) + file_extension)
            # print (i, file)
        except OSError as err:
            print("OS error: {0}".format(err))
            break

# Rename all the jpg images to a "your_new_name" + a number
# Example

### f_dir = 'C:/images'
### rename_files(f_dir, 'your_new_name', '.jpg')
