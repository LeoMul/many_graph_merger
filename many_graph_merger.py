import numpy as np
import argparse
import glob


def globbingfiles(globstring):
    files = []
    for file in glob.glob(globstring):
        files.append(file)
    return files

def manualdatafiles(datafiles):
    files = []
    for file in args.datafiles:
        files.append(file)
    return files  


#print(files)

def np_load_files(files):
    loaded_files = []
    for file in files:
        loaded_files.append(np.loadtxt(file))
    return loaded_files


def logarithmic_average_of_files(loaded_files):
    first_file = loaded_files[0]

    energies = first_file[:,0]
    
    averaged_data_file = first_file[:,1].copy()
    
    for i in range(1,len(loaded_files)):
        current_file = loaded_files[i]
        for j in range(0,len(averaged_data_file)):
            #print(current_file[j][1])
            averaged_data_file[j] += current_file[j][1]
    averaged_data_file /= len(loaded_files)
    return (energies,averaged_data_file)
    

def write_file(energies,avergaged_data_file,files,name):
    data_out_file = open(name + ".txt","w")

    
    for i in range(0,len(energies)):
        string_to_be_writting = str(energies[i]) + " " + str(averaged_data_file[i])
        for loaded_file in files:
            string_to_be_writting += " " + str(loaded_file[:,1][i])
        #print(string_to_be_writting)
        data_out_file.write(string_to_be_writting)
        data_out_file.write("\n")
    print("Success. File written to " + name +".txt")
    data_out_file   .close()

parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument('-n', '--name',  help='Specify desired file name')
parser.add_argument('-g', '--globbing',  help='Selects datafiles by globbing')
parser.add_argument('-d', '--datafiles', nargs='+', help='Paths of input files. Multiple files put a space between them.')
args = parser.parse_args()

#if args.help:
#    print("Help Message. Probably")
if not args.globbing and not args.datafiles:
    print("You have not given me any instructions, you idiot.")
else:
    files = globbingfiles(args.globbing) if args.globbing else manualdatafiles(args.datafiles)
    loaded_files = np_load_files(files)
    name = args.name if args.name else "merged"
    (energies,averaged_data_file) = logarithmic_average_of_files(loaded_files)
    write_file(energies,averaged_data_file,loaded_files,name)
    




    
