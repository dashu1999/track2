import tarfile


my_tar = tarfile.open('data.tar')
my_tar.extractall('./my_folder') # specify which folder to extract to
my_tar.close()